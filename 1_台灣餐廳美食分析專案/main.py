"""
台灣餐廳美食數據分析主程式
===========================
分析台北、台中、台南、高雄的餐廳評分、價格、類型等數據
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
import os

# 設定中文字型
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Arial Unicode MS', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# 設定視覺化風格
sns.set_style("whitegrid")
sns.set_palette("husl")

def load_data():
    """載入餐廳數據"""
    print("正在載入餐廳數據...")
    df = pd.read_csv('data/restaurants.csv', encoding='utf-8-sig')
    print(f"[OK] 已載入 {len(df)} 家餐廳資料")
    return df

def print_statistics(df):
    """輸出統計報告"""
    print("\n" + "="*60)
    print("台灣餐廳美食數據分析報告")
    print("="*60)

    # 整體統計
    print("\n[整體統計]")
    print(f"  總餐廳數: {len(df)} 家")
    print(f"  平均評分: {df['Rating'].mean():.2f} 星")
    print(f"  平均消費: ${df['Avg_Price'].mean():.0f} 元")
    print(f"  平均評論數: {df['Review_Count'].mean():.0f} 則")

    # 各城市統計
    print("\n[各城市統計]")
    print("-" * 60)
    for city in df['City'].unique():
        city_df = df[df['City'] == city]
        print(f"\n{city}:")
        print(f"  餐廳數量: {len(city_df)} 家")
        print(f"  平均評分: {city_df['Rating'].mean():.2f} 星")
        print(f"  平均消費: ${city_df['Avg_Price'].mean():.0f} 元")
        print(f"  最高評分餐廳: {city_df.loc[city_df['Rating'].idxmax(), 'Restaurant_Name']} ({city_df['Rating'].max():.1f}星)")

    # 餐廳類型統計
    print("\n[餐廳類型排行]")
    print("-" * 60)
    cuisine_stats = df.groupby('Cuisine_Type').agg({
        'Restaurant_Name': 'count',
        'Rating': 'mean',
        'Avg_Price': 'mean'
    }).round(2)
    cuisine_stats.columns = ['數量', '平均評分', '平均消費']
    cuisine_stats = cuisine_stats.sort_values('數量', ascending=False)
    print(cuisine_stats)

    # 價格區間統計
    print("\n[價格區間分布]")
    print("-" * 60)
    for price_range in ['平價', '中價位', '高價位']:
        count = len(df[df['Price_Range'] == price_range])
        percentage = count / len(df) * 100
        avg_rating = df[df['Price_Range'] == price_range]['Rating'].mean()
        print(f"  {price_range}: {count} 家 ({percentage:.1f}%) - 平均評分: {avg_rating:.2f}星")

    # 高評價餐廳 (4.5星以上)
    high_rated = df[df['Rating'] >= 4.5].sort_values('Rating', ascending=False)
    print(f"\n[高評價餐廳 (4.5星以上)]")
    print(f"  共 {len(high_rated)} 家")
    print("-" * 60)
    for idx, row in high_rated.head(10).iterrows():
        print(f"  {row['Restaurant_Name']} ({row['City']}) - {row['Rating']}星 - {row['Cuisine_Type']} - ${row['Avg_Price']}元")

def plot_rating_distribution(df):
    """繪製評分分布圖"""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('餐廳評分分布分析', fontsize=20, fontweight='bold', y=0.995)

    # 1. 評分直方圖
    ax1 = axes[0, 0]
    ax1.hist(df['Rating'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
    ax1.axvline(df['Rating'].mean(), color='red', linestyle='--', linewidth=2,
                label=f'平均: {df["Rating"].mean():.2f}星')
    ax1.set_xlabel('評分（星）', fontsize=12)
    ax1.set_ylabel('餐廳數量', fontsize=12)
    ax1.set_title('評分分布直方圖', fontsize=14, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # 2. 各城市評分箱型圖
    ax2 = axes[0, 1]
    cities = df['City'].unique()
    city_ratings = [df[df['City'] == city]['Rating'].values for city in cities]
    bp = ax2.boxplot(city_ratings, tick_labels=cities, patch_artist=True)
    for patch in bp['boxes']:
        patch.set_facecolor('lightgreen')
    ax2.set_ylabel('評分（星）', fontsize=12)
    ax2.set_title('各城市評分分布', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')

    # 3. 餐廳類型平均評分
    ax3 = axes[1, 0]
    cuisine_rating = df.groupby('Cuisine_Type')['Rating'].mean().sort_values(ascending=True)
    colors = plt.cm.viridis(np.linspace(0.3, 0.9, len(cuisine_rating)))
    bars = ax3.barh(cuisine_rating.index, cuisine_rating.values, color=colors, edgecolor='black')
    ax3.set_xlabel('平均評分（星）', fontsize=12)
    ax3.set_title('各餐廳類型平均評分', fontsize=14, fontweight='bold')
    ax3.grid(True, alpha=0.3, axis='x')

    # 在長條圖上顯示數值
    for i, (idx, value) in enumerate(cuisine_rating.items()):
        ax3.text(value + 0.05, i, f'{value:.2f}', va='center', fontsize=10)

    # 4. 評分區間餐廳數量
    ax4 = axes[1, 1]
    rating_ranges = ['1.0-2.0', '2.0-3.0', '3.0-4.0', '4.0-5.0']
    range_counts = [
        len(df[(df['Rating'] >= 1.0) & (df['Rating'] < 2.0)]),
        len(df[(df['Rating'] >= 2.0) & (df['Rating'] < 3.0)]),
        len(df[(df['Rating'] >= 3.0) & (df['Rating'] < 4.0)]),
        len(df[(df['Rating'] >= 4.0) & (df['Rating'] <= 5.0)])
    ]
    colors = ['#ff6b6b', '#feca57', '#48dbfb', '#1dd1a1']
    wedges, texts, autotexts = ax4.pie(range_counts, labels=rating_ranges, autopct='%1.1f%%',
                                         colors=colors, startangle=90)
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(11)
        autotext.set_fontweight('bold')
    ax4.set_title('評分區間分布', fontsize=14, fontweight='bold')

    plt.tight_layout()
    return fig

def plot_price_analysis(df):
    """繪製價格分析圖"""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('餐廳價格分析', fontsize=20, fontweight='bold', y=0.995)

    # 1. 價格分布直方圖
    ax1 = axes[0, 0]
    ax1.hist(df['Avg_Price'], bins=30, color='coral', edgecolor='black', alpha=0.7)
    ax1.axvline(df['Avg_Price'].mean(), color='red', linestyle='--', linewidth=2,
                label=f'平均: ${df["Avg_Price"].mean():.0f}元')
    ax1.set_xlabel('平均消費（元）', fontsize=12)
    ax1.set_ylabel('餐廳數量', fontsize=12)
    ax1.set_title('價格分布直方圖', fontsize=14, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # 2. 價格區間與評分關係
    ax2 = axes[0, 1]
    price_ranges = ['平價', '中價位', '高價位']
    price_data = [df[df['Price_Range'] == pr]['Rating'].values for pr in price_ranges]
    bp = ax2.boxplot(price_data, tick_labels=price_ranges, patch_artist=True)
    colors_box = ['lightblue', 'lightgreen', 'lightyellow']
    for patch, color in zip(bp['boxes'], colors_box):
        patch.set_facecolor(color)
    ax2.set_ylabel('評分（星）', fontsize=12)
    ax2.set_title('價格區間與評分關係', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')

    # 3. 各城市平均消費比較
    ax3 = axes[1, 0]
    city_price = df.groupby('City')['Avg_Price'].mean().sort_values(ascending=False)
    colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12']
    bars = ax3.bar(city_price.index, city_price.values, color=colors, edgecolor='black', alpha=0.8)
    ax3.set_ylabel('平均消費（元）', fontsize=12)
    ax3.set_title('各城市平均消費', fontsize=14, fontweight='bold')
    ax3.grid(True, alpha=0.3, axis='y')

    # 在長條圖上顯示數值
    for i, (city, price) in enumerate(city_price.items()):
        ax3.text(i, price + 10, f'${price:.0f}', ha='center', va='bottom', fontsize=11, fontweight='bold')

    # 4. 餐廳類型平均價格
    ax4 = axes[1, 1]
    cuisine_price = df.groupby('Cuisine_Type')['Avg_Price'].mean().sort_values(ascending=True)
    colors = plt.cm.Oranges(np.linspace(0.4, 0.9, len(cuisine_price)))
    bars = ax4.barh(cuisine_price.index, cuisine_price.values, color=colors, edgecolor='black')
    ax4.set_xlabel('平均消費（元）', fontsize=12)
    ax4.set_title('各餐廳類型平均價格', fontsize=14, fontweight='bold')
    ax4.grid(True, alpha=0.3, axis='x')

    # 在長條圖上顯示數值
    for i, (idx, value) in enumerate(cuisine_price.items()):
        ax4.text(value + 10, i, f'${value:.0f}', va='center', fontsize=10)

    plt.tight_layout()
    return fig

def plot_cuisine_analysis(df):
    """繪製餐廳類型分析圖"""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('餐廳類型分析', fontsize=20, fontweight='bold', y=0.995)

    # 1. 餐廳類型數量
    ax1 = axes[0, 0]
    cuisine_counts = df['Cuisine_Type'].value_counts()
    colors = plt.cm.Set3(np.linspace(0, 1, len(cuisine_counts)))
    wedges, texts, autotexts = ax1.pie(cuisine_counts.values, labels=cuisine_counts.index,
                                         autopct='%1.1f%%', colors=colors, startangle=90)
    for autotext in autotexts:
        autotext.set_color('black')
        autotext.set_fontsize(9)
        autotext.set_fontweight('bold')
    ax1.set_title('餐廳類型分布', fontsize=14, fontweight='bold')

    # 2. 各城市餐廳類型分布
    ax2 = axes[0, 1]
    city_cuisine = pd.crosstab(df['City'], df['Cuisine_Type'])
    city_cuisine.plot(kind='bar', stacked=True, ax=ax2, colormap='tab20')
    ax2.set_ylabel('餐廳數量', fontsize=12)
    ax2.set_xlabel('城市', fontsize=12)
    ax2.set_title('各城市餐廳類型分布', fontsize=14, fontweight='bold')
    ax2.legend(title='餐廳類型', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)
    ax2.grid(True, alpha=0.3, axis='y')
    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=0)

    # 3. 餐廳類型評論數比較
    ax3 = axes[1, 0]
    cuisine_reviews = df.groupby('Cuisine_Type')['Review_Count'].mean().sort_values(ascending=True)
    colors = plt.cm.Blues(np.linspace(0.4, 0.9, len(cuisine_reviews)))
    bars = ax3.barh(cuisine_reviews.index, cuisine_reviews.values, color=colors, edgecolor='black')
    ax3.set_xlabel('平均評論數', fontsize=12)
    ax3.set_title('各餐廳類型平均評論數', fontsize=14, fontweight='bold')
    ax3.grid(True, alpha=0.3, axis='x')

    # 在長條圖上顯示數值
    for i, (idx, value) in enumerate(cuisine_reviews.items()):
        ax3.text(value + 5, i, f'{value:.0f}', va='center', fontsize=10)

    # 4. 價格區間內餐廳類型分布
    ax4 = axes[1, 1]
    price_cuisine = pd.crosstab(df['Price_Range'], df['Cuisine_Type'])
    price_cuisine = price_cuisine.reindex(['平價', '中價位', '高價位'])
    price_cuisine.plot(kind='bar', ax=ax4, colormap='Spectral')
    ax4.set_ylabel('餐廳數量', fontsize=12)
    ax4.set_xlabel('價格區間', fontsize=12)
    ax4.set_title('各價格區間餐廳類型分布', fontsize=14, fontweight='bold')
    ax4.legend(title='餐廳類型', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)
    ax4.grid(True, alpha=0.3, axis='y')
    plt.setp(ax4.xaxis.get_majorticklabels(), rotation=0)

    plt.tight_layout()
    return fig

def plot_city_comparison(df):
    """繪製城市比較圖"""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('城市綜合比較', fontsize=20, fontweight='bold', y=0.995)

    cities = df['City'].unique()

    # 1. 各城市餐廳數量
    ax1 = axes[0, 0]
    city_counts = df['City'].value_counts().reindex(cities)
    colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12']
    bars = ax1.bar(city_counts.index, city_counts.values, color=colors, edgecolor='black', alpha=0.8)
    ax1.set_ylabel('餐廳數量', fontsize=12)
    ax1.set_title('各城市餐廳數量', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3, axis='y')

    for i, (city, count) in enumerate(city_counts.items()):
        ax1.text(i, count + 1, f'{count}家', ha='center', va='bottom', fontsize=11, fontweight='bold')

    # 2. 各城市平均評分
    ax2 = axes[0, 1]
    city_rating = df.groupby('City')['Rating'].mean().reindex(cities)
    bars = ax2.bar(city_rating.index, city_rating.values, color=colors, edgecolor='black', alpha=0.8)
    ax2.set_ylabel('平均評分（星）', fontsize=12)
    ax2.set_title('各城市平均評分', fontsize=14, fontweight='bold')
    ax2.set_ylim([0, 5])
    ax2.grid(True, alpha=0.3, axis='y')

    for i, (city, rating) in enumerate(city_rating.items()):
        ax2.text(i, rating + 0.1, f'{rating:.2f}星', ha='center', va='bottom', fontsize=11, fontweight='bold')

    # 3. 各城市價格區間分布
    ax3 = axes[1, 0]
    city_price_dist = pd.crosstab(df['City'], df['Price_Range'], normalize='index') * 100
    city_price_dist = city_price_dist[['平價', '中價位', '高價位']]
    city_price_dist.plot(kind='bar', stacked=True, ax=ax3,
                         color=['lightblue', 'lightgreen', 'lightyellow'],
                         edgecolor='black')
    ax3.set_ylabel('百分比 (%)', fontsize=12)
    ax3.set_xlabel('城市', fontsize=12)
    ax3.set_title('各城市價格區間分布', fontsize=14, fontweight='bold')
    ax3.legend(title='價格區間', loc='upper right')
    ax3.grid(True, alpha=0.3, axis='y')
    plt.setp(ax3.xaxis.get_majorticklabels(), rotation=0)

    # 4. 各城市高評價餐廳比例
    ax4 = axes[1, 1]
    high_rated_ratio = []
    for city in cities:
        city_df = df[df['City'] == city]
        high_rated = len(city_df[city_df['Rating'] >= 4.5])
        ratio = (high_rated / len(city_df)) * 100
        high_rated_ratio.append(ratio)

    bars = ax4.bar(cities, high_rated_ratio, color=colors, edgecolor='black', alpha=0.8)
    ax4.set_ylabel('高評價餐廳比例 (%)', fontsize=12)
    ax4.set_title('各城市高評價餐廳比例 (4.5星以上)', fontsize=14, fontweight='bold')
    ax4.grid(True, alpha=0.3, axis='y')

    for i, ratio in enumerate(high_rated_ratio):
        ax4.text(i, ratio + 1, f'{ratio:.1f}%', ha='center', va='bottom', fontsize=11, fontweight='bold')

    plt.tight_layout()
    return fig

def plot_correlation_heatmap(df):
    """繪製相關性熱力圖"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))

    # 選擇數值欄位
    numeric_cols = ['Rating', 'Review_Count', 'Avg_Price']
    corr_data = df[numeric_cols].corr()

    # 繪製熱力圖
    sns.heatmap(corr_data, annot=True, fmt='.3f', cmap='coolwarm',
                center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8},
                ax=ax, vmin=-1, vmax=1)

    ax.set_title('評分、評論數、價格相關性分析', fontsize=16, fontweight='bold', pad=20)

    # 設定標籤
    labels = ['評分', '評論數', '平均價格']
    ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.set_yticklabels(labels, rotation=0)

    plt.tight_layout()
    return fig

def plot_city_restaurant_histogram(df):
    """繪製城市對應餐廳數量的直方圖"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))

    # 統計各城市餐廳數量
    city_counts = df['City'].value_counts().sort_values(ascending=False)

    # 設定顏色
    colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6', '#1abc9c']
    bar_colors = colors[:len(city_counts)]

    # 繪製直方圖
    bars = ax.bar(city_counts.index, city_counts.values,
                   color=bar_colors, edgecolor='black', alpha=0.85, linewidth=2)

    # 設定標籤和標題
    ax.set_xlabel('城市', fontsize=14, fontweight='bold')
    ax.set_ylabel('餐廳數量', fontsize=14, fontweight='bold')
    ax.set_title('各城市餐廳數量分布直方圖', fontsize=18, fontweight='bold', pad=20)

    # 在每個長條上方顯示數值
    for i, (city, count) in enumerate(city_counts.items()):
        ax.text(i, count + 1, f'{count}家',
                ha='center', va='bottom', fontsize=12, fontweight='bold')

    # 加入網格線
    ax.grid(True, alpha=0.3, axis='y', linestyle='--')
    ax.set_axisbelow(True)

    # 設定 y 軸範圍，留一些空間給數值標籤
    max_count = city_counts.max()
    ax.set_ylim(0, max_count * 1.15)

    # 加入統計資訊文字框
    total_restaurants = len(df)
    avg_per_city = total_restaurants / len(city_counts)
    info_text = f'總餐廳數: {total_restaurants} 家\n平均每城市: {avg_per_city:.1f} 家'

    ax.text(0.98, 0.97, info_text,
            transform=ax.transAxes, fontsize=11,
            verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    plt.tight_layout()
    return fig

def save_figures(figs, filenames):
    """儲存圖表"""
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)

    print("\n正在儲存圖表...")
    for fig, filename in zip(figs, filenames):
        filepath = os.path.join(output_dir, filename)
        fig.savefig(filepath, dpi=300, bbox_inches='tight')
        print(f"  [OK] 已儲存: {filepath}")

    # 儲存 PDF 報表
    pdf_path = os.path.join(output_dir, '台灣餐廳美食分析報告.pdf')
    with PdfPages(pdf_path) as pdf:
        for fig in figs:
            pdf.savefig(fig, bbox_inches='tight')
    print(f"  [OK] 已儲存PDF報表: {pdf_path}")

def main():
    """主程式"""
    print("="*60)
    print("台灣餐廳美食數據分析程式")
    print("="*60)

    # 載入數據
    df = load_data()

    # 輸出統計報告
    print_statistics(df)

    # 生成視覺化圖表
    print("\n" + "="*60)
    print("正在生成視覺化圖表...")
    print("="*60)

    fig1 = plot_rating_distribution(df)
    print("  [1/6] 評分分布分析圖")

    fig2 = plot_price_analysis(df)
    print("  [2/6] 價格分析圖")

    fig3 = plot_cuisine_analysis(df)
    print("  [3/6] 餐廳類型分析圖")

    fig4 = plot_city_comparison(df)
    print("  [4/6] 城市比較圖")

    fig5 = plot_correlation_heatmap(df)
    print("  [5/6] 相關性熱力圖")

    fig6 = plot_city_restaurant_histogram(df)
    print("  [6/6] 城市餐廳數量直方圖")

    # 儲存圖表
    figs = [fig1, fig2, fig3, fig4, fig5, fig6]
    filenames = [
        '評分分布分析.png',
        '價格分析.png',
        '餐廳類型分析.png',
        '城市比較.png',
        '相關性分析.png',
        '城市餐廳數量直方圖.png'
    ]
    save_figures(figs, filenames)

    print("\n" + "="*60)
    print("分析完成！")
    print("="*60)
    print("\n所有圖表已儲存在 output 資料夾中：")
    print("  - 評分分布分析.png")
    print("  - 價格分析.png")
    print("  - 餐廳類型分析.png")
    print("  - 城市比較.png")
    print("  - 相關性分析.png")
    print("  - 城市餐廳數量直方圖.png")
    print("  - 台灣餐廳美食分析報告.pdf")
    print("\n" + "="*60)

if __name__ == "__main__":
    main()
