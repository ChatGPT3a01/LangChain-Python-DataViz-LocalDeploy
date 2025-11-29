@echo off
chcp 65001 >nul
echo ============================================================
echo 台灣餐廳美食分析程式 - 一鍵執行
echo ============================================================
echo.

echo [1/3] 檢查 Python 環境...
python --version
if errorlevel 1 (
    echo [錯誤] 找不到 Python，請先安裝 Python 3.8 或以上版本
    pause
    exit /b 1
)
echo.

echo [2/3] 檢查必要套件...
python -c "import matplotlib, numpy, pandas, seaborn" 2>nul
if errorlevel 1 (
    echo [警告] 缺少必要套件，正在安裝...
    pip install matplotlib numpy pandas seaborn
)
echo.

echo [3/3] 執行分析程式...
echo.
python main.py

echo.
echo ============================================================
echo 執行完成！圖表已儲存在 output 資料夾
echo ============================================================
echo.
echo 按任意鍵開啟 output 資料夾...
pause >nul
start output

exit
