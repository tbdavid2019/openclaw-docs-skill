#!/bin/sh

# OpenClaw Docs Sync Script
# This script pulls the latest documentation from the official OpenClaw repository.

REPO_URL="https://github.com/openclaw/openclaw.git"
TEMP_DIR=".tmp_repo"
SOURCE_FOLDER="docs"
DEST_FOLDER="references"

echo "🚀 Starting OpenClaw documentation sync..."

# Create temporary directory if it doesn't exist
mkdir -p "$TEMP_DIR"
cd "$TEMP_DIR" || exit 1

# Initialize git if not already initialized
if [ ! -d ".git" ]; then
    git init
    git remote add origin "$REPO_URL"
    git config core.sparseCheckout true
fi

# Set sparse-checkout to only include docs/
echo "$SOURCE_FOLDER/*" > .git/info/sparse-checkout

# Pull the latest changes from main branch (shallow clone for speed)
echo "📥 Fetching latest documentation (this may take a moment)..."
git pull --depth 1 origin main

# Return to parent directory
cd ..

# Clear destination folder
echo "🗑️ Cleaning up old references..."
rm -rf "${DEST_FOLDER:?}"/*

# Copy new files
echo "📂 Syncing files to $DEST_FOLDER..."
cp -R "$TEMP_DIR/$SOURCE_FOLDER/"* "$DEST_FOLDER/"

# Summary
FILE_COUNT=$(find "$DEST_FOLDER" -name "*.md" | wc -l)
echo "✅ Sync complete! $FILE_COUNT markdown files synced."

# Generate index
echo "🗂️ Generating documentation index..."
python3 scripts/generate_index.py

echo "💡 Tip: Run this script whenever you want to update the documentation."
