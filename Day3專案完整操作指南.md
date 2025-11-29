# Day 3 資料視覺化專案 - 完整操作指南

## 📋 目錄

1. [專案概述](#專案概述)
2. [環境準備](#環境準備)
3. [專案一：電商銷售數據分析](#專案一電商銷售數據分析)
4. [專案二：COVID-19 疫情數據視覺化](#專案二covid-19-疫情數據視覺化)
5. [常見問題排除](#常見問題排除)
6. [學習建議](#學習建議)

---

## 專案概述

本指南涵蓋兩個完整的 Python 資料視覺化專案：

### 📊 專案一：電商銷售數據分析專案
- **難度：** ⭐⭐☆☆☆（初級）
- **特色：** 模擬數據、無需網路連線
- **學習重點：** Matplotlib 基礎、資料生成、儀表板設計

### 🌐 專案二：COVID-19 疫情數據視覺化專案
- **難度：** ⭐⭐⭐☆☆（中級）
- **特色：** 真實數據、**已內建本地數據（無需網路）**、時間序列分析
- **學習重點：** 資料載入、清洗、時間序列視覺化
- **✨ 特別說明：已內建完整數據檔案，上課不怕網路斷線！**

---

## 環境準備

### 步驟 1：確認 Python 環境

打開終端機（命令提示字元），輸入以下命令：

```bash
python --version
```

**預期輸出範例：**
```
Python 3.11.5
```

如果版本低於 3.8，請先更新 Python。

**下載 Python：** https://www.python.org/downloads/

---

### 步驟 2：了解專案結構

執行本指南後，您會看到以下資料夾結構：

```
netlify/
├── 電商銷售數據分析專案/
│   ├── main.py                 # 主程式
│   ├── requirements.txt        # 依賴套件清單
│   ├── README.md              # 專案說明文件
│   └── output/                # 輸出資料夾（執行後自動建立）
│       ├── 銷售儀表板.png
│       ├── 銷售數據.csv
│       └── 銷售分析報告.pdf
│
├── COVID-19疫情數據視覺化專案/
│   ├── main.py                 # 主程式
│   ├── requirements.txt        # 依賴套件清單
│   ├── README.md              # 專案說明文件
│   └── output/                # 輸出資料夾（執行後自動建立）
│       ├── COVID-19疫情分析圖表.png
│       ├── 累計確診數據.csv
│       ├── 每日新增數據.csv
│       └── COVID-19疫情分析報告.pdf
│
└── Day3專案完整操作指南.md      # 本文件
```

---

## 專案一：電商銷售數據分析

### 🎯 專案目標

透過模擬電商數據，學習如何建立專業的銷售分析儀表板。

### ⏱ 預計時間

- **安裝環境：** 5-10 分鐘
- **執行程式：** 2-3 分鐘
- **學習理解：** 30-60 分鐘

---

### 📝 詳細操作步驟

#### 第 1 步：進入專案資料夾

打開終端機，輸入以下命令：

**Windows：**
```bash
cd "D:\Python_快速掌握Python專案開發實作\netlify\電商銷售數據分析專案"
```

**Mac/Linux：**
```bash
cd "/path/to/netlify/電商銷售數據分析專案"
```

**確認位置：**
```bash
# Windows
dir

# Mac/Linux
ls
```

**預期輸出：**
```
main.py
requirements.txt
README.md
```

---

#### 第 2 步：建立虛擬環境（強烈建議）

虛擬環境可以隔離不同專案的套件，避免版本衝突。

**Windows：**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux：**
```bash
python3 -m venv venv
source venv/bin/activate
```

**成功啟動後，命令列前方會顯示 `(venv)`：**
```
(venv) D:\...\電商銷售數據分析專案>
```

**💡 小提示：**
- 如果想退出虛擬環境，輸入 `deactivate`
- 下次使用時，只需再次執行 activate 命令

---

#### 第 3 步：安裝依賴套件

```bash
pip install -r requirements.txt
```

**如果下載速度很慢，使用國內鏡像：**
```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

**安裝過程會顯示：**
```
Collecting matplotlib==3.8.2
Collecting numpy==1.26.2
Collecting pandas==2.1.4
Collecting seaborn==0.13.0
...
Successfully installed matplotlib-3.8.2 numpy-1.26.2 pandas-2.1.4 seaborn-0.13.0
```

**驗證安裝：**
```bash
pip list
```

應該能看到 matplotlib、numpy、pandas、seaborn 等套件。

---

#### 第 4 步：執行程式

```bash
python main.py
```

**執行過程會顯示：**
```
==================================================
  電商銷售數據分析專案
==================================================
正在生成模擬電商數據...
✓ 數據生成完成！共 365 筆記錄

正在建立視覺化儀表板...
✓ 儀表板建立完成！

==================================================
📊 2026 年銷售統計摘要
==================================================
總營收：          $5,475,234 元
平均日營收：      $14,993 元
最高日營收：      $24,567 元
最低日營收：      $6,789 元
--------------------------------------------------
總訂單數：        18,234 筆
平均日訂單數：    50 筆
最高日訂單數：    89 筆
--------------------------------------------------
總新客戶：        7,345 人
平均日新客戶：    20.1 人
平均回購率：      45.23%
最高回購率：      59.87%
最低回購率：      30.12%
==================================================

🏆 營收最佳月份：7 月（$523,456 元）

正在儲存輸出檔案...
✓ 已儲存：output/銷售儀表板.png
✓ 已儲存：output/銷售數據.csv
✓ 已儲存：output/銷售分析報告.pdf

✅ 所有檔案已儲存至 'output' 資料夾

正在顯示視覺化儀表板...
🎉 程式執行完成！

提示：請檢查 'output' 資料夾查看所有輸出檔案
```

**程式執行後會彈出視覺化儀表板視窗，關閉視窗後程式結束。**

---

#### 第 5 步：查看輸出結果

開啟 `output` 資料夾，您會看到：

1. **銷售儀表板.png** - 高解析度圖表（可用於報告、簡報）
2. **銷售數據.csv** - 原始數據（可用 Excel 開啟）
3. **銷售分析報告.pdf** - 多頁 PDF 報表

**💡 建議：**
- 用圖片檢視器開啟 PNG 檔案
- 用 Excel 或 Google Sheets 開啟 CSV 檔案
- 用 PDF 閱讀器開啟 PDF 報表

---

### 🔍 儀表板解讀

#### 左上：營收趨勢線
- **藍色線：** 每日營收
- **紅色線：** 30 日移動平均（平滑後的趨勢）
- **觀察重點：** 是否有上升/下降趨勢、季節性波動

#### 右上：月度訂單數
- **長條圖：** 12 個月的總訂單數
- **紅色長條：** 訂單數最高的月份
- **觀察重點：** 哪些月份是銷售旺季

#### 左下：回購率分佈
- **直方圖：** 回購率的分佈情況
- **紅色虛線：** 平均回購率
- **觀察重點：** 大多數天的回購率落在哪個區間

#### 右下：新客戶 vs 訂單數
- **散佈圖：** 新客戶數與訂單數的關係
- **顏色：** 代表月份
- **觀察重點：** 新客戶數多時，訂單數是否也多（正相關）

---

### 🎓 進階練習

#### 練習 1：修改數據參數

開啟 `main.py`，找到 `generate_sales_data()` 函數：

```python
# 原始設定
'訂單數': np.random.poisson(50, len(dates))
'營收': np.random.normal(15000, 3000, len(dates))

# 試試看改為更高的值
'訂單數': np.random.poisson(100, len(dates))  # 訂單數增加
'營收': np.random.normal(30000, 5000, len(dates))  # 營收增加
```

**重新執行程式，觀察結果變化。**

#### 練習 2：新增更多統計指標

在 `print_statistics()` 函數中新增：

```python
# 計算標準差
print(f"營收標準差：      ${df['營收'].std():.0f} 元")

# 計算中位數
print(f"營收中位數：      ${df['營收'].median():.0f} 元")
```

#### 練習 3：修改圖表顏色

在 `create_dashboard()` 函數中修改顏色：

```python
# 原始
axes[0, 0].plot(..., color='#3498db', ...)

# 改為其他顏色
axes[0, 0].plot(..., color='purple', ...)
axes[0, 0].plot(..., color='#FF5733', ...)  # 使用 HEX 顏色代碼
```

**顏色參考：** https://htmlcolorcodes.com/

---

## 專案二：COVID-19 疫情數據視覺化

### 🎯 專案目標

載入真實疫情數據，學習資料清洗與時間序列視覺化技術。

### ✨ 重要特色：已內建本地數據

**本專案已經內建完整的本地數據檔案！**
- ✅ **無需網路連線**
- ✅ **上課或展示不怕斷網**
- ✅ **執行速度快**
- ✅ **數據一致性**

數據檔案位置：`data/covid19_confirmed_global.csv`
時間範圍：2020-01-22 至 2023-03-09（共 1143 天）

### ⏱ 預計時間

- **安裝環境：** 5-10 分鐘
- **執行程式：** 2-3 分鐘（使用本地數據，無需下載）
- **學習理解：** 45-90 分鐘

---

### 📝 詳細操作步驟

#### 第 1 步：進入專案資料夾

**Windows：**
```bash
cd "D:\Python_快速掌握Python專案開發實作\netlify\COVID-19疫情數據視覺化專案"
```

**Mac/Linux：**
```bash
cd "/path/to/netlify/COVID-19疫情數據視覺化專案"
```

---

#### 第 2 步：建立虛擬環境

**Windows：**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux：**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

#### 第 3 步：安裝依賴套件

```bash
pip install -r requirements.txt
```

**注意：** 此專案多了 `requests` 套件（用於網路請求）。

---

#### 第 4 步：執行程式（線上模式）

```bash
python main.py
```

**執行過程會顯示：**
```
============================================================
  COVID-19 疫情數據視覺化專案
============================================================
正在載入 COVID-19 疫情數據...
→ 使用本地數據檔案：data/covid19_confirmed_global.csv
✓ 本地數據載入成功！共 10 個國家/地區的記錄
  （無需網路連線）

正在處理數據...
✓ 數據處理完成！
  - 時間範圍：2020-01-22 至 2023-03-09
  - 國家數量：10

正在建立視覺化圖表...
✓ 視覺化圖表建立完成！

============================================================
📊 COVID-19 疫情統計摘要
============================================================
數據時間範圍：2020-01-22 至 2023-03-09
數據天數：1142 天
------------------------------------------------------------

🏆 累計確診數排行（前 5 名）：
  1. 美國：103,436,829 例
  2. 印度：44,690,738 例
  3. 法國：38,997,490 例
  4. 德國：38,437,756 例
  5. 英國：24,658,705 例

📈 最高單日新增確診數：
  美國：1,234,567 例（2022-01-15）
  印度：456,789 例（2021-05-07）
  ...

🇹🇼 台灣疫情數據：
  累計確診：10,187,696 例
  最高單日新增：94,808 例
  最高單日新增日期：2022-05-26
============================================================

正在儲存輸出檔案...
✓ 已儲存：output/COVID-19疫情分析圖表.png
✓ 已儲存：output/累計確診數據.csv
✓ 已儲存：output/每日新增數據.csv
✓ 已儲存：output/COVID-19疫情分析報告.pdf

✅ 所有檔案已儲存至 'output' 資料夾

正在顯示視覺化圖表...
🎉 程式執行完成！
```

---

#### 第 5 步：離線模式（可選）

如果網路連線不穩定或無法連線，可使用離線模式：

**方法 1：修改程式碼**

開啟 `main.py`，找到 `main()` 函數：

```python
def main():
    # 將 False 改為 True
    use_sample = True  # 使用模擬數據
    df_raw = load_covid_data(use_sample=use_sample)
```

**方法 2：程式會自動偵測**

如果網路連線失敗，程式會自動切換到模擬數據模式：

```
✗ 無法載入線上數據：HTTPSConnectionPool...
→ 切換到模擬數據模式
⚠ 使用模擬數據模式
✓ 模擬數據生成完成！共 10 個國家的記錄
```

---

### 🔍 圖表解讀

#### 左上：累計確診數趨勢
- 顯示所有 10 個國家的累計確診數
- **觀察重點：** 哪些國家增長速度最快、曲線形狀差異

#### 右上：前五名國家累計確診數
- 聚焦於確診數最多的 5 個國家
- **觀察重點：** 主要疫情國家的發展軌跡

#### 左下：每日新增確診數（7日移動平均）
- 顯示台灣、美國、日本、南韓的每日新增趨勢
- 使用 7 日移動平均平滑曲線
- **觀察重點：** 疫情波峰出現的時間點

#### 右下：累計確診數排行
- 水平長條圖顯示最終排名
- **觀察重點：** 各國疫情嚴重程度比較

---

### 🎓 進階練習

#### 練習 1：分析其他國家

開啟 `main.py`，修改國家列表：

```python
COUNTRIES = ['Taiwan*', 'US', 'China', 'Brazil', 'Russia']

COUNTRY_NAMES = {
    'Taiwan*': '台灣',
    'US': '美國',
    'China': '中國',
    'Brazil': '巴西',
    'Russia': '俄羅斯'
}
```

**💡 提示：** 國家名稱必須與數據來源一致，可先執行程式查看 `df_raw` 中的完整國家列表。

#### 練習 2：修改移動平均視窗

在 `main()` 函數中修改：

```python
# 原始（7 日移動平均）
df_ma = calculate_moving_average(df_daily, window=7)

# 改為 14 日移動平均（更平滑）
df_ma = calculate_moving_average(df_daily, window=14)

# 改為 3 日移動平均（更敏感）
df_ma = calculate_moving_average(df_daily, window=3)
```

#### 練習 3：分析特定時間範圍

在 `process_data()` 函數後新增：

```python
# 只分析 2022 年的數據
df_cumulative = df_cumulative['2022-01-01':'2022-12-31']
```

---

## 常見問題排除

### Q1：執行時出現 `ModuleNotFoundError: No module named 'matplotlib'`

**原因：** 套件未安裝或虛擬環境未啟動

**解決方法：**
```bash
# 確認虛擬環境已啟動（命令列前方應該有 (venv)）
# 如果沒有，執行：
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
1. 確認系統已安裝「微軟正黑體」（通常內建）
2. 如果仍有問題，開啟 `main.py`，修改字型設定：
   ```python
   plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
   ```

**Mac：**
1. 安裝中文字型：
   ```bash
   brew tap homebrew/cask-fonts
   brew install --cask font-noto-sans-cjk-tc
   ```
2. 修改 `main.py`：
   ```python
   plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC', 'Arial Unicode MS']
   ```

**Linux：**
```bash
sudo apt-get install fonts-noto-cjk
```

---

### Q3：如何確認使用的是本地數據？

**檢查方法：**
執行程式時，查看輸出訊息：
```
正在載入 COVID-19 疫情數據...
→ 使用本地數據檔案：data/covid19_confirmed_global.csv  ← 這行表示使用本地數據
✓ 本地數據載入成功！共 10 個國家/地區的記錄
  （無需網路連線）
```

如果看到「使用本地數據檔案」，就表示正在使用本地數據，無需網路連線。

---

### Q4：本地數據檔案遺失怎麼辦？

**錯誤訊息：**
```
✗ 本地數據載入失敗：...
→ 嘗試從網路載入...
```

**解決方法：**
重新生成本地數據檔案：
```bash
cd "COVID-19疫情數據視覺化專案"
python generate_local_data.py
```

這個腳本會在 `data` 資料夾中生成 `covid19_confirmed_global.csv` 檔案。

---

### Q5：想使用線上最新數據怎麼做？

**方法：**
開啟 `main.py`，找到這行：
```python
df_raw = load_covid_data(use_sample=use_sample)
```

改為：
```python
df_raw = load_covid_data(use_sample=False, use_local=False)
```

這樣會強制從網路載入數據（需要網路連線）。

**注意：** Johns Hopkins 已於 2023 年 3 月停止更新數據。

---

### Q4：圖表視窗無法顯示

**原因：** 在遠端伺服器或不支援 GUI 的環境中執行

**解決方法：**
註解掉 `plt.show()` 這行：
```python
# plt.show()  # 不顯示視窗
```

圖表仍會儲存至 output 資料夾。

---

### Q5：執行程式時出現權限錯誤

**錯誤訊息：**
```
PermissionError: [Errno 13] Permission denied: 'output'
```

**原因：** output 資料夾被其他程式佔用（例如 Excel 開啟 CSV 檔案）

**解決方法：**
1. 關閉所有開啟 output 資料夾中檔案的程式
2. 刪除 output 資料夾，讓程式重新建立
3. 重新執行程式

---

### Q6：虛擬環境無法啟動

**Windows 錯誤訊息：**
```
因為這個系統上已停用指令碼執行，所以無法載入...
```

**解決方法：**
以管理員身份開啟 PowerShell，執行：
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

然後重新啟動虛擬環境。

---

## 學習建議

### 📚 學習路徑

#### 第 1 週：基礎理解
1. 完整執行兩個專案
2. 閱讀程式碼註解，理解每一行的作用
3. 修改簡單參數（顏色、標題等）

#### 第 2 週：實作練習
1. 嘗試進階練習題
2. 修改數據範圍和參數
3. 新增自己的統計指標

#### 第 3 週：獨立專案
1. 使用自己的數據（CSV 檔案）
2. 設計自己的儀表板
3. 整合多種圖表類型

---

### 🎯 學習重點

#### 電商銷售專案重點
- Matplotlib 物件導向介面 (`fig, ax = plt.subplots()`)
- NumPy 隨機數生成 (`np.random.poisson`, `np.random.normal`)
- Pandas DataFrame 操作
- 移動平均計算 (`rolling().mean()`)
- 多子圖佈局

#### COVID-19 專案重點
- 網路數據載入 (`pd.read_csv(url)`)
- 資料清洗與轉置 (`groupby()`, `transpose()`)
- 日期時間處理 (`pd.to_datetime()`)
- 時間序列視覺化
- 錯誤處理與備援機制

---

### 💡 實用技巧

#### 技巧 1：快速測試

在開發過程中，可以先用小範圍數據測試：

```python
# 原始：生成一整年的數據
dates = pd.date_range('2026-01-01', '2026-12-31', freq='D')

# 測試：只生成一個月的數據（執行更快）
dates = pd.date_range('2026-01-01', '2026-01-31', freq='D')
```

#### 技巧 2：互動式開發

使用 Jupyter Notebook 可以更方便地測試和調整：

```bash
# 安裝 Jupyter
pip install jupyter

# 啟動 Jupyter Notebook
jupyter notebook
```

在 Notebook 中可以一段一段執行程式碼，即時看到結果。

#### 技巧 3：程式碼重用

把常用的函數獨立出來，建立 `utils.py`：

```python
# utils.py
def quick_plot(df, x_col, y_col, title):
    """快速繪圖函數"""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df[x_col], df[y_col])
    ax.set_title(title)
    plt.show()
```

在 `main.py` 中匯入使用：
```python
from utils import quick_plot
quick_plot(df, '日期', '營收', '營收趨勢')
```

---

### 📖 延伸學習資源

#### 官方文檔
- [Matplotlib 官方教學](https://matplotlib.org/stable/tutorials/index.html)
- [Pandas 視覺化指南](https://pandas.pydata.org/docs/user_guide/visualization.html)
- [Seaborn 教學](https://seaborn.pydata.org/tutorial.html)

#### 推薦書籍
- 《Python 資料視覺化之美》
- 《Python 資料科學手冊》

#### 線上課程
- Coursera: Applied Data Science with Python
- DataCamp: Data Visualization with Python

---

### 🎓 認證檢查清單

完成以下項目，確認您已掌握本課程內容：

#### 基礎技能
- [ ] 成功執行兩個專案
- [ ] 理解 requirements.txt 的作用
- [ ] 能夠建立和使用虛擬環境
- [ ] 知道如何安裝套件

#### 程式理解
- [ ] 理解 `fig, ax = plt.subplots()` 的意義
- [ ] 能夠修改圖表顏色、標題、標籤
- [ ] 理解移動平均的計算方式
- [ ] 知道如何讀取和處理 CSV 數據

#### 進階應用
- [ ] 能夠修改數據參數並觀察結果變化
- [ ] 能夠新增自己的統計指標
- [ ] 能夠分析其他國家的疫情數據
- [ ] 能夠設計自己的儀表板佈局

#### 問題解決
- [ ] 能夠排除常見錯誤（套件未安裝、字型問題等）
- [ ] 知道如何查詢官方文檔
- [ ] 能夠獨立完成簡單的資料視覺化任務

---

## 🎉 恭喜完成！

您已經完成了 Day 3 的兩個完整專案！

### 下一步建議

1. **練習鞏固：** 重複執行專案，嘗試不同的參數設定
2. **實作挑戰：** 使用自己的數據建立視覺化
3. **分享成果：** 把產生的圖表和報告分享給朋友
4. **繼續學習：** 進入 Day 4 的課程內容

---

## 📞 需要幫助？

如果遇到任何問題：

1. **檢查本指南的「常見問題排除」章節**
2. **閱讀專案資料夾中的 README.md**
3. **查詢官方文檔**
4. **Google 錯誤訊息**
5. **加入相關學習社群討論**

---

**祝您學習愉快！ 🚀**

---

**文件版本：** 1.0
**最後更新：** 2025-11-25
**作者：** Python 資料視覺化教學團隊
