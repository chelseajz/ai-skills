# Quant Reporting Standard

Use this when the user asks for full statistical analysis, significance tests, cross-tabs, or a chartbook rather than a light summary.

## 1. Minimum quantitative package

For substantial survey work, preserve all four:

1. Descriptive analysis
2. Cross-analysis tables
3. Statistical test output
4. Chartbook

Do not stop at a prose summary if the user asked for depth.

## 2. Cross-tab selection rule

Prefer decision-relevant cuts, not exhaustive all-by-all slicing.

Good cross dimensions often include:
- need state or adoption state
- important user labels or segments
- usage frequency
- identity or eligibility status
- income or value proxy
- major purpose or scenario
- expected amount, frequency, term, or repayment preference

## 3. Statistical testing rule

When the user asks for statistical differences, or when the report would otherwise imply differences between groups, prefer running a test instead of using hand-wavy wording.

For category-by-category comparisons, the default package is:
- Pearson chi-square
- p-value
- effect size such as Cramer's V
- adjusted standardized residuals or an equivalent cell-level explanation

If assumptions are weak, say so near the result.

Do not report impossible precision such as `p=0.0000`. Use standard threshold language such as `p<0.001`.

## 4. Table standard

Each important cross table should include:
- count
- row or column percentage
- total n
- test result
- note on low expected cells when relevant

If one business issue row combines multiple related coded sub-items, do not leave the table as an unexplained slash sequence such as `64 / 21` or `34 / 33 / 30`.
Instead:
- rename the column to `statistical composition`, `component counts`, or an equivalent label
- write each sub-item explicitly, for example `认为资金会到银行卡 n=64；不清楚钱会去哪里 n=21`
- note when one respondent can contribute to more than one sub-item so readers do not incorrectly sum them

## 5. Chart standard

Use a consistent, professional, color-blind-friendly palette across the whole report.

Default visual logic:
- single-series bar or column charts: one fixed primary color across the entire package
- semantic status charts: fixed status mapping reused chart to chart
- multi-series comparison charts: use a fixed, documented series mapping rather than ad hoc recoloring
- ordered variables such as age, income, visit frequency, amount, term, or usage frequency: preserve business order, not value-ranked order

Each reusable chart should include:
- conclusion-led title
- question number
- question text
- base / sample size
- percent rule
- recode note if categories were simplified
- test note if significance is shown

Do not put file paths in chart notes.

If significance is shown on the chart:
- use simple labels such as `significantly higher` or arrows
- keep the exact statistic in the footnote or the corresponding table

For cross charts:
- include subgroup sample size in the axis label or legend label, for example `High income (n=84)`
- if many cells make grouped bars hard to read, prefer a heatmap, labeled table chart, or another clearer format
- if only a subset of cells differ significantly, highlight the affected items rather than covering the whole chart with statistics
- when the report is meant for rich-doc consumption, build charts into the chapter where the finding appears rather than dumping them in an end appendix block

For chartbooks:
- use human-readable titles in the index, not only raw filenames
- provide a short key-chart index for business readers if the package is large

## 6. Recommended packaging

For thick deliverables, a good set is:
- `survey_analysis.md`
- `cross_analysis_tables.md`
- `chartbook.md`
- `key_chart_index.md`
- `results.json` or CSV exports for reuse

## 7. Failure modes

- Reporting cross-tabs with no denominator
- Implying significance without running a test
- Showing significance with no effect size
- Recoloring categories from chart to chart
- Sorting ordered categories by percentage instead of business order
- Using rainbow colors for single-series charts
- Using unreadable grouped bars for high-cardinality cross-tabs
- Making charts impossible to interpret without opening the raw spreadsheet
