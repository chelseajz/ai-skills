#!/bin/bash
#
# archive-reports.sh - Archive finished reports from output to archive directory
# Moves completed reports to external archive directory, keeps output clean
#

FINTECH_ROOT=~/.claude/fintech-reports
OUTPUT_DIR="$FINTECH_ROOT/output"
ARCHIVE_DIR="$FINTECH_ROOT/archive"

echo "=== Archiving finished reports ==="
echo "Output: $OUTPUT_DIR"
echo "Archive: $ARCHIVE_DIR"
echo

# Create archive if it doesn't exist
mkdir -p "$ARCHIVE_DIR"

# Check if output has any reports
REPORT_COUNT=$(ls -1 "$OUTPUT_DIR"/fintech-report-*.md 2>/dev/null | wc -l)

if [ "$REPORT_COUNT" -eq 0 ]; then
    echo "ℹ️ No reports found in output directory"
    exit 0
fi

echo "Found $REPORT_COUNT reports in output:"
ls -lh "$OUTPUT_DIR"/fintech-report-*.{md,html} 2>/dev/null
echo

read -p "Do you want to archive all these reports? (y/N) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Operation cancelled"
    exit 0
fi

# Move all reports to archive
mv "$OUTPUT_DIR"/fintech-report-*.{md,html} "$ARCHIVE_DIR"/ 2>/dev/null

echo
echo "✅ Archiving complete"
echo "Remaining files in output:"
ls -la "$OUTPUT_DIR"
