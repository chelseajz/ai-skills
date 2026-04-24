# Skill: export-feishu

## 描述
将研究报告导出为飞书文档。生成飞书友好的 Markdown 格式，支持一键复制粘贴，或发送到飞书群。

## 调用方式
```
/export-feishu --report_content="报告内容" --feishu_title="文档标题" --chat_id="飞书群ID" --mode="导出模式"
```

## 参数说明
- **report_content**: 报告内容（Markdown 文件路径或文本）
- **feishu_title**: 文档标题
- **chat_id**: 飞书群 ID（可选，默认发送到技能五子棋群）
- **mode**: 导出模式（clipboard / send）

## 输出内容
1. Clipboard 模式：生成优化后的 Markdown，可直接复制粘贴
2. Send 模式：发送消息到飞书群，包含报告摘要和完整 Markdown

## 飞书 Markdown 格式规范

### 支持的语法
- 标题：`# 一级标题`、`## 二级标题`、`### 三级标题`
- 粗体：`**粗体**`
- 斜体：`*斜体*`
- 删除线：`~~删除线~~`
- 引用块：`> **核心结论**：关键发现`
- 无序列表：`- 列表项`
- 有序列表：`1. 列表项`
- 待办事项：`- [ ] 待办`、`- [x] 已完成`
- 表格：`| 列1 | 列2 |`
- 代码块：````代码````
- 分隔线：`---`
- 链接：`[文字](URL)`

### 报告转飞书优化规则

1. **标题层级优化**：报告标题→一级，章节→二级，小节→三级
2. **关键结论用引用块**：`> **核心结论**：...`
3. **行动建议用待办列表**：`- [ ] 行动项`
4. **图表处理**：ASCII图表保留，添加截图提示
5. **数据表格简化**：不超过5行，关键数据加粗
6. **用户原声用引用块**：`> "原话" > — 用户类型`

## 飞书 API 配置

### 环境变量
```
FEISHU_APP_ID=cli_a94e2de491b8dcb3
FEISHU_APP_SECRET=3E18dhBDvPmNrCI820YiAhWFDnyIxqTs
```

### 获取 Token
```bash
curl -s -X POST https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal \
  -H "Content-Type: application/json" \
  -d '{"app_id": "YOUR_APP_ID", "app_secret": "YOUR_APP_SECRET"}'
```

### 发送到群
```bash
curl -s -X POST "https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=chat_id" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "receive_id": "CHAT_ID",
    "msg_type": "text",
    "content": "{\"text\": \"消息内容\"}"
  }'
```

## 质量检查
- [ ] 标题层级正确（#/##/###）
- [ ] 关键结论用引用块 >
- [ ] 行动建议用待办 - [ ]
- [ ] 表格不超过5行
- [ ] 用户原声用引用块
- [ ] 图表后添加截图提示
- [ ] 无学术术语
- [ ] 飞书 Markdown 语法兼容

## 注意事项
飞书 docx blocks API 写入内容较复杂，当前版本使用 Markdown 复制粘贴方案，简单可靠。
