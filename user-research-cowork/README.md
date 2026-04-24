# user-research-cowork

协作式用户研究 skill。基于 [chelseajz/user-research-skill](https://github.com/chelseajz/user-research-skill) claude 分支，增强新手友好引导入口。

## 两个入口

| 入口 | 适用场景 |
|------|----------|
| `/user-research` | 专业用研流程，细粒度控制 |
| `/user-research-guided` | 非用研背景同事，引导式全流程 |

## 核心特性

### 1. Zone 模型人机协作

- **Zone 1** — AI 自动执行（数据清洗、编码、图表、报告框架）
- **Zone 2** — 3 个确认点（Gate 1 编码表、Gate 2 发现定级、Gate 3 质量审核）
- **Zone 3** — 人类决策（开始范围确认、结束发布签字）

### 2. 发现定级（Gate 2）

每个候选发现必须定级：

- **正式发现**：证据强，可支撑报告和驱动建议
- **方向性信号**：模式存在但证据不完整，标记低置信度
- **降级置信度**：有坑，与结论一起说明
- **添加边界**：只在特定人群/场景成立
- **剔除噪音**：证据太弱或冲突

**保守原则**：默认不升级，除非证据充分。

### 3. 独立审核机制

Gate 3 使用独立 subagent，在严格输入控制下审查报告，避免自我辩护偏差。

### 4. 新手引导入口

`/user-research-guided` 提供：
- 大白话解释每个环节
- 分步推进，等待用户确认
- 术语对照表（编码→整理要点）
- 自动串联专业 skill

## 目录结构

```
user-research-cowork/
├── SKILL.md                      # 专业入口（基于 claude 分支）
├── user-research-guided.json     # 新手引导入口
├── README.md                     # 本文件
└── references/                   # 参考文件（19 个）
    ├── workflow.md
    ├── report-standard.md
    ├── review-rubric.md
    ├── evidence-confidence-standard.md
    ├── ...
```

## 安装

```bash
# 方式一：直接复制整个目录
cp -r user-research-cowork ~/.claude/skills/

# 方式二：只复制需要的 skill
cp user-research-cowork/SKILL.md ~/.claude/skills/
cp user-research-cowork/user-research-guided.json ~/.claude/skills/
```

## 使用方式

### 专业模式

```
/user-research --topic="新用户7天留存低" --context="产品是理财App"
```

### 引导模式

```
/user-research-guided --topic="新用户7天留存低" --context="产品是理财App"
```

## 与上游差异

基于 [chelseajz/user-research-skill](https://github.com/chelseajz/user-research-skill) claude 分支：
- 新增 `user-research-guided.json` 引导入口
- SKILL.md description 改为中英双语
- 保留所有专业实践（Zone 模型、Gate 机制、置信度标注）

## 参考

- 原始项目：[chelseajz/user-research-skill](https://github.com/chelseajz/user-research-skill)
- claude 分支：包含完整的 Zone 模型和 Gate 机制
