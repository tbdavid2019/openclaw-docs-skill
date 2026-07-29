import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]


def load_generate_index():
    module_path = REPO_ROOT / "scripts" / "generate_index.py"
    spec = importlib.util.spec_from_file_location("generate_index", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class GenerateIndexTests(unittest.TestCase):
    def test_build_indexes_uses_metadata_and_includes_mdx_and_landing_pages(self):
        module = load_generate_index()

        with tempfile.TemporaryDirectory() as temp_dir:
            references = Path(temp_dir) / "references"
            channels = references / "channels"
            install = references / "install"
            channels.mkdir(parents=True)
            install.mkdir()

            (channels / "index.md").write_text(
                "---\n"
                'title: "Channels"\n'
                'summary: "Choose and configure a chat channel."\n'
                "read_when:\n"
                "  - Selecting a messaging channel\n"
                "---\n"
                "# Channels\n",
                encoding="utf-8",
            )
            (channels / "telegram.md").write_text(
                "---\n"
                'title: "Telegram"\n'
                'summary: "Configure a Telegram bot."\n'
                "read_when:\n"
                "  - Setting up Telegram\n"
                "---\n"
                "# Telegram\n",
                encoding="utf-8",
            )
            (install / "render.mdx").write_text(
                "---\n"
                'title: "Render"\n'
                'summary: "Deploy OpenClaw on Render."\n'
                'read_when: "Deploying to Render"\n'
                "---\n"
                "# Render\n",
                encoding="utf-8",
            )

            indexes = module.build_indexes(references)

            self.assertIn("SKILL_INDEX.md", indexes)
            self.assertIn("_catalog/channels.md", indexes)
            self.assertIn("_catalog/install.md", indexes)
            self.assertIn("Choose and configure a chat channel.", indexes["_catalog/channels.md"])
            self.assertIn("../channels/index.md", indexes["_catalog/channels.md"])
            self.assertIn("../install/render.mdx", indexes["_catalog/install.md"])
            self.assertNotIn("telegram.md", indexes["SKILL_INDEX.md"])

    def test_large_categories_are_split_and_hidden_docs_are_ignored(self):
        module = load_generate_index()

        with tempfile.TemporaryDirectory() as temp_dir:
            references = Path(temp_dir) / "references"
            tools = references / "tools"
            hidden = references / ".internal"
            tools.mkdir(parents=True)
            hidden.mkdir()
            for index in range(31):
                (tools / f"tool-{index:02d}.md").write_text(
                    "---\n"
                    f'title: "Tool {index:02d}"\n'
                    f'summary: "Use tool {index:02d}."\n'
                    "---\n",
                    encoding="utf-8",
                )
            (hidden / "private.md").write_text("# Private\n", encoding="utf-8")

            indexes = module.build_indexes(references)

            self.assertIn("_catalog/tools.md", indexes)
            self.assertIn("_catalog/tools-01.md", indexes)
            self.assertIn("_catalog/tools-02.md", indexes)
            self.assertIn("tools-01.md", indexes["_catalog/tools.md"])
            self.assertNotIn("_catalog/.internal.md", indexes)
            self.assertLess(
                max(len(content.encode("utf-8")) for content in indexes.values()),
                12_000,
            )

    def test_committed_indexes_are_complete_and_all_links_resolve(self):
        module = load_generate_index()
        references = REPO_ROOT / "references"

        self.assertTrue(module.check_indexes(references, module.build_indexes(references)))

        generated_files = [references / "SKILL_INDEX.md"]
        generated_files.extend(sorted((references / "_catalog").glob("*.md")))
        link_pattern = re.compile(r"\]\(([^)#]+)")
        missing = []
        for generated_file in generated_files:
            for link in link_pattern.findall(generated_file.read_text(encoding="utf-8")):
                if not (generated_file.parent / link).resolve().exists():
                    missing.append(f"{generated_file.relative_to(REPO_ROOT)} -> {link}")
        self.assertEqual(missing, [])

        source = json.loads((references / "SOURCE.json").read_text(encoding="utf-8"))
        source_documents = [
            path
            for path in references.rglob("*")
            if path.is_file()
            and not path.is_symlink()
            and path.suffix.lower() in {".md", ".mdx"}
            and path.name != "SKILL_INDEX.md"
            and "_catalog" not in path.relative_to(references).parts
            and not any(part.startswith(".") for part in path.relative_to(references).parts)
        ]
        self.assertEqual(source["document_count"], len(source_documents))


class InstallerTests(unittest.TestCase):
    def test_installer_clones_a_new_target(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir) / "openclaw-docs"
            env = os.environ.copy()
            env["OPENCLAW_SKILL_REPO_URL"] = str(REPO_ROOT)

            result = subprocess.run(
                ["bash", str(REPO_ROOT / "scripts" / "install-skill.sh"), str(target)],
                cwd=REPO_ROOT,
                env=env,
                text=True,
                capture_output=True,
            )

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertTrue((target / ".git").is_dir())
            self.assertTrue((target / "SKILL.md").is_file())

    def test_installer_refuses_an_existing_non_git_target(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir) / "openclaw-docs"
            target.mkdir()
            sentinel = target / "keep.txt"
            sentinel.write_text("keep\n", encoding="utf-8")

            result = subprocess.run(
                ["bash", str(REPO_ROOT / "scripts" / "install-skill.sh"), str(target)],
                cwd=REPO_ROOT,
                text=True,
                capture_output=True,
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "keep\n")


class SkillGuidanceTests(unittest.TestCase):
    def test_skill_enforces_progressive_disclosure_version_checks_and_safe_actions(self):
        content = (REPO_ROOT / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("at most three", content.lower())
        self.assertIn("openclaw --version", content)
        self.assertIn("exact error", content.lower())
        self.assertIn("state-changing", content.lower())
        self.assertNotIn("MANDATORY: Always check", content)
        self.assertLess(len(content.encode("utf-8")), 10_000)

    def test_installation_docs_do_not_recommend_copying_or_per_request_updates(self):
        english = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        traditional_chinese = (REPO_ROOT / "README_TW.md").read_text(encoding="utf-8")
        combined = english + traditional_chinese

        self.assertNotIn("cp -r openclaw-docs-skill", combined)
        self.assertNotIn("每次被呼叫 → 自動 git pull", combined)
        self.assertNotIn("Hard Requirement", combined)


class SyncDocsTests(unittest.TestCase):
    def make_sync_repo(self, root):
        scripts = root / "scripts"
        references = root / "references"
        scripts.mkdir()
        references.mkdir()
        shutil.copy2(REPO_ROOT / "scripts" / "sync-docs.sh", scripts / "sync-docs.sh")
        shutil.copy2(REPO_ROOT / "scripts" / "generate_index.py", scripts / "generate_index.py")
        return references

    def test_failed_fetch_does_not_replace_existing_references(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "repo"
            root.mkdir()
            references = self.make_sync_repo(root)
            sentinel = references / "keep.md"
            sentinel.write_text("# Keep me\n", encoding="utf-8")

            fake_bin = Path(temp_dir) / "bin"
            fake_bin.mkdir()
            fake_git = fake_bin / "git"
            fake_git.write_text("#!/bin/sh\nexit 42\n", encoding="utf-8")
            fake_git.chmod(0o755)

            env = os.environ.copy()
            env["PATH"] = f"{fake_bin}{os.pathsep}{env['PATH']}"
            result = subprocess.run(
                ["sh", "scripts/sync-docs.sh"],
                cwd=root,
                env=env,
                text=True,
                capture_output=True,
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "# Keep me\n")

    def test_local_source_sync_generates_catalogs_and_provenance(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "repo"
            root.mkdir()
            references = self.make_sync_repo(root)
            (references / "old.md").write_text("# Old\n", encoding="utf-8")

            source_docs = Path(temp_dir) / "upstream-docs"
            (source_docs / "gateway").mkdir(parents=True)
            (source_docs / "cli").mkdir()
            (source_docs / "index.md").write_text(
                "---\ntitle: OpenClaw\nsummary: Main documentation.\n---\n# OpenClaw\n",
                encoding="utf-8",
            )
            (source_docs / "gateway" / "index.md").write_text(
                "---\ntitle: Gateway\nsummary: Operate the Gateway.\n---\n# Gateway\n",
                encoding="utf-8",
            )
            (source_docs / "cli" / "index.md").write_text(
                "---\ntitle: CLI\nsummary: Use the CLI.\n---\n# CLI\n",
                encoding="utf-8",
            )
            (source_docs / "install.mdx").write_text(
                "---\ntitle: Install\nsummary: Install OpenClaw.\n---\n# Install\n",
                encoding="utf-8",
            )

            env = os.environ.copy()
            env.update(
                {
                    "OPENCLAW_DOCS_SOURCE_DIR": str(source_docs),
                    "OPENCLAW_SOURCE_REPOSITORY": "example/openclaw",
                    "OPENCLAW_SOURCE_COMMIT": "abc123",
                    "OPENCLAW_SOURCE_COMMIT_DATE": "2026-07-29T00:00:00Z",
                    "OPENCLAW_SYNC_MIN_DOCS": "4",
                }
            )
            result = subprocess.run(
                ["sh", "scripts/sync-docs.sh"],
                cwd=root,
                env=env,
                text=True,
                capture_output=True,
            )

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertFalse((references / "old.md").exists())
            self.assertTrue((references / "_catalog" / "gateway.md").is_file())
            self.assertTrue((references / "_catalog" / "general.md").is_file())
            self.assertTrue((references / "SKILL_INDEX.md").is_file())
            source = json.loads((references / "SOURCE.json").read_text(encoding="utf-8"))
            self.assertEqual(source["upstream_commit"], "abc123")
            self.assertEqual(source["document_count"], 4)


if __name__ == "__main__":
    unittest.main()
