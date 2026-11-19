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

Agent 從 `SKILL.md` 開始，只讀取任務相關段落。Gateway 健康檢查和 Telegram 設定
等常見任務有直達連結。

遇到精確錯誤、CLI 指令或設定鍵時，先搜尋相關主題的本機文件，再視需要擴大範圍。
廣泛問題先選主題索引，主題不明時使用精簡的 `references/SKILL_INDEX.md`。
分類索引利用上游的 `title`、`summary` 與 `read_when`，每次縮小到最多三篇候選文件。

## 安裝

### 透過 npm 安裝

npm 套件上架後，在專案目錄用 Node.js 22.20 以上與 Git 執行以下指令。
Codex 的預設安裝路徑是 `.agents/skills/openclaw-docs`。

```bash
npx -y openclaw-docs-skill@latest
```

可用 `--global` 安裝至使用者目錄，或用 `--agent` 指定其他宿主。 [支援的 Agent](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)

```bash
npx -y openclaw-docs-skill@latest --global
npx -y openclaw-docs-skill@latest --agent openclaw
```

npm 安裝後，用相同指令和選項更新。安裝器會從 GitHub 取得最新的同步快照，驗證後回報
安裝路徑、Skill repository commit 和上游文件 commit。GitHub 每日同步完成後，新安裝
與主動更新即可取得新版文件。平常使用時，Agent 直接查閱本機快照。

### 透過 SkillHub 安裝（CLI）

直接使用 [SkillHub](https://skills.palebluedot.live/owner/tbdavid2019) 安裝：

```bash
# 安裝至 Codex
npx skillhub install tbdavid2019/openclaw-docs-skill/openclaw-docs --platform codex

# 安裝至目前專案
npx skillhub install tbdavid2019/openclaw-docs-skill/openclaw-docs --project

# 或全域安裝
npx skillhub install tbdavid2019/openclaw-docs-skill/openclaw-docs -g
```

### 透過 Git Clone 安裝

需要 Git 工作副本時，可以依 Agent 的 Skills 目錄調整 clone 目的地。

```bash
git clone https://github.com/tbdavid2019/openclaw-docs-skill.git \
  ~/.gemini/antigravity/skills/openclaw-docs
```

Codex 常見安裝位置：

```bash
git clone https://github.com/tbdavid2019/openclaw-docs-skill.git \
  ~/.codex/skills/openclaw-docs
```

直接 clone 後，請執行一次 installer，以 fast-forward-only 方式拉取、驗證 snapshot 並輸出
commit 資訊：

```bash
bash <skill-directory>/scripts/install-skill.sh
```

也可以從另一份 checkout 直接使用 installer 安裝到新目標：

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

## AI Agent 安裝契約

當使用者提供這個 repository URL 並要求安裝 Skill 時：

1. 辨識宿主與安裝範圍。若已有安裝，先確認其管理方式並沿用原本的更新機制。
   若目的地與既有安裝衝突，先和使用者確認處理方式。
2. 新安裝或更新 npm 管理的 Skill 時，使用 `npx -y openclaw-docs-skill@latest`，
   並依宿主和範圍指定 `--agent` 和 `--global`。SkillHub 管理的安裝請使用 SkillHub。
3. 若走 Git checkout，先驗證來源及目的地。新 clone 或更新既有 checkout 時必須執行 installer
   `bash <skill-directory>/scripts/install-skill.sh`，並確認 `git pull --ff-only` 和驗證都成功。
4. 讀取已安裝的 `SKILL.md`。安裝時不要執行 `scripts/sync-docs.sh` 或
   `scripts/generate_index.py`。這些是維護者工具；安裝程序應使用 repository 已提交的
   文件 snapshot。
5. 驗證目的地包含 `SKILL.md`、`agents/openai.yaml`、`references/SOURCE.json`、
   `references/SKILL_INDEX.md` 與 `references/_catalog/`。
6. 讀取 `references/SOURCE.json`，回報絕對安裝目錄、Skill repository commit 與上游文件
   commit；installer 會輸出這三項資訊。
7. 若宿主只在啟動時探索 Skills，請使用者 reload 或 restart。接著用以下 prompt 測試：
   `Use $openclaw-docs to explain how to check OpenClaw Gateway health.`
8. 安裝或更新、驗證、commit 回報及必要的 reload 指示全部完成前，不要宣稱安裝成功。
   回報時僅列出安裝相關資訊。

可直接交給 AI Agent 的安裝要求：

```text
請把以下 repository 安裝為 OpenClaw 文件 Skill：
https://github.com/tbdavid2019/openclaw-docs-skill

請依 README.md 的「AI Agent Installation Contract」執行：
1. 辨識宿主平台並確認安裝範圍。新安裝優先使用 npm 安裝器。
2. 若已有安裝，沿用原本的安裝方式更新。
3. 讀取 SKILL.md。
4. 確認 references/SOURCE.json、references/SKILL_INDEX.md 與 references/_catalog/ 存在。
5. 回報安裝目錄、Skill repository commit 與目前 upstream documentation commit。

安裝後請這樣測試：
使用 $openclaw-docs，依本地同步的 OpenClaw 官方文件，說明如何檢查 Gateway health。
請列出引用的本地文件路徑，並區分官方文件事實與你的推論。

GitHub repository 每日自動同步。需要最新快照時，重新執行相應的安裝器。
```

## Repository 結構

```text
openclaw-docs-skill/
├── package.json
├── SKILL.md
├── agents/openai.yaml
├── scripts/
│   ├── install-npm.mjs
│   ├── install-skill.sh
│   ├── sync-docs.sh
│   └── generate_index.py
├── tests/test_repo.py
├── .github/workflows/auto-sync.yml
├── .github/workflows/publish-npm.yml
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

### 發佈 npm 安裝器

每日文件快照由 GitHub 提供。安裝器改版時才發佈新的 npm 版本。可先執行 `npm ci --ignore-scripts`
及 `npm pack` 產生 tarball，測試後用有發佈權限的 npm 帳號執行
`npm publish <tarball> --access public` 上架首版。
接著為 `tbdavid2019/openclaw-docs-skill` 的 `publish-npm.yml` 設定 npm Trusted Publishing，
並允許 `npm publish`。之後更新套件版本與 lockfile，推送符合 `v<version>` 的 tag，
發佈流程會先測試打包好的安裝器。 [npm Trusted Publishing](https://docs.npmjs.com/trusted-publishers/)

## 文件來源

內容同步自官方 [OpenClaw repository](https://github.com/openclaw/openclaw)
與 [OpenClaw 文件](https://docs.openclaw.ai/)。

## 授權

[AGPL-3.0](LICENSE)。OpenClaw 文件仍受上游授權條款約束。

## 致謝

本專案受到 [win4r/OpenClaw-Skill](https://github.com/win4r/OpenClaw-Skill) 啟發。
