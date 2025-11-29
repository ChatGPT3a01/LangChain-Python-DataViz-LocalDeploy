"""
生成本地 COVID-19 數據檔案
====================================
此腳本用於生成模擬的 COVID-19 疫情數據，供離線使用。
執行此腳本一次，即可生成 data/covid19_confirmed_global.csv 檔案。
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 設定隨機種子，確保每次生成的數據一致
np.random.seed(42)

# 定義國家列表
COUNTRIES = ['Taiwan*', 'US', 'United Kingdom', 'Japan', 'Korea, South',
             'Germany', 'France', 'Italy', 'Spain', 'India']

# 建立日期範圍（從 2020-01-22 到 2023-03-09，Johns Hopkins 停止更新的日期）
start_date = datetime(2020, 1, 22)
end_date = datetime(2023, 3, 9)
dates = pd.date_range(start_date, end_date, freq='D')

print("="*60)
print("正在生成本地 COVID-19 數據檔案...")
print("="*60)
print(f"時間範圍: {start_date.strftime('%Y-%m-%d')} 至 {end_date.strftime('%Y-%m-%d')}")
print(f"總天數: {len(dates)} 天")
print(f"國家數: {len(COUNTRIES)} 個")
print("-"*60)

# 建立基礎 DataFrame
data = {
    'Province/State': [''] * len(COUNTRIES),
    'Country/Region': COUNTRIES,
    'Lat': [25.0, 40.0, 55.0, 36.0, 37.5, 51.0, 46.0, 41.9, 40.4, 20.6],  # 緯度
    'Long': [121.0, -100.0, -3.0, 138.0, 127.5, 9.0, 2.0, 12.5, -3.7, 78.9]  # 經度
}

# 為每個國家生成模擬的累計確診數據
print("\n正在生成各國疫情數據...")

for i, date in enumerate(dates):
    # 格式化日期為 Johns Hopkins 的格式：m/d/yy
    # Windows 使用 %#m，其他系統使用 %-m
    try:
        date_str = date.strftime('%-m/%-d/%y')  # Mac/Linux
    except:
        date_str = date.strftime('%#m/%#d/%y')  # Windows

    # 計算天數（從第一天開始）
    days_passed = i

    # 為每個國家生成累計確診數
    country_cases = []

    for j, country in enumerate(COUNTRIES):
        # 不同國家有不同的基礎值和增長率
        if country == 'Taiwan*':
            # 台灣：前期控制良好，2022年開始大幅增加
            if days_passed < 800:  # 2022年3月前
                base = days_passed * 2
                cases = base + np.random.randint(-5, 20)
            else:  # 2022年3月後
                base = 1600 + (days_passed - 800) ** 1.8
                cases = int(base + np.random.randint(-1000, 5000))

        elif country == 'US':
            # 美國：持續增長，最終超過1億
            base = days_passed ** 2.1 * 15
            cases = int(base + np.random.randint(-10000, 50000))

        elif country == 'United Kingdom':
            # 英國：穩定增長
            base = days_passed ** 2.0 * 8
            cases = int(base + np.random.randint(-5000, 20000))

        elif country == 'Japan':
            # 日本：多波疫情
            base = days_passed ** 1.9 * 10
            wave_factor = np.sin(days_passed / 100) * 500000
            cases = int(base + wave_factor + np.random.randint(-3000, 10000))

        elif country == 'Korea, South':
            # 南韓：類似台灣，後期大增
            if days_passed < 750:
                base = days_passed * 50
            else:
                base = 37500 + (days_passed - 750) ** 1.9 * 20
            cases = int(base + np.random.randint(-2000, 8000))

        elif country == 'Germany':
            # 德國：穩定高增長
            base = days_passed ** 2.05 * 10
            cases = int(base + np.random.randint(-5000, 25000))

        elif country == 'France':
            # 法國：高確診數
            base = days_passed ** 2.08 * 9
            cases = int(base + np.random.randint(-5000, 25000))

        elif country == 'Italy':
            # 義大利：前期重災區
            base = days_passed ** 2.0 * 7
            cases = int(base + np.random.randint(-3000, 15000))

        elif country == 'Spain':
            # 西班牙：類似義大利
            base = days_passed ** 1.98 * 7
            cases = int(base + np.random.randint(-3000, 15000))

        elif country == 'India':
            # 印度：2021年大爆發
            if days_passed < 450:
                base = days_passed ** 2.0 * 5
            else:
                base = days_passed ** 2.1 * 8
            cases = int(base + np.random.randint(-5000, 30000))

        else:
            base = days_passed ** 2.0 * 5
            cases = int(base)

        # 確保數值為正且單調遞增
        cases = max(0, cases)
        if j < len(country_cases) and len(country_cases) > 0:
            # 確保累計數不會減少
            pass

        country_cases.append(cases)

    # 確保每個國家的數據單調遞增
    data[date_str] = country_cases

# 建立 DataFrame
df = pd.DataFrame(data)

# 確保累計數據單調遞增（修正）
date_columns = [col for col in df.columns if col not in ['Province/State', 'Country/Region', 'Lat', 'Long']]

for idx in df.index:
    prev_value = 0
    for col in date_columns:
        if df.loc[idx, col] < prev_value:
            df.loc[idx, col] = prev_value
        prev_value = df.loc[idx, col]

# 儲存為 CSV
output_file = 'data/covid19_confirmed_global.csv'
df.to_csv(output_file, index=False)

print(f"\n[OK] 數據生成完成！")
print(f"[OK] 檔案已儲存至: {output_file}")
print(f"\n數據摘要:")
print("-"*60)

# 顯示最終累計確診數
print("\n各國最終累計確診數（2023-03-09）:")
final_date_col = date_columns[-1]
for idx, country in enumerate(COUNTRIES):
    final_cases = df.loc[idx, final_date_col]
    print(f"  {country:20s}: {final_cases:>12,} 例")

print("\n" + "="*60)
print("數據檔案生成完成！現在可以在離線狀態下執行 main.py")
print("="*60)
