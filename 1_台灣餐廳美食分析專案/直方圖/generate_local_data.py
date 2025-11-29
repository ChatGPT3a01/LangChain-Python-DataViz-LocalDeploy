"""
生成台灣餐廳美食本地數據
=======================
生成台北、台中、台南、高雄各地區餐廳的模擬數據
"""

import pandas as pd
import numpy as np
import os

np.random.seed(42)

# 餐廳類型列表
CUISINE_TYPES = [
    '台式料理', '日式料理', '義式料理', '美式料理',
    '中式料理', '韓式料理', '泰式料理', '咖啡廳',
    '火鍋', '燒烤', '小吃', '甜點店'
]

# 價格區間
PRICE_RANGES = ['平價', '中價位', '高價位']

# 城市
CITIES = ['台北', '台中', '台南', '高雄']

def generate_restaurant_name(cuisine_type, index):
    """生成餐廳名稱"""
    prefixes = ['老', '阿', '小', '大', '正宗', '道地', '美味', '香濃']
    suffixes = ['餐廳', '食堂', '館', '屋', '小館', '料理']

    if cuisine_type == '咖啡廳':
        names = ['星巴克', 'Cafe', 'Coffee', '咖啡館', '咖啡廳', 'Brew']
        return f"{np.random.choice(names)}{index}"
    elif cuisine_type == '小吃':
        names = ['夜市', '老店', '名店', '傳統', '古早味']
        return f"{np.random.choice(names)}{cuisine_type}{index}"
    elif cuisine_type == '甜點店':
        names = ['甜心', '夢幻', '蜜糖', '香甜', '烘焙']
        return f"{np.random.choice(names)}{cuisine_type}{index}"
    else:
        prefix = np.random.choice(prefixes)
        suffix = np.random.choice(suffixes)
        return f"{prefix}{cuisine_type}{suffix}{index}"

def generate_restaurants_for_city(city, num_restaurants=50):
    """為單一城市生成餐廳數據"""
    print(f"正在生成 {city} 的餐廳數據...")

    restaurants = []

    for i in range(num_restaurants):
        # 隨機選擇餐廳類型
        cuisine_type = np.random.choice(CUISINE_TYPES)

        # 生成餐廳名稱
        name = generate_restaurant_name(cuisine_type, i+1)

        # 生成評分（1.0 - 5.0，偏向高分）
        # 使用 beta 分佈讓評分更真實（大多數餐廳在 3.5-4.5 之間）
        rating_base = np.random.beta(8, 2) * 4 + 1  # 偏向高分
        rating = round(rating_base, 1)
        rating = np.clip(rating, 1.0, 5.0)

        # 生成評論數（10-1000）
        # 評分高的餐廳通常評論數也多
        review_count_base = int(np.random.exponential(100))
        review_count = min(review_count_base + int((rating - 1) * 50), 1000)
        review_count = max(review_count, 10)

        # 根據餐廳類型決定價格區間
        if cuisine_type in ['小吃', '台式料理']:
            price_range = np.random.choice(PRICE_RANGES, p=[0.7, 0.25, 0.05])
        elif cuisine_type in ['日式料理', '義式料理', '韓式料理']:
            price_range = np.random.choice(PRICE_RANGES, p=[0.2, 0.5, 0.3])
        elif cuisine_type in ['火鍋', '燒烤']:
            price_range = np.random.choice(PRICE_RANGES, p=[0.3, 0.5, 0.2])
        else:
            price_range = np.random.choice(PRICE_RANGES, p=[0.4, 0.4, 0.2])

        # 計算平均消費（元）
        if price_range == '平價':
            avg_price = int(np.random.normal(150, 30))
            avg_price = np.clip(avg_price, 80, 250)
        elif price_range == '中價位':
            avg_price = int(np.random.normal(400, 80))
            avg_price = np.clip(avg_price, 250, 700)
        else:  # 高價位
            avg_price = int(np.random.normal(800, 150))
            avg_price = np.clip(avg_price, 700, 1500)

        # 生成特色標籤
        tags = []
        if rating >= 4.5:
            tags.append('高評價')
        if review_count > 500:
            tags.append('超人氣')
        if price_range == '平價':
            tags.append('平價美食')
        if cuisine_type in ['台式料理', '小吃']:
            tags.append('在地美食')

        restaurants.append({
            'Restaurant_Name': name,
            'City': city,
            'Cuisine_Type': cuisine_type,
            'Rating': rating,
            'Review_Count': review_count,
            'Price_Range': price_range,
            'Avg_Price': avg_price,
            'Tags': ', '.join(tags) if tags else '無'
        })

    return restaurants

print("="*60)
print("台灣餐廳美食數據生成工具")
print("="*60)

# 生成所有城市的餐廳數據
all_restaurants = []

for city in CITIES:
    city_restaurants = generate_restaurants_for_city(city, num_restaurants=50)
    all_restaurants.extend(city_restaurants)

# 建立 DataFrame
df = pd.DataFrame(all_restaurants)

# 建立 data 資料夾
os.makedirs('data', exist_ok=True)

# 儲存數據
df.to_csv('data/restaurants.csv', index=False, encoding='utf-8-sig')

print(f"\n[OK] 已儲存: data/restaurants.csv")
print(f"  - 總餐廳數: {len(df)} 家")
print(f"  - 城市數: {df['City'].nunique()} 個")
print(f"  - 餐廳類型: {df['Cuisine_Type'].nunique()} 種")
print()

# 顯示統計摘要
print("="*60)
print("數據統計摘要")
print("="*60)

print("\n各城市餐廳數：")
for city in CITIES:
    count = len(df[df['City'] == city])
    print(f"  {city}: {count} 家")

print("\n餐廳類型分布（前5名）：")
cuisine_counts = df['Cuisine_Type'].value_counts().head(5)
for cuisine, count in cuisine_counts.items():
    print(f"  {cuisine}: {count} 家")

print("\n價格區間分布：")
for price_range in PRICE_RANGES:
    count = len(df[df['Price_Range'] == price_range])
    percentage = count / len(df) * 100
    print(f"  {price_range}: {count} 家 ({percentage:.1f}%)")

print(f"\n平均評分: {df['Rating'].mean():.2f} 星")
print(f"平均消費: ${df['Avg_Price'].mean():.0f} 元")

print("\n" + "="*60)
print("數據生成完成！")
print("="*60)
print("\n可以開始執行 main.py 進行分析！")
