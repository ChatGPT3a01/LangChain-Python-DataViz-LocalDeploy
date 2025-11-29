# 📘 Jupyter Lab 專案教學指南

## Day3 資料視覺化專案完整操作教學

---

## 🎯 教學目標

本教學將帶領學員使用 **Jupyter Lab** 來：
1. 開啟並瀏覽專案程式碼
2. 執行數據生成程式
3. 執行數據分析程式
4. 查看輸出結果

---

## 📦 包含的 4 個專案

| 專案名稱 | 難度 | 特色 |
|---------|------|------|
| 台灣股市數據分析 | ⭐⭐⭐ 高級 | 技術指標、K線圖 |
| 台灣氣象數據視覺化 | ⭐ 初級 | 熱力圖、趨勢分析 |
| 台灣餐廳美食分析 | ⭐ 初級 | 評分分布、相關性 |
| 社群媒體數據分析 | ⭐⭐ 中級 | 多平台比較、成長率 |

---

## 🚀 步驟 1：啟動 Jupyter Lab

### 方法 A：從專案資料夾啟動（推薦）

**Windows：**
```bash
# 1. 開啟命令提示字元（CMD）或 PowerShell

# 2. 進入 Day3 資料夾
cd "D:\Python_快速掌握Python專案開發實作\netlify\Day3_資料視覺化專案"

# 3. 啟動虛擬環境（如果有建立）
venv\Scripts\activate

# 4. 啟動 Jupyter Lab
jupyter lab
```

**Mac/Linux：**
```bash
# 1. 開啟終端機

# 2. 進入 Day3 資料夾
cd "/path/to/Day3_資料視覺化專案"

# 3. 啟動虛擬環境（如果有建立）
source venv/bin/activate

# 4. 啟動 Jupyter Lab
jupyter lab
```

### 方法 B：從 Anaconda Navigator 啟動

1. 開啟 **Anaconda Navigator**
2. 點選 **Jupyter Lab** 的 Launch 按鈕
3. 在瀏覽器中導航到專案資料夾

---

**啟動成功後，會自動開啟瀏覽器，顯示：**
```
http://localhost:8888/lab
```

---

## 📂 步驟 2：瀏覽專案結構

在 Jupyter Lab 左側檔案瀏覽器中，你會看到：

```
Day3_資料視覺化專案/
├── 台灣股市數據分析專案/
│   ├── data/               ← 數據資料夾
│   ├── output/             ← 輸出結果資料夾
│   ├── generate_local_data.py  ← 數據生成程式
│   ├── main.py            ← 主分析程式
│   ├── requirements.txt   ← 套件清單
│   └── README.md          ← 說明文件
│
├── 台灣氣象數據視覺化專案/
│   ├── data/
│   ├── output/
│   ├── generate_local_data.py
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
│
├── 台灣餐廳美食分析專案/
│   ├── data/
│   ├── output/
│   ├── generate_local_data.py
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
│
└── 社群媒體數據分析專案/
    ├── data/
    ├── output/
    ├── generate_local_data.py
    ├── main.py
    ├── requirements.txt
    └── README.md
```

---

## 🔍 步驟 3：查看程式碼

### 方法 1：直接雙擊開啟

1. 在左側檔案瀏覽器中，點選專案資料夾
2. 雙擊 `.py` 檔案即可開啟
3. Jupyter Lab 會以**文字編輯器模式**開啟

**可以查看的檔案：**
- `README.md` - 專案說明文件（會以 Markdown 渲染顯示）
- `generate_local_data.py` - 數據生成程式碼
- `main.py` - 主分析程式碼
- `requirements.txt` - 套件清單

### 方法 2：在終端機中查看

1. 點選 Jupyter Lab 頂部選單：**File → New → Terminal**
2. 在終端機中輸入：
   ```bash
   cd 台灣股市數據分析專案
   cat main.py
   # 或使用
   more main.py
   ```

---

## 💻 步驟 4：執行程式

### 方法 A：使用 Jupyter Lab 終端機（推薦教學使用）

#### 4.1 開啟終端機

點選：**File → New → Terminal**

或點擊左側 **+** 按鈕，然後選擇 **Terminal**

#### 4.2 進入專案資料夾

以**台灣股市數據分析專案**為例：

```bash
cd 台灣股市數據分析專案
```

#### 4.3 查看檔案列表

```bash
# Windows
dir

# Mac/Linux
ls
```

應該會看到：
```
data/
generate_local_data.py
main.py
README.md
requirements.txt
```

#### 4.4 執行數據生成程式

```bash
python generate_local_data.py
```

**預期輸出：**
```
============================================================
台灣股市數據生成工具
============================================================
正在生成 台積電(2330) 的股價數據...
  [OK] 已儲存: data/2330.csv
  - 數據天數: 250 天
  - 平均股價: $550.00
  ...
```

⚠️ **中文可能亂碼，但不影響執行！**

#### 4.5 執行主分析程式

```bash
python main.py
```

**預期輸出：**
```
============================================================
台灣股市數據分析程式
============================================================
正在載入股市數據...
[OK] 載入 台積電(2330) 數據成功
...
[OK] 已儲存：output/台積電_技術分析.png
...
```

---

### 方法 B：建立 Jupyter Notebook 執行

如果你想**一步一步展示**，可以建立 Notebook：

#### 建立新的 Notebook

1. 點選：**File → New → Notebook**
2. 選擇 Kernel：**Python 3**

#### 在 Notebook 中執行

**Cell 1：切換到專案資料夾**
```python
%cd 台灣股市數據分析專案
```

**Cell 2：執行數據生成**
```python
%run generate_local_data.py
```

**Cell 3：執行主程式**
```python
%run main.py
```

**Cell 4：查看輸出檔案**
```python
import os
print("輸出檔案：")
for file in os.listdir('output'):
    print(f"  - {file}")
```

**Cell 5：顯示圖片**
```python
from IPython.display import Image, display

# 顯示第一張圖
display(Image(filename='output/台積電_技術分析.png'))
```

---

## 📊 步驟 5：查看輸出結果

### 方法 1：在 Jupyter Lab 中直接查看圖片

1. 在左側檔案瀏覽器中
2. 進入 `output/` 資料夾
3. 雙擊 `.png` 圖片檔案
4. Jupyter Lab 會顯示圖片預覽

### 方法 2：查看 CSV 數據檔案

1. 雙擊 `.csv` 檔案
2. Jupyter Lab 會以**表格形式**顯示數據

### 方法 3：查看 PDF 報表

1. 雙擊 `.pdf` 檔案
2. Jupyter Lab 會在新分頁中開啟 PDF

### 方法 4：使用 Pandas 讀取並查看

在 Notebook 中：

```python
import pandas as pd

# 讀取 CSV
df = pd.read_csv('output/社群媒體原始數據.csv')

# 顯示前 10 筆
df.head(10)

# 顯示統計摘要
df.describe()
```

---

## 🎓 教學示範流程（完整版）

### 以「台灣股市數據分析專案」為例

#### 第 1 步：開啟專案說明

```bash
# 在終端機中
cd 台灣股市數據分析專案
cat README.md
```

或在 Jupyter Lab 中雙擊 `README.md`

#### 第 2 步：查看數據生成程式

雙擊 `generate_local_data.py`，向學員說明：

```python
# 這段程式碼：
# 1. 生成模擬股價數據
# 2. 使用隨機遊走模型
# 3. 加入季節性波動
# 4. 儲存為 CSV 檔案
```

#### 第 3 步：執行數據生成

```bash
python generate_local_data.py
```

**向學員展示：**
- 終端機輸出的進度訊息
- `data/` 資料夾中新增的 CSV 檔案

#### 第 4 步：查看生成的數據

```python
import pandas as pd

# 讀取台積電數據
df = pd.read_csv('data/2330.csv')

# 顯示前 10 筆
print(df.head(10))

# 顯示欄位
print(df.columns)

# 顯示統計摘要
print(df.describe())
```

#### 第 5 步：查看主程式

雙擊 `main.py`，向學員說明程式結構：

```python
# main.py 結構：
# 1. load_stock_data() - 載入數據
# 2. calculate_indicators() - 計算技術指標
# 3. plot_candlestick() - 繪製 K線圖
# 4. compare_stocks() - 多檔股票比較
# 5. save_outputs() - 儲存結果
```

#### 第 6 步：執行主程式

```bash
python main.py
```

**向學員展示：**
- 程式執行過程
- 終端機統計報告
- 生成的圖表檔案

#### 第 7 步：查看輸出結果

在 Jupyter Lab 中開啟：
1. `output/台積電_技術分析.png` - K線圖
2. `output/多檔股票比較.png` - 比較圖
3. `output/台股分析報告.pdf` - PDF 報表

---

## 🔧 進階技巧

### 技巧 1：分割視窗查看

1. 拖曳檔案標籤頁到畫面右側
2. 可以**同時查看程式碼和輸出結果**

### 技巧 2：使用快捷鍵

- `Ctrl + B`：切換左側邊欄顯示/隱藏
- `Ctrl + Shift + C`：開啟命令面板
- `Ctrl + S`：儲存檔案
- `Ctrl + Shift + -`：分割編輯器

### 技巧 3：即時修改程式碼

1. 在 Jupyter Lab 中直接修改 `.py` 檔案
2. 按 `Ctrl + S` 儲存
3. 在終端機中重新執行程式

### 技巧 4：批次執行所有專案

建立一個 Notebook：

```python
import os
import subprocess

projects = [
    '台灣股市數據分析專案',
    '台灣氣象數據視覺化專案',
    '台灣餐廳美食分析專案',
    '社群媒體數據分析專案'
]

for project in projects:
    print(f"\n{'='*60}")
    print(f"執行專案：{project}")
    print('='*60)

    os.chdir(project)

    # 生成數據
    subprocess.run(['python', 'generate_local_data.py'])

    # 執行分析
    subprocess.run(['python', 'main.py'])

    # 回到上層目錄
    os.chdir('..')

print("\n所有專案執行完成！")
```

---

## ⚠️ 常見問題與解決

### Q1：終端機顯示中文亂碼？

**現象：**
```
���s�C��ƾڤ��R�M��  ← 亂碼
```

**解決方法：**
- **不影響程式執行！** 程式會正常運作
- 圖表和檔案中的中文都正常
- 如果需要看清楚：
  1. 使用 Windows Terminal
  2. 或直接查看輸出檔案

### Q2：找不到套件（ModuleNotFoundError）

**錯誤訊息：**
```
ModuleNotFoundError: No module named 'matplotlib'
```

**解決方法：**

在 Jupyter Lab 終端機中：
```bash
pip install -r requirements.txt
```

或安裝個別套件：
```bash
pip install matplotlib pandas numpy seaborn
```

### Q3：Jupyter Lab 無法開啟？

**檢查方法：**

```bash
# 檢查 Jupyter Lab 是否已安裝
jupyter lab --version

# 如果未安裝
pip install jupyterlab

# 如果使用 Anaconda
conda install -c conda-forge jupyterlab
```

### Q4：想修改圖表樣式？

**步驟：**
1. 在 Jupyter Lab 中開啟 `main.py`
2. 找到繪圖函數（例如 `plot_candlestick()`）
3. 修改顏色、字型、大小等參數
4. 儲存檔案
5. 重新執行程式

**範例修改：**
```python
# 原本
plt.figure(figsize=(16, 10))

# 改為更大的圖
plt.figure(figsize=(20, 12))
```

---

## 📋 教學檢查清單

### 課前準備
- [ ] 確認所有專案的 `data/` 資料夾已生成數據
- [ ] 確認所有套件已安裝
- [ ] 測試每個專案都能正常執行
- [ ] 準備好示範用的 Notebook

### 教學流程
- [ ] 展示如何啟動 Jupyter Lab
- [ ] 說明專案資料夾結構
- [ ] 示範查看 README.md 說明文件
- [ ] 示範執行 generate_local_data.py
- [ ] 示範執行 main.py
- [ ] 展示輸出結果（圖表、CSV、PDF）
- [ ] 說明如何修改程式碼
- [ ] 回答學員問題

### 學員練習
- [ ] 讓學員自行開啟一個專案
- [ ] 讓學員執行數據生成
- [ ] 讓學員執行主程式
- [ ] 讓學員查看輸出結果
- [ ] 讓學員嘗試修改參數

---

## 🎯 4 個專案的教學重點

### 專案 1：台灣股市數據分析（高級）

**教學重點：**
- 📊 **技術指標**：MA、MACD、RSI、布林通道
- 📈 **K線圖**：使用 mplfinance 套件
- 🔢 **數據處理**：時間序列、滾動計算
- 💼 **金融應用**：投資分析實務

**適合對象：** 有程式基礎、對金融有興趣的學員

**教學時間：** 90 分鐘

---

### 專案 2：台灣氣象數據視覺化（初級）

**教學重點：**
- 🌡️ **熱力圖**：Seaborn heatmap
- 📊 **趨勢分析**：溫度、降雨、濕度
- 🗓️ **季節分組**：時間序列分組
- 🏙️ **多城市比較**：資料合併與分析

**適合對象：** 初學者、視覺化入門

**教學時間：** 60 分鐘

---

### 專案 3：台灣餐廳美食分析（初級）

**教學重點：**
- ⭐ **評分分析**：分布、箱型圖
- 💰 **價格分析**：相關性分析
- 🍜 **類型統計**：分組統計
- 📊 **多種圖表**：圓餅圖、長條圖、熱力圖

**適合對象：** 初學者、對美食有興趣的學員

**教學時間：** 60 分鐘

---

### 專案 4：社群媒體數據分析（中級）

**教學重點：**
- 📱 **多平台比較**：6 個社群平台
- 📈 **成長率計算**：成長指標分析
- 💬 **互動率**：粉絲互動分析
- 📊 **儀表板**：綜合視覺化

**適合對象：** 有基礎、對社群媒體有興趣的學員

**教學時間：** 75 分鐘

---

## 💡 教學建議

### 建議 1：由簡入難

**建議順序：**
1. 台灣餐廳美食分析（初級）← 最簡單
2. 台灣氣象數據視覺化（初級）
3. 社群媒體數據分析（中級）
4. 台灣股市數據分析（高級）← 最難

### 建議 2：互動式教學

- ✅ 讓學員跟著操作
- ✅ 鼓勵學員修改參數
- ✅ 讓學員嘗試新增功能
- ✅ 分組討論分析結果

### 建議 3：實務應用

每個專案都可以延伸：
- **股市專案**：實際股票投資策略
- **氣象專案**：氣候變遷分析
- **餐廳專案**：開店選址決策
- **社群專案**：社群經營策略

---

## 🔗 相關資源

### 官方文檔
- [Jupyter Lab 官方文檔](https://jupyterlab.readthedocs.io/)
- [Pandas 教學](https://pandas.pydata.org/docs/)
- [Matplotlib 教學](https://matplotlib.org/stable/tutorials/index.html)

### 延伸學習
- [Python 資料分析入門](https://www.datacamp.com/)
- [視覺化最佳實踐](https://www.storytellingwithdata.com/)

---

## 📞 支援與回饋

如果在教學過程中遇到問題：
1. 查看各專案的 `README.md` 常見問題
2. 檢查 Jupyter Lab 終端機的錯誤訊息
3. 確認所有套件已正確安裝

---

**教學愉快！** 🎉

---

**文件版本：** 1.0
**最後更新：** 2026-11-25
**作者：** Python 資料視覺化教學團隊
