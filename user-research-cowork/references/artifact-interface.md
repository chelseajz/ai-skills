# Artifact Interface

Use this for substantial multi-step projects so each phase hands off stable outputs to the next.

## Principle

Prefer file-based handoffs over conversational memory. Later stages should read prior outputs from files whenever possible.

## Recommended directories

### Quantitative outputs

`survey_output/`

Recommended files:
- `build_summary.json`
- `survey_results.json`
- `survey_analysis.md`
- `quant_support_longtable.csv`
- `quant_support_crosstab_quickview.csv`
- `quant_support_workbook.xlsx`
- `charts/`

If the package will feed charting, audit, or follow-up slicing, the quantitative support table should:
- separate absolute counts and percentages into distinct fields
- keep question, option, segment, base, statistic type, note, and source columns as needed
- remain sortable and filterable without re-parsing prose
- include a navigation or directory layer when the file is large

For quantitative pipelines, preserve the sample funnel explicitly in file outputs:
- raw rows
- invalid-row removal
- deduped respondent base
- target-population base
- question-valid base where relevant

If legacy analyses exist, keep a reconciliation note or summary file that explains whether older outputs used a different denominator or cleaning rule.

## Qualitative outputs

`code_output/`

Recommended files:
- `coding_summary.json`
- `codebook.md`
- `quote_bank.md`
- `casebook.md`
- `contradictions.md`
- `quote_digest.md`
- `case_sampling_note.md`

If a casebook includes low-priority or edge-demand users, add a bucket-definition note so readers do not confuse `weak or already-resolved demand` with `no demand`.

## Mixed-method outputs

`analyze_output/`

Recommended files:
- `integration_results.json`
- `integration_memo.md`
- `propositions.md`
- `charts/`

## Insight outputs

`insight_output/`

Recommended files:
- `insights.md`
- `finding_ledger.md`

## Report outputs

`report_output/`

Recommended files:
- `final_report.md`
- `meeting_report.md`
- `review_findings.md`
- `revision_note.md`

For substantial cross-functional work, prefer:
- one formal main report that is readable on its own
- one compressed meeting or readout version
- supporting qual and quant artifacts beneath those reports rather than split top-level narratives

If the report is synchronized into Feishu or another rich-text system:
- remove raw local markdown image paths from the doc-facing text
- insert charts near the sections they support when placement matters
- preserve the local markdown source separately if needed for version control

## Reading rule

When a valid file path is available, read the artifact rather than relying only on the conversation history.
