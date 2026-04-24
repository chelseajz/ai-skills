---
name: user-research
description: 用户研究全流程支持。适用于互联网产品用户研究规划、定性编码、问卷分析、混合方法研究、报告撰写与审核。尤其适合产出具有明确证据链、置信度标注、局限性说明和专业可落地建议的高质量研究报告。ALWAYS use this skill when the user mentions 用户研究、UX研究、用户访谈、问卷分析、定性分析、访谈编码、研究报告、可用性研究、焦点小组、研究发现、混合方法、交叉表、语录库、编码本、案例集、访谈记录、讨论指南、研究方案、筛选器，或任何涉及将原始用户数据转化为结构化研究产出物的任务 — 即使用户没有明确说"研究"。同时提供新手友好引导入口（user-research-guided），非用研背景的同事也可快速上手。
---

# User Research

This skill turns broad "do research" requests into a disciplined workflow that protects evidence quality and report credibility.

Use it for:
- Research planning for product, growth, monetization, retention, trust, service, or experience topics
- Qualitative analysis of interviews, tickets, feedback, chats, or call notes
- Survey analysis and mixed-method synthesis
- Writing or reviewing research reports for product, design, operations, strategy, or leadership
- Auditing and revising reports written by agencies, vendors, teammates, or other AI systems

Do not use it for:
- Pure market news lookups with no user data
- Fabricating research findings or overstating weak evidence
- Treating small qualitative samples as representative population estimates

## Human-AI collaboration model

Not every research step should be fully automated. This skill follows a three-zone model inspired by current best practices in AI-assisted research (REFINE framework, Great Question 6-step pipeline, and the augmentation-not-replacement consensus). The zones determine when Claude acts autonomously, when it proposes for human review, and when it must defer to human judgment.

### Zone 1 — Claude autonomous

Claude executes and moves on. No confirmation needed unless the user has asked for step-by-step approval.

- Data inventory, cleaning, deduplication, sample funnel construction
- Descriptive statistics, cross-tabs, significance tests, chart generation
- Transcript structuring (timestamping, speaker labeling, segmentation)
- Initial open coding (first-pass thematic tagging)
- Pattern extraction and candidate pattern surfacing
- Quote and case selection following evidence rules
- Confidence labeling (High/Medium/Low) based on evidence strength
- Report scaffolding, denominator reconciliation, formatting, packaging
- Red-teaming against review-rubric.md and auto-fixing mechanical issues
- Iteration triage (P0/P1/P2 categorization) and applying fixes
- Executive compression following template
- Assumption statements (state and proceed; flag non-obvious ones in output)

### Zone 2 — Human checkpoint (3 gates)

These are the only points where Claude pauses and waits for user input. Each gate controls a phase transition where wrong direction is costly to reverse.

**Gate 1 — Codebook confirmation** (after initial coding, before full analysis)
Claude presents the proposed codebook (10-15 codes with definitions and examples). User reviews, merges, splits, or adds codes. This shapes the entire downstream analysis — getting it wrong means recoding everything.

**Gate 2 — Finding / hypothesis / noise classification** (after draft findings, before report assembly)
This is the single most consequential checkpoint. Many report problems — inflated summaries, overloaded recommendations, titles that promise more than the data delivers — trace back to this step not being done rigorously enough. Claude presents each candidate finding and the user must decide its status:
- **Promote to formal finding**: evidence is strong enough to anchor a report section and drive a recommendation.
- **Keep as directional signal**: pattern exists but evidence is incomplete, sample is narrow, or effect is small. Label as Low confidence and do not let it drive a P0 recommendation.
- **Downgrade confidence**: the pattern looked strong at first glance but has caveats that need to be stated alongside the conclusion, not buried in limitations.
- **Add caveat or boundary**: the finding holds for a subgroup or scenario but not universally. Narrow the claim before it enters the report.
- **Drop as noise**: insufficient support, single-source anecdote, or pattern that dissolves under negative-case review.
Default stance is conservative: do not promote to formal finding unless evidence strength, denominator stability, and counter-example explanation are all adequate. If any one of these is insufficient, default to directional signal, downgrade confidence, or add boundary — not promote. Without this discipline, models tend to over-promote findings to make the report feel more complete, which inflates conclusions and erodes stakeholder trust.

Claude presents this as a structured table (candidate finding → proposed status → reasoning → supporting evidence → counter-signals). The user reviews and adjusts. Nothing proceeds to report assembly until this classification is locked.

**Gate 3 — Independent report quality review** (after complete report draft, before finalization)
This gate solves **research quality problems** — it is not about whether to publish.

To avoid self-review bias (the same model defending its own writing choices), Gate 3 uses an **independent reviewer subagent** under strict input control.

The subagent receives ONLY:
1. The final report draft (the document being reviewed)
2. [review-rubric.md](references/review-rubric.md) (the evaluation standard)
3. Source artifacts necessary for fact-checking: finding ledger, crosstabs, quote tables, sample notes — whatever the reviewer needs to verify claims against raw evidence

The subagent does NOT receive:
- The writing agent's chain-of-thought or drafting history
- Codebook evolution notes or finding-classification rationale
- Strategy discussion history between user and writing agent (unless a specific decision is needed to judge report scope)
- Any intermediate drafts or revision notes

This boundary matters: if the reviewer sees why the writer made each choice, it stops being an independent audit and becomes a rationalization exercise. The goal is a fresh-eyes review — closer to how a senior researcher would audit a report they did not write.

The subagent produces a severity-ordered issue list covering:
- Evidence-chain gaps or denominator inconsistencies
- Red-team issues classified as P0 (block publication) / P1 (improve but not block) / P2 (nice to have)
- Interpretations that cross the line from supported inference to speculation
- Recommendations that exceed the strength of the supporting evidence — a recommendation anchored to a Low-confidence or directional-only finding must be flagged
- Ethical, compliance, or bias concerns that need to be addressed in the report text

The user reviews the subagent's issue list and decides which issues to fix. The original writing agent then applies the approved fixes, retaining full context of how findings were built. For review tasks, this is where the user decides whether to accept the issue list or ask for proposed fixes.

### Zone 3 — Human decision (2 points)

Only two moments require human authority. Everything else Claude handles or folds into Gate 2.

**Start — Scope confirmation**
If the user's request is missing the business decision, audience, or data files, Claude asks once upfront. If all three are clear from context, skip this entirely and start working. For review tasks, also confirm: list issues only, or also propose fixes?

**End — Publication sign-off**
This solves **business release problems** — distinct from Gate 3's research quality review. Claude presents the finalized package and the user decides:
- Whether this version can be released, or needs to be held
- Who receives it and in what order (e.g., leadership first, then product, then broader circulation)
- Whether the tone needs to be adjusted for the audience (e.g., soften a sensitive finding for external stakeholders, add context for a cross-functional audience)
- Whether any finding needs to be flagged for escalation before wider distribution

### How to apply the zones

- Zone 1 (most steps): execute and move on. Report results in output but do not wait for confirmation.
- Zone 2 (3 gates): produce a clear proposal, explain reasoning, pause for user input. If the user has said "just go ahead," proceed but flag key decisions.
- Zone 3 (2 points): ask once at the start if scope is unclear; ask once at the end for sign-off. Do not create additional stops.

## Core principles

These principles apply to every output from this skill. They exist because research that lacks these qualities gets misread, misused, or ignored by decision-makers.

- **Be objective**: separate observation, interpretation, and recommendation. Mixing them erodes trust.
- **Be traceable**: every important claim should point to a metric, quote, or both. Untraceable claims invite challenge.
- **Be bounded**: state what the data can and cannot support. Over-claiming destroys credibility faster than under-claiming.
- **Be decision-oriented**: recommendations must connect to concrete product or business choices. Abstract advice wastes stakeholder time.
- **Be anti-hallucination**: if evidence is missing, say so plainly and lower confidence. Readers respect honesty.
- **Be denominator-disciplined**: do not mix raw rows, deduped respondents, valid-question bases, and target-segment bases without naming each base explicitly. Denominator confusion is the single most common quant error.
- **Be concrete in language**: avoid inflated AI-style phrasing, empty abstractions, and generic business cliches. If a passage could describe any app or any service, it needs rewriting.
- **Keep researcher voice**: write as analysis, not as delivery management. Avoid meta narration about handoff, packaging, or "how to use this file" inside the research body.
- **Keep the user alive on the page**: preserve real scenes, tensions, and phrasing instead of over-compressing everything into abstract labels. Reports that feel like they were written by someone who never met a user lose influence.
- **Prefer integrated reporting**: when quant and qual answer the same question, combine them into one finding rather than writing two parallel sections.
- **Treat user-requested capabilities as signals first**: if feasibility is unknown or constrained, frame the item as a discussion point, dependency, or unresolved product decision — not as a shipped-feature recommendation.

## Workflow selection

Choose the lightest path that fits the request. Read the reference map at [references/README.md](references/README.md) to see which files each mode needs.

### Quick mode menu

1. **Planning only** — study design, hypotheses, sample plan, screener logic, discussion guide
   Read: [workflow.md](references/workflow.md) and [analysis-standards.md](references/analysis-standards.md)

2. **Qualitative only** — interviews, transcripts, notes, feedback, tickets, open text
   Read: [workflow.md](references/workflow.md), [qualitative-deep-dive.md](references/qualitative-deep-dive.md), [qual-packaging-standard.md](references/qual-packaging-standard.md)

3. **Quantitative only** — survey data, crosstabs, statistical tests, chartbooks
   Read: [workflow.md](references/workflow.md), [artifact-interface.md](references/artifact-interface.md), [quant-reporting-standard.md](references/quant-reporting-standard.md)

4. **Mixed methods** — linked or parallel qual + quant, triangulated reporting
   Read: all core files, [qualitative-deep-dive.md](references/qualitative-deep-dive.md), [mixed-method-integration.md](references/mixed-method-integration.md), [mixed-method-report-skeleton.md](references/mixed-method-report-skeleton.md), [artifact-interface.md](references/artifact-interface.md)

5. **Report review** — auditing, critiquing, hardening, or rewriting a report
   Read: [review-rubric.md](references/review-rubric.md) and [iteration-playbook.md](references/iteration-playbook.md)

6. **Executive-ready reporting** — leadership audience, decision-ready framing
   Read: [executive-report-template.md](references/executive-report-template.md) and [evidence-confidence-standard.md](references/evidence-confidence-standard.md)

7. **Research asset packaging** — reusable artifacts, multi-layer deliverables
   Read: [finding-ledger-template.md](references/finding-ledger-template.md) and [research-assets-template.md](references/research-assets-template.md)

8. **Citation and rollback discipline** — substantial, multi-step, or heavily revised work
   Read: [citation-style.md](references/citation-style.md) and [rollback-rules.md](references/rollback-rules.md)

## Default operating procedure

Steps marked ⏸ are human checkpoints (Zone 2 gates or Zone 3 decisions). All other steps Claude runs autonomously.

1. ⏸ **Scope confirmation** — If business decision, audience, or data files are unclear, ask once. If clear from context, skip and start. For review tasks, confirm: list issues only or also propose fixes?
2. Inventory available evidence: raw data, processed tables, existing outputs, source-of-truth definitions.
3. Detect method type: qualitative, quantitative, or mixed. State assumptions and flag non-obvious ones in output.
4. For quantitative work, lock the sample funnel, name denominators, reconcile with legacy reports if any.
5. Run descriptive analysis, cross-tabs, significance tests, and generate charts.
6. For qualitative work, produce an initial codebook (10-15 codes with definitions and examples).
7. ⏸ **Gate 1 — Codebook confirmation** — Present codebook for user review. Wait for adjustments before proceeding. (Skip for pure quant or review tasks.)
8. Apply codes to data, surface candidate patterns, identify contradictions and negative cases.
9. Draft findings with confidence labels, select representative quotes and cases, assign recommendation priorities.
10. ⏸ **Gate 2 — Finding classification** — Present each candidate finding as a structured table: finding → proposed status (formal finding / directional signal / noise) → evidence → counter-signals. User decides what gets promoted, what gets caveated, and what gets dropped. Lock this before proceeding to report assembly.
11. Produce a full report draft using [report-standard.md](references/report-standard.md).
12. Auto-fix mechanical issues (formatting, denominator labels, citation format) against [review-rubric.md](references/review-rubric.md). Run `scripts/validate_report.py`.
13. For leadership audiences, compress into executive format using [executive-report-template.md](references/executive-report-template.md).
14. ⏸ **Gate 3 — Independent report quality review** — Launch a **separate reviewer subagent** with only the report draft, original data, and [review-rubric.md](references/review-rubric.md) (no writing-phase reasoning history). The subagent produces a severity-ordered issue list. Present the subagent's issues to the user. User decides which to fix. This gate is about research quality, not publication readiness.
15. Apply approved fixes, maintain finding ledger for substantial projects, apply delivery formatting rules.
16. ⏸ **Publication sign-off** — Present the finalized package. User decides: can this be released? To whom? In what order? Does the tone need adjusting for the audience?

## Interaction rules

- Do not force a questionnaire-style intake if the needed facts are already in the prompt or files.
- Ask only for missing information that changes research validity — sample origin, metric definition, or whether datasets can be linked.
- If blocked by missing inputs, name the exact blocker and offer the smallest next step.
- Prefer making a reasonable assumption and labeling it over stalling.
- When reviewing a third-party report, default to reviewer mode: findings first, severity-ordered, with direct references to the weak claim. After listing issues, explicitly ask the user whether they want fixes proposed or just the issue list — do not auto-pilot into the iteration playbook.
- When the user provides comments on a shared doc, treat the comment trail as revision input.
- When the user says "just do it" or similar, shift Zone 2 steps toward autonomous execution but flag key decisions made.
- When starting any analysis or review task, confirm the data or report file is available before proceeding. If the user references "this report" or "these interviews" but has not provided files, ask for them immediately.

## Evidence rules

- Never describe a pattern as universal without support.
- Never convert qualitative signals into population size estimates.
- When quantitative significance is unknown, do not imply certainty.
- When quotes are edited for clarity, say they were lightly edited without changing meaning.
- When samples are biased or narrow, surface that limitation near the affected conclusion, not only in an appendix.
- Use the confidence scale from [evidence-confidence-standard.md](references/evidence-confidence-standard.md).
- If a feature request appears frequently but feasibility is unknown, report it as a validated need, then explicitly separate the product implication from the implementation commitment.

## Deliverable bar

A strong output from this skill should:
- answer the research question quickly
- preserve methodological honesty
- show the strongest supporting evidence
- include counter-signals or caveats
- lead to actionable product or business decisions
- survive adversarial review from a skeptical research lead
- sound like a strong human researcher, not a generic AI summary
- give the reader one clear main report to read, plus thicker appendices for auditability
- keep chart and table systems reusable without manual cleanup
- preserve enough user voice and scene detail that the report feels credible

## Reference library

If the task is substantial, consult the references below as needed. Start with [references/README.md](references/README.md) for navigation.

Core operating flow:
- [workflow.md](references/workflow.md) — end-to-end workflow
- [analysis-standards.md](references/analysis-standards.md) — analysis quality bar
- [report-standard.md](references/report-standard.md) — report structure and writing bar
- [evidence-confidence-standard.md](references/evidence-confidence-standard.md) — confidence labels and claim taxonomy
- [citation-style.md](references/citation-style.md) — reference consistency
- [rollback-rules.md](references/rollback-rules.md) — when to go upstream

Qualitative stack:
- [qualitative-deep-dive.md](references/qualitative-deep-dive.md) — deep qualitative operating guide
- [qual-packaging-standard.md](references/qual-packaging-standard.md) — minimum qualitative asset package

Quantitative stack:
- [artifact-interface.md](references/artifact-interface.md) — stable file-based outputs
- [quant-reporting-standard.md](references/quant-reporting-standard.md) — stats, charts, packaging

Mixed-method stack:
- [mixed-method-integration.md](references/mixed-method-integration.md) — triangulation logic
- [mixed-method-report-skeleton.md](references/mixed-method-report-skeleton.md) — integrated report shape
- [single-report-multistakeholder.md](references/single-report-multistakeholder.md) — one report for multiple audiences

Executive and review:
- [executive-report-template.md](references/executive-report-template.md) — leadership summary template
- [review-rubric.md](references/review-rubric.md) — publish-readiness audit
- [iteration-playbook.md](references/iteration-playbook.md) — revision workflow

Assets and packaging:
- [finding-ledger-template.md](references/finding-ledger-template.md) — traceable finding inventory
- [research-assets-template.md](references/research-assets-template.md) — codebook, quote bank, casebook templates

Delivery and formatting:
- [delivery-formatting.md](references/delivery-formatting.md) — rich-doc delivery, Chinese report conventions, case labeling

Validation:
- `scripts/validate_report.py` — lightweight markdown report quality checker
