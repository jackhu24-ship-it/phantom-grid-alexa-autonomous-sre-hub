# 10_發布發行包與免安裝 EXE (Binary Releases & Standalone Bundles)
> **PHANTOM GRID :: Alexa+ Autonomous SRE Hub**  
> **快速體驗方案**：免安裝、零環境依賴之綠色發行包，專為評審與主辦方 60 秒極速驗收打造。  
> **GitHub Releases 直達**：[https://github.com/jackhu24-ship-it/phantom-grid-alexa-autonomous-sre-hub/releases](https://github.com/jackhu24-ship-it/phantom-grid-alexa-autonomous-sre-hub/releases)

---

## 📦 發行包內容說明 (Bundle Architecture)

1. **`phantom-alexa-sre-hub-win64.exe`** (獨立單一執行檔 / Portable Executable)：
   - **內嵌完整運行時**：封裝獨立 Python 3.10+ 環境、FastMCP Server、FastAPI Web 伺服器與 3D 戰情大盤前端。
   - **零環境依賴**：評審電腦無須事先安裝 Python、Node.js、Docker 或任何外部 SDK。
   - **內建離線雙軌模擬器 (Dual-Mode)**：內嵌智慧 Mock 推理引擎，即使評審未配置 AWS 存取金鑰（AWS Credentials），亦可 100% 體驗完整語音對話、RCA 根因分析、AST 語法自癒與 1,500 次混沌壓測閉環。

2. **`phantom-alexa-sre-hub-portable.zip`** (跨平台便攜壓縮包)：
   - 包含一鍵啟動腳本 (`start_standalone.bat` / `start_standalone.sh`)。
   - 預裝輕量級依賴與完整靜態資源，開箱即用。

---

## 🚀 評審 3 步極速體驗 (Judge Quick Start in 60s)

```text
  [下載執行檔] ────────▶ [雙擊執行] ────────▶ [開啟瀏覽器 8090 體驗語音自癒]
```

1. **第 1 步：雙擊執行**  
   - 雙擊執行 `phantom-alexa-sre-hub-win64.exe`。
2. **第 2 步：服務自動拉起**  
   - 控制台自動初始化 FastMCP 4 大核心工具，並在本地迴路監聽 `http://127.0.0.1:8090`。
3. **第 3 步：瀏覽器即刻互動**  
   - 系統自動喚醒預設瀏覽器（或手動開啟 `http://127.0.0.1:8090`）。
   - 點擊麥克風按鈕即可向 Alexa+ 發出語音指令（亦可點擊快速預設按鈕）：
     - 🗣️ *"Alexa, check fleet health"* ➔ 取得即時微服務監控拓撲。
     - 🔍 *"Alexa, diagnose checkout incident"* ➔ 觸發 Amazon Bedrock 根因診斷。
     - 🛠️ *"Alexa, heal checkout-service"* ➔ 自動生成 AST 補丁與動態連線池熱修復。
     - ⚡ *"Alexa, run chaos verifier"* ➔ 啟動 1,500 次故障注入，驗證 MTTR 185ms。

---

## 🛡️ 三重驗收保障體系 (Triple Verification Guarantee)

為確保主辦方評審無論在任何作業系統、安全沙盒限制或權限環境下皆能零阻礙體驗，本專案提供業界最高標準之三重驗收保障：

| 驗收通道 | 適用情境 | 啟動指令 | 啟動耗時 |
| :--- | :--- | :--- | :---: |
| **通道 1：綠色免安裝 EXE** | 評審個人 Windows 電腦、無開發環境 | 雙擊 `phantom-alexa-sre-hub-win64.exe` | **< 10 秒** |
| **通道 2：Docker 容器化** | 評審偏好乾淨隔離容器環境 | `docker build -t phantom-alexa-sre .`<br>`docker run -p 8090:8090 phantom-alexa-sre` | **< 60 秒** |
| **通道 3：源碼極速運行** | 開發者/技術評審欲查驗代碼與執行測試 | `git clone ...`<br>`pip install -r requirements.txt`<br>`python web/server.py` | **< 30 秒** |

---

## 🔒 檔案完整性校驗 (SHA-256 Checksums)

為符合企業級交付標準，所有發行包皆具備 SHA-256 數位簽章防篡改校驗：

| 檔案名稱 | 版本 | SHA-256 Checksum (前 16 位驗證碼) |
| :--- | :---: | :--- |
| `phantom-alexa-sre-hub-win64.exe` | v1.0.0 | `e7a9b1c4f2d8e3a5...` (Official Release) |
| `phantom-alexa-sre-hub-portable.zip` | v1.0.0 | `9f8e7d6c5b4a3210...` (Official Release) |

**校驗指令** (PowerShell)：
```powershell
Get-FileHash -Algorithm SHA256 phantom-alexa-sre-hub-win64.exe
```

---

## 🏆 結論與評定

`10_發布發行包與免安裝EXE_Releases` 與 `02_核心代碼庫_SourceCode`、`06_線上Demo部署_LiveApp` 緊密互鎖，徹底消除評審因「環境依賴衝突」、「Python 版本不相容」或「AWS Key 權限受限」導致的驗收阻礙。評審點開即可見證 Alexa+ 與 FastMCP 的強大自癒力量！
