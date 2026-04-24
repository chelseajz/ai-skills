# Fintech 月报共享资源

本目录包含 3 个子 skill 共享的知识库、参考文档、模板和脚本：

- **knowledge-base/** — 行业知识、竞品档案、核心玩家图谱、护城河分析框架
- **reference/** — 搜索清单、信源分类、分析框架、格式规范、检查清单
- **examples/** — Markdown 模板、HTML 模板
- **scripts/** — 验证脚本、归档脚本、初始化脚本

## 使用方式

各子 skill 通过相对路径引用本目录资源：

```
../fintech-shared/knowledge-base/core-players.md
../fintech-shared/reference/01-search-queries.md
../fintech-shared/examples/html-template.html
../fintech-shared/scripts/validate-report.py
```

原始 `fintech-monthly-report/` 目录下保留符号链接以保持向后兼容。

## 更新规则

- 知识库/参考文件更新直接修改 `fintech-shared/` 下的文件
- 不要修改符号链接指向的文件，除非要全局更新
- 添加新的知识文件时，放在 `fintech-shared/knowledge-base/` 对应子目录下
