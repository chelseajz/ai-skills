## Metadata
name: user-research
description: 用户研究全流程技能系统，覆盖研究规划、数据编码、交叉分析、洞察提炼、报告撰写、质量审查到迭代优化

## Overview
用户研究全流程技能系统，基于 JTBD、Fogg Behavior Model、Hook Model、Kano Model 等经典理论，提供从研究设计到报告输出的完整工作流。

## 子技能

### 方案设计
| 技能 | 功能 | 调用方式 |
|:---|:---|:---|
| research-plan | 研究规划（理论驱动） | `/research-plan --topic="..." --context="..."` |
| research-plan-review | 方案审核（独立审核） | `/research-plan-review --plan_content="..."` |

### 数据处理
| 技能 | 功能 | 调用方式 |
|:---|:---|:---|
| research-code | 定性编码（Grounded Theory） | `/research-code --input="..."` |
| research-analyze | 交叉分析（六维矩阵） | `/research-analyze --coded_data="..." --quantitative_data="..."` |
| research-insight | 洞察提炼（So-What链） | `/research-insight --analysis_results="..."` |

### 输出与审核
| 技能 | 功能 | 调用方式 |
|:---|:---|:---|
| research-report | 报告生成（飞书格式） | `/research-report --insight_results="..."` |
| research-report-review | 报告审核（独立审核） | `/research-report-review --report_content="..."` |
| research-iterate | 迭代优化（根因分析） | `/research-iterate --review_feedback="..."` |

### 导出
| 技能 | 功能 | 调用方式 |
|:---|:---|:---|
| export-feishu | 飞书导出 | `/export-feishu --report_content="..."` |

## 完整工作流

```
┌─────────────────────────────────────────────────────────────────────┐
│                           独立审核流程                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   方案设计 ──────→ 方案审核（独立）                                   │
│       │              │                                              │
│       │         审核通过? ──否──→ 返回修改 ──→ 方案审核               │
│       │              │是                                           │
│       ↓              ↓                                              │
│   数据编码 ──────→ [数据处理流程] ──→ 洞察提炼                       │
│                                             │                        │
│                                             ↓                        │
│                                      报告生成 ──→ 报告审核（独立）     │
│                                                  │                   │
│                                             审核通过? ──否──→ 迭代   │
│                                                  │是                 │
│                                                  ↓                   │
│                                              发布                     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 审核独立性原则

- **方案审核** 与 **报告审核** 是两个独立的 skill，各自独立运行
- 审核者不参与生成流程，避免\"自己审自己\"的偏见
- 审核意见 → 迭代修改 → 重新审核，形成质量飞轮

## 快速开始

### 场景 1：从 0 开始完整研究
```
/research-plan --topic="新用户留存率低" --context="协作工具，互联网用户"
# 按规划收集数据后
/research-code --input=interviews.txt
/research-analyze --coded_data=coded.json --quantitative_data=survey.csv
/research-insight --analysis_results=analysis.json
/research-report --insight_results=insights.json --format=feishu
```

### 场景 2：已有数据直接生成报告
```
/research-code --input=interviews.txt
/research-analyze --coded_data=coded.json --quantitative_data=survey.csv
/research-insight --analysis_results=analysis.json
/research-report --insight_results=insights.json
/export-feishu --report_content=report.md --mode=clipboard
```

### 场景 3：审查和迭代
```
/research-review --report_content=report.md
/research-iterate --review_feedback=review.json --current_deliverable=report.md
```

## 设计原则

1. **理论驱动**：内置 JTBD、Fogg Behavior Model、Hook Model、Kano Model 等经典理论
2. **去学术化**：使用互联网产品语言，避免"主轴编码"、"预测因子"等术语
3. **六维分析**：画像 × 场景 × 需求 × 痛点 × 竞品 × 期望
4. **质量飞轮**：每个环节都有质量检查，支持回退迭代
5. **飞书集成**：原生支持飞书文档格式导出
