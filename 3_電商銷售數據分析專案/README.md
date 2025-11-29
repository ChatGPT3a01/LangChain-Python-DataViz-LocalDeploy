# 電商銷售數據分析專案

## 專案簡介

本專案模擬電商銷售數據，並透過 Python 進行資料分析與視覺化，產生專業的銷售儀表板和報表。

### 功能特色

- 生成 2026 年全年的模擬電商數據（包含季節性變化）
- 分析關鍵指標：訂單數、營收、新客戶、回購率
- 產生 2x2 綜合視覺化儀表板
- 輸出詳細統計摘要報告
- 匯出高解析度圖表（PNG）和多頁 PDF 報表
- 儲存原始數據為 CSV 格式

## 環境需求

- Python 3.8 或以上版本
- 必要套件（請參考 requirements.txt）

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

```bash
python main.py
```

## 輸出結果

執行程式後，會在 `output` 資料夾中生成以下檔案：

1. **銷售儀表板.png** - 高解析度視覺化儀表板（300 DPI）
2. **銷售數據.csv** - 完整的原始數據
3. **銷售分析報告.pdf** - 多頁 PDF 報表，包含：
   - 綜合儀表板
   - 月度營收分析
   - 月度新客戶分析

## 視覺化內容

### 儀表板包含四個子圖：

1. **左上：營收趨勢線**
   - 每日營收折線圖
   - 30 日移動平均線

2. **右上：月度訂單數**
   - 12 個月的總訂單數長條圖
   - 標註最高月份

3. **左下：回購率分佈**
   - 直方圖顯示回購率分佈
   - 平均回購率標記線

4. **右下：新客戶 vs 訂單數**
   - 散佈圖顯示相關性
   - 顏色代表月份

## 統計報告內容

程式執行時會在終端機輸出以下統計資訊：

- 總營收、平均日營收、最高/最低日營收
- 總訂單數、平均日訂單數、最高日訂單數
- 總新客戶、平均日新客戶
- 平均回購率、最高/最低回購率
- 營收最佳月份

## 常見問題

### Q1：出現中文亂碼怎麼辦？

**解決方法：**
- Windows：確保系統已安裝「微軟正黑體」字型
- Mac：程式會自動使用 Arial Unicode MS
- 如仍有問題，可在 main.py 中修改字型設定：
  ```python
  plt.rcParams['font.sans-serif'] = ['你的字型名稱']
  ```

### Q2：圖表無法顯示？

**解決方法：**
- 確認是否在支援 GUI 的環境中執行
- 若在遠端伺服器上執行，可註解掉 `plt.show()` 這行
- 圖表仍會儲存至 output 資料夾

### Q3：如何修改數據範圍或參數？

**解決方法：**
- 在 `generate_sales_data()` 函數中修改：
  - 日期範圍：`pd.date_range('起始日期', '結束日期')`
  - 訂單數範圍：`np.random.poisson(平均值, 數量)`
  - 營收範圍：`np.random.normal(平均值, 標準差, 數量)`

## 進階使用

### 自訂分析週期

修改 main.py 中的日期範圍：
```python
dates = pd.date_range('2024-01-01', '2024-12-31', freq='D')  # 改為 2024 年
```

### 調整圖表樣式

修改顏色、字型大小等參數：
```python
# 在 create_dashboard() 函數中調整
axes[0, 0].plot(..., color='你的顏色代碼', linewidth=線寬)
```

### 匯出其他格式

在 `save_outputs()` 函數中新增：
```python
# 匯出 SVG 向量圖
fig.savefig(f'{output_dir}/銷售儀表板.svg', format='svg', bbox_inches='tight')

# 匯出 Excel
df.to_excel(f'{output_dir}/銷售數據.xlsx', index=False)
```

## 學習重點

本專案涵蓋以下技能：

1. **資料生成與處理**
   - Pandas DataFrame 操作
   - NumPy 隨機數生成
   - 日期時間處理
   - 移動平均計算

2. **視覺化技巧**
   - Matplotlib 物件導向介面
   - 多子圖佈局（Subplots）
   - 折線圖、長條圖、直方圖、散佈圖
   - 顏色映射與色條

3. **報表輸出**
   - 高解析度圖片匯出
   - 多頁 PDF 報表製作
   - CSV 數據匯出

## 延伸練習

1. 新增更多指標（例如：客單價、轉換率）
2. 加入地區維度分析
3. 實作預測功能（使用時間序列分析）
4. 連接真實資料庫
5. 建立互動式儀表板（使用 Plotly 或 Dash）

## 授權

本專案僅供學習使用。

## 聯絡資訊

如有任何問題或建議，歡迎提出討論！
