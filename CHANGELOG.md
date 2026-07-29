# Changelog

## 2026-07-29 — 分層文件路由與安全同步架構

### 摘要

本次變更將 OpenClaw 文件 Skill 從單一大型索引改為分層路由架構，降低 LLM
每次查詢需要載入的上下文。同步、安裝、來源追蹤與 CI 驗證流程一併重整。

### 架構變更

舊架構：

```text
SKILL.md
  → 完整 SKILL_INDEX.md
  → 目標文件
```

新架構：

```text
SKILL.md
  → 精簡 SKILL_INDEX.md
  → 主題 catalog
  → 必要時進入字母區段 catalog
  → 最相關的 1–3 篇文件
  → 只讀取相關段落
```

精確錯誤訊息、CLI 指令與設定鍵會直接搜尋 `references/`，不需要先載入全域索引。

### LLM 引導

- 將 `SKILL.md` 精簡為文件搜尋、版本判斷、診斷、安全操作與回答規則。
- 廣泛問題先經過主題路由；精確問題直接全文搜尋。
- 每輪最多選擇三篇候選文件。
- 長分類每 30 篇切分一個 catalog 區段。
- catalog 使用上游文件的 `title`、`summary` 與 `read_when` metadata。
- 要求先確認 OpenClaw 版本，並標示上游 `main` 與本機安裝版本的差異風險。
- 將修改設定、更新、重啟、`--fix`、`--force`、配對與訊息發送列為
  state-changing actions。
- 要求引用實際使用的本地參考文件，並區分文件事實與推論。

### 索引生成

- `scripts/generate_index.py` 支援 `.md` 與 `.mdx`。
- 索引納入分類首頁文件。
- 忽略 symlink、隱藏文件與既有生成結果。
- 產生精簡的 `references/SKILL_INDEX.md`。
- 產生 `references/_catalog/` 分類與區段索引。
- 提供 `--check` 模式驗證 committed indexes 是否過期。
- 驗證所有生成連結均可解析。

本次生成結果：

- 主索引：約 2.6 KB。
- `SKILL.md`：約 6.3 KB。
- 最大單一 catalog：約 9.3 KB。
- catalog：52 份。

### 文件同步

- `scripts/sync-docs.sh` 改為嚴格錯誤處理。
- 在 repository 內建立暫存工作目錄，確保替換操作位於相同 filesystem。
- 先下載、複製、統計及驗證上游文件。
- 驗證最低文件數量與必要入口文件。
- 產生索引並執行一致性檢查後才替換 `references/`。
- 同步失敗時保留既有 references。
- 排除上游隱藏維護資料，避免非使用者文件進入 Skill catalog。
- 新增 `references/SOURCE.json`，記錄：
  - 上游 repository
  - 上游 commit SHA
  - commit 日期
  - 來源文件數量

本次同步來源：

- Upstream：`openclaw/openclaw`
- Commit：`b231de68090643601cd213412e85afb4a08c79b7`
- 來源文件：752 篇

### 安裝與更新

- `scripts/install-skill.sh` 現在可 clone 到不存在的新目標。
- 既有 Git checkout 使用 fast-forward-only 更新。
- 拒絕覆蓋既有的非 Git 目錄。
- 支援自訂 repository URL 與 branch。
- 移除「每次使用 Skill 都自動更新」行為。
- 統一英文與繁體中文安裝說明。
- 說明受管 Skill 目錄與 Git checkout 的更新差異。

### Agent metadata

- 新增 `agents/openai.yaml`。
- 提供 OpenClaw Docs 顯示名稱、簡短描述與預設 prompt。

### CI 與測試

- GitHub Actions 加入 concurrency control。
- 每次同步前執行 repository tests。
- 同步後驗證 `SOURCE.json`、`SKILL_INDEX.md` 與 catalog 一致性。
- 新增 9 個回歸測試，涵蓋：
  - `.mdx`、分類首頁與 metadata 索引
  - 大分類切分
  - 隱藏文件與 symlink 排除
  - 生成連結與來源文件數量
  - 新目標安裝
  - 非 Git 目標保護
  - 漸進式披露與安全指引
  - 同步失敗資料保護
  - 本地 fixture 同步與來源資訊

### 相容性

- 既有 Git checkout 可繼續使用。
- 舊版安裝不含 `_catalog/` 時，Skill 會退回直接搜尋對應 `references/<topic>/`。
- 只複製檔案的安裝仍可使用現有 snapshot，但需由宿主平台負責更新。
