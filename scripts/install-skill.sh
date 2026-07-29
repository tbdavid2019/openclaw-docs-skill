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
    TARGET_DIR="$(cd "$TARGET_DIR" && pwd)"
else
    TARGET_PARENT="$(dirname "$TARGET_DIR")"
    mkdir -p "$TARGET_PARENT"
    TARGET_PARENT="$(cd "$TARGET_PARENT" && pwd)"
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

if [[ ! -f "$TARGET_DIR/SKILL.md" ]]; then
    echo "error: installation completed without SKILL.md" >&2
    exit 1
fi

echo "OpenClaw docs skill is ready at $TARGET_DIR"
