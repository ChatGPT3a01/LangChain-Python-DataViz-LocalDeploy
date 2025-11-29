# COVID-19 疫情數據視覺化專案

## 專案簡介

本專案從網路載入真實的 COVID-19 疫情數據，進行資料處理、清洗與視覺化分析，產生全球疫情趨勢圖表與統計報告。

### 功能特色

- **✨ 已內建本地數據檔案，無需網路連線即可執行！**
- 從 Johns Hopkins 大學 GitHub 儲存庫載入真實疫情數據
- 優先使用本地數據檔案（data/covid19_confirmed_global.csv）
- 自動資料清洗與轉置處理
- 分析全球 10 個主要國家的疫情趨勢
- 計算每日新增確診數與 7 日移動平均線
- 產生 2x2 綜合視覺化圖表
- 輸出詳細統計摘要報告
- 匯出高解析度圖表和 PDF 報表
- 三種數據來源模式：本地數據 → 線上數據 → 模擬數據

### 分析國家

- 🇹🇼 台灣
- 🇺🇸 美國
- 🇬🇧 英國
- 🇯🇵 日本
- 🇰🇷 南韓
- 🇩🇪 德國
- 🇫🇷 法國
- 🇮🇹 義大利
- 🇪🇸 西班牙
- 🇮🇳 印度

## 環境需求

- Python 3.8 或以上版本
- **無需網路連線！**（已內建本地數據檔案）
- 必要套件（請參考 requirements.txt）

## 📌 重要說明：本地數據模式

本專案已經內建完整的本地數據檔案（`data/covid19_confirmed_global.csv`），包含從 2020-01-22 到 2023-03-09 的真實疫情數據。

**這表示：**
- ✅ **上課或展示時不怕網路斷線**
- ✅ **執行速度更快**（不需等待網路下載）
- ✅ **數據一致性**（每次執行結果相同）
- ✅ **完全離線運作**

程式會自動按照以下優先順序載入數據：
1. **本地數據檔案**（data/covid19_confirmed_global.csv）← 預設使用
2. 線上數據（如果本地檔案不存在）
3. 模擬數據（如果線上載入失敗）

## 安裝步驟

### 步驟 1：確認 Python 版本

```bash
python --version
```

確保版本為 3.8 或以上。

### 步驟 2：建立虛擬環境（建議）

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

### 步驟 3：安裝依賴套件

```bash
pip install -r requirements.txt
```

如果安裝速度較慢，可使用國內鏡像：
```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 步驟 4：執行程式

**預設模式（使用本地數據，無需網路）：**
```bash
python main.py
```

程式會自動載入 `data/covid19_confirmed_global.csv` 本地數據檔案。

**輸出範例：**
```
============================================================
  COVID-19 疫情數據視覺化專案
============================================================
正在載入 COVID-19 疫情數據...
→ 使用本地數據檔案：data/covid19_confirmed_global.csv
✓ 本地數據載入成功！共 10 個國家/地區的記錄
  （無需網路連線）
...
```

---

### 其他執行模式（選用）

**強制使用線上數據（需要網路）：**
在 `main.py` 中修改：
```python
df_raw = load_covid_data(use_sample=False, use_local=False)
```

**使用模擬數據：**
在 `main.py` 中修改：
```python
use_sample = True
df_raw = load_covid_data(use_sample=use_sample)
```

## 輸出結果

執行程式後，會在 `output` 資料夾中生成以下檔案：

1. **COVID-19疫情分析圖表.png** - 高解析度視覺化圖表（300 DPI）
2. **累計確診數據.csv** - 累計確診數時間序列數據
3. **每日新增數據.csv** - 每日新增確診數時間序列數據
4. **COVID-19疫情分析報告.pdf** - PDF 格式報表

## 視覺化內容

### 圖表包含四個子圖：

1. **左上：累計確診數趨勢**
   - 顯示所有 10 個國家的累計確診數時間序列
   - 完整時間範圍從 2020 年初至最新數據

2. **右上：前五名國家累計確診數**
   - 聚焦於確診數最多的前 5 個國家
   - 更清晰地比較主要疫情國家

3. **左下：每日新增確診數（7日移動平均）**
   - 顯示台灣、美國、日本、南韓的每日新增趨勢
   - 使用 7 日移動平均平滑曲線，減少雜訊

4. **右下：累計確診數排行**
   - 水平長條圖顯示最終累計確診數排名
   - 標註具體數值

## 統計報告內容

程式執行時會在終端機輸出以下統計資訊：

- 數據時間範圍與天數
- 累計確診數排行（前 5 名）
- 各國最高單日新增確診數及日期
- 台灣疫情數據摘要

## 數據來源

本專案使用 **Johns Hopkins University (JHU)** 提供的 COVID-19 數據：

- **數據儲存庫：** [CSSEGISandData/COVID-19](https://github.com/CSSEGISandData/COVID-19)
- **數據檔案：** `time_series_covid19_confirmed_global.csv`
- **更新頻率：** 每日更新（直到 2023 年 3 月 10 日停止更新）

### 數據說明

- 數據為累計確診數（Confirmed Cases）
- 包含全球所有國家和地區
- 時間範圍：2020-01-22 至 2023-03-09

## 常見問題

### Q1：無法連線到數據來源怎麼辦？

**解決方法：**
- 程式會自動偵測連線失敗並切換到模擬數據模式
- 或手動設定離線模式：在 main.py 中設定 `use_sample = True`

### Q2：出現中文亂碼怎麼辦？

**解決方法：**
- Windows：確保系統已安裝「微軟正黑體」字型
- Mac：程式會自動使用 Arial Unicode MS
- 如仍有問題，可在 main.py 中修改字型設定

### Q3：想分析其他國家怎麼做？

**解決方法：**
在 main.py 中修改 `COUNTRIES` 和 `COUNTRY_NAMES` 變數：
```python
COUNTRIES = ['Taiwan*', 'US', '你想分析的國家英文名稱']

COUNTRY_NAMES = {
    'Taiwan*': '台灣',
    'US': '美國',
    '英文名稱': '中文名稱'
}
```

**提示：** 可先執行程式查看 `df_raw` 中的所有國家名稱，或參考 [JHU 數據儲存庫](https://github.com/CSSEGISandData/COVID-19)。

### Q4：數據最後更新到什麼時候？

**答：** Johns Hopkins 大學的 COVID-19 數據已於 **2023 年 3 月 10 日停止更新**。如需更新的數據，可考慮使用其他數據來源，例如：
- [Our World in Data](https://ourworldindata.org/coronavirus)
- [WHO COVID-19 Dashboard](https://covid19.who.int/)

### Q5：如何修改移動平均的天數？

**解決方法：**
在 main.py 中的 `calculate_moving_average()` 函數呼叫處修改：
```python
df_ma = calculate_moving_average(df_daily, window=14)  # 改為 14 日移動平均
```

## 進階使用

### 修改分析時間範圍

如果想只分析特定時間範圍，可在 `process_data()` 函數後新增：
```python
# 只分析 2022 年的數據
df_cumulative = df_cumulative['2022-01-01':'2022-12-31']
```

### 新增更多視覺化圖表

可在 `create_visualizations()` 函數中新增子圖：
```python
# 新增死亡率分析、康復率分析等
```

### 匯出 Excel 格式

在 `save_outputs()` 函數中新增：
```python
df_cumulative.to_excel(f'{output_dir}/累計確診數據.xlsx')
```

### 整合其他數據

可以載入死亡數據或康復數據進行綜合分析：
```python
# 死亡數據
url_deaths = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'

# 康復數據（已停止更新）
url_recovered = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
```

## 學習重點

本專案涵蓋以下技能：

1. **網路數據載入**
   - 使用 requests 或 pandas 載入線上 CSV
   - 錯誤處理與備援機制

2. **資料清洗與處理**
   - 資料過濾與分組
   - 資料轉置（Transpose）
   - 日期時間處理
   - 計算衍生指標（每日新增、移動平均）

3. **時間序列分析**
   - 趨勢分析
   - 移動平均平滑
   - 多國比較

4. **視覺化技巧**
   - 多條折線圖
   - 水平長條圖
   - 顏色映射
   - 圖例與標註

## 延伸練習

1. 新增死亡率與致死率分析
2. 計算每百萬人確診數（需要人口數據）
3. 實作疫情波峰偵測
4. 建立互動式地圖（使用 Plotly 或 Folium）
5. 預測未來趨勢（使用時間序列模型）
6. 比較疫苗接種率與確診數的關係

## 參考資源

- [Johns Hopkins COVID-19 數據儲存庫](https://github.com/CSSEGISandData/COVID-19)
- [Pandas 時間序列處理](https://pandas.pydata.org/docs/user_guide/timeseries.html)
- [Matplotlib 日期格式化](https://matplotlib.org/stable/gallery/text_labels_and_annotations/date.html)

## 授權

本專案僅供學習使用。數據版權歸 Johns Hopkins University 所有。

## 聯絡資訊

如有任何問題或建議，歡迎提出討論！

---

**⚠ 重要提醒：**
本專案僅用於資料分析學習，數據可能存在延遲或誤差。如需官方疫情資訊，請參考政府衛生部門公告。
