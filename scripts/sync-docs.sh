#!/bin/sh
# Atomically synchronize official OpenClaw documentation into references/.

set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
REPO_DIR=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
DEST_DIR="$REPO_DIR/references"
REPO_URL="${OPENCLAW_DOCS_REPO_URL:-https://github.com/openclaw/openclaw.git}"
SOURCE_REPOSITORY="${OPENCLAW_SOURCE_REPOSITORY:-openclaw/openclaw}"
MIN_DOCS="${OPENCLAW_SYNC_MIN_DOCS:-600}"
WORK_DIR=$(mktemp -d "$REPO_DIR/.sync-docs.XXXXXX")
STAGED_DIR="$WORK_DIR/next-references"
BACKUP_DIR="$WORK_DIR/previous-references"

cleanup() {
    if [ ! -e "$DEST_DIR" ] && [ -e "$BACKUP_DIR" ]; then
        mv "$BACKUP_DIR" "$DEST_DIR"
    fi
    rm -rf "$WORK_DIR"
}
trap cleanup EXIT
trap 'exit 1' HUP INT TERM

case "$MIN_DOCS" in
    ''|*[!0-9]*)
        echo "error: OPENCLAW_SYNC_MIN_DOCS must be a non-negative integer" >&2
        exit 1
        ;;
esac

echo "Preparing OpenClaw documentation sync..."

if [ -n "${OPENCLAW_DOCS_SOURCE_DIR:-}" ]; then
    SOURCE_DOCS="$OPENCLAW_DOCS_SOURCE_DIR"
    SOURCE_COMMIT="${OPENCLAW_SOURCE_COMMIT:-local-source}"
    SOURCE_COMMIT_DATE="${OPENCLAW_SOURCE_COMMIT_DATE:-unknown}"
else
    UPSTREAM_DIR="$WORK_DIR/upstream"
    git clone --depth 1 --filter=blob:none --sparse "$REPO_URL" "$UPSTREAM_DIR"
    git -C "$UPSTREAM_DIR" sparse-checkout set docs
    SOURCE_DOCS="$UPSTREAM_DIR/docs"
    SOURCE_COMMIT=$(git -C "$UPSTREAM_DIR" rev-parse HEAD)
    SOURCE_COMMIT_DATE=$(git -C "$UPSTREAM_DIR" show -s --format=%cI HEAD)
fi

if [ ! -d "$SOURCE_DOCS" ]; then
    echo "error: source documentation directory not found: $SOURCE_DOCS" >&2
    exit 1
fi

mkdir "$STAGED_DIR"
for SOURCE_ITEM in "$SOURCE_DOCS"/*; do
    cp -R "$SOURCE_ITEM" "$STAGED_DIR/"
done

DOC_COUNT=$(find "$STAGED_DIR" -type f \( -name '*.md' -o -name '*.mdx' \) | wc -l | tr -d ' ')
if [ "$DOC_COUNT" -lt "$MIN_DOCS" ]; then
    echo "error: expected at least $MIN_DOCS documents, found $DOC_COUNT" >&2
    exit 1
fi

for REQUIRED_PATH in index.md gateway/index.md cli/index.md; do
    if [ ! -f "$STAGED_DIR/$REQUIRED_PATH" ]; then
        echo "error: required upstream document is missing: $REQUIRED_PATH" >&2
        exit 1
    fi
done

python3 - "$STAGED_DIR/SOURCE.json" "$SOURCE_REPOSITORY" "$SOURCE_COMMIT" "$SOURCE_COMMIT_DATE" "$DOC_COUNT" <<'PY'
import json
from pathlib import Path
import sys

output, repository, commit, commit_date, count = sys.argv[1:]
payload = {
    "upstream_repository": repository,
    "upstream_commit": commit,
    "upstream_commit_date": commit_date,
    "document_count": int(count),
}
Path(output).write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
PY

python3 "$SCRIPT_DIR/generate_index.py" --root "$STAGED_DIR"
python3 "$SCRIPT_DIR/generate_index.py" --root "$STAGED_DIR" --check

if [ -e "$DEST_DIR" ]; then
    mv "$DEST_DIR" "$BACKUP_DIR"
fi

if ! mv "$STAGED_DIR" "$DEST_DIR"; then
    if [ -e "$BACKUP_DIR" ]; then
        mv "$BACKUP_DIR" "$DEST_DIR"
    fi
    echo "error: could not activate synchronized documentation" >&2
    exit 1
fi

rm -rf "$BACKUP_DIR"
echo "Synchronized $DOC_COUNT documents from $SOURCE_REPOSITORY at $SOURCE_COMMIT."
