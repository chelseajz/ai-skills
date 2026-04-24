#!/bin/bash
#
# init.sh - Initialize output directory structure for fintech-monthly-report
# Creates the external directory structure outside skill directory

FINTECH_ROOT=~/.claude/fintech-reports

echo "=== Initializing fintech-report directory structure ==="
echo "Root: $FINTECH_ROOT"
echo

mkdir -p "$FINTECH_ROOT"/{output,logs,data/macro-indicators,archive}

if [ -d "$FINTECH_ROOT" ]; then
    echo "✅ Directory structure created successfully"
    echo
    ls -la "$FINTECH_ROOT"
else
    echo "❌ Failed to create directory structure"
    exit 1
fi

echo
echo "Next step: Run /fintech-monthly-report to generate your first report!"
