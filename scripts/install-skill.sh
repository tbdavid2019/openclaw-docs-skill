#!/usr/bin/env bash
# Install or update this skill while preserving it as a Git checkout.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
TARGET_INPUT="${1:-$SKILL_DIR}"
BRANCH="${OPENCLAW_SKILL_BRANCH:-main}"

if [[ "$TARGET_INPUT" = /* ]]; then
    TARGET_DIR="$TARGET_INPUT"
else
    TARGET_DIR="$(pwd)/$TARGET_INPUT"
fi

if [[ -e "$TARGET_DIR" ]]; then
    if [[ ! -d "$TARGET_DIR" ]]; then
        echo "error: installation target is not a directory: $TARGET_DIR" >&2
        exit 1
    fi
    TARGET_DIR="$(cd "$TARGET_DIR" && pwd -P)"
else
    TARGET_PARENT="$(dirname "$TARGET_DIR")"
    mkdir -p "$TARGET_PARENT"
    TARGET_PARENT="$(cd "$TARGET_PARENT" && pwd -P)"
    TARGET_DIR="$TARGET_PARENT/$(basename "$TARGET_DIR")"
fi

if [[ -n "${OPENCLAW_SKILL_REPO_URL:-}" ]]; then
    REPO_URL="$OPENCLAW_SKILL_REPO_URL"
elif git -C "$SKILL_DIR" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    REPO_URL="$(git -C "$SKILL_DIR" remote get-url origin)"
else
    REPO_URL="https://github.com/tbdavid2019/openclaw-docs-skill.git"
fi

TARGET_GIT_ROOT=""
if [[ -e "$TARGET_DIR" ]]; then
    TARGET_GIT_ROOT="$(git -C "$TARGET_DIR" rev-parse --show-toplevel 2>/dev/null || true)"
fi

if [[ ! -e "$TARGET_DIR" ]]; then
    echo "Installing OpenClaw docs skill into $TARGET_DIR..."
    git clone --depth 1 --branch "$BRANCH" "$REPO_URL" "$TARGET_DIR"
elif [[ "$TARGET_GIT_ROOT" == "$TARGET_DIR" ]]; then
    echo "Updating OpenClaw docs skill in $TARGET_DIR..."
    git -C "$TARGET_DIR" pull --ff-only origin "$BRANCH"
else
    echo "error: target exists but is not a Git checkout: $TARGET_DIR" >&2
    echo "Move it aside or choose a new target so updates remain reliable." >&2
    exit 1
fi

REQUIRED_FILES=(
    "SKILL.md"
    "agents/openai.yaml"
    "references/SOURCE.json"
    "references/SKILL_INDEX.md"
)

for REQUIRED_FILE in "${REQUIRED_FILES[@]}"; do
    if [[ ! -f "$TARGET_DIR/$REQUIRED_FILE" ]]; then
        echo "error: required installation artifact is missing: $REQUIRED_FILE" >&2
        exit 1
    fi
done

if [[ ! -d "$TARGET_DIR/references/_catalog" ]]; then
    echo "error: required installation artifact is missing: references/_catalog" >&2
    exit 1
fi

SKILL_COMMIT="$(git -C "$TARGET_DIR" rev-parse HEAD)"
if ! UPSTREAM_COMMIT="$(
    python3 - "$TARGET_DIR/references/SOURCE.json" <<'PY'
import json
from pathlib import Path
import re
import sys

source = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
commit = source.get("upstream_commit", "")
if not re.fullmatch(r"[0-9a-f]{40}", commit):
    raise SystemExit("SOURCE.json does not contain a valid upstream_commit")
print(commit)
PY
)"; then
    echo "error: unable to read a valid upstream commit from references/SOURCE.json" >&2
    exit 1
fi

echo "OpenClaw docs skill is ready at $TARGET_DIR"
echo "Installation directory: $TARGET_DIR"
echo "Skill repository commit: $SKILL_COMMIT"
echo "Upstream documentation commit: $UPSTREAM_COMMIT"
