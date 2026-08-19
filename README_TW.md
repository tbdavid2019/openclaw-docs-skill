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

1. 寫入前先辨識宿主平台，確認實際的 Skills 目錄。Codex 若有設定 `CODEX_HOME`，優先使用
   `$CODEX_HOME/skills/openclaw-docs`，否則使用 `~/.codex/skills/openclaw-docs`。
   Antigravity 常見位置是 `~/.gemini/antigravity/skills/openclaw-docs`。其他宿主應先檢查
   設定；無法確認時詢問使用者，不要猜測。
2. 檢查目的地。不存在時 clone 本 repository，最終目錄名稱使用 `openclaw-docs`；若已是
   本 repository 的 Git checkout，保留該目錄。若是非 Git 目錄，不得覆蓋，應說明衝突
   並詢問使用者如何處理。
3. 驗證前必須執行 installer：`bash <skill-directory>/scripts/install-skill.sh`。既有
   checkout 必須成功完成 `git pull --ff-only`；pull 或驗證失敗即表示安裝或更新失敗。
   新 clone 之後也必須執行 installer，套用相同驗證。
4. 讀取已安裝的 `SKILL.md`。安裝時不要執行 `scripts/sync-docs.sh` 或
   `scripts/generate_index.py`。這些是維護者工具；安裝程序應使用 repository 已提交的
   文件 snapshot。
5. 驗證目的地包含 `SKILL.md`、`agents/openai.yaml`、`references/SOURCE.json`、
   `references/SKILL_INDEX.md` 與 `references/_catalog/`。
6. 讀取 `references/SOURCE.json`，回報絕對安裝目錄、Skill repository commit 與上游文件
   commit；installer 會輸出這三項資訊。
7. 若宿主只在啟動時探索 Skills，請使用者 reload 或 restart。接著用以下 prompt 測試：
   `Use $openclaw-docs to explain how to check OpenClaw Gateway health.`
8. pull、驗證、commit 回報及必要的 reload 指示全部完成前，不要宣稱安裝成功。不得輸出
   憑證或不相關的設定值。

可直接交給 AI Agent 的安裝要求：

```text
請把以下 repository 安裝為 OpenClaw 文件 Skill：
https://github.com/tbdavid2019/openclaw-docs-skill

請依 README.md 的「AI Agent Installation Contract」執行：
1. Clone 到你的 Skills 目錄，最終目錄名稱使用 openclaw-docs。
2. 執行 scripts/install-skill.sh；既有 checkout 必須完成 git pull --ff-only。
3. 讀取 SKILL.md。
4. 確認 references/SOURCE.json、references/SKILL_INDEX.md 與 references/_catalog/ 存在。
5. 回報安裝目錄、Skill repository commit 與目前 upstream documentation commit。

安裝後請這樣測試：
使用 $openclaw-docs，依本地同步的 OpenClaw 官方文件，說明如何檢查 Gateway health。
請列出引用的本地文件路徑，並區分官方文件事實與你的推論。

GitHub repository 每日自動同步，但已安裝的 Skill checkout 不會自己更新。
需要最新 snapshot 時，必須重新執行 installer；installer 會執行 git pull --ff-only。
```

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
