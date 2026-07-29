#!/usr/bin/env python3
"""Generate compact, layered routing indexes for the OpenClaw docs skill."""

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass
from pathlib import Path
import re
import shutil
import sys


CATEGORY_DESCRIPTIONS = {
    "announcements": "Breaking changes and migration announcements",
    "automation": "Cron, hooks, tasks, standing orders, and webhooks",
    "channels": "Messaging channel setup, routing, and troubleshooting",
    "cli": "Exact OpenClaw CLI command reference",
    "clawhub": "ClawHub CLI and publishing",
    "concepts": "Architecture, agents, sessions, memory, models, and routing",
    "diagnostics": "Diagnostic flags and failure investigation",
    "gateway": "Gateway configuration, operations, security, and networking",
    "general": "Top-level concepts and cross-cutting documentation",
    "help": "Symptom-first troubleshooting and support",
    "install": "Installation, updates, migration, deployment, and uninstall",
    "nodes": "Mobile, desktop, and headless node capabilities",
    "platforms": "Platform-specific setup and operation",
    "plugins": "Plugin architecture, SDKs, and bundled integrations",
    "providers": "Model provider authentication and configuration",
    "security": "Threat models, hardening, and incident response",
    "start": "Getting started, onboarding, and setup",
    "tools": "Agent tools, browser, exec, web, skills, and permissions",
    "web": "Control UI, dashboard, WebChat, and TUI",
}

GENERATED_INDEX = "SKILL_INDEX.md"
GENERATED_CATALOG_DIR = "_catalog"
MAX_DOCUMENTS_PER_CATALOG = 30


@dataclass(frozen=True)
class Document:
    path: str
    category: str
    title: str
    summary: str
    read_when: tuple[str, ...]


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        try:
            parsed = ast.literal_eval(value)
            if isinstance(parsed, str):
                return parsed
        except (SyntaxError, ValueError):
            return value[1:-1]
    return value


def parse_frontmatter(content: str) -> dict[str, object]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", content, re.DOTALL)
    if not match:
        return {}

    metadata: dict[str, object] = {}
    list_key: str | None = None
    for raw_line in match.group(1).splitlines():
        field = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", raw_line)
        if field:
            key, raw_value = field.groups()
            list_key = None
            if raw_value:
                value = unquote(raw_value)
                if value.startswith("[") and value.endswith("]"):
                    items = [unquote(item) for item in value[1:-1].split(",") if item.strip()]
                    metadata[key] = items
                else:
                    metadata[key] = value
            else:
                metadata[key] = []
                list_key = key
            continue

        item = re.match(r"^\s+-\s+(.+?)\s*$", raw_line)
        if item and list_key:
            current = metadata.setdefault(list_key, [])
            if isinstance(current, list):
                current.append(unquote(item.group(1)))

    return metadata


def fallback_title(path: Path, content: str) -> str:
    heading = re.search(r"^#\s+(.+?)\s*$", content, re.MULTILINE)
    if heading:
        return heading.group(1)
    if path.name.lower() == "index.md":
        return path.parent.name.replace("-", " ").title()
    return path.stem.replace("-", " ").replace("_", " ").title()


def load_document(path: Path, root: Path) -> Document:
    content = path.read_text(encoding="utf-8", errors="replace")
    metadata = parse_frontmatter(content)
    relative = path.relative_to(root)
    title = str(metadata.get("title") or fallback_title(path, content))
    summary = str(metadata.get("summary") or "")
    raw_read_when = metadata.get("read_when", [])
    if isinstance(raw_read_when, str):
        read_when = (raw_read_when,)
    elif isinstance(raw_read_when, list):
        read_when = tuple(str(item) for item in raw_read_when if item)
    else:
        read_when = ()
    category = relative.parts[0] if len(relative.parts) > 1 else "general"
    return Document(relative.as_posix(), category, title, summary, read_when)


def discover_documents(root: Path) -> list[Document]:
    documents = []
    for path in sorted(root.rglob("*")):
        if (
            not path.is_file()
            or path.is_symlink()
            or path.suffix.lower() not in {".md", ".mdx"}
        ):
            continue
        relative = path.relative_to(root)
        if (
            path.name == GENERATED_INDEX
            or GENERATED_CATALOG_DIR in relative.parts
            or any(part.startswith(".") for part in relative.parts)
        ):
            continue
        documents.append(load_document(path, root))
    return documents


def escape_markdown(text: str) -> str:
    return text.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")


def catalog_content(category: str, documents: list[Document]) -> str:
    display_name = "General" if category == "general" else category.replace("-", " ").title()
    description = CATEGORY_DESCRIPTIONS.get(category, f"Documentation under `{category}/`")
    lines = [
        f"# {display_name} documentation catalog",
        "",
        description + ".",
        "",
        "Open only the entries relevant to the current request. Start with at most three documents.",
        "",
    ]
    for document in documents:
        details = []
        if document.summary:
            details.append(document.summary.rstrip(".") + ".")
        if document.read_when:
            details.append("Read when: " + "; ".join(document.read_when) + ".")
        suffix = " — " + " ".join(details) if details else ""
        lines.append(
            f"- [{escape_markdown(document.title)}](../{document.path}){suffix}"
        )
    lines.append("")
    return "\n".join(lines)


def catalog_router_content(
    category: str, chunks: list[tuple[str, list[Document]]]
) -> str:
    display_name = "General" if category == "general" else category.replace("-", " ").title()
    description = CATEGORY_DESCRIPTIONS.get(category, f"Documentation under `{category}/`")
    lines = [
        f"# {display_name} documentation catalog",
        "",
        description + ".",
        "",
        "Choose one section by its title range, then select at most three documents from it.",
        "",
    ]
    for filename, documents in chunks:
        first = escape_markdown(documents[0].title)
        last = escape_markdown(documents[-1].title)
        lines.append(
            f"- [{first} – {last}]({filename}) — {len(documents)} documents."
        )
    lines.append("")
    return "\n".join(lines)


def main_index_content(categories: dict[str, list[Document]], has_source: bool) -> str:
    lines = [
        "# OpenClaw documentation router",
        "",
        "Use this compact router only for broad topics. For an exact error message, CLI",
        "command, or configuration key, search `references/` directly instead.",
        "",
        "Open one topic catalog, then load at most three relevant documents. Expand only",
        "when those documents do not answer the request.",
        "",
    ]
    if has_source:
        lines.extend(
            [
                "Source revision and document count: [SOURCE.json](SOURCE.json).",
                "",
            ]
        )
    lines.extend(
        [
            "## Topic catalogs",
            "",
            "| Topic | Coverage | Documents |",
            "|---|---|---:|",
        ]
    )
    for category in sorted(categories, key=lambda item: (item != "general", item)):
        display_name = "General" if category == "general" else category.replace("-", " ").title()
        description = CATEGORY_DESCRIPTIONS.get(category, f"Documentation under `{category}/`")
        lines.append(
            f"| [{display_name}]({GENERATED_CATALOG_DIR}/{category}.md) "
            f"| {description} | {len(categories[category])} |"
        )
    lines.append("")
    return "\n".join(lines)


def build_indexes(root_dir: str | Path) -> dict[str, str]:
    root = Path(root_dir)
    documents = discover_documents(root)
    categories: dict[str, list[Document]] = {}
    for document in documents:
        categories.setdefault(document.category, []).append(document)

    indexes = {
        GENERATED_INDEX: main_index_content(categories, (root / "SOURCE.json").is_file())
    }
    for category, category_documents in categories.items():
        ordered_documents = sorted(
            category_documents, key=lambda document: (document.title.casefold(), document.path)
        )
        if len(ordered_documents) <= MAX_DOCUMENTS_PER_CATALOG:
            indexes[f"{GENERATED_CATALOG_DIR}/{category}.md"] = catalog_content(
                category, ordered_documents
            )
            continue

        chunks = []
        for offset in range(0, len(ordered_documents), MAX_DOCUMENTS_PER_CATALOG):
            chunk = ordered_documents[offset : offset + MAX_DOCUMENTS_PER_CATALOG]
            part = offset // MAX_DOCUMENTS_PER_CATALOG + 1
            filename = f"{category}-{part:02d}.md"
            chunks.append((filename, chunk))
            indexes[f"{GENERATED_CATALOG_DIR}/{filename}"] = catalog_content(
                category, chunk
            )
        indexes[f"{GENERATED_CATALOG_DIR}/{category}.md"] = catalog_router_content(
            category, chunks
        )
    return indexes


def write_indexes(root: Path, indexes: dict[str, str]) -> None:
    catalog_dir = root / GENERATED_CATALOG_DIR
    if catalog_dir.exists():
        shutil.rmtree(catalog_dir)
    for relative_path, content in indexes.items():
        output = root / relative_path
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(content, encoding="utf-8")


def check_indexes(root: Path, indexes: dict[str, str]) -> bool:
    expected_paths = {root / relative for relative in indexes}
    actual_catalogs = set((root / GENERATED_CATALOG_DIR).glob("*.md"))
    valid = actual_catalogs == {
        path for path in expected_paths if path.parent == root / GENERATED_CATALOG_DIR
    }
    for relative_path, expected in indexes.items():
        path = root / relative_path
        if not path.is_file() or path.read_text(encoding="utf-8") != expected:
            valid = False
    return valid


def parse_args() -> argparse.Namespace:
    default_root = Path(__file__).resolve().parents[1] / "references"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=default_root)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit non-zero when committed indexes do not match the source documents.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        print(f"error: references directory not found: {root}", file=sys.stderr)
        return 1

    indexes = build_indexes(root)
    if args.check:
        if check_indexes(root, indexes):
            print("Documentation indexes are up to date.")
            return 0
        print("Documentation indexes are stale.", file=sys.stderr)
        return 1

    write_indexes(root, indexes)
    catalog_count = sum(path.startswith(f"{GENERATED_CATALOG_DIR}/") for path in indexes)
    print(f"Generated {GENERATED_INDEX} and {catalog_count} topic catalogs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
