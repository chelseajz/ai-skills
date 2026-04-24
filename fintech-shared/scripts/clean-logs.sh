#!/bin/bash
#
# clean-logs.sh - Clean log files for fresh report generation
# Use this when you need to regenerate a report from scratch
#

FINTECH_ROOT=~/.claude/fintech-reports
LOGS_DIR="$FINTECH_ROOT/logs"

echo "=== Clean log files for fresh run ==="
echo "Logs directory: $LOGS_DIR"
echo

if [ ! -d "$LOGS_DIR" ]; then
    echo "ℹ️ Logs directory doesn't exist yet"
    exit 0
fi

LOG_COUNT=$(ls -1 "$LOGS_DIR"/*.json "$LOGS_DIR"/*.md 2>/dev/null | wc -l)

if [ "$LOG_COUNT" -eq 0 ]; then
    echo "ℹ️ No log files found"
    exit 0
fi

echo "Found $LOG_COUNT log files:"
ls -lh "$LOGS_DIR"/*.json "$LOGS_DIR"/*.md 2>/dev/null
echo

read -p "This will DELETE all log files. Continue? (y/N) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Operation cancelled"
    exit 0
fi

# Remove all logs
rm -f "$LOGS_DIR"/*.json "$LOGS_DIR"/*.md "$LOGS_DIR"/url-cache.json

echo "✅ Logs cleaned"
ls -la "$LOGS_DIR"
