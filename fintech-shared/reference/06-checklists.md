# 执行清单与流程

## 执行前检查清单

- [ ] Phase 0: 输出目录已创建 `~/.claude/fintech-reports/{output,logs,data}`
- [ ] Phase 0: 宏观指标模板已复制

## 执行流程

```
Phase 0: 初始化
    ↓
✓ 检查：目录创建完成
    ↓
Phase 1: 一级信源直接抓取（HKMA/Fed/ECB/Stripe官网）
    ↓ 输出: phase1-primary-sources.json
✓ 检查：一级信源 ≥ 3 条
    ↓
Phase 2: 二级信源搜索+验证（必须执行全部128个查询）
    ↓ 输出: phase2-secondary-sources.json
✓ 检查：所有128个搜索已执行
    ↓
Phase 3: 聚合与去重
    ↓ 输出: phase3-unique-events.json
✓ 检查：总事件数统计完成
    ↓
Phase 4: 信源分级与评分
    ↓ 输出: phase4-scored-events.json
✓ 检查：所有事件已评分
    ↓
Phase 5: 深度分析
    ↓ 输出: phase5-analysis.md
✓ 检查：高价值事件分析完成
    ↓
Phase 6: 报告生成
    ↓ 输出: fintech-report-{YYYYMM}.md/.html
✓ 检查：grep "{{" 输出为空
    ↓
Phase 7: 自动化质量校验
   ↓ 脚本验证通过 → 完成
   ↓ 验证失败 → 根据错误修复
    ↓
完成
```

## 执行后检查清单

- [ ] Phase 0: 输出目录已创建 `~/.claude/fintech-reports/{output,logs,data}`
- [ ] Phase 0: 宏观指标模板已复制
- [ ] Phase 1: `phase1-primary-sources.json` 已生成，一级信源 ≥ 3 条
- [ ] Phase 2: `phase2-secondary-sources.json` 已生成，**128 个搜索查询全部执行并保存**
- [ ] Phase 2: 每个查询结果都保存在 `results` 数组中
- [ ] Phase 3: `phase3-unique-events.json` 已生成，去重完成
- [ ] Phase 4: `phase4-scored-events.json` 已生成，评分完成
- [ ] Phase 5: `phase5-analysis.md` 已生成，深度分析完成
- [ ] Phase 6: Markdown 报告生成，无占位符
- [ ] Phase 6: HTML 报告生成，`grep "{{"` 输出为空
- [ ] Phase 7: 自动化验证脚本执行通过
