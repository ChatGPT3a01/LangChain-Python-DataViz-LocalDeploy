# Python 資料視覺化與 AI 專案開發

> LangChain + 實戰專案完整教學

## 📘 教學簡報入口

本專案搭配完整簡報教材，請由此進入：

👉 **[Python 資料視覺化 x LangChain｜簡報入口](https://chatgpt3a01.github.io/LangChain-Python-DataViz-LocalDeploy/簡報/index.html)**

## 下載專案

### 方式一：直接下載 ZIP

1. 點擊頁面上方的綠色 **Code** 按鈕
2. 選擇 **Download ZIP**
3. 解壓縮到你想要的資料夾

### 方式二：使用 Git Clone

```bash
git clone https://github.com/ChatGPT3a01/LangChain-Python-DataViz-LocalDeploy.git
```

---

## 快速開始

### 1. 安裝 Python 環境

確保你的電腦已安裝 Python 3.8 或以上版本：

```bash
python --version
```

### 2. 進入專案資料夾

```bash
cd Day3-LangChain-Python-DataViz-LocalDeploy
```

### 3. 建立虛擬環境（建議）

```bash
python -m venv venv
```

### 4. 啟動虛擬環境

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 5. 安裝依賴套件

進入任一專案資料夾，安裝所需套件：

```bash
cd 1_台灣餐廳美食分析專案
pip install -r requirements.txt
```

### 6. 執行專案

```bash
python main.py
```

---

## 課程內容

### 環境建置 (Unit 0)
- Unit 0-1: Jupyter Lab 環境建置
- Unit 0-2: Jupyter Lab 中文化設定

### LangChain 基礎 (Unit 1-4)
| 單元 | 主題 | 資料夾 |
|------|------|--------|
| Unit 1 | LangChain 環境建置 | `0_LangChain基礎實作/Unit1_環境建置` |
| Unit 2 | 提示詞工程 | `0_LangChain基礎實作/Unit2_提示詞工程` |
| Unit 3 | 輸出解析器 | `0_LangChain基礎實作/Unit3_輸出解析器` |
| Unit 4 | 鏈式調用 | `0_LangChain基礎實作/Unit4_鏈式調用` |

### AI 專案實戰 (Unit 5-10)
| 單元 | 專案名稱 | 資料夾 |
|------|----------|--------|
| Unit 5 | 台灣餐廳美食分析專案 | `1_台灣餐廳美食分析專案` |
| Unit 6 | 台灣氣象數據視覺化專案 | `2_台灣氣象數據視覺化專案` |
| Unit 7 | 電商銷售數據分析專案 | `3_電商銷售數據分析專案` |
| Unit 8 | 社群媒體數據分析專案 | `4_社群媒體數據分析專案` |
| Unit 9 | COVID-19 疫情數據視覺化專案 | `5_COVID-19疫情數據視覺化專案` |
| Unit 10 | 台灣股市數據分析專案 | `6_台灣股市數據分析專案` |

---

## 資料夾結構

```
Day3-LangChain-Python-DataViz-LocalDeploy/
├── index.html                     # 網站首頁
├── 簡報/                          # 所有 HTML 簡報
│   ├── index.html                 # 簡報索引頁
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
├── 0_LangChain基礎實作/            # LangChain 基礎程式碼
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

## 自行部署網站

如果你想 Fork 這個專案並自行部署：

### 步驟 1: Fork 專案

點擊頁面右上角的 **Fork** 按鈕

### 步驟 2: 啟用 GitHub Pages

1. 進入你 Fork 的 Repository
2. 點擊 **Settings**（設定）
3. 左側選單找到 **Pages**
4. 在 **Source** 選擇 **Deploy from a branch**
5. 在 **Branch** 選擇 `main`，路徑選擇 `/ (root)`
6. 點擊 **Save**

### 步驟 3: 等待部署完成

約 1-2 分鐘後，你的網站就會上線：

```
https://你的GitHub帳號.github.io/Day3-LangChain-Python-DataViz-LocalDeploy/
```

---

## 使用 Jupyter Lab 學習

### 安裝 Jupyter Lab

```bash
pip install jupyterlab
```

### 啟動 Jupyter Lab

```bash
cd Day3-LangChain-Python-DataViz-LocalDeploy
jupyter lab
```

### 在 Jupyter Lab 中執行專案

1. 開啟 Terminal 終端機
2. 進入專案資料夾
3. 執行 `python main.py`

---

## 系統需求

- **Python:** 3.8 或以上版本
- **記憶體:** 至少 4GB RAM
- **硬碟空間:** 約 500MB（含套件）
- **網路:** 不需要（專案可完全離線執行）

---

## 依賴套件

```
matplotlib>=3.8.0
numpy>=1.26.0
pandas>=2.1.0
seaborn>=0.13.0
requests>=2.31.0
langchain>=0.1.0
langchain-openai>=0.0.5
python-dotenv>=1.0.0
```

---

## 學習路徑建議

### 完全新手
1. 閱讀課程簡報 Unit 0（環境建置）
2. 設定好 Python 和 Jupyter Lab 環境
3. 從 Unit 1 開始學習 LangChain 基礎
4. 逐步完成 Unit 5-10 的專案實作

### 有 Python 基礎
1. 快速瀏覽 Unit 1-4 的簡報
2. 直接執行專案程式碼
3. 閱讀程式碼註解理解實作方式
4. 嘗試修改和擴展專案功能

---

## 課程資源

- **Facebook:** https://www.facebook.com/
- **YouTube:** https://www.youtube.com/@Liang-yt02
- **3A 社團:** https://www.facebook.com/groups/2754139931432955

---

## 授權

本專案為教學用途，歡迎學習使用。

---

**版本：** 2.0
**更新日期：** 2025-11-30
**課程：** Python 資料視覺化與 AI 專案開發
**講師：** 曾慶良（阿亮老師）
