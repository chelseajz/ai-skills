# Report Standard

## Default structure

Use this structure unless the user asks for another format:

1. Background and objective
2. Method and sample
3. Executive findings
4. Recommended actions
5. Detailed analysis
6. Limitations and open questions
7. Appendix

Placing recommendations right after executive findings lets decision-makers see "what we found → what to do" in one pass without scrolling through the full analysis body. Readers who want the evidence can continue into the detailed analysis section.

For mixed-method work, also use [mixed-method-integration.md](mixed-method-integration.md).
For substantial multi-step work, keep outputs aligned with [artifact-interface.md](artifact-interface.md).
Use consistent references from [citation-style.md](citation-style.md).

Default interpretation for mixed-method work:
- prefer one complete main report that contains both core conclusions and detailed findings
- organize the body by business question or finding theme
- do not split the whole body into `quantitative findings` and `qualitative findings` unless the methods are answering materially different questions

For leadership-facing substantial work, prefer a two-layer package:
- one formal main report with both concise conclusions and full support, standalone as the source of truth
- one compressed meeting or readout version for fast circulation
- supporting quant, qual, and asset files beneath those two top-layer outputs
- when the report is destined for a rich-doc tool, build in reading order so charts sit beside the claims they support

## Section requirements

For one-report workflows serving multiple roles, also use [single-report-multistakeholder.md](single-report-multistakeholder.md).

### 1. Background and objective

Include:
- why this research was conducted
- the decision it supports
- the research questions

### 2. Method and sample

Include:
- data source description
- collection window
- sample size and important segment definitions
- cleaning, deduplication, or linkage notes
- limitations that affect interpretation

If the study is mixed-method, explicitly state:
- whether data sources were linked
- what the match rate was
- whether the interview sample differs from the survey base

Prefer compact tables over long prose for:
- stage-by-stage sample counts
- raw -> deduped -> target-population -> question-valid sample funnel
- linkage and effective sample
- what each evidence source primarily supports
- major sample skews or interpretation limits

When multiple denominator choices are possible, name them explicitly:
- raw rows
- deduped respondents
- target-population base
- question-valid base

Do not let a report imply these are the same sample.

### 3. Executive findings

Include 3-7 findings. Each should have:
- a one-sentence takeaway
- supporting evidence in brief
- confidence label
- plain language that a non-research stakeholder can understand on first read

Suggested format:

```markdown
**Finding:** [one-sentence conclusion]
Evidence: [metric, quote, or both]
Confidence: High | Medium | Low
Why it matters: [decision relevance]
```

For substantial reports, front-load only the most decision-relevant points here. Do not try to compress the entire study into the executive section. The body should still contain the full reasoning, boundary conditions, and supporting evidence.

Preferred format when space allows:

```markdown
**Finding:** [clear bounded conclusion]
What we saw: [specific metric, subgroup, or behavioral pattern]
User reality: [short quote or scene]
Confidence: High | Medium | Low
Why it matters: [decision relevance]
```

When the report is substantial and leadership-facing, place this section before the body and keep it compact:
- 3-7 conclusions only
- each conclusion starts with the number or evidence anchor when available
- each conclusion is followed by a short interpretation in plain language
- each conclusion carries a confidence label
- any directional-only claim is clearly marked as such
- if a conclusion uses a filtered denominator, name that denominator in the sentence instead of leaving it implicit
- keep the support layer scannable: prefer one bounded takeaway line, one compact support table or chart, and a few high-signal bullets rather than dense explanatory prose
- if the audience is executive-heavy, add one obvious bullet-list summary and one one-sentence summary before the full body

### 4. Recommended actions

Place this immediately after executive findings so decision-makers get "what we found → what to do" without reading the full analysis.

Recommendations must be:
- specific
- attributable to findings
- realistic to execute
- measurable where possible

Suggested fields:
- priority
- action
- supported by finding(s)
- expected impact
- risk or dependency

Also state who most needs to act on the recommendation:
- leadership
- product
- design
- operations

### 5. Detailed analysis

For each key theme:
- present evidence
- explain interpretation
- note meaningful variation or exceptions
- tie back to the business context
- include enough user context that readers can picture the situation, not just memorize a label
- keep the voice in researcher mode; do not add packaging notes or "how to read this file" commentary inside the finding body unless the user explicitly asks for a methods note

Preferred block structure for major findings:
- one-line conclusion
- key numbers
- detailed analysis
- key case summary or case table
- representative quote or scene
- business implication
- include the detailed support in the same report if this is the formal main report, rather than forcing readers into a separate "detailed findings" document for core understanding

Preferred finding block for the formal main report:

```markdown
### [Finding title]

**Conclusion**
[one short, concrete conclusion]

**What the numbers show**
- [metric]
- [subgroup difference or test]

**How users describe it**
> [short quote]

**Typical case**
[2-4 sentence case summary with scene, choice, barrier, and outcome]

**How to read this finding**
[interpretation, boundary, exception, or implication]
```

For mixed-method findings, make clear whether the relationship is:
- agreement
- tension
- complementarity

When quant and qual address the same issue:
- integrate them into one finding block
- let the numbers establish scale or structure
- let the interviews explain mechanism, scene, or trade-off

When a user-requested capability is not confirmed feasible:
- report it as a strong need, friction, or expectation
- explicitly separate that from any product commitment
- if needed, place it in a dedicated discussion or dependency subsection

When the main report uses direct quotes:
- use a natural reader-facing tag that includes the case id and enough profile context for the reader to understand the speaker
- define one reader-facing case id system and stick to it through the whole report
- do not leave raw trace labels or internal ids in the polished report
- for detailed case labeling conventions and identifier discipline, see [delivery-formatting.md](delivery-formatting.md)

When the same detailed finding appears in both a main report and a companion file:
- keep the fully readable version inside the main report
- use companion files to add depth, not to hold essential interpretation that the main report lacks
- avoid forcing readers to switch documents to understand the core evidence chain
- if the companion file is a reference layer, refer to it as a supporting analysis layer rather than as a handoff instruction

When multiple detailed discovery documents exist, the formal main report should absorb the important findings rather than merely pointing outward. Separate detail files can still exist for auditability, but the main report should remain readable on its own.

When the report uses multiple count systems (e.g., multi-select vs mutually-exclusive recoding):
- state the systems explicitly and do not place them side by side as if they share a denominator
- for detailed rules, see [delivery-formatting.md](delivery-formatting.md)

### 6. Limitations and open questions

Always include:
- sample and method limitations
- places where evidence is directional only
- what requires follow-up validation

### 7. Appendix

May include:
- codebook
- cross-tabs
- extra charts
- key chart index
- respondent profiles
- glossary and metric definitions
- finding ledger
- segment cards
- quote bank
- detailed findings companion
- decision and conversion analysis
- product feedback deep-dive
- case sampling note
- decision log
- linkage note
- integration memo
- proposition list

## Casebook and quote-bank packaging

When a report includes a casebook or quote digest:
- explain the case sampling logic
- cover major user types, decision paths, and edge cases rather than only vivid examples
- keep bucket names faithful to the actual inclusion rule
- if a bucket mixes `true no need`, `weak need`, and `strong substitutes`, rename it to reflect that boundary logic
- ensure each case is rich enough to reconstruct the scene, workaround, friction, and implication
- if a case is described as representative or typical, the rationale must be consistent with the segment label and the quote evidence shown in the case
- for language-specific prose conventions, see [delivery-formatting.md](delivery-formatting.md)

For product-demo or prototype-feedback sections:
- keep issue labels behaviorally specific when the evidence supports it (e.g., "unclear where funds go" rather than just "trust issue"; "confused by currency switching" rather than just "usability problem")
- avoid collapsing distinct issues into one vague bucket if that would hide different design or communication implications

## Quantitative support packaging

When a support table is meant for downstream charting or audit:
- separate absolute counts and percentages into distinct columns or fields
- keep one row model that can be filtered, pivoted, or charted without manual cleanup
- include a directory or navigation area for large support sheets
- also keep a fast-reading crosstab or wide-table companion when stakeholders need to scan tables directly
- preserve test statistics, base sizes, notes, and subgroup labels
- do not make the support layer a thin summary if the report depends on many cuts or crosstabs

When a report reuses older analyses or legacy drafts:
- compare sample funnels before copying any number
- rewrite any inherited statement whose denominator no longer matches the current analysis base
- never merge old and new counts in one package without an explicit reconciliation note

## Rich document delivery

For detailed rich-document delivery rules (Feishu, Notion, Google Docs), case labeling, and Chinese-language conventions, see [delivery-formatting.md](delivery-formatting.md).

Key principles:
- place charts next to the argument they support, not only in a terminal appendix
- remove raw markdown artifacts and placeholder links from reader-facing documents
- if the tool cannot reliably place charts in one pass, rebuild in reading order

## Writing bar

- Lead with the answer, not the process.
- Use precise language and concrete numbers.
- Avoid inflated certainty.
- Keep the tone neutral and professional.
- Make it easy for a busy stakeholder to scan.
- Avoid AI-sounding filler, management cliches, and vague intensifiers.
- Use short, direct sentences for conclusions.
- For important findings, pair summary language with supporting data and at least one vivid user quote or scene.
- Do not over-compress the report so much that users stop sounding like real people.
- If the audience will consume the report in Feishu or a similar rich-text system, structure the document so important callouts can become highlights, quotes, and compact tables without redesigning the argument.
- Use tables when they reduce reading load, especially for method summary, sample accounting, linkage rate, segment comparison, recommendation matrix, or product feedback summary.
- Put charts next to the argument they support. Do not leave them only in an appendix unless they are secondary.
- Before treating a report as final, clear all drafting residue such as `待补`, `TBD`, `to fill`, note-to-self text, and half-resolved placeholders.

## Anti-generic writing test

Rewrite a passage if any of these are true:
- it could describe almost any app or service
- it names a `pain point` but not the concrete moment causing it
- it says users `need trust`, `want convenience`, or `seek efficiency` without showing how that appeared in the data
- it recommends `optimize`, `strengthen`, or `improve` without naming the object and expected effect

## Leadership-ready additions

When the audience includes executives, also include:
- one page of decision-ready summary before the body
- a short list of decisions enabled by this research
- the top risks of misreading the data
- a note on what should happen now versus what needs more validation
- a report structure where readers can stop after the summary or continue into the detailed evidence without switching documents
- concise highlight blocks for decisions, risks, and "do not over-read this" warnings

For that format, use [executive-report-template.md](executive-report-template.md).
