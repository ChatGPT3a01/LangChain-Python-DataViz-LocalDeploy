"""
生成台灣氣象本地數據
====================
生成台北、台中、台南、高雄、花蓮等城市的模擬氣象數據
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

def generate_weather_data(city_name, base_temp, temp_range, rainfall_prob, days=365):
    """
    生成單一城市的氣象數據

    Args:
        city_name: 城市名稱
        base_temp: 基準溫度
        temp_range: 溫度變化範圍
        rainfall_prob: 降雨機率
        days: 天數
    """
    print(f"正在生成 {city_name} 的氣象數據...")

    # 建立日期範圍（2024年全年）
    start_date = datetime(2024, 1, 1)
    dates = pd.date_range(start_date, periods=days, freq='D')

    # 生成溫度數據（考慮季節性）
    # 使用正弦函數模擬季節變化
    seasonal_cycle = np.sin(np.arange(days) * 2 * np.pi / 365 - np.pi/2)  # -1 到 1

    # 溫度 = 基準溫度 + 季節變化 + 隨機波動
    temperatures = base_temp + seasonal_cycle * temp_range + np.random.normal(0, 2, days)

    # 最高溫和最低溫
    max_temps = temperatures + np.random.uniform(2, 5, days)
    min_temps = temperatures - np.random.uniform(2, 5, days)

    # 生成降雨量（mm）
    # 降雨天數根據機率決定
    is_rainy = np.random.random(days) < rainfall_prob
    rainfall = np.where(is_rainy,
                       np.random.exponential(20, days),  # 下雨時的降雨量
                       0)  # 不下雨

    # 增加夏季降雨（梅雨季和颱風季）
    summer_months = (dates.month >= 5) & (dates.month <= 9)
    rainfall[summer_months] *= 1.5

    # 生成濕度（%）
    # 濕度與降雨相關
    base_humidity = 70
    humidity = base_humidity + np.random.normal(0, 10, days)
    humidity[is_rainy] += 15  # 下雨時濕度較高
    humidity = np.clip(humidity, 40, 100)  # 限制在合理範圍

    # 生成天氣狀況
    weather_conditions = []
    for i in range(days):
        if rainfall[i] > 50:
            weather_conditions.append('大雨')
        elif rainfall[i] > 10:
            weather_conditions.append('中雨')
        elif rainfall[i] > 0:
            weather_conditions.append('小雨')
        elif temperatures[i] > 30:
            weather_conditions.append('晴朗炎熱')
        else:
            weather_conditions.append('晴朗')

    # 建立 DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'City': city_name,
        'Temp_Avg': temperatures.round(1),
        'Temp_Max': max_temps.round(1),
        'Temp_Min': min_temps.round(1),
        'Rainfall': rainfall.round(1),
        'Humidity': humidity.round(1),
        'Weather': weather_conditions
    })

    return df

print("="*60)
print("台灣氣象數據生成工具")
print("="*60)

# 生成五大城市的氣象數據
cities = [
    ('台北', 23, 8, 0.35),    # 城市名稱, 基準溫度, 溫度變化範圍, 降雨機率
    ('台中', 24, 9, 0.25),
    ('台南', 25, 9, 0.20),
    ('高雄', 26, 8, 0.22),
    ('花蓮', 23, 8, 0.30)
]

all_data = []

for city_name, base_temp, temp_range, rainfall_prob in cities:
    df = generate_weather_data(city_name, base_temp, temp_range, rainfall_prob, days=365)
    all_data.append(df)

    # 儲存個別城市數據
    filename = f'data/{city_name}_weather.csv'
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"  [OK] 已儲存: {filename}")
    print(f"  - 數據天數: {len(df)} 天")
    print(f"  - 平均溫度: {df['Temp_Avg'].mean():.1f}°C")
    print(f"  - 總降雨量: {df['Rainfall'].sum():.1f} mm")
    print(f"  - 平均濕度: {df['Humidity'].mean():.1f}%")
    print()

# 合併所有數據
combined_df = pd.concat(all_data, ignore_index=True)
combined_df.to_csv('data/all_cities_weather.csv', index=False, encoding='utf-8-sig')
print(f"[OK] 已儲存合併數據: data/all_cities_weather.csv")

print("\n" + "="*60)
print("數據生成完成！")
print("="*60)
print(f"\n總共生成 {len(cities)} 個城市的氣象數據")
print(f"時間範圍: {all_data[0]['Date'].min().strftime('%Y-%m-%d')} 至 {all_data[0]['Date'].max().strftime('%Y-%m-%d')}")
print("\n可以開始執行 main.py 進行分析！")
