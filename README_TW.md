# OpenClaw 文件 Skill（自動同步版）

[English](README.md) | 繁體中文

一個完整的 **Agent Skill**，涵蓋 [OpenClaw](https://github.com/openclaw/openclaw) 的安裝、設定、操作與故障排除——OpenClaw 是一個自主架設、支援多頻道的 AI Agent 閘道器。

與靜態 Skill 不同，本版本內建了**同步引擎**，可直接從 OpenClaw 官方倉庫拉取最新文件，確保你的 AI 助手永遠掌握最新資訊。

> [!TIP]
> **AI Agent 閱讀指南**：本倉庫是一個結構化的 **Agent Skill**。在回答任何與 OpenClaw 相關的問題前，請優先閱讀 [SKILL.md](SKILL.md)，以了解可用指令、診斷流程與文件索引。

## 這是什麼？

本 Skill 專為 AI 編碼助手設計（如 Claude + Antigravity）。安裝後，AI 助手即可深入了解 OpenClaw，並協助你處理：

- **安裝與更新** — 安裝、升級或遷移 OpenClaw
- **配置管理** — 編輯 `openclaw.json`、設定模型、管理 Secrets
- **頻道管理** — 設定 WhatsApp、Telegram、Discord、Slack、iMessage 及 15+ 個其他頻道
- **Gateway 操作** — 啟動、停止、重啟、健康檢查、遠端存取
- **多代理路由** — 設定多個 Agent 並隔離工作空間與會話
- **ACP Agents** — 生成外部 AI 運行環境（Codex、Claude Code、Gemini CLI、14+ 種）
- **瀏覽器自動化** — 多設定檔瀏覽器控制、Chrome MCP 已有會話、快照
- **外掛系統** — 能力模型、Context Engine 外掛、SDK、Hook API
- **自動化** — Cron 任務、常設指令、背景任務、Webhooks、Hooks
- **安全加固** — 稽核、存取鎖定、Token 管理、受信任代理、事件響應
- **故障排除** — 診斷並修復 CLI 與 Gateway 的常見錯誤

## Skill 結構

```
openclaw-docs-skill/
├── SKILL.md                     # 主要入口（370 行的專家級工作流程、指令與故障排除）
├── scripts/
│   └── sync-docs.sh             # 同步引擎 — 從上游拉取最新文件
├── .github/
│   └── workflows/
│       └── auto-sync.yml        # GitHub Action — 每日 04:00 UTC 自動同步
└── references/                  # 400+ 個 Markdown 文件（知識庫）
    ├── channels/                # 各頻道設定（WhatsApp、Telegram、Discord 等）
    ├── tools/                   # 所有內建工具（瀏覽器、搜尋、Exec、ACP 等）
    ├── plugins/                 # 外掛架構與 SDK
    ├── providers/               # 35+ 個模型服務商（Anthropic、OpenAI、Google、Ollama 等）
    ├── concepts/                # 核心概念：Agent 循環、記憶體、佇列、串流
    ├── gateway/                 # Gateway 配置、操作、安全性、沙箱
    ├── security/                # 安全加固策略
    ├── nodes/                   # 節點（iOS/Android/macOS/無介面）
    ├── automation/              # Cron 任務、Webhooks、背景任務、常設指令
    ├── install/                 # 安裝、更新、回滾、遷移、解除安裝
    ├── platforms/               # 平台指南（macOS、iOS、Android、Linux、Windows）
    ├── web/                     # Web 介面：Dashboard、Control UI、WebChat、TUI
    ├── diagnostics/             # 故障排除與失敗演練
    └── cli/                     # CLI 參考
```

## AI Agent 安裝指南

### 適用於 Antigravity（Claude）

將 Skill 資料夾複製到你的 Antigravity Skills 目錄：

```bash
# 複製此倉庫
git clone https://github.com/tbdavid2019/openclaw-docs-skill.git

# 複製到你的 Skills 目錄
cp -r openclaw-docs-skill ~/.gemini/antigravity/skills/openclaw-docs
```

安裝後，當你詢問 OpenClaw 相關問題時，Skill 將自動被觸發。

### 適用於其他 AI 助手

`SKILL.md` 和 `references/` 中的結構化文件可適配任何支援 Skill/知識注入的 AI 助手。

## 使用範例

安裝後，只需自然地提問：

| 當你說... | AI 會做什麼... |
|---|---|
| 「幫我升級 OpenClaw」 | 執行 `openclaw update`，再用 `openclaw doctor` 套用遷移，重啟 Gateway |
| 「設定 Telegram 機器人」 | 引導完成 Bot Token 建立、`openclaw channels add` 及 QR 驗證 |
| 「Gateway 沒有回應」 | 執行診斷梯隊：`status` → `logs` → `doctor` → `channels status --probe` |
| 「加強 OpenClaw 的安全性」 | 執行 `openclaw security audit --fix`，套用強化基準並修復權限 |
| 「幫工作加一個 Agent」 | 建立 Agent、設定工作空間、配置綁定、重啟 |
| 「啟動 Claude Code ACP 會話」 | 配置 `acp-agents` 外掛、設定權限、生成綁定會話 |
| `EADDRINUSE` 錯誤 | 執行 `openclaw gateway --force` 或協助在配置中更改連接埠 |
| 「Embedding provider 401 錯誤」 | 找到 `~/.openclaw/.env` 中的佔位符 API Key，引導替換 |

## 快速指令參考

```bash
# 狀態與健康檢查
openclaw status                    # 整體狀態
openclaw gateway status            # Gateway 守護進程狀態
openclaw doctor                    # 診斷問題
openclaw channels status --probe   # 頻道健康檢查

# Gateway 管理
openclaw gateway install           # 安裝為系統服務
openclaw gateway start/stop/restart
openclaw gateway --force           # 強制關閉現有並重啟

# 配置
openclaw config get <path>         # 讀取配置值
openclaw config set <path> <value> # 設定配置值
openclaw configure                 # 互動式精靈

# 安全性
openclaw security audit            # 檢查安全態勢
openclaw security audit --fix      # 自動修復問題
openclaw secrets reload            # 重新載入 Secrets

# 頻道
openclaw channels add              # 新增頻道（精靈）
openclaw channels login            # WhatsApp QR 配對
openclaw channels list             # 顯示已設定的頻道

# 模型
openclaw models set <model>        # 設定預設模型
openclaw models status --probe     # 檢查認證狀態
```

## 如何更新文件？

本 Skill 的 `references/` 資料夾從 OpenClaw 官方倉庫同步。執行以下指令取得最新文件：

```bash
sh scripts/sync-docs.sh
```

或在 [GitHub Actions](https://github.com/tbdavid2019/openclaw-docs-skill/actions) 頁籤中觸發 **Auto-Sync Documentation** 工作流程。

GitHub Action 每天 UTC 04:00（台灣/香港時間 12:00）自動執行，無需手動介入。

## 文件來源

本 Skill 知識庫來自官方 [OpenClaw 文件](https://docs.openclaw.ai/)，涵蓋：

- [安裝](https://docs.openclaw.ai/install)
- [Gateway 架構](https://docs.openclaw.ai/concepts/architecture)
- [頻道](https://docs.openclaw.ai/channels)
- [模型服務商](https://docs.openclaw.ai/providers)
- [工具](https://docs.openclaw.ai/tools)
- [外掛架構](https://docs.openclaw.ai/plugins/architecture)
- [多代理路由](https://docs.openclaw.ai/concepts/multi-agent)
- [安全性](https://docs.openclaw.ai/gateway/security)
- [故障排除](https://docs.openclaw.ai/gateway/troubleshooting)
- [CLI 參考](https://docs.openclaw.ai/cli)

## 貢獻

歡迎提交 Issues 和 PR！特別期待以下方面的貢獻：
- `SKILL.md` — Agent 的推理邏輯與診斷流程
- `scripts/sync-docs.sh` — 同步引擎效率優化
- `references/` — 精選文件品質提升

## 授權

[AGPL-3.0](LICENSE) — 任何衍生作品均須以相同授權開源。OpenClaw 文件來源於官方 [OpenClaw 倉庫](https://github.com/openclaw/openclaw)。
