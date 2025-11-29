"""
生成台灣股市本地數據
====================
生成台積電(2330)、鴻海(2317)、聯發科(2454)的模擬股價數據
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

def generate_stock_data(stock_name, stock_code, base_price, volatility, days=365):
    """
    生成單一股票的模擬數據

    Args:
        stock_name: 股票名稱
        stock_code: 股票代碼
        base_price: 基準價格
        volatility: 波動率
        days: 天數
    """
    print(f"正在生成 {stock_name}({stock_code}) 的數據...")

    # 建立日期範圍（只包含工作日）
    start_date = datetime(2024, 1, 2)
    all_dates = []
    current_date = start_date

    while len(all_dates) < days:
        # 跳過週末
        if current_date.weekday() < 5:  # 0-4 是週一到週五
            all_dates.append(current_date)
        current_date += timedelta(days=1)

    dates = pd.DatetimeIndex(all_dates)

    # 生成價格數據（使用隨機遊走 + 趨勢）
    returns = np.random.normal(0.001, volatility, len(dates))  # 平均上漲 0.1%

    # 加入趨勢和周期性
    trend = np.linspace(0, 0.3, len(dates))  # 整體上漲趨勢 30%
    cycle = np.sin(np.arange(len(dates)) * 2 * np.pi / 60) * 0.05  # 60天週期

    cumulative_returns = np.cumsum(returns) + trend + cycle
    close_prices = base_price * (1 + cumulative_returns)

    # 生成 Open, High, Low 價格
    open_prices = close_prices * (1 + np.random.uniform(-0.01, 0.01, len(dates)))
    high_prices = np.maximum(open_prices, close_prices) * (1 + np.random.uniform(0, 0.02, len(dates)))
    low_prices = np.minimum(open_prices, close_prices) * (1 - np.random.uniform(0, 0.02, len(dates)))

    # 生成成交量（單位：千股）
    base_volume = 50000  # 5萬張
    volumes = base_volume * (1 + np.random.uniform(-0.3, 0.5, len(dates)))

    # 建立 DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'Open': open_prices,
        'High': high_prices,
        'Low': low_prices,
        'Close': close_prices,
        'Volume': volumes.astype(int),
        'Stock_Code': stock_code,
        'Stock_Name': stock_name
    })

    return df

print("="*60)
print("台灣股市數據生成工具")
print("="*60)

# 生成三檔熱門股票的數據
stocks = [
    ('台積電', '2330', 600, 0.015),   # 基準價 600, 波動率 1.5%
    ('鴻海', '2317', 100, 0.020),     # 基準價 100, 波動率 2.0%
    ('聯發科', '2454', 800, 0.025)    # 基準價 800, 波動率 2.5%
]

all_data = []

for stock_name, stock_code, base_price, volatility in stocks:
    df = generate_stock_data(stock_name, stock_code, base_price, volatility, days=250)
    all_data.append(df)

    # 儲存個別股票數據
    filename = f'data/{stock_code}_{stock_name}.csv'
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"  [OK] 已儲存: {filename}")
    print(f"  - 數據天數: {len(df)} 天")
    print(f"  - 價格範圍: {df['Close'].min():.2f} - {df['Close'].max():.2f}")
    print(f"  - 平均成交量: {df['Volume'].mean():,.0f} 千股")
    print()

# 合併所有數據
combined_df = pd.concat(all_data, ignore_index=True)
combined_df.to_csv('data/all_stocks.csv', index=False, encoding='utf-8-sig')
print(f"[OK] 已儲存合併數據: data/all_stocks.csv")

print("\n" + "="*60)
print("數據生成完成！")
print("="*60)
print(f"\n總共生成 {len(stocks)} 檔股票的數據")
print(f"時間範圍: {all_data[0]['Date'].min().strftime('%Y-%m-%d')} 至 {all_data[0]['Date'].max().strftime('%Y-%m-%d')}")
print("\n可以開始執行 main.py 進行分析！")
