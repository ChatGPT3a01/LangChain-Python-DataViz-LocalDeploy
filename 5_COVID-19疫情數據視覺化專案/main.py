"""
COVID-19 疫情數據視覺化專案
===================================
本程式從網路載入真實的 COVID-19 疫情數據，進行資料處理與視覺化分析。

功能：
1. 從 GitHub 載入 Johns Hopkins 大學的 COVID-19 數據
2. 資料清洗與轉置處理
3. 分析全球主要國家的確診趨勢
4. 計算移動平均線
5. 產生時間序列比較圖表
6. 輸出視覺化報表和統計摘要
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
import os
from datetime import datetime

# 設定中文字型（解決中文亂碼問題）
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Arial Unicode MS', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# 全球主要國家列表（用於分析）
COUNTRIES = ['Taiwan*', 'US', 'United Kingdom', 'Japan', 'Korea, South',
             'Germany', 'France', 'Italy', 'Spain', 'India']

# 國家名稱中英對照
COUNTRY_NAMES = {
    'Taiwan*': '台灣',
    'US': '美國',
    'United Kingdom': '英國',
    'Japan': '日本',
    'Korea, South': '南韓',
    'Germany': '德國',
    'France': '法國',
    'Italy': '義大利',
    'Spain': '西班牙',
    'India': '印度'
}

def load_covid_data(use_sample=False, use_local=True):
    """
    載入 COVID-19 疫情數據

    Args:
        use_sample (bool): 是否使用範例數據（當無法連線時）
        use_local (bool): 是否優先使用本地數據檔案（預設：True）

    Returns:
        DataFrame: 疫情數據
    """
    print("正在載入 COVID-19 疫情數據...")

    # 優先載入本地數據檔案
    local_file = 'data/covid19_confirmed_global.csv'
    if use_local and os.path.exists(local_file):
        try:
            print(f"→ 使用本地數據檔案：{local_file}")
            df = pd.read_csv(local_file)
            print(f"[OK] 本地數據載入成功！共 {len(df)} 個國家/地區的記錄")
            print("  （無需網路連線）")
            return df
        except Exception as e:
            print(f"✗ 本地數據載入失敗：{e}")
            print("→ 嘗試從網路載入...")

    if use_sample:
        # 使用模擬數據（當無法連線網路時）
        print("⚠ 使用模擬數據模式")
        return generate_sample_data()

    try:
        # 從 Johns Hopkins 大學的 GitHub 儲存庫載入數據
        print("→ 從網路載入數據...")
        url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

        df = pd.read_csv(url)
        print(f"[OK] 線上數據載入成功！共 {len(df)} 個國家/地區的記錄")
        return df

    except Exception as e:
        print(f"✗ 無法載入線上數據：{e}")
        print("→ 切換到模擬數據模式")
        return generate_sample_data()

def generate_sample_data():
    """
    生成模擬的疫情數據（當無法連線網路時使用）

    Returns:
        DataFrame: 模擬疫情數據
    """
    np.random.seed(42)

    # 建立日期範圍（2020-01-22 到 2026-12-31）
    dates = pd.date_range('2020-01-22', '2026-12-31', freq='D')
    date_columns = [d.strftime('%-m/%-d/%y') if os.name != 'nt' else d.strftime('%#m/%#d/%y') for d in dates]

    # 建立基礎 DataFrame
    data = {
        'Province/State': [''] * len(COUNTRIES),
        'Country/Region': COUNTRIES,
        'Lat': [0] * len(COUNTRIES),
        'Long': [0] * len(COUNTRIES)
    }

    # 為每個國家生成模擬的累計確診數據
    for i, date_col in enumerate(date_columns):
        # 使用指數增長 + 隨機噪音模擬疫情發展
        growth_factor = np.exp(i / 100) - 1
        noise = np.random.normal(0, growth_factor * 0.1, len(COUNTRIES))

        # 不同國家有不同的基數
        base_values = np.array([100, 10000, 5000, 1000, 800, 3000, 4000, 3500, 3000, 5000])
        data[date_col] = (base_values * growth_factor + noise * 1000).clip(min=0).astype(int)

    df = pd.DataFrame(data)
    print(f"[OK] 模擬數據生成完成！共 {len(df)} 個國家的記錄")
    return df

def process_data(df):
    """
    處理和清洗疫情數據

    Args:
        df (DataFrame): 原始數據

    Returns:
        DataFrame: 處理後的數據（轉置格式，日期為索引）
    """
    print("\n正在處理數據...")

    # 選擇目標國家
    df_filtered = df[df['Country/Region'].isin(COUNTRIES)].copy()

    # 合併同一國家的多個地區數據
    df_grouped = df_filtered.groupby('Country/Region').sum(numeric_only=True)

    # 轉置數據：將日期從欄位轉為列索引
    df_transposed = df_grouped.T

    # 將索引轉換為日期格式
    df_transposed.index = pd.to_datetime(df_transposed.index, format='%m/%d/%y', errors='coerce')

    # 移除索引為 NaT 的行
    df_transposed = df_transposed[df_transposed.index.notna()]

    # 移除可能的空值
    df_transposed = df_transposed.dropna()

    # 重新命名欄位為中文
    df_transposed.columns = [COUNTRY_NAMES.get(c, c) for c in df_transposed.columns]

    print(f"[OK] 數據處理完成！")
    print(f"  - 時間範圍：{df_transposed.index[0].strftime('%Y-%m-%d')} 至 {df_transposed.index[-1].strftime('%Y-%m-%d')}")
    print(f"  - 國家數量：{len(df_transposed.columns)}")

    return df_transposed

def calculate_daily_cases(df):
    """
    計算每日新增確診數（從累計數據計算）

    Args:
        df (DataFrame): 累計確診數據

    Returns:
        DataFrame: 每日新增確診數據
    """
    df_daily = df.diff().fillna(0)
    df_daily[df_daily < 0] = 0  # 移除負值（可能的數據修正）
    return df_daily

def calculate_moving_average(df, window=7):
    """
    計算移動平均線

    Args:
        df (DataFrame): 原始數據
        window (int): 移動平均視窗大小（天數）

    Returns:
        DataFrame: 移動平均數據
    """
    return df.rolling(window=window).mean()

def create_visualizations(df_cumulative, df_daily, df_ma):
    """
    建立視覺化圖表

    Args:
        df_cumulative (DataFrame): 累計確診數據
        df_daily (DataFrame): 每日新增確診數據
        df_ma (DataFrame): 移動平均數據

    Returns:
        Figure: Matplotlib 圖形物件
    """
    print("\n正在建立視覺化圖表...")

    # 建立 2x2 子圖佈局
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('COVID-19 全球疫情數據分析', fontsize=20, fontweight='bold', y=0.995)

    # 顏色配置
    colors = plt.cm.tab10(np.linspace(0, 1, len(df_cumulative.columns)))

    # 子圖 1：累計確診數（左上）
    for i, country in enumerate(df_cumulative.columns):
        axes[0, 0].plot(df_cumulative.index, df_cumulative[country],
                       label=country, linewidth=2, color=colors[i], alpha=0.8)

    axes[0, 0].set_title('累計確診數趨勢', fontsize=14, fontweight='bold')
    axes[0, 0].set_xlabel('日期', fontsize=11)
    axes[0, 0].set_ylabel('累計確診數', fontsize=11)
    axes[0, 0].legend(loc='upper left', fontsize=9, ncol=2)
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].tick_params(axis='x', rotation=45)

    # 子圖 2：前五名國家累計確診數（右上）
    top5_countries = df_cumulative.iloc[-1].nlargest(5).index
    for country in top5_countries:
        axes[0, 1].plot(df_cumulative.index, df_cumulative[country],
                       label=country, linewidth=2.5, alpha=0.8)

    axes[0, 1].set_title('前五名國家累計確診數', fontsize=14, fontweight='bold')
    axes[0, 1].set_xlabel('日期', fontsize=11)
    axes[0, 1].set_ylabel('累計確診數', fontsize=11)
    axes[0, 1].legend(loc='upper left', fontsize=10)
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].tick_params(axis='x', rotation=45)

    # 子圖 3：每日新增確診數（7日移動平均）（左下）
    for i, country in enumerate(['台灣', '美國', '日本', '南韓']):
        if country in df_ma.columns:
            axes[1, 0].plot(df_ma.index, df_ma[country],
                           label=f'{country}（7日均）', linewidth=2, alpha=0.8)

    axes[1, 0].set_title('每日新增確診數（7日移動平均）', fontsize=14, fontweight='bold')
    axes[1, 0].set_xlabel('日期', fontsize=11)
    axes[1, 0].set_ylabel('新增確診數', fontsize=11)
    axes[1, 0].legend(loc='upper left', fontsize=10)
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].tick_params(axis='x', rotation=45)

    # 子圖 4：最終累計確診數排行（右下）
    final_counts = df_cumulative.iloc[-1].sort_values(ascending=True)
    colors_bar = plt.cm.viridis(np.linspace(0.3, 0.9, len(final_counts)))

    axes[1, 1].barh(final_counts.index, final_counts.values,
                    color=colors_bar, edgecolor='black', linewidth=1)
    axes[1, 1].set_title(f'累計確診數排行（截至 {df_cumulative.index[-1].strftime("%Y-%m-%d")}）',
                        fontsize=14, fontweight='bold')
    axes[1, 1].set_xlabel('累計確診數', fontsize=11)
    axes[1, 1].grid(True, axis='x', alpha=0.3)

    # 在長條上標註數值
    for i, (country, value) in enumerate(final_counts.items()):
        axes[1, 1].text(value, i, f' {value:,.0f}',
                       va='center', fontsize=9, fontweight='bold')

    plt.tight_layout()
    print("[OK] 視覺化圖表建立完成！")

    return fig

def print_statistics(df_cumulative, df_daily):
    """
    輸出統計摘要報告

    Args:
        df_cumulative (DataFrame): 累計確診數據
        df_daily (DataFrame): 每日新增確診數據
    """
    print("\n" + "="*60)
    print("[統計] COVID-19 疫情統計摘要")
    print("="*60)
    print(f"數據時間範圍：{df_cumulative.index[0].strftime('%Y-%m-%d')} 至 {df_cumulative.index[-1].strftime('%Y-%m-%d')}")
    print(f"數據天數：{len(df_cumulative)} 天")
    print("-"*60)

    # 最終累計確診數排行
    final_counts = df_cumulative.iloc[-1].sort_values(ascending=False)
    print("\n[排行] 累計確診數排行（前 5 名）：")
    for i, (country, count) in enumerate(final_counts.head(5).items(), 1):
        print(f"  {i}. {country}：{count:,.0f} 例")

    # 最高單日新增
    print("\n[最高] 最高單日新增確診數：")
    for country in final_counts.head(5).index:
        max_daily = df_daily[country].max()
        max_date = df_daily[country].idxmax()
        print(f"  {country}：{max_daily:,.0f} 例（{max_date.strftime('%Y-%m-%d')}）")

    # 台灣數據
    if '台灣' in df_cumulative.columns:
        print("\n[台灣] 台灣疫情數據：")
        print(f"  累計確診：{df_cumulative['台灣'].iloc[-1]:,.0f} 例")
        print(f"  最高單日新增：{df_daily['台灣'].max():,.0f} 例")
        print(f"  最高單日新增日期：{df_daily['台灣'].idxmax().strftime('%Y-%m-%d')}")

    print("="*60)

def save_outputs(fig, df_cumulative, df_daily):
    """
    儲存輸出檔案

    Args:
        fig (Figure): Matplotlib 圖形物件
        df_cumulative (DataFrame): 累計確診數據
        df_daily (DataFrame): 每日新增確診數據
    """
    print("\n正在儲存輸出檔案...")

    # 建立 output 資料夾
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 1. 儲存高解析度 PNG 圖片
    fig.savefig(f'{output_dir}/COVID-19疫情分析圖表.png',
                dpi=300,
                bbox_inches='tight',
                facecolor='white')
    print(f"[OK] 已儲存：{output_dir}/COVID-19疫情分析圖表.png")

    # 2. 儲存 CSV 數據
    df_cumulative.to_csv(f'{output_dir}/累計確診數據.csv', encoding='utf-8-sig')
    df_daily.to_csv(f'{output_dir}/每日新增數據.csv', encoding='utf-8-sig')
    print(f"[OK] 已儲存：{output_dir}/累計確診數據.csv")
    print(f"[OK] 已儲存：{output_dir}/每日新增數據.csv")

    # 3. 建立 PDF 報表
    with PdfPages(f'{output_dir}/COVID-19疫情分析報告.pdf') as pdf:
        pdf.savefig(fig, bbox_inches='tight')

        # 設定 PDF 元數據
        d = pdf.infodict()
        d['Title'] = 'COVID-19 疫情數據分析報告'
        d['Author'] = 'Python 資料分析系統'
        d['Subject'] = '全球疫情趨勢統計'
        d['CreationDate'] = datetime.now()

    print(f"[OK] 已儲存：{output_dir}/COVID-19疫情分析報告.pdf")
    print(f"\n[完成] 所有檔案已儲存至 '{output_dir}' 資料夾")

def main():
    """主程式"""
    print("\n" + "="*60)
    print("  COVID-19 疫情數據視覺化專案")
    print("="*60)

    # 1. 載入數據
    use_sample = False  # 設定為 True 使用模擬數據
    df_raw = load_covid_data(use_sample=use_sample)

    # 2. 處理數據
    df_cumulative = process_data(df_raw)

    # 3. 計算衍生指標
    df_daily = calculate_daily_cases(df_cumulative)
    df_ma = calculate_moving_average(df_daily, window=7)

    # 4. 建立視覺化
    fig = create_visualizations(df_cumulative, df_daily, df_ma)

    # 5. 輸出統計報告
    print_statistics(df_cumulative, df_daily)

    # 6. 儲存輸出檔案
    save_outputs(fig, df_cumulative, df_daily)

    # 7. 顯示圖表
    print("\n正在顯示視覺化圖表...")
    plt.show()

    print("\n[完成] 程式執行完成！")
    print("\n提示：請檢查 'output' 資料夾查看所有輸出檔案")
    print("\n[提示] 小提示：")
    print("  - 如果無法連線網路，程式會自動使用模擬數據")
    print("  - 可在程式中設定 use_sample=True 強制使用模擬數據")

if __name__ == "__main__":
    main()
