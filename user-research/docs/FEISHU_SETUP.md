# 飞书文档导出配置指南

## 方案选择

提供两种方案，按复杂度从低到高排列：

### 方案 1：Markdown 复制粘贴（推荐，最简单）

无需配置，直接复制生成的 Markdown 到飞书文档。

**使用方法**：
```bash
/research-report --output_format=feishu --copy_to_clipboard=true
```

**飞书兼容性**：
- ✅ 标题、粗体、列表、表格、引用块
- ✅ ASCII 图表（已优化为飞书友好格式）
- ⚠️ 复杂图表需手动截图粘贴

---

### 方案 2：飞书 API 自动创建文档

需要配置飞书应用，但可以一键生成文档。

## 飞书 API 配置步骤

### 步骤 1：创建飞书应用

1. 访问 [飞书开放平台](https://open.feishu.cn/)
2. 登录你的飞书账号
3. 点击「创建应用」
4. 选择「企业自建应用」
5. 填写应用名称（如"用研报告生成"）
6. 创建后进入应用详情页

### 步骤 2：获取凭证

在应用详情页的「凭证与基础信息」中获取：

```
App ID: cli_xxxxxxxxxxxxxxxx
App Secret: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 步骤 3：配置权限

进入「权限管理」，添加以下权限：

| 权限 | 说明 |
|:---|:---|
| `docx:document:write` | 创建文档 |
| `docx:document:read` | 读取文档 |
| `drive:drive:write` | 写入云空间 |

### 步骤 4：发布应用

进入「版本管理与发布」，点击「创建版本」，填写版本信息后发布。

**注意**：
- 如果是个人使用，选择「仅管理员可用」
- 需要企业管理员审批

### 步骤 5：获取 Tenant Access Token

使用以下命令获取 token：

```bash
curl -X POST https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal \
  -H "Content-Type: application/json" \
  -d '{
    "app_id": "cli_xxxxxxxxxxxxxxxx",
    "app_secret": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  }'
```

返回示例：
```json
{
  "code": 0,
  "msg": "ok",
  "tenant_access_token": "t-xxxxxxxxx",
  "expire": 7200
}
```

**token 有效期 2 小时**，需要定期刷新。

---

## 在 Claude Code 中使用

### 配置环境变量

```bash
# 添加到 ~/.zshrc 或 ~/.bashrc
export FEISHU_APP_ID="cli_xxxxxxxxxxxxxxxx"
export FEISHU_APP_SECRET="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### 使用 Skill 生成飞书文档

```bash
/research-report \
  --output_format=feishu_api \
  --feishu_folder_token="Foldxxxxxxxxxx" \
  --feishu_title="Q3用户调研报告"
```

参数说明：
- `feishu_folder_token`: 飞书文件夹 token（从 URL 中获取）
- `feishu_title`: 文档标题

---

## 快速测试

如果你已经有 App ID 和 App Secret，可以立即测试：

```bash
# 测试 token 获取
curl -X POST https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal \
  -H "Content-Type: application/json" \
  -d "{\"app_id\":\"$FEISHU_APP_ID\",\"app_secret\":\"$FEISHU_APP_SECRET\"}"
```

---

## 方案对比

| 方案 | 配置复杂度 | 使用便捷度 | 格式保留 | 推荐场景 |
|:---|:---|:---|:---|:---|
| Markdown 复制 | 无 | 中（需手动粘贴） | 90% | 个人使用、快速分享 |
| 飞书 API | 中（需创建应用） | 高（一键生成） | 100% | 团队协作、定期报告 |

---

## 下一步

1. **想立即使用**：选择方案 1，我现在就优化 skill 支持飞书 Markdown 格式
2. **想自动化**：按上述步骤创建飞书应用，提供 App ID 和 App Secret，我帮你配置 API 调用

你倾向哪种方案？
