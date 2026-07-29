# OpenClaw 文件 Skill

[English](README.md) | 繁體中文

這個 repository 將 OpenClaw 官方文件整理成可自動更新的 Agent Skill。GitHub Actions
每天同步上游 `docs/`，記錄精確來源版本，並依文件的 metadata 產生適合逐層披露的主題索引。

## Skill 可以協助什麼

- 安裝、更新、遷移與部署
- Gateway 設定、操作、網路與安全
- Telegram、WhatsApp、Discord、Slack、LINE、Signal 等訊息頻道
- 模型服務商、認證、failover 與本地模型
- Agent、Session、Memory、工具、Plugin、Node 與自動化
- CLI 錯誤與依症狀進行的故障排除

## 逐層披露

完整文件不會一次塞進模型上下文：

```text
SKILL.md
  → 精簡的 references/SKILL_INDEX.md
  → 一個 references/_catalog/<topic>.md
  → 最相關的 1–3 篇文件
  → 只讀取需要的段落
```

若使用者提供精確錯誤、CLI 指令或設定鍵，模型會直接搜尋 `references/`，不必先載入索引。
分類索引會利用上游文件既有的 `title`、`summary` 與 `read_when` metadata。

## 安裝

請用 Git checkout 安裝，才能可靠更新。依 AI Agent 使用的 Skills 目錄調整目的地：

```bash
git clone https://github.com/tbdavid2019/openclaw-docs-skill.git \
  ~/.gemini/antigravity/skills/openclaw-docs
```

Codex 常見安裝位置：

```bash
git clone https://github.com/tbdavid2019/openclaw-docs-skill.git \
  ~/.codex/skills/openclaw-docs
```

也可以從另一份 checkout 使用 installer 安裝到新目標：

```bash
bash openclaw-docs-skill/scripts/install-skill.sh <skill-directory>
```

日後更新已安裝的 checkout：

```bash
bash <skill-directory>/scripts/install-skill.sh
```

公開 repository 每天同步一次；本機安裝不會在每次提問時自動連網更新，只有明確執行
installer 或 `git pull` 才會改變。

若 AI 平台會把 Skill 複製進受管目錄，請使用該平台的更新機制。複製的 snapshot 仍可使用，
但無法以 Git checkout 方式自行更新。

## Repository 結構

```text
openclaw-docs-skill/
├── SKILL.md
├── agents/openai.yaml
├── scripts/
│   ├── install-skill.sh
│   ├── sync-docs.sh
│   └── generate_index.py
├── tests/test_repo.py
├── .github/workflows/auto-sync.yml
└── references/
    ├── SOURCE.json
    ├── SKILL_INDEX.md
    ├── _catalog/
    └── <OpenClaw 官方文件>
```

`references/SOURCE.json` 會記錄上游 repository、commit、commit 日期與文件數量。

## 維護者流程

從官方 repository 更新：

```bash
sh scripts/sync-docs.sh
```

驗證 Skill 與生成內容：

```bash
python3 -m unittest -v tests/test_repo.py
python3 scripts/generate_index.py --check
```

同步流程會先在臨時目錄下載、產生索引並驗證，最後才替換 `references/`。下載失敗、
文件數量異常、必要文件缺少或索引驗證失敗時，既有文件會保留。

請勿手動修改同步文件、`references/SOURCE.json`、`references/SKILL_INDEX.md`
或 `references/_catalog/`。

## 文件來源

內容同步自官方 [OpenClaw repository](https://github.com/openclaw/openclaw)
與 [OpenClaw 文件](https://docs.openclaw.ai/)。

## 授權

[AGPL-3.0](LICENSE)。OpenClaw 文件仍受上游授權條款約束。

## 致謝

本專案受到 [win4r/OpenClaw-Skill](https://github.com/win4r/OpenClaw-Skill) 啟發。
