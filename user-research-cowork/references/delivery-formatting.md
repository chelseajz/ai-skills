# Delivery Formatting

This file covers formatting conventions for final deliverables, especially when publishing to rich-document tools or writing in Chinese.

## Rich-document delivery (Feishu, Notion, Google Docs)

When publishing to a rich-document tool rather than shipping a plain markdown or docx file:

- Place charts next to the argument they support, not only in a terminal appendix block.
- Remove raw markdown image syntax, local file paths, and placeholder links from the reader-facing document.
- Use callout blocks, quotes, and tables intentionally to surface the most decision-relevant points.
- If the tool cannot reliably place charts into an existing document in one pass, rebuild the document in reading order: append the text for a section, then place the relevant chart immediately after the supporting claim.
- Do not ship a visually broken version when sequential construction would produce a clean one.

## Chinese-language report conventions

When the report language is Chinese:

- Prefer Chinese narrative prose for case descriptions and casebook entries. Keep English only for product names, financial terms, or source text that must remain verbatim.
- Use natural reader-facing case tags such as `——案例#247，常驻内地，23-30岁，在校学生，有需求未借过`.
- If the full profile is unavailable, use a bounded fallback such as `——案例#1278，产品反馈样本`.
- Do not leave raw trace labels such as `来源：ID...` in the final polished report unless the user explicitly asks for audit-first formatting.
- Clear all drafting residue such as `待补`, `TBD`, `to fill`, note-to-self text, and half-resolved placeholders before treating the report as final.

## Case identifier discipline

When multiple identifier systems exist in the data (interview id, questionnaire id, row id, linkage id):

- Define one reader-facing case id system and stick to it through the whole report.
- Prefer the interview or case id used in qualitative source files.
- Do not accidentally expose questionnaire ids, linkage ids, or sheet row ids as the polished `案例#`.
- If a quote is tagged with a case id, verify that the id really belongs to the interview/case system rather than to the questionnaire linkage field.

## Multi-system denominator display

When one section combines raw multi-select usage counts with simplified mutually-exclusive recoding:

- State the two systems explicitly before showing both.
- Do not place them side by side as if they were the same denominator.
- Prefer one system in the main report body unless the comparison itself is analytically important.
- If both must appear, explain why totals differ before the reader sees conflicting `N` values.

## Embedded support objects

When a chart, sheet, or appendix table carries critical proof:

- Restate the key numbers and takeaway in the body text so the report remains auditable without clicking away.
- If the report uses both a top recommendation callout and a recommendation table, separate them by layer: the callout should contain only the few highest-level decisions; the table should contain execution priority, concrete action, and rationale. Do not restate the same action twice in different wording.

## Report naming

- Use the naming convention the business asked for.
- Formal main reports should keep the requested main title.
- Reference materials should use `参考-<topic>-<subtopic>` naming so the source-of-truth layer is obvious.

## Casebook bucket naming

- Keep bucket names faithful to the actual inclusion logic.
- Do not label a section as `no need` if it mixes weak demand, edge cases, strong substitutes, or non-priority opportunities.
- Keep the "why selected" note consistent with the segment label and the quote content.
- If a case is described as representative or typical, the rationale must be consistent with the segment label and the quote evidence.

## Statistical caveat consistency

When one segment label is statistically non-significant but directionally interesting:

- Keep that caveat synchronized across the title, summary, recommendation block, and detailed body.
- Do not soften the caveat only in the appendix or only in the detailed findings layer.
