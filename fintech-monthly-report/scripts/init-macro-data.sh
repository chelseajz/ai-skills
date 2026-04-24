#!/bin/bash
#
# init-macro-data.sh - Initialize macro data directory by copying templates
# Copies historical template data from skill to external data directory
# This only needs to be run once after init.sh
#

SKILL_MACRO_TEMPLATES=~/.claude/skills/fintech-monthly-report/knowledge-base/macro-indicators/templates
TARGET_DATA_DIR=~/.claude/fintech-reports/data/macro-indicators

echo "=== Initialize macro indicator data ==="
echo "Source templates: $SKILL_MACRO_TEMPLATES"
echo "Target directory: $TARGET_DATA_DIR"
echo

# Check source exists
if [ ! -d "$SKILL_MACRO_TEMPLATES" ]; then
    echo "❌ Template directory not found: $SKILL_MACRO_TEMPLATES"
    exit 1
fi

# Create target if not exists
mkdir -p "$TARGET_DATA_DIR"

# Check if target already has files
FILE_COUNT=$(ls -1 "$TARGET_DATA_DIR"/*.csv 2>/dev/null | wc -l)
if [ "$FILE_COUNT" -gt 0 ]; then
    echo "⚠️ Target directory already contains $FILE_COUNT CSV files:"
    ls -lh "$TARGET_DATA_DIR"/*.csv
    echo
    read -p "Overwrite existing files with templates? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Operation cancelled - existing files kept"
        exit 0
    fi
fi

# Copy all CSV templates
cp "$SKILL_MACRO_TEMPLATES"/*.csv "$TARGET_DATA_DIR"/

echo "✅ Macro data initialized"
echo "Copied $(ls -1 "$TARGET_DATA_DIR"/*.csv | wc -l) CSV files to $TARGET_DATA_DIR"
ls -lh "$TARGET_DATA_DIR"
