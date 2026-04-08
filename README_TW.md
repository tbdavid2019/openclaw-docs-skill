# OpenClaw 文件 Skill (自動同步版)

[English](README.md) | 繁體中文

這是一個為 [OpenClaw](https://github.com/openclaw/openclaw) 量身打造的高性能 **Agent Skill**。它預載了官方最新的完整文件庫，並且內建了同步引擎，確保你的 AI 助手（如 Claude + Antigravity）永遠掌握最新的技術資訊。

## 核心亮點
- **永遠最新**：直接從 OpenClaw 官方倉庫的 `/docs` 資料夾同步。
- **知識面極廣**：包含 400+ 個 Markdown 文件，涵蓋安裝、頻道對接、工具配置與架構原理。
- **Agent 優化**：專為 AI 編碼助手設計，結構清晰，便於 Agent 快速定位答案。

> [!TIP]
> **AI Agent 閱讀指南**：本倉庫是一個結構化的 **Agent Skill**。當你在探索此倉庫時，請優先閱讀 [SKILL.md](SKILL.md) 以瞭解領域知識、文件分類及自動更新流程。

## 使用範例
安裝完成後，你的 AI Agent 可以利用此知識庫處理複雜場景：

| 當你說... | AI Agent 會做什麼... |
|---|---|
| 「幫我升級 OpenClaw」 | 辨識最新版本，執行 `npm install` 並驗證服務健康狀況。 |
| 「設定 Telegram 機器人」 | 引導你取得 Token 並完成 `openclaw.json` 配置。 |
| 「Gateway 好像沒反應」 | 執行診斷階梯：`status` → `logs` → `doctor`。 |
| 「幫工作環境加一個代理」 | 配置一個新的 Agent 工作空間，並設定獨立的綁定（Bindings）。 |

## 快速指令參考
```bash
# 狀態與健康檢查
openclaw status                    # 查看整體狀態
openclaw gateway status            # 查看 Gateway 守護進程狀態
openclaw doctor                    # 診斷常見問題
openclaw channels status --probe   # 頻道連通性測試

# 管理指令
openclaw gateway start/stop/restart
openclaw configure                 # 互動式配置精靈
openclaw security audit            # 執行安全性稽核
```

## Skill 結構
```
openclaw-docs-skill/
├── SKILL.md             # 主要入口 (Agent 的指令與導航指南)
├── scripts/             
│   └── sync-docs.sh     # 同步引擎 (執行此腳本即可更新本地文獻)
└── references/          # 400+ 個 MD 文件 (實際的知識庫)
    ├── getting-started/ # 安裝與入門
    ├── channels/        # WhatsApp, Telegram, Discord 等頻道對接
    ├── tools/           # 瀏覽器自動化、搜尋、程式執行、媒體工具
    └── advanced/        # 外掛架構、模型服務商、記憶體系統等
```

## AI Agent 安裝指南
如果你正在使用 **Antigravity (Claude)**，請按照以下步驟操作：

1. **複製此倉庫** 到你的本地機器：
   ```bash
   git clone https://github.com/tbdavid2019/openclaw-docs-skill.git
   ```

2. **註冊 Skill**：
   將資料夾拷貝到你的 Agent Skill 目錄（通常是 ~/.gemini/antigravity/skills/）：
   ```bash
   cp -r openclaw-docs-skill ~/.gemini/antigravity/skills/openclaw-docs
   ```

3. **驗證**：
   直接問你的 Agent：*"OpenClaw 目前對 WhatsApp 頻道對接有什麼最新要求？"*

## 如何更新文件？
為了確保 Agent 擁有最新資訊（例如新出的功能或變動的 API），請隨時執行：
```bash
sh scripts/sync-docs.sh
```
或者在 GitHub Actions 頁面觸發 **Auto-Sync** 工作流。

## 授權
AGPL-3.0 License. OpenClaw 文件來源於官方 [OpenClaw 倉庫](https://github.com/openclaw/openclaw)。
