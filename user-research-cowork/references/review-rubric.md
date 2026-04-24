# Review Rubric

Use this rubric before treating a report as publish-ready. It is also the default audit framework when reviewing a report written by someone else.

Typical standalone use cases:
- review a teammate's draft before leadership circulation
- audit a vendor or agency report for methodological and decision risk
- harden an AI-generated report before it is used by business teams

## Reviewer mode

### Context isolation for Gate 3 subagent review

When this rubric is used by the Gate 3 independent reviewer subagent, strict input control applies.

**Allowed inputs:**
- The final report draft (the document being reviewed)
- This rubric (the evaluation standard)
- Source artifacts for fact-checking: finding ledger, crosstabs, quote tables, sample notes

**Blocked inputs:**
- Writing agent's chain-of-thought or drafting history
- Codebook evolution notes or finding-classification rationale
- Strategy discussion history between user and writing agent (unless a specific decision is needed to judge report scope)
- Intermediate drafts or revision notes

The subagent must treat the report as if written by an unknown author and evaluate it purely on the evidence presented. If the reviewer sees why the writer made each choice, it stops being an independent audit and becomes a rationalization exercise.

### General review rules

When the user asks for a review:
- list findings first
- order them by severity
- focus on factual errors, evidence gaps, reasoning flaws, bias, and decision risk
- keep praise brief and secondary

Use severity labels:
- P0: report should not be used for decision-making until fixed
- P1: important weakness that materially lowers trust or usefulness
- P2: worthwhile improvement in clarity, framing, or structure

For each finding, include:
- what is wrong
- why it matters
- what evidence is missing or contradictory
- the smallest credible fix

When the reviewed report was authored by someone else, also check:
- whether the report is auditable without access to the author's head
- whether important assumptions were hidden in wording rather than stated directly
- whether polished presentation is masking weak evidence or weak linkage

## 1. Method transparency

Check:
- Can a reader understand where the data came from?
- Are sample, timeframe, cleaning, and linkage rules described?
- Are limitations concrete rather than generic?

## 2. Evidence integrity

Check:
- Do important numbers reconcile across sections?
- Do denominator choices reconcile across sections, files, charts, and legacy drafts?
- Does each key claim have evidence?
- Are quote sources and metric definitions traceable?
- Are chart takeaways consistent with the underlying data?
- If significance or subgroup differences are claimed, are the tests, sample sizes, and direction of difference actually shown?
- Are p-values written in a standard interpretable way, for example `p<0.001` rather than impossible precision such as `p=0.0000`?
- If case ids are shown in reader-facing quote labels, do they correspond to the real interview/case id system rather than to questionnaire ids or linkage ids?
- If the same concept appears with two different `N`, is that because two coding systems are being mixed, and is that difference clearly explained before interpretation?
- If the package contains a quantitative support table, is it reusable for audit and re-charting without manual cleanup, including separate count and percent fields where needed?
- If old reports or old tables were reused, was their sample funnel reconciled before numbers were carried over?
- If the report is meant for Feishu or another rich-doc tool, are charts placed in the reading flow rather than dumped into an appendix-like block?

## 3. Reasoning quality

Check:
- Is the jump from evidence to conclusion justified?
- Are correlation and causation kept separate?
- Are alternative explanations or exceptions considered?
- Are confidence labels proportional to the evidence?

## 4. Insight depth

Check:
- Does the report explain why, not only what?
- Does it identify tensions, trade-offs, or hidden mechanisms?
- Does it avoid repackaging obvious observations as insights?
- For qualitative work, does it go beyond theme summary into pattern logic, decision logic, barriers, and conversion drivers?

## 5. Communication quality

Check:
- Can the reader grasp the main message quickly?
- Are findings concise, scannable, and decision-relevant?
- Are vague terms replaced by numbers or bounded statements?
- Does the report sound concrete and human, rather than generic or AI-written?
- Does the report stay in researcher voice, or does it drift into delivery-management language, packaging notes, or usage instructions?
- Do leadership-facing findings compress to a takeaway line plus compact support, or are they still dense blocks of explanatory prose?
- Do key sections retain user scenes, tensions, and real wording instead of flattening everything into abstract labels?
- If charts are included, do they use a coherent system rather than looking like mixed templates?
- If the package includes a formal report and a meeting version, do they share the same claims, caveats, and decision logic?
- In Feishu or other rich-doc outputs, are there any raw markdown image strings, broken local paths, or misplaced charts left visible to readers?
- In tool-rendered deliverables such as Feishu docs, are images placed near the right argument, and is the document free of stray markdown image syntax or formatting residue?
- If the report has a formal version and a meeting version, are they materially aligned rather than competing sources of truth?

## 6. Decision usefulness

Check:
- Do recommendations clearly connect to findings?
- Are they specific enough to execute?
- Are risks, dependencies, and measurement considerations noted?
- Is it clear which functions should act on which conclusion, even though the report is shared?
- If users repeatedly request an experience that may not be feasible, does the report frame it as a discussion point or dependency rather than an implied shipped commitment?

## 7. Multi-stakeholder usefulness

Check:
- Can leadership quickly see the decision implications?
- Can product see which journey step or behavior needs intervention?
- Can design see what confusion, unmet expectation, or trust issue is actually happening?
- Can operations see what service or process issue needs attention?
- Does the report achieve this without duplicating itself into separate audience versions?

## 8. Delivery system quality

Check:
- Is there one clear source-of-truth main report?
- If a compressed meeting deck or memo exists, does it faithfully compress rather than reinterpret the main report?
- Are key charts placed near the findings they support?
- Are casebook sections named accurately based on their inclusion logic?
- Are quantitative support tables reusable for charting, with counts and percentages separated and enough navigation to audit them quickly?
- Does the formal main report stand on its own, or does it improperly depend on external detail files for core understanding?
- If a casebook is included, does each case's "why selected" note match the segment label and the quote evidence, or does the rationale conflict with the case content?
- If a decision / pattern / demo deep-dive exists, is there enough original user voice to support the interpretation, or does the section collapse into statistics alone?
- If a table row aggregates several related issues, is the composition explicitly explained rather than shown as unexplained slash counts?
- Are polished reader-facing quote labels standardized, or does the document still expose raw internal id tags?
- If quote labels were standardized, were any ids silently converted into the wrong numbering system during cleanup?
- For detailed case labeling and identifier discipline rules, see [delivery-formatting.md](delivery-formatting.md)

## Adversarial checks

Stress-test each major conclusion with questions like:
- What would make this conclusion false?
- Is this actually description disguised as explanation?
- Does the data support scope, or only direction?
- Is the report confusing self-report, observed behavior, and inferred motivation?
- Would a skeptical product lead say "show me the evidence" and get a clear answer?
- Are recommendations stronger than the evidence allows?

## Evidence trace test

For each executive finding, verify the chain:

```text
Finding -> source metric or quote -> definition / context -> limitation
```

If any link is missing, the claim is not yet publish-ready.

## Common report failures

- Executive summary overclaims compared with the body
- Limitations exist but do not constrain the final recommendation
- Quotes are vivid but not representative of the underlying pattern
- Quantitative cuts are exhaustive but not decision-relevant
- A causal story is presented without enough support
- Recommendations are generic, unprioritized, or not traceable to findings
- The prose is polished but interchangeable, with too many empty words and too little observed reality
- The report over-summarizes users until their actual need, fear, or workaround is no longer visible
- The report looks polished but cannot be audited because tables, tests, quotes, or linkage logic are missing
- The report mixes raw-row counts, deduped counts, and filtered analytic bases without naming the switches
- Charts appear to come from multiple incompatible styles, weakening trust in the package
- The document contains visible markdown residue, local file paths, or chart placeholders from the authoring workflow
- The main report depends on a separate "detailed findings" file to make core claims intelligible
- Casebook labels overstate certainty by naming edge or weak-demand buckets as `no need`
- Quantitative support files are too summarized to reproduce or extend the report's charts
- The main report is too thin, forcing readers into separate detailed-finding files for the actual argument
- The exported or synced document contains raw markdown image paths, broken chart placement, or formatting artifacts that make the package look unfinished
- Casebook buckets are mislabeled in ways that distort the real user distribution or imply users had no demand when they actually had weak, deferred, or already-solved demand
- A rich-doc report was built by overwrite and ended up dumping charts into the appendix rather than placing them in reading order
- The report explains a companion file as a usage note instead of as a supporting analysis layer
- The report still contains drafting residue such as `待补`, `TBD`, `to fill`, or note-to-self placeholders
- Demo or prototype feedback is reported only as vague high-level labels (e.g., "trust issues") even though the evidence supports more actionable issue-level categories

## Final gate

A report is not ready if any of these remain:
- core figures cannot be traced
- core figures use inconsistent or unnamed denominators
- limitations are omitted or materially understated
- key recommendations are not grounded in findings
- qualitative evidence is used as if it were population-representative
- reader-facing deliverables still contain obvious formatting residue or broken chart placement
