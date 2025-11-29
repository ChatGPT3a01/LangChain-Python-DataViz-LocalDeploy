"""
台灣氣象數據視覺化專案
====================
分析台北、台中、台南、高雄、花蓮的氣象數據

功能：
1. 溫度趨勢分析
2. 降雨量統計
3. 濕度分析
4. 地區比較
5. 季節性分析
6. 熱力圖視覺化
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
import os
import warnings
warnings.filterwarnings('ignore')

# 設定中文字型
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Arial Unicode MS', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

def load_weather_data():
    """載入氣象數據"""
    print("正在載入氣象數據...")

    filename = 'data/all_cities_weather.csv'

    if not os.path.exists(filename):
        print(f"[X] 找不到數據檔案：{filename}")
        print("請先執行 generate_local_data.py 生成數據")
        return None

    df = pd.read_csv(filename)
    df['Date'] = pd.to_datetime(df['Date'])

    # 新增月份欄位
    df['Month'] = df['Date'].dt.month
    df['Month_Name'] = df['Date'].dt.strftime('%m月')

    # 新增季節欄位
    def get_season(month):
        if month in [3, 4, 5]:
            return '春季'
        elif month in [6, 7, 8]:
            return '夏季'
        elif month in [9, 10, 11]:
            return '秋季'
        else:
            return '冬季'

    df['Season'] = df['Month'].apply(get_season)

    print(f"[OK] 數據載入成功")
    print(f"  時間範圍：{df['Date'].min().strftime('%Y-%m-%d')} 至 {df['Date'].max().strftime('%Y-%m-%d')}")
    print(f"  城市數量：{df['City'].nunique()} 個")
    print(f"  數據筆數：{len(df)} 筆")

    return df

def plot_temperature_trends(df):
    """繪製溫度趨勢圖"""
    print("\n正在繪製溫度趨勢圖...")

    fig, axes = plt.subplots(2, 1, figsize=(16, 10))
    fig.suptitle('台灣各地溫度趨勢分析（2024年）', fontsize=18, fontweight='bold', y=0.995)

    cities = df['City'].unique()
    colors = plt.cm.Set2(np.linspace(0, 1, len(cities)))

    # 子圖1：每日平均溫度
    for i, city in enumerate(cities):
        city_data = df[df['City'] == city]
        axes[0].plot(city_data['Date'], city_data['Temp_Avg'],
                    label=city, linewidth=2, color=colors[i], alpha=0.8)

    axes[0].set_title('每日平均溫度', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('日期', fontsize=12)
    axes[0].set_ylabel('溫度（°C）', fontsize=12)
    axes[0].legend(loc='upper left', fontsize=11, ncol=5)
    axes[0].grid(True, alpha=0.3)
    axes[0].tick_params(axis='x', rotation=45)

    # 子圖2：月平均溫度比較
    monthly_temp = df.groupby(['Month_Name', 'City'])['Temp_Avg'].mean().unstack()
    month_order = [f'{i:02d}月' for i in range(1, 13)]
    monthly_temp = monthly_temp.reindex(month_order)

    x = np.arange(len(month_order))
    width = 0.15

    for i, city in enumerate(cities):
        offset = (i - len(cities)/2 + 0.5) * width
        axes[1].bar(x + offset, monthly_temp[city],
                   width, label=city, color=colors[i], alpha=0.8)

    axes[1].set_title('月平均溫度比較', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('月份', fontsize=12)
    axes[1].set_ylabel('平均溫度（°C）', fontsize=12)
    axes[1].set_xticks(x)
    axes[1].set_xticklabels(month_order)
    axes[1].legend(loc='upper left', fontsize=11, ncol=5)
    axes[1].grid(True, axis='y', alpha=0.3)

    plt.tight_layout()

    return fig

def plot_rainfall_analysis(df):
    """繪製降雨量分析圖"""
    print("正在繪製降雨量分析圖...")

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('台灣各地降雨量分析（2024年）', fontsize=18, fontweight='bold', y=0.995)

    cities = df['City'].unique()
    colors = plt.cm.Set2(np.linspace(0, 1, len(cities)))

    # 子圖1：累計降雨量趨勢
    for i, city in enumerate(cities):
        city_data = df[df['City'] == city].sort_values('Date')
        cumulative_rainfall = city_data['Rainfall'].cumsum()
        axes[0, 0].plot(city_data['Date'], cumulative_rainfall,
                       label=city, linewidth=2, color=colors[i], alpha=0.8)

    axes[0, 0].set_title('累計降雨量趨勢', fontsize=14, fontweight='bold')
    axes[0, 0].set_xlabel('日期', fontsize=12)
    axes[0, 0].set_ylabel('累計降雨量（mm）', fontsize=12)
    axes[0, 0].legend(loc='upper left', fontsize=11)
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].tick_params(axis='x', rotation=45)

    # 子圖2：月降雨量比較
    monthly_rainfall = df.groupby(['Month_Name', 'City'])['Rainfall'].sum().unstack()
    month_order = [f'{i:02d}月' for i in range(1, 13)]
    monthly_rainfall = monthly_rainfall.reindex(month_order)

    x = np.arange(len(month_order))
    width = 0.15

    for i, city in enumerate(cities):
        offset = (i - len(cities)/2 + 0.5) * width
        axes[0, 1].bar(x + offset, monthly_rainfall[city],
                      width, label=city, color=colors[i], alpha=0.8)

    axes[0, 1].set_title('月降雨量比較', fontsize=14, fontweight='bold')
    axes[0, 1].set_xlabel('月份', fontsize=12)
    axes[0, 1].set_ylabel('降雨量（mm）', fontsize=12)
    axes[0, 1].set_xticks(x)
    axes[0, 1].set_xticklabels(month_order, rotation=45)
    axes[0, 1].legend(loc='upper left', fontsize=9, ncol=5)
    axes[0, 1].grid(True, axis='y', alpha=0.3)

    # 子圖3：總降雨量排行
    total_rainfall = df.groupby('City')['Rainfall'].sum().sort_values(ascending=True)
    colors_bar = plt.cm.Blues(np.linspace(0.4, 0.8, len(total_rainfall)))

    axes[1, 0].barh(total_rainfall.index, total_rainfall.values,
                   color=colors_bar, edgecolor='black', linewidth=1.5)
    axes[1, 0].set_title('年度總降雨量排行', fontsize=14, fontweight='bold')
    axes[1, 0].set_xlabel('總降雨量（mm）', fontsize=12)
    axes[1, 0].grid(True, axis='x', alpha=0.3)

    # 標註數值
    for i, (city, value) in enumerate(total_rainfall.items()):
        axes[1, 0].text(value + 50, i, f'{value:.0f} mm',
                       va='center', fontsize=11, fontweight='bold')

    # 子圖4：季節降雨量比較
    seasonal_rainfall = df.groupby(['Season', 'City'])['Rainfall'].sum().unstack()
    season_order = ['春季', '夏季', '秋季', '冬季']
    seasonal_rainfall = seasonal_rainfall.reindex(season_order)

    x = np.arange(len(season_order))
    width = 0.15

    for i, city in enumerate(cities):
        offset = (i - len(cities)/2 + 0.5) * width
        axes[1, 1].bar(x + offset, seasonal_rainfall[city],
                      width, label=city, color=colors[i], alpha=0.8)

    axes[1, 1].set_title('季節降雨量比較', fontsize=14, fontweight='bold')
    axes[1, 1].set_xlabel('季節', fontsize=12)
    axes[1, 1].set_ylabel('降雨量（mm）', fontsize=12)
    axes[1, 1].set_xticks(x)
    axes[1, 1].set_xticklabels(season_order)
    axes[1, 1].legend(loc='upper left', fontsize=11, ncol=5)
    axes[1, 1].grid(True, axis='y', alpha=0.3)

    plt.tight_layout()

    return fig

def plot_heatmaps(df):
    """繪製熱力圖"""
    print("正在繪製氣象熱力圖...")

    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    fig.suptitle('台灣各地氣象數據熱力圖（月平均）', fontsize=18, fontweight='bold')

    # 準備數據
    month_order = [f'{i:02d}月' for i in range(1, 13)]
    cities = sorted(df['City'].unique())

    # 熱力圖1：平均溫度
    temp_pivot = df.groupby(['Month_Name', 'City'])['Temp_Avg'].mean().unstack()
    temp_pivot = temp_pivot.reindex(month_order)
    temp_pivot = temp_pivot[cities]

    sns.heatmap(temp_pivot.T, annot=True, fmt='.1f', cmap='RdYlBu_r',
               cbar_kws={'label': '溫度（°C）'}, ax=axes[0],
               linewidths=0.5, linecolor='white')
    axes[0].set_title('平均溫度', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('月份', fontsize=12)
    axes[0].set_ylabel('城市', fontsize=12)

    # 熱力圖2：降雨量
    rain_pivot = df.groupby(['Month_Name', 'City'])['Rainfall'].sum().unstack()
    rain_pivot = rain_pivot.reindex(month_order)
    rain_pivot = rain_pivot[cities]

    sns.heatmap(rain_pivot.T, annot=True, fmt='.0f', cmap='Blues',
               cbar_kws={'label': '降雨量（mm）'}, ax=axes[1],
               linewidths=0.5, linecolor='white')
    axes[1].set_title('降雨量', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('月份', fontsize=12)
    axes[1].set_ylabel('', fontsize=12)

    # 熱力圖3：濕度
    humid_pivot = df.groupby(['Month_Name', 'City'])['Humidity'].mean().unstack()
    humid_pivot = humid_pivot.reindex(month_order)
    humid_pivot = humid_pivot[cities]

    sns.heatmap(humid_pivot.T, annot=True, fmt='.0f', cmap='YlGnBu',
               cbar_kws={'label': '濕度（%）'}, ax=axes[2],
               linewidths=0.5, linecolor='white')
    axes[2].set_title('平均濕度', fontsize=14, fontweight='bold')
    axes[2].set_xlabel('月份', fontsize=12)
    axes[2].set_ylabel('', fontsize=12)

    plt.tight_layout()

    return fig

def plot_city_comparison(df):
    """繪製城市綜合比較"""
    print("正在繪製城市綜合比較圖...")

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('台灣城市氣象綜合比較（2024年）', fontsize=18, fontweight='bold', y=0.995)

    cities = sorted(df['City'].unique())
    colors = plt.cm.Set2(np.linspace(0, 1, len(cities)))

    # 子圖1：平均溫度比較
    avg_temps = df.groupby('City')['Temp_Avg'].mean().sort_values(ascending=False)

    axes[0, 0].bar(range(len(avg_temps)), avg_temps.values,
                  color=colors, edgecolor='black', linewidth=1.5, alpha=0.8)
    axes[0, 0].set_xticks(range(len(avg_temps)))
    axes[0, 0].set_xticklabels(avg_temps.index)
    axes[0, 0].set_title('年平均溫度比較', fontsize=14, fontweight='bold')
    axes[0, 0].set_ylabel('平均溫度（°C）', fontsize=12)
    axes[0, 0].grid(True, axis='y', alpha=0.3)

    for i, (city, temp) in enumerate(avg_temps.items()):
        axes[0, 0].text(i, temp + 0.3, f'{temp:.1f}°C',
                       ha='center', fontsize=11, fontweight='bold')

    # 子圖2：溫度變化範圍
    temp_ranges = df.groupby('City').apply(
        lambda x: x['Temp_Max'].max() - x['Temp_Min'].min()
    ).sort_values(ascending=False)

    axes[0, 1].bar(range(len(temp_ranges)), temp_ranges.values,
                  color=colors, edgecolor='black', linewidth=1.5, alpha=0.8)
    axes[0, 1].set_xticks(range(len(temp_ranges)))
    axes[0, 1].set_xticklabels(temp_ranges.index)
    axes[0, 1].set_title('年度溫差範圍', fontsize=14, fontweight='bold')
    axes[0, 1].set_ylabel('溫差（°C）', fontsize=12)
    axes[0, 1].grid(True, axis='y', alpha=0.3)

    for i, (city, temp_range) in enumerate(temp_ranges.items()):
        axes[0, 1].text(i, temp_range + 0.5, f'{temp_range:.1f}°C',
                       ha='center', fontsize=11, fontweight='bold')

    # 子圖3：總降雨量比較
    total_rainfall = df.groupby('City')['Rainfall'].sum().sort_values(ascending=False)

    axes[1, 0].bar(range(len(total_rainfall)), total_rainfall.values,
                  color=colors, edgecolor='black', linewidth=1.5, alpha=0.8)
    axes[1, 0].set_xticks(range(len(total_rainfall)))
    axes[1, 0].set_xticklabels(total_rainfall.index)
    axes[1, 0].set_title('年度總降雨量比較', fontsize=14, fontweight='bold')
    axes[1, 0].set_ylabel('降雨量（mm）', fontsize=12)
    axes[1, 0].grid(True, axis='y', alpha=0.3)

    for i, (city, rain) in enumerate(total_rainfall.items()):
        axes[1, 0].text(i, rain + 50, f'{rain:.0f}',
                       ha='center', fontsize=11, fontweight='bold')

    # 子圖4：平均濕度比較
    avg_humidity = df.groupby('City')['Humidity'].mean().sort_values(ascending=False)

    axes[1, 1].bar(range(len(avg_humidity)), avg_humidity.values,
                  color=colors, edgecolor='black', linewidth=1.5, alpha=0.8)
    axes[1, 1].set_xticks(range(len(avg_humidity)))
    axes[1, 1].set_xticklabels(avg_humidity.index)
    axes[1, 1].set_title('年平均濕度比較', fontsize=14, fontweight='bold')
    axes[1, 1].set_ylabel('濕度（%）', fontsize=12)
    axes[1, 1].grid(True, axis='y', alpha=0.3)

    for i, (city, humid) in enumerate(avg_humidity.items()):
        axes[1, 1].text(i, humid + 1, f'{humid:.1f}%',
                       ha='center', fontsize=11, fontweight='bold')

    plt.tight_layout()

    return fig

def print_statistics(df):
    """輸出統計報告"""
    print("\n" + "="*70)
    print("[報告] 台灣氣象數據分析報告")
    print("="*70)

    cities = sorted(df['City'].unique())

    for city in cities:
        city_data = df[df['City'] == city]

        print(f"\n【{city}】")
        print("-"*70)

        # 溫度統計
        print(f"  溫度統計：")
        print(f"    平均溫度：{city_data['Temp_Avg'].mean():.1f}°C")
        print(f"    最高溫度：{city_data['Temp_Max'].max():.1f}°C")
        print(f"    最低溫度：{city_data['Temp_Min'].min():.1f}°C")
        print(f"    溫度範圍：{city_data['Temp_Max'].max() - city_data['Temp_Min'].min():.1f}°C")

        # 降雨統計
        rainy_days = (city_data['Rainfall'] > 0).sum()
        print(f"\n  降雨統計：")
        print(f"    總降雨量：{city_data['Rainfall'].sum():.1f} mm")
        print(f"    降雨天數：{rainy_days} 天")
        print(f"    平均每次降雨：{city_data[city_data['Rainfall'] > 0]['Rainfall'].mean():.1f} mm")

        # 濕度統計
        print(f"\n  濕度統計：")
        print(f"    平均濕度：{city_data['Humidity'].mean():.1f}%")
        print(f"    最高濕度：{city_data['Humidity'].max():.1f}%")
        print(f"    最低濕度：{city_data['Humidity'].min():.1f}%")

        # 季節統計
        print(f"\n  季節平均溫度：")
        for season in ['春季', '夏季', '秋季', '冬季']:
            season_temp = city_data[city_data['Season'] == season]['Temp_Avg'].mean()
            print(f"    {season}：{season_temp:.1f}°C")

    print("\n" + "="*70)

def save_reports(figures):
    """儲存報表"""
    print("\n正在儲存報表...")

    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 儲存 PNG 圖表
    figure_names = ['溫度趨勢分析', '降雨量分析', '氣象熱力圖', '城市綜合比較']

    for i, fig in enumerate(figures):
        filename = f'{output_dir}/{figure_names[i]}.png'
        fig.savefig(filename, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"[OK] 已儲存：{filename}")

    # 儲存 PDF 報表
    with PdfPages(f'{output_dir}/台灣氣象分析報告.pdf') as pdf:
        for fig in figures:
            pdf.savefig(fig, bbox_inches='tight')
        print(f"[OK] 已儲存：{output_dir}/台灣氣象分析報告.pdf")

    print(f"\n[OK] 所有檔案已儲存至 '{output_dir}' 資料夾")

def main():
    """主程式"""
    print("\n" + "="*70)
    print("  台灣氣象數據視覺化專案")
    print("="*70)

    # 載入數據
    df = load_weather_data()
    if df is None:
        return

    # 繪製圖表
    figures = []

    fig1 = plot_temperature_trends(df)
    figures.append(fig1)

    fig2 = plot_rainfall_analysis(df)
    figures.append(fig2)

    fig3 = plot_heatmaps(df)
    figures.append(fig3)

    fig4 = plot_city_comparison(df)
    figures.append(fig4)

    # 輸出統計報告
    print_statistics(df)

    # 儲存報表
    save_reports(figures)

    # 顯示圖表
    print("\n正在顯示圖表...")
    plt.show()

    print("\n[OK] 分析完成！")
    print("\n提示：請檢查 'output' 資料夾查看所有輸出檔案")

if __name__ == "__main__":
    main()
