#!/bin/bash
# install-skill.sh - Setup and update script for AI Agent documentation skills
# This script ensures the skill remains a proper git checkout for easy updates.

SKILL_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SKILL_NAME=$(basename "$SKILL_DIR")
# If a target directory is provided, use it. Otherwise assume the skill is already in its home.
TARGET_DIR="${1:-$SKILL_DIR}"

echo "--- Skill Setup: $SKILL_NAME ---"

if [ -d "$TARGET_DIR/.git" ]; then
    echo "Updating existing installation in $TARGET_DIR..."
    git -C "$TARGET_DIR" pull origin main --ff-only
    echo "Update complete."
else
    echo "Running in non-git mode or fresh directory."
    echo "If you want auto-updates, ensure this directory is a git clone."
    echo "Current location: $SKILL_DIR"
fi

echo "Please refer to $TARGET_DIR/SKILL.md for usage instructions."
