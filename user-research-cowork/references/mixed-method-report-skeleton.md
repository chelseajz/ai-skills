# Mixed-Method Report Skeleton

Use this when one study combines survey data and interviews, and the final deliverable must work for both executives and working teams.

Default stance:
- produce one complete main report that combines core conclusions and detailed findings
- organize the body by integrated business questions or finding themes, not by method unless separation is analytically necessary
- keep separate quant and qual files as support layers, appendices, or audit trails

## 1. Title and decision line

```markdown
# [Study title]

## What decision this supports
- [Decision 1]
- [Decision 2]
```

## 2. Executive summary

Keep this to one page or one screen.

```markdown
## Executive summary

### What we found
- [Finding 1]
- [Finding 2]
- [Finding 3]

### Why it matters
- [Business implication 1]
- [Business implication 2]

### What to do now
- P0: [Action]
- P1: [Action]

### What not to overread
- [Key caveat]
```

## 3. Executive bullets for leadership

Use 3-5 bullets, each with:
- one bounded conclusion
- strongest metric
- one short quote or scene
- no dense explanatory paragraph below the bullet unless it is needed to stop overreading

Also add:
- one one-sentence study summary
- one obvious bullet-list block that a leader can scan in under a minute

```markdown
## Leadership takeaways

- [Conclusion]. Evidence: [metric]. User reality: [quote or scene].
```

## 4. Method and sample

Prefer tables over long prose.

```markdown
## Method and sample

| Stage | n | Notes |
|:---|---:|:---|
| Survey total | [n] | [note] |
| Valid survey | [n] | [note] |
| Target subgroup | [n] | [note] |
| Interview total | [n] | [note] |
| Linked interviews | [n] | [note] |
| Main qualitative sample | [n] | [note] |

| Analysis layer | Primary source |
|:---|:---|
| Market size / structure | Survey |
| Motivation / workaround / pain points | Interviews |
| Integrated conclusions | Mixed-method |
```

Also include:
- linkage rule
- key sample skews
- what each source can and cannot support

## 5. Integrated findings

This should usually be the main body of the report.

Preferred logic:
- one section per business question or decision area
- combine quant and qual in the same section when they speak to the same issue
- only break out a method-specific subsection when one method adds a clearly complementary layer

Suggested finding format:

```markdown
## F1 [integrated finding title]

### What is happening
[bounded conclusion in plain language]

### Evidence
- Quant: [metric + denominator + subgroup + test if relevant]
- Qual: [mechanism, scene, or friction]

### What this means
[interpretation and implication]

### Why it matters
[product / ops / risk / leadership implication]

### Key exhibit
- [chart or table reference]

### User reality
> [1-2 strong quotes or scene fragments]
```

Typical integrated sections might include:
- demand size and conversion structure
- user segments or borrowing types
- scenario and use-case differences
- decision factors and conversion drivers
- product concept or demo feedback
- unresolved discussion points or dependency-sensitive opportunities

When the integrated section is about product concept or demo feedback, prefer this sub-structure:
- landing perception
- usage understanding
- conversion blockers
- improvement requests

If one row aggregates several closely related sub-issues, write the composition explicitly instead of using opaque slash counts. For example, prefer `认为资金会到银行卡 n=64；不清楚钱会去哪里 n=21` over `64 / 21`.

## 6. Method-specific deepening when needed

Use this only when a separate layer materially helps the reader.

Examples:
- a short `Quantitative deepening` subsection for full significance results
- a short `Qualitative deepening` subsection for mechanism, decision logic, or scene detail
- a standalone discussion subsection for strong user needs that product feasibility has not confirmed

```markdown
### Discussion point: [topic]
What users are signaling: [need or friction]
What remains unresolved: [feasibility / policy / dependency]
How to use this insight: [design principle, communication need, or decision question]
```

## 7. Mixed-method synthesis

Always separate these three buckets:

```markdown
## Mixed-method synthesis

### Agreement
- [survey and interviews point the same way]

### Tension
- [survey and interviews differ, or one highlights a different priority]

### Complementarity
- [survey shows where; interviews explain why]
```

## 8. Role-specific recommendations

Keep one shared table.

```markdown
## Recommendations

| Priority | Action | Owner role | Supported by | Expected impact | Risk / dependency |
|:---|:---|:---|:---|:---|:---|
| P0 | [action] | Leadership / Product / Design / Ops / Risk | [finding ids] | [impact] | [risk] |
```

## 9. Limitations and open questions

Include:
- sample bias
- linkage limits
- testing or measurement limits
- unresolved product questions
- any user-requested feature that should be treated as a discussion point rather than an implied commitment

## 10. Appendix package

For substantial studies, append or link to:
- cross-tab pack
- chartbook
- detailed findings companion if the main report must stay shorter
- key-chart index
- interview profiles
- codebook
- user patterns
- decision and conversion analysis
- product feedback deep-dive
- quote bank / voice digest
- casebook
- case sampling note
- finding ledger
