# Python 資料視覺化與 AI 專案開發 - 完整操作指南

## 線上課程資源

**課程簡報網址：** https://chatgpt3a01.github.io/Day3-Python-AI-Data-Visualization/

**GitHub Repository：** https://github.com/ChatGPT3a01/Day3-Python-AI-Data-Visualization

---

## 目錄

1. [課程概述](#課程概述)
2. [環境準備](#環境準備)
3. [LangChain 基礎教學](#langchain-基礎教學)
4. [六大 AI 專案實戰](#六大-ai-專案實戰)
5. [常見問題排除](#常見問題排除)
6. [學習建議](#學習建議)

---

## 課程概述

本課程涵蓋 LangChain 基礎知識與六大 AI 實戰專案，從環境建置到完整專案開發。

### 課程單元總覽

| 單元 | 主題 | 難度 | 說明 |
|------|------|------|------|
| Unit 0-1 | Jupyter Lab 環境建置 | ⭐ | 開發環境設定 |
| Unit 0-2 | Jupyter Lab 中文化設定 | ⭐ | 介面中文化 |
| Unit 1 | LangChain 環境建置 | ⭐⭐ | API 金鑰設定 |
| Unit 2 | 提示詞工程 | ⭐⭐ | Prompt 設計技巧 |
| Unit 3 | 輸出解析器 | ⭐⭐ | 結構化輸出 |
| Unit 4 | 鏈式調用 | ⭐⭐⭐ | Chain 串接 |
| Unit 5 | 台灣餐廳美食分析專案 | ⭐⭐⭐ | 資料分析實戰 |
| Unit 6 | 台灣氣象數據視覺化專案 | ⭐⭐⭐ | 時間序列分析 |
| Unit 7 | 電商銷售數據分析專案 | ⭐⭐ | 儀表板設計 |
| Unit 8 | 社群媒體數據分析專案 | ⭐⭐⭐ | 多平台分析 |
| Unit 9 | COVID-19 疫情數據視覺化專案 | ⭐⭐⭐ | 真實數據分析 |
| Unit 10 | 台灣股市數據分析專案 | ⭐⭐⭐⭐ | 金融數據分析 |

---

## 環境準備

### 步驟 1：下載專案

**方式一：直接下載 ZIP**

1. 前往 https://github.com/ChatGPT3a01/Day3-Python-AI-Data-Visualization
2. 點擊綠色 **Code** 按鈕
3. 選擇 **Download ZIP**
4. 解壓縮到你想要的資料夾

**方式二：使用 Git Clone**

```bash
git clone https://github.com/ChatGPT3a01/Day3-Python-AI-Data-Visualization.git
```

---

### 步驟 2：確認 Python 環境

打開終端機（命令提示字元），輸入：

```bash
python --version
```

**預期輸出：**
```
Python 3.11.5
```

如果版本低於 3.8，請先更新 Python。

**下載 Python：** https://www.python.org/downloads/

---

### 步驟 3：專案結構說明

```
Day3-Python-AI-Data-Visualization/
├── index.html                      # 網站首頁
├── 簡報/                           # 課程簡報
│   ├── index.html                  # 簡報索引
│   ├── unit0-1_jupyter_setup.html
│   ├── unit0-2_jupyter_chinese.html
│   ├── unit1_langchain_setup.html
│   ├── unit2_prompt_engineering.html
│   ├── unit3_output_parsers.html
│   ├── unit4_chains.html
│   ├── unit5_restaurant_ai.html
│   ├── unit6_weather_ai.html
│   ├── unit7_ecommerce_ai.html
│   ├── unit8_social_media_ai.html
│   ├── unit9_covid_ai.html
│   └── unit10_stock_ai.html
├── 0_LangChain基礎實作/
│   ├── Unit1_環境建置/
│   ├── Unit2_提示詞工程/
│   ├── Unit3_輸出解析器/
│   └── Unit4_鏈式調用/
├── 1_台灣餐廳美食分析專案/
├── 2_台灣氣象數據視覺化專案/
├── 3_電商銷售數據分析專案/
├── 4_社群媒體數據分析專案/
├── 5_COVID-19疫情數據視覺化專案/
└── 6_台灣股市數據分析專案/
```

---

## LangChain 基礎教學

### Unit 1：環境建置

**位置：** `0_LangChain基礎實作/Unit1_環境建置/`

#### 操作步驟

```bash
# 1. 進入資料夾
cd "0_LangChain基礎實作/Unit1_環境建置"

# 2. 建立虛擬環境
python -m venv venv

# 3. 啟動虛擬環境（Windows）
venv\Scripts\activate

# 4. 安裝套件
pip install langchain langchain-openai python-dotenv

# 5. 設定 API 金鑰
# 複製 .env.example 為 .env，填入你的 OpenAI API Key
copy .env.example .env

# 6. 執行程式
python main.py
```

#### 設定 API 金鑰

編輯 `.env` 檔案：

```
OPENAI_API_KEY=sk-your-api-key-here
```

**取得 API Key：** https://platform.openai.com/api-keys

---

### Unit 2：提示詞工程

**位置：** `0_LangChain基礎實作/Unit2_提示詞工程/`

學習如何設計有效的 Prompt，包括：
- 角色設定
- 任務描述
- 輸出格式指定
- 範例提供（Few-shot）

---

### Unit 3：輸出解析器

**位置：** `0_LangChain基礎實作/Unit3_輸出解析器/`

學習如何將 AI 輸出轉換為結構化資料：
- JSON 解析器
- Pydantic 解析器
- 列表解析器

---

### Unit 4：鏈式調用

**位置：** `0_LangChain基礎實作/Unit4_鏈式調用/`

學習如何串接多個處理步驟：
- 簡單鏈（SimpleChain）
- 順序鏈（SequentialChain）
- LCEL 表達式

---

## 六大 AI 專案實戰

### 專案一：台灣餐廳美食分析專案（Unit 5）

**位置：** `1_台灣餐廳美食分析專案/`

**難度：** ⭐⭐⭐

**學習重點：**
- 餐廳評論資料分析
- 評分分佈視覺化
- 城市美食比較
- 價格與評分相關性分析

#### 執行步驟

```bash
# 1. 進入專案資料夾
cd "1_台灣餐廳美食分析專案"

# 2. 建立虛擬環境
python -m venv venv
venv\Scripts\activate

# 3. 安裝依賴
pip install -r requirements.txt

# 4. 執行程式
python main.py
```

#### 輸出檔案

- `output/城市餐廳數量直方圖.png`
- `output/評分分佈分析.png`
- `output/價格分析.png`
- `output/餐廳類型分析.png`
- `output/相關性分析.png`
- `output/城市比較.png`
- `output/台灣餐廳美食分析報告.pdf`

---

### 專案二：台灣氣象數據視覺化專案（Unit 6）

**位置：** `2_台灣氣象數據視覺化專案/`

**難度：** ⭐⭐⭐

**學習重點：**
- 氣象資料處理
- 時間序列分析
- 多城市比較
- 熱力圖繪製

#### 執行步驟

```bash
cd "2_台灣氣象數據視覺化專案"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

#### 輸出檔案

- `output/溫度趨勢分析.png`
- `output/降雨量分析.png`
- `output/氣象熱力圖.png`
- `output/城市綜合比較.png`
- `output/台灣氣象分析報告.pdf`

---

### 專案三：電商銷售數據分析專案（Unit 7）

**位置：** `3_電商銷售數據分析專案/`

**難度：** ⭐⭐

**學習重點：**
- 銷售數據模擬生成
- 營收趨勢分析
- 移動平均計算
- 儀表板設計

#### 執行步驟

```bash
cd "3_電商銷售數據分析專案"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

#### 輸出檔案

- `output/銷售儀表板.png`
- `output/銷售數據.csv`
- `output/銷售分析報告.pdf`

---

### 專案四：社群媒體數據分析專案（Unit 8）

**位置：** `4_社群媒體數據分析專案/`

**難度：** ⭐⭐⭐

**學習重點：**
- 多平台數據整合
- 互動率計算
- 成長趨勢分析
- 平台比較視覺化

#### 執行步驟

```bash
cd "4_社群媒體數據分析專案"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

#### 輸出檔案

- `output/社群媒體分析儀表板.png`
- `output/社群媒體詳細分析.png`
- `output/社群媒體原始數據.csv`
- `output/社群媒體成長指標.csv`
- `output/社群媒體分析報告.pdf`

---

### 專案五：COVID-19 疫情數據視覺化專案（Unit 9）

**位置：** `5_COVID-19疫情數據視覺化專案/`

**難度：** ⭐⭐⭐

**特色：** 已內建本地數據，無需網路連線

**學習重點：**
- 真實疫情數據分析
- 累計確診趨勢
- 每日新增分析
- 國家排行比較

#### 執行步驟

```bash
cd "5_COVID-19疫情數據視覺化專案"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

#### 輸出檔案

- `output/COVID-19疫情分析圖表.png`
- `output/累計確診數據.csv`
- `output/每日新增數據.csv`
- `output/COVID-19疫情分析報告.pdf`

---

### 專案六：台灣股市數據分析專案（Unit 10）

**位置：** `6_台灣股市數據分析專案/`

**難度：** ⭐⭐⭐⭐

**學習重點：**
- 股價走勢分析
- 技術指標計算（MA、RSI）
- K線圖繪製
- 多股票比較

#### 執行步驟

```bash
cd "6_台灣股市數據分析專案"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

#### 輸出檔案

- `output/2330_台積電_分析圖.png`
- `output/2317_鴻海_分析圖.png`
- `output/2454_聯發科_分析圖.png`
- `output/股票比較分析.png`
- `output/台股分析報告.pdf`

---

## 常見問題排除

### Q1：ModuleNotFoundError: No module named 'xxx'

**原因：** 套件未安裝或虛擬環境未啟動

**解決方法：**

```bash
# 確認虛擬環境已啟動（命令列前方應該有 (venv)）
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# 重新安裝套件
pip install -r requirements.txt
```

---

### Q2：中文字型顯示為方框或亂碼

**原因：** 系統缺少中文字型

**解決方法：**

**Windows：**
程式已自動設定使用「微軟正黑體」，通常內建。

**Mac：**
```bash
brew tap homebrew/cask-fonts
brew install --cask font-noto-sans-cjk-tc
```

修改程式碼：
```python
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Arial Unicode MS']
```

---

### Q3：API 金鑰錯誤

**錯誤訊息：**
```
AuthenticationError: Incorrect API key provided
```

**解決方法：**

1. 確認 `.env` 檔案存在
2. 確認 API Key 格式正確（以 `sk-` 開頭）
3. 確認 API Key 有足夠的額度

---

### Q4：虛擬環境無法啟動（Windows）

**錯誤訊息：**
```
因為這個系統上已停用指令碼執行，所以無法載入...
```

**解決方法：**

以管理員身份開啟 PowerShell，執行：
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

### Q5：pip install 速度很慢

**解決方法：**

使用國內鏡像：
```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

---

### Q6：圖表視窗無法顯示

**原因：** 在遠端伺服器或不支援 GUI 的環境中執行

**解決方法：**

在程式碼開頭加入：
```python
import matplotlib
matplotlib.use('Agg')  # 不顯示視窗，直接儲存
```

---

### Q7：PermissionError: Permission denied

**原因：** 檔案被其他程式佔用

**解決方法：**

1. 關閉所有開啟 output 資料夾中檔案的程式（如 Excel、PDF 閱讀器）
2. 刪除 output 資料夾
3. 重新執行程式

---

### Q8：本地數據檔案遺失

**解決方法：**

重新生成本地數據：
```bash
python generate_local_data.py
```

---

## 學習建議

### 學習路徑

#### 第 1 週：環境建置與基礎

1. 完成 Unit 0-1, 0-2（Jupyter Lab 設定）
2. 完成 Unit 1（LangChain 環境建置）
3. 執行專案三（電商銷售）熟悉流程

#### 第 2 週：LangChain 核心概念

1. 完成 Unit 2（提示詞工程）
2. 完成 Unit 3（輸出解析器）
3. 完成 Unit 4（鏈式調用）

#### 第 3 週：專案實戰

1. 完成專案一（餐廳分析）
2. 完成專案二（氣象視覺化）
3. 完成專案四（社群媒體）

#### 第 4 週：進階應用

1. 完成專案五（COVID-19）
2. 完成專案六（股市分析）
3. 嘗試修改程式碼，新增自己的分析

---

### 學習重點

#### 資料處理技能

- Pandas DataFrame 操作
- 資料清洗與轉換
- 時間序列處理
- 資料聚合與分組

#### 視覺化技能

- Matplotlib 基礎繪圖
- 多子圖佈局（Subplots）
- 圖表美化（顏色、標籤、圖例）
- 高解析度輸出

#### AI 應用技能

- LangChain 框架使用
- Prompt 設計技巧
- API 整合
- 結構化輸出

---

### 進階練習

#### 練習 1：修改視覺化參數

嘗試修改以下項目：
- 圖表顏色
- 標題文字
- 圖例位置
- 輸出解析度

#### 練習 2：新增統計指標

在程式中新增：
```python
# 計算標準差
print(f"標準差：{df['欄位'].std():.2f}")

# 計算中位數
print(f"中位數：{df['欄位'].median():.2f}")
```

#### 練習 3：整合多個專案

嘗試將不同專案的技術結合，例如：
- 用 LangChain 分析股市新聞
- 用 AI 生成資料分析報告

---

## 認證檢查清單

完成以下項目，確認您已掌握本課程內容：

### 基礎技能

- [ ] 成功下載並設定專案
- [ ] 能夠建立和使用虛擬環境
- [ ] 能夠安裝 Python 套件
- [ ] 能夠設定 API 金鑰

### LangChain 技能

- [ ] 理解 Prompt 設計原則
- [ ] 能夠使用輸出解析器
- [ ] 能夠建立簡單的 Chain

### 資料視覺化技能

- [ ] 能夠使用 Matplotlib 繪圖
- [ ] 能夠建立多子圖佈局
- [ ] 能夠匯出高解析度圖表
- [ ] 能夠製作 PDF 報表

### 專案完成度

- [ ] 完成 6 個 AI 專案
- [ ] 理解每個專案的程式碼
- [ ] 能夠修改參數觀察結果
- [ ] 能夠排除常見錯誤

---

## 課程資源

- **線上簡報：** https://chatgpt3a01.github.io/Day3-Python-AI-Data-Visualization/
- **GitHub：** https://github.com/ChatGPT3a01/Day3-Python-AI-Data-Visualization
- **YouTube：** https://www.youtube.com/@Liang-yt02
- **3A 社團：** https://www.facebook.com/groups/2754139931432955

---

**祝您學習愉快！**

---

**文件版本：** 2.0
**最後更新：** 2025-11-30
**講師：** 曾慶良（阿亮老師）
