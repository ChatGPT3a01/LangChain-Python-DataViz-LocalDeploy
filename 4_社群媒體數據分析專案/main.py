"""
社群媒體數據分析專案
===================
分析多個社群媒體平台的數據，包含粉絲成長、互動率、貼文表現等

功能：
1. 載入多平台社群媒體數據
2. 分析粉絲成長趨勢
3. 計算互動率和表現指標
4. 平台間比較分析
5. 產生視覺化圖表和報表
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import os
import warnings
warnings.filterwarnings('ignore')

# 設定中文字型
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Arial Unicode MS', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# 定義平台列表
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

def load_social_media_data():
    """載入所有平台的社群媒體數據"""
    print("正在載入社群媒體數據...")
    
    data_file = 'data/all_social_media_data.csv'
    
    if not os.path.exists(data_file):
        print(f"✗ 找不到數據檔案：{data_file}")
        print("請先執行 generate_local_data.py 生成數據")
        return None
    
    df = pd.read_csv(data_file)
    df['Date'] = pd.to_datetime(df['Date'])

    print(f"[OK] 數據載入成功！")
    print(f"  時間範圍：{df['Date'].min().strftime('%Y-%m-%d')} 至 {df['Date'].max().strftime('%Y-%m-%d')}")
    print(f"  平台數量：{df['Platform'].nunique()} 個")
    print(f"  總數據筆數：{len(df)} 筆")
    
    return df

def calculate_growth_metrics(df):
    """計算成長指標"""
    print("\n正在計算成長指標...")
    
    growth_data = []
    
    for platform in PLATFORMS:
        platform_df = df[df['Platform'] == platform].copy()
        platform_df = platform_df.sort_values('Date')
        
        # 計算總成長率
        initial_followers = platform_df['Followers'].iloc[0]
        final_followers = platform_df['Followers'].iloc[-1]
        total_growth = ((final_followers - initial_followers) / initial_followers) * 100
        
        # 計算平均每日成長
        avg_daily_growth = platform_df['Followers'].pct_change().mean() * 100
        
        # 計算平均互動率
        avg_engagement_rate = platform_df['Engagement_Rate'].mean() * 100
        
        # 計算總互動數
        total_engagement = platform_df['Total_Engagement'].sum()
        
        # 計算平均每日貼文數
        avg_posts = platform_df['Posts'].mean()
        
        growth_data.append({
            'Platform': platform,
            'Initial_Followers': initial_followers,
            'Final_Followers': final_followers,
            'Total_Growth_Percent': total_growth,
            'Avg_Daily_Growth_Percent': avg_daily_growth,
            'Avg_Engagement_Rate': avg_engagement_rate,
            'Total_Engagement': total_engagement,
            'Avg_Posts_Per_Day': avg_posts
        })
    
    growth_df = pd.DataFrame(growth_data)
    print("[OK] 成長指標計算完成！")

    return growth_df

def create_visualizations(df, growth_df):
    """建立視覺化圖表"""
    print("\n正在建立視覺化圖表...")
    
    # 建立 2x2 子圖佈局
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('社群媒體數據分析儀表板', fontsize=20, fontweight='bold', y=0.995)
    
    # 顏色配置
    colors = plt.cm.Set3(np.linspace(0, 0.8, len(PLATFORMS)))
    color_map = dict(zip(PLATFORMS, colors))
    
    # 子圖 1：粉絲數成長趨勢（左上）
    for platform in PLATFORMS:
        platform_df = df[df['Platform'] == platform].sort_values('Date')
        axes[0, 0].plot(platform_df['Date'], platform_df['Followers'],
                       label=platform, linewidth=2.5, color=color_map[platform], alpha=0.8)
    
    axes[0, 0].set_title('粉絲數成長趨勢', fontsize=14, fontweight='bold')
    axes[0, 0].set_xlabel('日期', fontsize=11)
    axes[0, 0].set_ylabel('粉絲數', fontsize=11)
    axes[0, 0].legend(loc='upper left', fontsize=9, ncol=2)
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].tick_params(axis='x', rotation=45)
    axes[0, 0].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1000:.0f}K'))
    
    # 子圖 2：總成長率比較（右上）
    growth_sorted = growth_df.sort_values('Total_Growth_Percent', ascending=True)
    colors_bar = [color_map[p] for p in growth_sorted['Platform']]
    
    axes[0, 1].barh(growth_sorted['Platform'], growth_sorted['Total_Growth_Percent'],
                    color=colors_bar, edgecolor='black', linewidth=1, alpha=0.8)
    axes[0, 1].set_title('總成長率比較（%）', fontsize=14, fontweight='bold')
    axes[0, 1].set_xlabel('成長率（%）', fontsize=11)
    axes[0, 1].grid(True, axis='x', alpha=0.3)
    
    # 在長條上標註數值
    for i, (platform, value) in enumerate(zip(growth_sorted['Platform'], growth_sorted['Total_Growth_Percent'])):
        axes[0, 1].text(value, i, f' {value:.1f}%',
                       va='center', fontsize=9, fontweight='bold')
    
    # 子圖 3：平均互動率比較（左下）
    engagement_sorted = growth_df.sort_values('Avg_Engagement_Rate', ascending=True)
    colors_bar2 = [color_map[p] for p in engagement_sorted['Platform']]
    
    axes[1, 0].barh(engagement_sorted['Platform'], engagement_sorted['Avg_Engagement_Rate'],
                    color=colors_bar2, edgecolor='black', linewidth=1, alpha=0.8)
    axes[1, 0].set_title('平均互動率比較（%）', fontsize=14, fontweight='bold')
    axes[1, 0].set_xlabel('互動率（%）', fontsize=11)
    axes[1, 0].grid(True, axis='x', alpha=0.3)
    
    # 在長條上標註數值
    for i, (platform, value) in enumerate(zip(engagement_sorted['Platform'], engagement_sorted['Avg_Engagement_Rate'])):
        axes[1, 0].text(value, i, f' {value:.2f}%',
                       va='center', fontsize=9, fontweight='bold')
    
    # 子圖 4：總互動數 vs 平均每日貼文數（右下）
    scatter_colors = [color_map[p] for p in growth_df['Platform']]
    
    scatter = axes[1, 1].scatter(growth_df['Avg_Posts_Per_Day'], growth_df['Total_Engagement'],
                                s=growth_df['Final_Followers']/100,  # 大小代表粉絲數
                                c=scatter_colors, alpha=0.6, edgecolors='black', linewidth=1.5)
    
    # 標註平台名稱
    for i, row in growth_df.iterrows():
        axes[1, 1].annotate(row['Platform'],
                           (row['Avg_Posts_Per_Day'], row['Total_Engagement']),
                           fontsize=9, ha='center', va='bottom')
    
    axes[1, 1].set_title('貼文頻率 vs 總互動數', fontsize=14, fontweight='bold')
    axes[1, 1].set_xlabel('平均每日貼文數', fontsize=11)
    axes[1, 1].set_ylabel('總互動數', fontsize=11)
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1000:.0f}K'))
    
    plt.tight_layout()
    print("[OK] 視覺化圖表建立完成！")

    return fig

def create_detailed_analysis(df):
    """建立詳細分析圖表"""
    print("\n正在建立詳細分析圖表...")
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('社群媒體詳細分析', fontsize=20, fontweight='bold', y=0.995)
    
    colors = plt.cm.Set3(np.linspace(0, 0.8, len(PLATFORMS)))
    color_map = dict(zip(PLATFORMS, colors))
    
    # 子圖 1：互動數趨勢（左上）
    for platform in PLATFORMS:
        platform_df = df[df['Platform'] == platform].sort_values('Date')
        # 計算7日移動平均
        platform_df['MA7_Engagement'] = platform_df['Total_Engagement'].rolling(window=7).mean()
        axes[0, 0].plot(platform_df['Date'], platform_df['MA7_Engagement'],
                       label=platform, linewidth=2, color=color_map[platform], alpha=0.8)
    
    axes[0, 0].set_title('總互動數趨勢（7日移動平均）', fontsize=14, fontweight='bold')
    axes[0, 0].set_xlabel('日期', fontsize=11)
    axes[0, 0].set_ylabel('互動數', fontsize=11)
    axes[0, 0].legend(loc='upper left', fontsize=9, ncol=2)
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # 子圖 2：最終粉絲數排行（右上）
    final_followers = df.groupby('Platform')['Followers'].last().sort_values(ascending=True)
    colors_bar = [color_map[p] for p in final_followers.index]
    
    axes[0, 1].barh(final_followers.index, final_followers.values,
                    color=colors_bar, edgecolor='black', linewidth=1, alpha=0.8)
    axes[0, 1].set_title('最終粉絲數排行', fontsize=14, fontweight='bold')
    axes[0, 1].set_xlabel('粉絲數', fontsize=11)
    axes[0, 1].grid(True, axis='x', alpha=0.3)
    axes[0, 1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1000:.0f}K'))
    
    for i, (platform, value) in enumerate(final_followers.items()):
        axes[0, 1].text(value, i, f' {value:,.0f}',
                       va='center', fontsize=9, fontweight='bold')
    
    # 子圖 3：按讚、分享、留言分佈（左下）- 改用堆疊長條圖
    engagement_types = df.groupby('Platform')[['Likes', 'Shares', 'Comments']].sum()

    # 使用堆疊長條圖
    engagement_types.plot(kind='bar', stacked=True, ax=axes[1, 0],
                         color=['#87CEEB', '#98D8C8', '#FFB6C1'],
                         alpha=0.85, edgecolor='black', linewidth=0.8)

    axes[1, 0].set_title('互動類型分佈', fontsize=14, fontweight='bold')
    axes[1, 0].set_xlabel('平台', fontsize=11)
    axes[1, 0].set_ylabel('總數', fontsize=11)
    axes[1, 0].set_xticklabels(PLATFORMS, rotation=45, ha='right')
    axes[1, 0].legend(['按讚', '分享', '留言'], fontsize=10, loc='upper left')
    axes[1, 0].grid(True, axis='y', alpha=0.3)
    axes[1, 0].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1000:.0f}K'))
    
    # 子圖 4：平均每日貼文數（右下）
    avg_posts = df.groupby('Platform')['Posts'].mean().sort_values(ascending=True)
    colors_bar3 = [color_map[p] for p in avg_posts.index]
    
    axes[1, 1].barh(avg_posts.index, avg_posts.values,
                    color=colors_bar3, edgecolor='black', linewidth=1, alpha=0.8)
    axes[1, 1].set_title('平均每日貼文數', fontsize=14, fontweight='bold')
    axes[1, 1].set_xlabel('貼文數', fontsize=11)
    axes[1, 1].grid(True, axis='x', alpha=0.3)
    
    for i, (platform, value) in enumerate(avg_posts.items()):
        axes[1, 1].text(value, i, f' {value:.2f}',
                       va='center', fontsize=9, fontweight='bold')
    
    plt.tight_layout()
    print("[OK] 詳細分析圖表建立完成！")

    return fig

def print_statistics(df, growth_df):
    """輸出統計摘要報告"""
    print("\n" + "="*70)
    print("[報告] 社群媒體數據分析報告")
    print("="*70)
    print(f"數據時間範圍：{df['Date'].min().strftime('%Y-%m-%d')} 至 {df['Date'].max().strftime('%Y-%m-%d')}")
    print(f"數據天數：{df['Date'].nunique()} 天")
    print(f"分析平台數：{len(PLATFORMS)} 個")
    print("-"*70)
    
    # 各平台統計
    print("\n[總覽] 各平台表現總覽：")
    print("-"*70)
    
    for _, row in growth_df.iterrows():
        platform = row['Platform']
        print(f"\n【{platform}】")
        print(f"  初始粉絲數：{row['Initial_Followers']:,}")
        print(f"  最終粉絲數：{row['Final_Followers']:,}")
        print(f"  總成長率：{row['Total_Growth_Percent']:.2f}%")
        print(f"  平均每日成長：{row['Avg_Daily_Growth_Percent']:.3f}%")
        print(f"  平均互動率：{row['Avg_Engagement_Rate']:.2f}%")
        print(f"  總互動數：{row['Total_Engagement']:,}")
        print(f"  平均每日貼文：{row['Avg_Posts_Per_Day']:.2f} 篇")
    
    # 排行榜
    print("\n" + "="*70)
    print("[排行榜] 各項排名")
    print("="*70)

    # 粉絲數排行
    top_followers = growth_df.nlargest(3, 'Final_Followers')
    print("\n[第1名] 粉絲數前三名：")
    for i, (_, row) in enumerate(top_followers.iterrows(), 1):
        print(f"  {i}. {row['Platform']}：{row['Final_Followers']:,} 粉絲")

    # 成長率排行
    top_growth = growth_df.nlargest(3, 'Total_Growth_Percent')
    print("\n[第2名] 成長率前三名：")
    for i, (_, row) in enumerate(top_growth.iterrows(), 1):
        print(f"  {i}. {row['Platform']}：{row['Total_Growth_Percent']:.2f}%")

    # 互動率排行
    top_engagement = growth_df.nlargest(3, 'Avg_Engagement_Rate')
    print("\n[第3名] 互動率前三名：")
    for i, (_, row) in enumerate(top_engagement.iterrows(), 1):
        print(f"  {i}. {row['Platform']}：{row['Avg_Engagement_Rate']:.2f}%")
    
    print("\n" + "="*70)

def save_outputs(fig1, fig2, df, growth_df):
    """儲存輸出檔案"""
    print("\n正在儲存輸出檔案...")
    
    # 建立 output 資料夾
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 1. 儲存高解析度 PNG 圖片
    fig1.savefig(f'{output_dir}/社群媒體分析儀表板.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    print(f"[OK] 已儲存：{output_dir}/社群媒體分析儀表板.png")

    fig2.savefig(f'{output_dir}/社群媒體詳細分析.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    print(f"[OK] 已儲存：{output_dir}/社群媒體詳細分析.png")

    # 2. 儲存 CSV 數據
    df.to_csv(f'{output_dir}/社群媒體原始數據.csv', index=False, encoding='utf-8-sig')
    growth_df.to_csv(f'{output_dir}/社群媒體成長指標.csv', index=False, encoding='utf-8-sig')
    print(f"[OK] 已儲存：{output_dir}/社群媒體原始數據.csv")
    print(f"[OK] 已儲存：{output_dir}/社群媒體成長指標.csv")
    
    # 3. 建立 PDF 報表
    with PdfPages(f'{output_dir}/社群媒體分析報告.pdf') as pdf:
        pdf.savefig(fig1, bbox_inches='tight')
        pdf.savefig(fig2, bbox_inches='tight')
        
        # 設定 PDF 元數據
        d = pdf.infodict()
        d['Title'] = '社群媒體數據分析報告'
        d['Author'] = 'Python 資料分析系統'
        d['Subject'] = '多平台社群媒體表現分析'
        from datetime import datetime
        d['CreationDate'] = datetime.now()

    print(f"[OK] 已儲存：{output_dir}/社群媒體分析報告.pdf")
    print(f"\n[OK] 所有檔案已儲存至 '{output_dir}' 資料夾")

def main():
    """主程式"""
    print("\n" + "="*70)
    print("  社群媒體數據分析專案")
    print("="*70)
    
    # 1. 載入數據
    df = load_social_media_data()
    if df is None:
        return
    
    # 2. 計算成長指標
    growth_df = calculate_growth_metrics(df)
    
    # 3. 建立視覺化
    fig1 = create_visualizations(df, growth_df)
    fig2 = create_detailed_analysis(df)
    
    # 4. 輸出統計報告
    print_statistics(df, growth_df)
    
    # 5. 儲存輸出檔案
    save_outputs(fig1, fig2, df, growth_df)
    
    # 6. 顯示圖表
    print("\n正在顯示視覺化圖表...")
    plt.show()

    print("\n[完成] 程式執行完成！")
    print("\n提示：請檢查 'output' 資料夾查看所有輸出檔案")

if __name__ == "__main__":
    main()

