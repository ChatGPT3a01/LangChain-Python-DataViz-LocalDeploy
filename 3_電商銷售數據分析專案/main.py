"""
電商銷售數據分析專案
===================================
本程式模擬並分析電商銷售數據，產生視覺化儀表板和報表。

功能：
1. 生成 2026 年全年的模擬電商數據
2. 分析訂單數、營收、新客戶、回購率等指標
3. 產生綜合視覺化儀表板（2x2 子圖）
4. 輸出統計摘要報告
5. 儲存高解析度圖表和 PDF 報表
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
import os

# 設定中文字型（解決中文亂碼問題）
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Arial Unicode MS', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

def generate_sales_data():
    """
    生成模擬電商銷售數據

    Returns:
        DataFrame: 包含日期、訂單數、營收、新客戶、回購率等欄位的數據
    """
    print("正在生成模擬電商數據...")
    np.random.seed(42)

    # 建立日期範圍：2026 年全年
    dates = pd.date_range('2026-01-01', '2026-12-31', freq='D')

    # 模擬數據（加入季節性變化）
    seasonal_factor = np.sin(np.arange(len(dates)) * 2 * np.pi / 365)

    data = {
        '日期': dates,
        '訂單數': np.random.poisson(50, len(dates)) + (seasonal_factor * 20).astype(int),
        '營收': (np.random.normal(15000, 3000, len(dates)) + seasonal_factor * 5000).astype(int),
        '新客戶': np.random.poisson(20, len(dates)),
        '回購率': np.random.uniform(0.3, 0.6, len(dates))
    }

    df = pd.DataFrame(data)
    df['訂單數'] = df['訂單數'].clip(lower=0)  # 確保沒有負值
    df['營收'] = df['營收'].clip(lower=0)
    df['月份'] = df['日期'].dt.month

    # 計算 30 日移動平均
    df['營收_MA30'] = df['營收'].rolling(window=30).mean()

    print(f"[OK] 數據生成完成！共 {len(df)} 筆記錄")
    return df

def create_dashboard(df):
    """
    建立綜合視覺化儀表板

    Args:
        df (DataFrame): 銷售數據

    Returns:
        Figure: Matplotlib 圖形物件
    """
    print("\n正在建立視覺化儀表板...")

    # 建立 2x2 子圖佈局
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('電商銷售數據分析儀表板（2026 年）', fontsize=20, fontweight='bold', y=0.995)

    # 子圖 1：營收趨勢線（左上）
    axes[0, 0].plot(df['日期'], df['營收'], color='#3498db', linewidth=1.5, alpha=0.7, label='每日營收')
    axes[0, 0].plot(df['日期'], df['營收_MA30'], color='red', linewidth=2.5, label='30 日移動平均')
    axes[0, 0].set_title('每日營收趨勢', fontsize=14, fontweight='bold')
    axes[0, 0].set_xlabel('日期', fontsize=11)
    axes[0, 0].set_ylabel('營收（元）', fontsize=11)
    axes[0, 0].legend(fontsize=10, loc='upper left')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].tick_params(axis='x', rotation=45)

    # 子圖 2：月度訂單數長條圖（右上）
    monthly_orders = df.groupby('月份')['訂單數'].sum()
    colors_bar = ['#FF6B6B' if x == monthly_orders.max() else '#4ECDC4' for x in monthly_orders]
    axes[0, 1].bar(monthly_orders.index, monthly_orders.values, color=colors_bar, edgecolor='black', linewidth=1)
    axes[0, 1].set_title('月度總訂單數', fontsize=14, fontweight='bold')
    axes[0, 1].set_xlabel('月份', fontsize=11)
    axes[0, 1].set_ylabel('訂單數', fontsize=11)
    axes[0, 1].set_xticks(range(1, 13))
    axes[0, 1].grid(True, axis='y', alpha=0.3)

    # 在最高的長條上標註
    max_month = monthly_orders.idxmax()
    max_value = monthly_orders.max()
    axes[0, 1].text(max_month, max_value + 50, f'最高：{max_value}',
                    ha='center', fontsize=10, fontweight='bold', color='#FF6B6B')

    # 子圖 3：回購率分佈直方圖（左下）
    axes[1, 0].hist(df['回購率'], bins=30, color='#9b59b6', edgecolor='black', alpha=0.7)
    mean_rate = df['回購率'].mean()
    axes[1, 0].axvline(mean_rate, color='red', linestyle='--', linewidth=2,
                       label=f"平均回購率: {mean_rate:.2%}")
    axes[1, 0].set_title('回購率分佈', fontsize=14, fontweight='bold')
    axes[1, 0].set_xlabel('回購率', fontsize=11)
    axes[1, 0].set_ylabel('天數', fontsize=11)
    axes[1, 0].legend(fontsize=10)
    axes[1, 0].grid(True, axis='y', alpha=0.3)

    # 子圖 4：新客戶與訂單數散佈圖（右下）
    scatter = axes[1, 1].scatter(df['新客戶'], df['訂單數'],
                                c=df['月份'], cmap='viridis',
                                s=50, alpha=0.6, edgecolors='black', linewidth=0.5)
    axes[1, 1].set_title('新客戶數 vs 訂單數', fontsize=14, fontweight='bold')
    axes[1, 1].set_xlabel('新客戶數', fontsize=11)
    axes[1, 1].set_ylabel('訂單數', fontsize=11)
    axes[1, 1].grid(True, alpha=0.3)
    cbar = plt.colorbar(scatter, ax=axes[1, 1])
    cbar.set_label('月份', fontsize=10)

    # 自動調整佈局
    plt.tight_layout()

    print("[OK] 儀表板建立完成！")
    return fig

def print_statistics(df):
    """
    輸出統計摘要報告

    Args:
        df (DataFrame): 銷售數據
    """
    print("\n" + "="*50)
    print("[統計] 2026 年銷售統計摘要")
    print("="*50)
    print(f"總營收：          ${df['營收'].sum():,} 元")
    print(f"平均日營收：      ${df['營收'].mean():.0f} 元")
    print(f"最高日營收：      ${df['營收'].max():,} 元")
    print(f"最低日營收：      ${df['營收'].min():,} 元")
    print("-"*50)
    print(f"總訂單數：        {df['訂單數'].sum():,} 筆")
    print(f"平均日訂單數：    {df['訂單數'].mean():.0f} 筆")
    print(f"最高日訂單數：    {df['訂單數'].max()} 筆")
    print("-"*50)
    print(f"總新客戶：        {df['新客戶'].sum():,} 人")
    print(f"平均日新客戶：    {df['新客戶'].mean():.1f} 人")
    print(f"平均回購率：      {df['回購率'].mean():.2%}")
    print(f"最高回購率：      {df['回購率'].max():.2%}")
    print(f"最低回購率：      {df['回購率'].min():.2%}")
    print("="*50)

    # 找出營收最高的月份
    monthly_revenue = df.groupby('月份')['營收'].sum()
    best_month = monthly_revenue.idxmax()
    print(f"\n[最佳] 營收最佳月份：{best_month} 月（${monthly_revenue[best_month]:,} 元）")

def save_outputs(fig, df):
    """
    儲存輸出檔案

    Args:
        fig (Figure): Matplotlib 圖形物件
        df (DataFrame): 銷售數據
    """
    print("\n正在儲存輸出檔案...")

    # 建立 output 資料夾
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 1. 儲存高解析度 PNG 圖片
    fig.savefig(f'{output_dir}/銷售儀表板.png',
                dpi=300,
                bbox_inches='tight',
                facecolor='white')
    print(f"[OK] 已儲存：{output_dir}/銷售儀表板.png")

    # 2. 儲存 CSV 數據
    df.to_csv(f'{output_dir}/銷售數據.csv', index=False, encoding='utf-8-sig')
    print(f"[OK] 已儲存：{output_dir}/銷售數據.csv")

    # 3. 建立多頁 PDF 報表
    with PdfPages(f'{output_dir}/銷售分析報告.pdf') as pdf:
        # 第一頁：儀表板
        pdf.savefig(fig, bbox_inches='tight')

        # 第二頁：月度詳細分析
        fig2, axes2 = plt.subplots(2, 1, figsize=(11, 8.5))

        # 月度營收
        monthly_revenue = df.groupby('月份')['營收'].sum()
        axes2[0].bar(monthly_revenue.index, monthly_revenue.values,
                     color='#3498db', edgecolor='black', linewidth=1.5)
        axes2[0].set_title('月度總營收', fontsize=16, fontweight='bold')
        axes2[0].set_xlabel('月份', fontsize=12)
        axes2[0].set_ylabel('營收（元）', fontsize=12)
        axes2[0].set_xticks(range(1, 13))
        axes2[0].grid(True, axis='y', alpha=0.3)

        # 月度新客戶
        monthly_customers = df.groupby('月份')['新客戶'].sum()
        axes2[1].plot(monthly_customers.index, monthly_customers.values,
                      marker='o', linewidth=2, markersize=8, color='#2ecc71')
        axes2[1].set_title('月度新客戶數', fontsize=16, fontweight='bold')
        axes2[1].set_xlabel('月份', fontsize=12)
        axes2[1].set_ylabel('新客戶數', fontsize=12)
        axes2[1].set_xticks(range(1, 13))
        axes2[1].grid(True, alpha=0.3)

        plt.tight_layout()
        pdf.savefig(fig2, bbox_inches='tight')
        plt.close(fig2)

        # 設定 PDF 元數據
        d = pdf.infodict()
        d['Title'] = '電商銷售數據分析報告'
        d['Author'] = 'Python 資料分析系統'
        d['Subject'] = '2026 年度銷售數據統計'
        d['CreationDate'] = pd.Timestamp.now()

    print(f"[OK] 已儲存：{output_dir}/銷售分析報告.pdf")
    print(f"\n[完成] 所有檔案已儲存至 '{output_dir}' 資料夾")

def main():
    """主程式"""
    print("\n" + "="*50)
    print("  電商銷售數據分析專案")
    print("="*50)

    # 1. 生成數據
    df = generate_sales_data()

    # 2. 建立儀表板
    fig = create_dashboard(df)

    # 3. 輸出統計報告
    print_statistics(df)

    # 4. 儲存輸出檔案
    save_outputs(fig, df)

    # 5. 顯示圖表
    print("\n正在顯示視覺化儀表板...")
    plt.show()

    print("\n[完成] 程式執行完成！")
    print("\n提示：請檢查 'output' 資料夾查看所有輸出檔案")

if __name__ == "__main__":
    main()
