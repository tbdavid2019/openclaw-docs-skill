# OpenClaw 文件 Skill (自動同步版)

[English](README.md) | 繁體中文

這是一個為 [OpenClaw](https://github.com/openclaw/openclaw) 量身打造的高性能 **Agent Skill**。它預載了官方最新的完整文件庫，並且內建了同步引擎，確保你的 AI 助手（如 Claude + Antigravity）永遠掌握最新的技術資訊。

## 核心亮點
- **永遠最新**：直接從 OpenClaw 官方倉庫的 `/docs` 資料夾同步。
- **知識面極廣**：包含 400+ 個 Markdown 文件，涵蓋安裝、頻道對接、工具配置與架構原理。
- **Agent 優化**：專為 AI 編碼助手設計，結構清晰，便於 Agent 快速定位答案。

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
這本版本最大的優勢在於它可以手動更新。為了確保 Agent 擁有最新資訊（例如新出的功能或變動的 API），請隨時執行：
```bash
sh scripts/sync-docs.sh
```
該腳本使用 `sparse-checkout` 技術，只抓取官方倉庫中的文件變更，不會下載多餘的程式碼，速度極快。

## 貢獻
歡迎提交 Pull Request 或 Issue！特別是如果你發現 `SKILL.md`（Agent 的導引邏輯）有改進空間，或者同步腳本有更好的寫法。

## 授權
MIT License. OpenClaw 文件來源於官方 [OpenClaw 倉庫](https://github.com/openclaw/openclaw)。
