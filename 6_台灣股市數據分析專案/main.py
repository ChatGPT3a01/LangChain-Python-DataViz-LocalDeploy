"""
台灣股市數據分析專案
===================
分析台積電、鴻海、聯發科的股價趨勢和技術指標

功能：
1. K線圖分析
2. 技術指標：MA、MACD、RSI、布林通道
3. 成交量分析
4. 多檔股票比較
5. 輸出分析報表
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import mplfinance as mpf
from matplotlib.backends.backend_pdf import PdfPages
import os
import warnings
warnings.filterwarnings('ignore')

# 設定中文字型
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Arial Unicode MS', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

def load_stock_data(stock_code):
    """載入股票數據"""
    stock_names = {
        '2330': '台積電',
        '2317': '鴻海',
        '2454': '聯發科'
    }

    filename = f'data/{stock_code}_{stock_names[stock_code]}.csv'

    if not os.path.exists(filename):
        print(f"✗ 找不到數據檔案：{filename}")
        print("請先執行 generate_local_data.py 生成數據")
        return None

    df = pd.read_csv(filename)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    print(f"[OK] 載入 {stock_names[stock_code]}({stock_code}) 數據成功")
    print(f"  時間範圍：{df.index[0].strftime('%Y-%m-%d')} 至 {df.index[-1].strftime('%Y-%m-%d')}")
    print(f"  數據筆數：{len(df)} 筆")

    return df

def calculate_ma(df, periods=[5, 10, 20]):
    """計算移動平均線"""
    for period in periods:
        df[f'MA{period}'] = df['Close'].rolling(window=period).mean()
    return df

def calculate_macd(df, fast=12, slow=26, signal=9):
    """計算 MACD 指標"""
    ema_fast = df['Close'].ewm(span=fast).mean()
    ema_slow = df['Close'].ewm(span=slow).mean()
    df['MACD'] = ema_fast - ema_slow
    df['MACD_Signal'] = df['MACD'].ewm(span=signal).mean()
    df['MACD_Hist'] = df['MACD'] - df['MACD_Signal']
    return df

def calculate_rsi(df, period=14):
    """計算 RSI 指標"""
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    return df

def calculate_bollinger_bands(df, period=20, std_dev=2):
    """計算布林通道"""
    df['BB_Middle'] = df['Close'].rolling(window=period).mean()
    rolling_std = df['Close'].rolling(window=period).std()
    df['BB_Upper'] = df['BB_Middle'] + (rolling_std * std_dev)
    df['BB_Lower'] = df['BB_Middle'] - (rolling_std * std_dev)
    return df

def plot_candlestick_with_indicators(df, stock_name, stock_code):
    """繪製K線圖和技術指標"""
    print(f"\n正在繪製 {stock_name} 的K線圖...")

    # 準備數據（最近60天）
    df_recent = df.tail(60).copy()

    # 建立子圖
    fig = plt.figure(figsize=(16, 12))
    gs = fig.add_gridspec(4, 1, height_ratios=[3, 1, 1, 1], hspace=0.3)

    # 子圖1：K線圖 + 移動平均線 + 布林通道
    ax1 = fig.add_subplot(gs[0])
    ax1.plot(df_recent.index, df_recent['Close'], 'k-', linewidth=2, label='收盤價')
    ax1.plot(df_recent.index, df_recent['MA5'], 'r-', linewidth=1.5, label='MA5', alpha=0.8)
    ax1.plot(df_recent.index, df_recent['MA10'], 'b-', linewidth=1.5, label='MA10', alpha=0.8)
    ax1.plot(df_recent.index, df_recent['MA20'], 'g-', linewidth=1.5, label='MA20', alpha=0.8)

    # 布林通道
    ax1.plot(df_recent.index, df_recent['BB_Upper'], 'gray', linestyle='--', alpha=0.5, label='布林上軌')
    ax1.plot(df_recent.index, df_recent['BB_Lower'], 'gray', linestyle='--', alpha=0.5, label='布林下軌')
    ax1.fill_between(df_recent.index, df_recent['BB_Upper'], df_recent['BB_Lower'],
                     color='gray', alpha=0.1)

    ax1.set_title(f'{stock_name}({stock_code}) 股價走勢與技術指標（最近60天）',
                 fontsize=16, fontweight='bold', pad=20)
    ax1.set_ylabel('股價（元）', fontsize=12)
    ax1.legend(loc='upper left', fontsize=10, ncol=3)
    ax1.grid(True, alpha=0.3)

    # 子圖2：成交量
    ax2 = fig.add_subplot(gs[1], sharex=ax1)
    colors = ['red' if df_recent['Close'].iloc[i] >= df_recent['Open'].iloc[i]
             else 'green' for i in range(len(df_recent))]
    ax2.bar(df_recent.index, df_recent['Volume']/1000, color=colors, alpha=0.6, width=0.8)
    ax2.set_ylabel('成交量（萬張）', fontsize=12)
    ax2.set_title('成交量', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3)

    # 子圖3：MACD
    ax3 = fig.add_subplot(gs[2], sharex=ax1)
    ax3.plot(df_recent.index, df_recent['MACD'], 'b-', linewidth=1.5, label='MACD')
    ax3.plot(df_recent.index, df_recent['MACD_Signal'], 'r-', linewidth=1.5, label='Signal')

    # MACD 柱狀圖
    colors = ['red' if val >= 0 else 'green' for val in df_recent['MACD_Hist']]
    ax3.bar(df_recent.index, df_recent['MACD_Hist'], color=colors, alpha=0.5, width=0.8)

    ax3.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax3.set_ylabel('MACD', fontsize=12)
    ax3.set_title('MACD 指標', fontsize=12, fontweight='bold')
    ax3.legend(loc='upper left', fontsize=10)
    ax3.grid(True, alpha=0.3)

    # 子圖4：RSI
    ax4 = fig.add_subplot(gs[3], sharex=ax1)
    ax4.plot(df_recent.index, df_recent['RSI'], 'purple', linewidth=2, label='RSI(14)')
    ax4.axhline(y=70, color='red', linestyle='--', linewidth=1, alpha=0.5, label='超買線(70)')
    ax4.axhline(y=30, color='green', linestyle='--', linewidth=1, alpha=0.5, label='超賣線(30)')
    ax4.fill_between(df_recent.index, 70, 100, color='red', alpha=0.1)
    ax4.fill_between(df_recent.index, 0, 30, color='green', alpha=0.1)

    ax4.set_ylabel('RSI', fontsize=12)
    ax4.set_xlabel('日期', fontsize=12)
    ax4.set_title('RSI 指標', fontsize=12, fontweight='bold')
    ax4.set_ylim(0, 100)
    ax4.legend(loc='upper left', fontsize=10)
    ax4.grid(True, alpha=0.3)

    # 調整 x 軸標籤角度
    plt.setp(ax4.xaxis.get_majorticklabels(), rotation=45)

    plt.tight_layout()

    return fig

def compare_stocks(stocks_data):
    """比較多檔股票"""
    print("\n正在繪製股票比較圖...")

    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    fig.suptitle('台股三雄比較分析', fontsize=18, fontweight='bold', y=0.995)

    # 標準化價格（以第一天為基準 = 100）
    for stock_code, df in stocks_data.items():
        normalized = (df['Close'] / df['Close'].iloc[0]) * 100
        df['Normalized'] = normalized

    # 子圖1：標準化價格比較
    for stock_code, df in stocks_data.items():
        stock_name = df['Stock_Name'].iloc[0]
        axes[0, 0].plot(df.index, df['Normalized'],
                       linewidth=2, label=f'{stock_name}({stock_code})', alpha=0.8)

    axes[0, 0].set_title('股價漲跌幅比較（標準化）', fontsize=14, fontweight='bold')
    axes[0, 0].set_xlabel('日期', fontsize=11)
    axes[0, 0].set_ylabel('相對漲跌幅（基期=100）', fontsize=11)
    axes[0, 0].legend(fontsize=11)
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].tick_params(axis='x', rotation=45)

    # 子圖2：平均成交量比較
    avg_volumes = {code: df['Volume'].mean()/1000 for code, df in stocks_data.items()}
    stock_names = [stocks_data[code]['Stock_Name'].iloc[0] for code in avg_volumes.keys()]
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']

    axes[0, 1].bar(range(len(avg_volumes)), list(avg_volumes.values()),
                  color=colors, edgecolor='black', linewidth=1.5, alpha=0.8)
    axes[0, 1].set_xticks(range(len(avg_volumes)))
    axes[0, 1].set_xticklabels(stock_names, fontsize=11)
    axes[0, 1].set_title('平均成交量比較', fontsize=14, fontweight='bold')
    axes[0, 1].set_ylabel('成交量（萬張）', fontsize=11)
    axes[0, 1].grid(True, axis='y', alpha=0.3)

    # 在長條上標註數值
    for i, (code, vol) in enumerate(avg_volumes.items()):
        axes[0, 1].text(i, vol + 500, f'{vol:,.0f}',
                       ha='center', fontsize=10, fontweight='bold')

    # 子圖3：價格波動率比較
    volatilities = {}
    for stock_code, df in stocks_data.items():
        daily_returns = df['Close'].pct_change()
        volatility = daily_returns.std() * 100  # 轉換為百分比
        volatilities[stock_code] = volatility

    axes[1, 0].bar(range(len(volatilities)), list(volatilities.values()),
                  color=colors, edgecolor='black', linewidth=1.5, alpha=0.8)
    axes[1, 0].set_xticks(range(len(volatilities)))
    axes[1, 0].set_xticklabels(stock_names, fontsize=11)
    axes[1, 0].set_title('價格波動率比較', fontsize=14, fontweight='bold')
    axes[1, 0].set_ylabel('日波動率（%）', fontsize=11)
    axes[1, 0].grid(True, axis='y', alpha=0.3)

    for i, (code, vol) in enumerate(volatilities.items()):
        axes[1, 0].text(i, vol + 0.05, f'{vol:.2f}%',
                       ha='center', fontsize=10, fontweight='bold')

    # 子圖4：報酬率比較
    returns = {}
    for stock_code, df in stocks_data.items():
        total_return = ((df['Close'].iloc[-1] - df['Close'].iloc[0]) / df['Close'].iloc[0]) * 100
        returns[stock_code] = total_return

    colors_return = ['red' if r >= 0 else 'green' for r in returns.values()]

    axes[1, 1].bar(range(len(returns)), list(returns.values()),
                  color=colors_return, edgecolor='black', linewidth=1.5, alpha=0.8)
    axes[1, 1].set_xticks(range(len(returns)))
    axes[1, 1].set_xticklabels(stock_names, fontsize=11)
    axes[1, 1].set_title('累計報酬率比較', fontsize=14, fontweight='bold')
    axes[1, 1].set_ylabel('報酬率（%）', fontsize=11)
    axes[1, 1].axhline(y=0, color='black', linestyle='-', linewidth=1)
    axes[1, 1].grid(True, axis='y', alpha=0.3)

    for i, (code, ret) in enumerate(returns.items()):
        y_pos = ret + 1 if ret >= 0 else ret - 1
        axes[1, 1].text(i, y_pos, f'{ret:+.2f}%',
                       ha='center', fontsize=10, fontweight='bold')

    plt.tight_layout()

    return fig

def print_statistics(stocks_data):
    """輸出統計報告"""
    print("\n" + "="*70)
    print("[報告] 台灣股市數據分析報告")
    print("="*70)

    for stock_code, df in stocks_data.items():
        stock_name = df['Stock_Name'].iloc[0]

        print(f"\n【{stock_name}({stock_code})】")
        print("-"*70)

        # 價格統計
        print(f"  價格統計：")
        print(f"    最高價：{df['High'].max():.2f} 元")
        print(f"    最低價：{df['Low'].min():.2f} 元")
        print(f"    平均價：{df['Close'].mean():.2f} 元")
        print(f"    最新價：{df['Close'].iloc[-1]:.2f} 元")

        # 報酬率
        total_return = ((df['Close'].iloc[-1] - df['Close'].iloc[0]) / df['Close'].iloc[0]) * 100
        print(f"\n  報酬率：{total_return:+.2f}%")

        # 波動率
        daily_returns = df['Close'].pct_change()
        volatility = daily_returns.std() * 100
        print(f"  日波動率：{volatility:.2f}%")

        # 成交量
        print(f"\n  成交量：")
        print(f"    平均成交量：{df['Volume'].mean()/1000:,.0f} 萬張")
        print(f"    最大成交量：{df['Volume'].max()/1000:,.0f} 萬張")

        # 技術指標
        print(f"\n  技術指標（最新）：")
        print(f"    RSI(14)：{df['RSI'].iloc[-1]:.2f}")
        print(f"    MACD：{df['MACD'].iloc[-1]:.2f}")

        # 趨勢判斷
        ma5_trend = "上漲" if df['Close'].iloc[-1] > df['MA5'].iloc[-1] else "下跌"
        ma20_trend = "多頭" if df['MA5'].iloc[-1] > df['MA20'].iloc[-1] else "空頭"

        print(f"\n  趨勢判斷：")
        print(f"    短期趨勢（vs MA5）：{ma5_trend}")
        print(f"    中期趨勢（MA5 vs MA20）：{ma20_trend}")

    print("\n" + "="*70)

def save_reports(figures, stocks_data):
    """儲存報表"""
    print("\n正在儲存報表...")

    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 儲存 PNG 圖表
    for i, fig in enumerate(figures):
        if i < len(figures) - 1:
            stock_code = list(stocks_data.keys())[i]
            stock_name = stocks_data[stock_code]['Stock_Name'].iloc[0]
            filename = f'{output_dir}/{stock_code}_{stock_name}_分析圖.png'
        else:
            filename = f'{output_dir}/股票比較分析.png'

        fig.savefig(filename, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"[OK] 已儲存：{filename}")

    # 儲存 PDF 報表
    with PdfPages(f'{output_dir}/台股分析報告.pdf') as pdf:
        for fig in figures:
            pdf.savefig(fig, bbox_inches='tight')
        print(f"[OK] 已儲存：{output_dir}/台股分析報告.pdf")

    print(f"\n[完成] 所有檔案已儲存至 '{output_dir}' 資料夾")

def main():
    """主程式"""
    print("\n" + "="*70)
    print("  台灣股市數據分析專案")
    print("="*70)

    # 載入數據
    stock_codes = ['2330', '2317', '2454']
    stocks_data = {}

    print("\n正在載入股票數據...")
    for code in stock_codes:
        df = load_stock_data(code)
        if df is None:
            return

        # 計算技術指標
        df = calculate_ma(df)
        df = calculate_macd(df)
        df = calculate_rsi(df)
        df = calculate_bollinger_bands(df)

        stocks_data[code] = df

    # 繪製個別股票圖表
    figures = []
    for stock_code, df in stocks_data.items():
        stock_name = df['Stock_Name'].iloc[0]
        fig = plot_candlestick_with_indicators(df, stock_name, stock_code)
        figures.append(fig)

    # 繪製比較圖
    fig_compare = compare_stocks(stocks_data)
    figures.append(fig_compare)

    # 輸出統計報告
    print_statistics(stocks_data)

    # 儲存報表
    save_reports(figures, stocks_data)

    # 顯示圖表
    print("\n正在顯示圖表...")
    plt.show()

    print("\n[完成] 分析完成！")
    print("\n提示：請檢查 'output' 資料夾查看所有輸出檔案")

if __name__ == "__main__":
    main()
