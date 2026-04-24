# Qual Packaging Standard

Use this when the user wants a deeper qualitative analysis package, not just a theme summary.

## 1. Minimum qualitative package

For substantial interview-based work, preserve at least:

1. Interview profiles
2. Immersion memos
3. Codebook
4. Pattern analysis
5. Quote bank or voice digest
6. Casebook

Add these when the study is decision-heavy, behavior-heavy, or product-feedback-heavy:
- decision and conversion analysis
- product feedback deep-dive
- case sampling note

## 2. Sample and limitation standard

Always state:
- interview count
- linked / unlinked status if mixed with survey data
- quality tiers if relevant
- what makes the sample stronger
- what makes it biased or narrow
- what qualitative evidence can and cannot support

Do not hide sample bias in an appendix if it affects the main conclusions.

## 3. Pattern standard

Patterns should be organized by:
- need
- motivation
- workaround
- barrier
- decision logic
- conversion driver
- trust or feasibility concern

Do not rely on pure demographic buckets unless the research question is specifically demographic.

For each major pattern, include:
- short pattern name
- what defines it
- typical trigger scene
- common workaround
- main pain points
- key conversion driver
- key blocker or trust break
- where the pattern breaks or varies
- product or business implication

## 4. Quote density standard

For major findings:
- main report: usually 1-3 strong quotes or scene fragments
- supporting asset: usually 5+ traceable quotes if the user wants rigor or reusability

Each quote should ideally carry:
- respondent id
- relevant profile or label
- source question

For polished main-report quotes, prefer a natural tag format such as:
- `——案例#247，常驻内地，23-30岁，在校学生，有需求未借过`

If full profile detail is unavailable, use a bounded fallback such as:
- `——案例#1278，产品反馈样本`

Avoid leaving raw audit strings such as `来源：ID...` in a reader-facing final report unless the user explicitly wants audit-first formatting.

Prefer quotes that show reasoning, trade-offs, or emotion. Avoid only keeping short slogan-like lines.

For decision factors, pattern analysis, demo feedback, or scenario analysis, do not reduce the asset to counts plus one or two quotes. Preserve enough original voice that the mechanism is believable and the user's own logic is visible.

For product-demo or concept-feedback analysis, preserve issue-level granularity when the evidence allows it. Distinguish between items such as:
- funds destination
- currency logic
- repayment mechanism
- pricing or fee explanation
- institutional backing or lending主体 clarity

Do not collapse these into one generic bucket such as `trust` if doing so would hide materially different design or communication problems.

## 5. Casebook standard

Each case should include:
- profile
- event background
- scene reconstruction
- direct quote(s)
- workaround
- decision logic
- implication
- why this case was selected
- which finding, pattern, or sample bucket it is meant to support

If a case is included mainly as a boundary example, weak-evidence example, or counterexample, label that role explicitly at the case level instead of leaving readers to infer its weight.

The casebook should feel like a human reality layer, not a compressed summary.

If the casebook is meant to represent the study rather than only illustrate one idea, add a short sampling note that explains:
- which segments or states were covered
- why the selected cases are not all from one extreme
- which combinations were intentionally included, such as label x need state x borrowing history
- how boundary buckets are defined when they mix `no demand`, `weak demand`, `already solved demand`, or `mature substitute` cases
- if the case includes a "why selected" line, make sure it agrees with the segment label and the quote evidence shown in the case

## 6. Deep-analysis add-ons

When the user asks for more than a summary, consider adding dedicated assets for:
- user patterns by behavioral logic rather than demographics
- decision factors and conversion drivers
- product-demo or concept-feedback analysis
- negative cases or counter-patterns
- interview quality tiers and representativeness notes

These assets are especially important when the report must support product, risk, ops, and leadership at the same time.

## 7. Failure modes

- Converting all interviews into abstract theme bullets
- Losing the user's scene and sequence of events
- Using only one quote for an important finding
- Hiding limitations about linkage or sample quality
- Naming a pain point without describing the moment that produced it
- Picking cases opportunistically with no coverage logic
- Putting cases into misleading buckets, such as labeling them `no need` when they actually show low-priority or already-resolved need
- Describing motivation and pain points without explaining decision or conversion mechanics
