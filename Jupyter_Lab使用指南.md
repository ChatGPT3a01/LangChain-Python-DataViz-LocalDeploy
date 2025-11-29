# 使用 Jupyter Lab 執行 Day 3 專案完整指南

## 目錄

1. [為什麼使用 Jupyter Lab？](#為什麼使用-jupyter-lab)
2. [安裝 Jupyter Lab](#安裝-jupyter-lab)
3. [啟動 Jupyter Lab](#啟動-jupyter-lab)
4. [方法一：使用 Jupyter Lab 終端機](#方法一使用-jupyter-lab-終端機)
5. [方法二：使用 Jupyter Notebook](#方法二使用-jupyter-notebook)
6. [常見問題](#常見問題)

---

## 為什麼使用 Jupyter Lab？

### ✨ Jupyter Lab 的優勢

| 特色 | 說明 |
|------|------|
| 🖥️ **整合環境** | 終端機、編輯器、Notebook 都在同一介面 |
| 📊 **即時預覽** | 執行程式碼，立即看到圖表 |
| 📝 **互動式** | 可以一段一段執行程式碼 |
| 🔄 **方便調試** | 修改參數立即重新執行 |
| 👨‍🏫 **適合教學** | 可以加入文字說明和圖表 |
| 💾 **保存結果** | Notebook 會保存輸出結果 |

---

## 安裝 Jupyter Lab

### 方法 1：全域安裝（推薦給初學者）

```bash
pip install jupyterlab
```

### 方法 2：在專案虛擬環境中安裝

```bash
# 先進入專案資料夾
cd "D:\Python_快速掌握Python專案開發實作\netlify\電商銷售數據分析專案"

# 啟動虛擬環境
venv\Scripts\activate

# 安裝 Jupyter Lab
pip install jupyterlab
```

---

## 啟動 Jupyter Lab

### 從專案根目錄啟動

```bash
# 進入 netlify 資料夾
cd "D:\Python_快速掌握Python專案開發實作\netlify"

# 啟動 Jupyter Lab
jupyter lab
```

**啟動後會自動開啟瀏覽器**，顯示 Jupyter Lab 介面。

**瀏覽器網址：** `http://localhost:8888/lab`

---

## 方法一：使用 Jupyter Lab 終端機

### 步驟 1：開啟 Jupyter Lab 終端機

1. 啟動 Jupyter Lab
2. 在左側面板中，點擊「**+**」（New Launcher）
3. 在「Other」區塊中，點擊「**Terminal**」

**現在你就有一個完整功能的終端機了！**

---

### 步驟 2：執行電商銷售專案

在 Jupyter Lab 終端機中輸入：

```bash
# 進入專案資料夾
cd "電商銷售數據分析專案"

# 建立虛擬環境（如果還沒建立）
python -m venv venv

# 啟動虛擬環境
venv\Scripts\activate

# 安裝依賴套件
pip install -r requirements.txt

# 執行程式
python main.py
```

**執行結果：**
- 終端機會顯示統計摘要
- 會彈出圖表視窗
- 在 `output` 資料夾生成檔案

---

### 步驟 3：執行 COVID-19 專案

在 Jupyter Lab 終端機中輸入：

```bash
# 進入專案資料夾
cd "COVID-19疫情數據視覺化專案"

# 建立虛擬環境（如果還沒建立）
python -m venv venv

# 啟動虛擬環境
venv\Scripts\activate

# 安裝依賴套件
pip install -r requirements.txt

# 執行程式
python main.py
```

---

### 💡 Jupyter Lab 終端機的優勢

- ✅ **多個終端機**：可以同時開啟多個終端機視窗
- ✅ **不會關閉**：關閉瀏覽器標籤，終端機仍在背景執行
- ✅ **視覺化介面**：比命令提示字元更美觀
- ✅ **整合開發**：可以同時編輯程式碼和執行命令

---

## 方法二：使用 Jupyter Notebook

### 為什麼使用 Notebook 版本？

- 📝 可以加入文字說明
- 📊 圖表直接顯示在 Notebook 中（不會彈出視窗）
- 🔄 可以一段一段執行程式碼
- 💾 保存執行結果
- 👨‍🏫 **最適合教學和學習**

---

### 電商銷售專案 Notebook 版本

我已經為你建立了 `電商銷售分析.ipynb`，包含以下內容：

#### Notebook 結構

1. **環境設定**
   - 匯入套件
   - 設定中文字型

2. **數據生成**
   - 生成 2026 年模擬數據
   - 顯示數據摘要

3. **數據分析**
   - 計算統計指標
   - 顯示統計表格

4. **視覺化**
   - 營收趨勢圖
   - 月度訂單數
   - 回購率分佈
   - 散佈圖

5. **儲存結果**
   - 匯出 CSV
   - 匯出 PNG
   - 匯出 PDF

---

### 如何使用 Notebook

#### 步驟 1：在 Jupyter Lab 中開啟 Notebook

1. 在左側檔案列表中，進入專案資料夾
2. 雙擊 `電商銷售分析.ipynb` 或 `COVID-19疫情分析.ipynb`

#### 步驟 2：執行 Notebook

**方法 1：逐格執行**
- 點選一個 Cell（格子）
- 按 `Shift + Enter` 執行該格，並移到下一格
- 或按工具列的「▶」按鈕

**方法 2：全部執行**
- 點選選單「Run」→「Run All Cells」
- 會自動執行所有格子

**方法 3：從頭執行**
- 點選選單「Kernel」→「Restart Kernel and Run All Cells」
- 重新啟動核心並執行所有格子

---

### 💡 Notebook 使用技巧

#### 快捷鍵

| 快捷鍵 | 功能 |
|--------|------|
| `Shift + Enter` | 執行當前格子，移到下一格 |
| `Ctrl + Enter` | 執行當前格子，停留在當前格 |
| `A` | 在上方插入新格子（命令模式） |
| `B` | 在下方插入新格子（命令模式） |
| `DD` | 刪除當前格子（命令模式） |
| `M` | 轉換為 Markdown 格子 |
| `Y` | 轉換為程式碼格子 |

#### 命令模式 vs 編輯模式

- **編輯模式**：格子邊框是**綠色**，可以輸入程式碼
- **命令模式**：格子邊框是**藍色**，可以使用快捷鍵
- 按 `Esc` 進入命令模式
- 按 `Enter` 進入編輯模式

---

## 兩種方法的比較

| 項目 | Jupyter 終端機 | Jupyter Notebook |
|------|---------------|-----------------|
| **執行方式** | 執行整個程式 | 一段一段執行 |
| **圖表顯示** | 彈出視窗 | 內嵌在 Notebook |
| **互動性** | 低 | 高 |
| **適合** | 執行完整程式 | 學習、調試、展示 |
| **修改參數** | 需要編輯 .py 檔案 | 直接在 Notebook 中修改 |
| **保存結果** | 輸出到檔案 | 保存在 Notebook 中 |
| **適合新手** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

---

## 實際操作示範

### 🎯 場景 1：上課展示

**推薦：Jupyter Notebook**

```
1. 啟動 Jupyter Lab
2. 開啟「電商銷售分析.ipynb」
3. 選擇「Run」→「Run All Cells」
4. 所有圖表會依序顯示在 Notebook 中
5. 可以即時修改參數並重新執行
```

**優點：**
- 圖表不會被視窗遮住
- 可以一邊講解一邊執行
- 學生可以看到每一步的結果

---

### 🎯 場景 2：快速執行完整程式

**推薦：Jupyter 終端機**

```
1. 啟動 Jupyter Lab
2. 開啟終端機
3. cd 到專案資料夾
4. python main.py
5. 查看 output 資料夾的結果
```

**優點：**
- 執行速度快
- 一次產生所有輸出檔案
- 適合產生報表

---

### 🎯 場景 3：學習和實驗

**推薦：Jupyter Notebook**

```
1. 開啟 Notebook
2. 修改數據參數（例如：訂單數、營收）
3. 只執行該格子（Shift + Enter）
4. 重新執行視覺化格子
5. 觀察結果變化
```

**優點：**
- 不需要重新執行整個程式
- 可以快速實驗不同參數
- 保存多種結果進行比較

---

## 常見問題

### Q1：Jupyter Lab 無法啟動？

**錯誤訊息：**
```
'jupyter' 不是內部或外部命令
```

**解決方法：**
```bash
# 確認是否已安裝
pip install jupyterlab

# 重新啟動
jupyter lab
```

---

### Q2：終端機中文亂碼？

**解決方法：**
在 Jupyter Lab 中，中文可能顯示為亂碼，但這不影響程式執行。圖表中的中文會正常顯示。

如果需要在終端機看清楚中文：
1. 使用 Notebook 版本（推薦）
2. 或使用 Windows Terminal

---

### Q3：圖表無法顯示在 Notebook 中？

**解決方法：**
在 Notebook 的第一個 Cell 加入：
```python
%matplotlib inline
```

這會讓圖表內嵌在 Notebook 中。

---

### Q4：如何在 Notebook 中顯示高解析度圖表？

**方法：**
在 Notebook 開頭加入：
```python
%config InlineBackend.figure_format = 'retina'
```

這會讓圖表使用 2x 解析度顯示。

---

### Q5：Notebook 執行很慢？

**原因：**
可能是核心（Kernel）卡住或記憶體不足。

**解決方法：**
1. 重新啟動核心：選單「Kernel」→「Restart Kernel」
2. 清除輸出：選單「Edit」→「Clear All Outputs」
3. 關閉不用的 Notebook

---

### Q6：如何切換 Python 環境？

**在 Jupyter Notebook 中：**
1. 點選右上角的核心名稱
2. 選擇「Select Kernel」
3. 選擇你要的 Python 環境

**在終端機中：**
```bash
# 啟動虛擬環境
venv\Scripts\activate

# 確認 Python 版本
python --version
```

---

## 📚 延伸學習

### Jupyter Lab 進階功能

1. **拖曳排列**
   - 可以拖曳 Notebook、終端機、編輯器
   - 並排顯示多個視窗

2. **擴充功能**
   - 安裝 Jupyter Lab 擴充功能
   - 例如：目錄導航、程式碼折疊等

3. **Git 整合**
   - Jupyter Lab 內建 Git 支援
   - 可以直接進行版本控制

4. **協作功能**
   - 使用 JupyterHub 多人協作
   - 共享 Notebook

---

## 🎓 學習路徑建議

### 第 1 週：熟悉基本操作
- 使用 Jupyter 終端機執行專案
- 了解虛擬環境和套件安裝
- 查看輸出結果

### 第 2 週：使用 Notebook
- 開啟 Notebook 版本
- 逐格執行程式碼
- 修改參數觀察變化

### 第 3 週：自己動手
- 建立自己的 Notebook
- 加入文字說明和註解
- 實作自己的數據分析

---

## 🎉 總結

### Jupyter Lab 是最適合學習的工具！

**優勢：**
- ✅ 終端機和 Notebook 整合在一起
- ✅ 圖表直接顯示，不需要彈出視窗
- ✅ 可以一段一段執行，方便學習
- ✅ 保存執行結果，可以回顧
- ✅ 適合教學和展示

**建議使用場景：**
- 📖 **學習**：使用 Notebook，一步一步理解程式碼
- 👨‍🏫 **教學**：使用 Notebook，邊講解邊執行
- 🔧 **開發調試**：使用 Notebook，快速測試修改
- 📊 **產生報表**：使用終端機，執行完整程式

---

## 📂 專案檔案對照

| Python 腳本 | Jupyter Notebook | 說明 |
|-------------|------------------|------|
| `電商銷售數據分析專案/main.py` | `電商銷售分析.ipynb` | 電商銷售分析 |
| `COVID-19疫情數據視覺化專案/main.py` | `COVID-19疫情分析.ipynb` | 疫情數據分析 |

兩個版本功能相同，只是執行方式不同！

---

**祝你使用 Jupyter Lab 學習愉快！** 🚀

---

**文件版本：** 1.0
**最後更新：** 2025-11-25
**作者：** Python 資料視覺化教學團隊
