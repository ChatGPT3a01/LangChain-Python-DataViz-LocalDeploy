"""
生成社群媒體本地數據
====================
生成多個社群媒體平台的模擬數據，包含粉絲數、互動率、貼文數等指標
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

np.random.seed(42)

# 定義社群媒體平台
PLATFORMS = ['Facebook', 'Instagram', 'Twitter', 'YouTube', 'TikTok', 'LinkedIn']

# 平台中文名稱對照
PLATFORM_NAMES = {
    'Facebook': 'Facebook',
    'Instagram': 'Instagram',
    'Twitter': 'Twitter',
    'YouTube': 'YouTube',
    'TikTok': 'TikTok',
    'LinkedIn': 'LinkedIn'
}

def generate_social_media_data(platform, base_followers, growth_rate, days=365):
    """
    生成單一平台的社群媒體數據

    Args:
        platform: 平台名稱
        base_followers: 基準粉絲數
        growth_rate: 成長率（每日）
        days: 天數
    """
    print(f"正在生成 {platform} 的數據...")

    # 建立日期範圍
    start_date = datetime(2026, 1, 1)
    dates = pd.date_range(start_date, periods=days, freq='D')

    # 生成粉絲數（指數成長 + 隨機波動）
    growth_factor = np.exp(np.arange(days) * growth_rate)
    noise = np.random.normal(0, 0.02, days)
    followers = (base_followers * growth_factor * (1 + noise)).astype(int)

    # 確保粉絲數單調遞增
    for i in range(1, len(followers)):
        if followers[i] < followers[i-1]:
            followers[i] = followers[i-1] + np.random.randint(0, 100)

    # 生成每日貼文數（1-5篇，週末較少）
    posts_per_day = []
    for date in dates:
        if date.weekday() >= 5:  # 週末
            posts = np.random.randint(0, 2)
        else:
            posts = np.random.randint(1, 5)
        posts_per_day.append(posts)

    # 生成互動數據（按讚、分享、留言）
    # 互動數與粉絲數和貼文數相關
    likes = []
    shares = []
    comments = []
    engagement_rates = []

    for i in range(days):
        # 基礎互動率（不同平台不同）
        if platform == 'Instagram':
            base_engagement = 0.05  # 5%
        elif platform == 'Facebook':
            base_engagement = 0.03  # 3%
        elif platform == 'Twitter':
            base_engagement = 0.02  # 2%
        elif platform == 'YouTube':
            base_engagement = 0.04  # 4%
        elif platform == 'TikTok':
            base_engagement = 0.08  # 8%
        else:  # LinkedIn
            base_engagement = 0.015  # 1.5%

        # 加入隨機波動
        engagement_rate = base_engagement * (1 + np.random.uniform(-0.3, 0.5))
        engagement_rates.append(engagement_rate)

        # 計算互動數
        daily_engagement = int(followers[i] * posts_per_day[i] * engagement_rate)

        # 按讚數（約70%的互動）
        like_count = int(daily_engagement * 0.7 * (1 + np.random.uniform(-0.2, 0.2)))
        likes.append(max(0, like_count))

        # 分享數（約15%的互動）
        share_count = int(daily_engagement * 0.15 * (1 + np.random.uniform(-0.3, 0.3)))
        shares.append(max(0, share_count))

        # 留言數（約15%的互動）
        comment_count = int(daily_engagement * 0.15 * (1 + np.random.uniform(-0.3, 0.3)))
        comments.append(max(0, comment_count))

    # 建立 DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'Platform': platform,
        'Followers': followers,
        'Posts': posts_per_day,
        'Likes': likes,
        'Shares': shares,
        'Comments': comments,
        'Engagement_Rate': engagement_rates,
        'Total_Engagement': [l + s + c for l, s, c in zip(likes, shares, comments)]
    })

    return df

print("="*60)
print("社群媒體數據生成工具")
print("="*60)

# 定義各平台的參數
platform_configs = [
    ('Facebook', 50000, 0.0005),      # 基準粉絲5萬，每日成長0.05%
    ('Instagram', 80000, 0.0008),     # 基準粉絲8萬，每日成長0.08%
    ('Twitter', 30000, 0.0003),        # 基準粉絲3萬，每日成長0.03%
    ('YouTube', 120000, 0.001),        # 基準粉絲12萬，每日成長0.1%
    ('TikTok', 150000, 0.0012),       # 基準粉絲15萬，每日成長0.12%
    ('LinkedIn', 20000, 0.0002)       # 基準粉絲2萬，每日成長0.02%
]

all_data = []

# 建立 data 資料夾
os.makedirs('data', exist_ok=True)

for platform, base_followers, growth_rate in platform_configs:
    df = generate_social_media_data(platform, base_followers, growth_rate, days=365)
    all_data.append(df)

    # 儲存個別平台數據
    filename = f'data/{platform}_data.csv'
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"  [OK] 已儲存: {filename}")
    print(f"  - 數據天數: {len(df)} 天")
    print(f"  - 粉絲數範圍: {df['Followers'].min():,} - {df['Followers'].max():,}")
    print(f"  - 平均每日貼文: {df['Posts'].mean():.1f} 篇")
    print(f"  - 平均互動率: {df['Engagement_Rate'].mean()*100:.2f}%")
    print()

# 合併所有數據
combined_df = pd.concat(all_data, ignore_index=True)
combined_df.to_csv('data/all_social_media_data.csv', index=False, encoding='utf-8-sig')
print(f"[OK] 已儲存合併數據: data/all_social_media_data.csv")

print("\n" + "="*60)
print("數據生成完成！")
print("="*60)
print(f"\n總共生成 {len(platform_configs)} 個平台的數據")
print(f"時間範圍: {all_data[0]['Date'].min().strftime('%Y-%m-%d')} 至 {all_data[0]['Date'].max().strftime('%Y-%m-%d')}")
print("\n可以開始執行 main.py 進行分析！")

