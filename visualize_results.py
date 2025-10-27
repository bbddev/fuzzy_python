"""
SCRIPT VẼ BIỂU ĐỒ KẾT QUẢ THỰC NGHIỆM
====================================

Script này đọc file kết quả thực nghiệm và tạo các biểu đồ trực quan
để phân tích và biện minh tính đúng đắn của hệ thống.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from fuzzy_shopping_system import ShoppingTrendFuzzySystem

# Cấu hình font để hiển thị tiếng Việt (nếu cần)
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

# Cấu hình style
sns.set_style("whitegrid")
sns.set_palette("husl")


def load_results():
    """
    Đọc file kết quả thực nghiệm
    """
    try:
        df = pd.read_csv('ket_qua_thuc_nghiem.csv', encoding='utf-8-sig')
        print(f"✓ Đã đọc {len(df)} test case từ file ket_qua_thuc_nghiem.csv")
        return df
    except FileNotFoundError:
        print("✗ Không tìm thấy file ket_qua_thuc_nghiem.csv")
        print("  Vui lòng chạy test_system.py trước!")
        return None


def plot_trend_distribution(df):
    """
    Vẽ biểu đồ phân bố xu hướng mua sắm
    """
    plt.figure(figsize=(10, 6))
    
    trend_counts = df['Xu hướng mua sắm'].value_counts()
    colors = ['#ff6b6b', '#4ecdc4', '#45b7d1']
    
    plt.bar(trend_counts.index, trend_counts.values, color=colors, edgecolor='black', linewidth=1.5)
    plt.title('Phan bo xu huong mua sam', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Xu huong mua sam', fontsize=12, fontweight='bold')
    plt.ylabel('So luong truong hop', fontsize=12, fontweight='bold')
    
    # Thêm giá trị lên trên cột
    for i, (trend, count) in enumerate(trend_counts.items()):
        percentage = (count / len(df)) * 100
        plt.text(i, count + 1, f'{count}\n({percentage:.1f}%)', 
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.tight_layout()
    plt.savefig('bieu_do_1_phan_bo_xu_huong.png', dpi=300, bbox_inches='tight')
    print("✓ Đã tạo: bieu_do_1_phan_bo_xu_huong.png")
    plt.close()


def plot_category_analysis(df):
    """
    Vẽ biểu đồ phân tích theo danh mục sản phẩm
    """
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Biểu đồ 1: Điểm trung bình theo danh mục
    category_means = df.groupby('Danh mục')['Điểm xu hướng'].mean().sort_values(ascending=False)
    colors = ['#ff6b6b', '#4ecdc4', '#45b7d1']
    
    axes[0].bar(category_means.index, category_means.values, color=colors, 
                edgecolor='black', linewidth=1.5)
    axes[0].set_title('Diem trung binh theo danh muc', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Danh muc san pham', fontsize=11, fontweight='bold')
    axes[0].set_ylabel('Diem xu huong trung binh', fontsize=11, fontweight='bold')
    axes[0].grid(axis='y', alpha=0.3, linestyle='--')
    
    for i, (cat, val) in enumerate(category_means.items()):
        axes[0].text(i, val + 1, f'{val:.2f}', ha='center', va='bottom', 
                    fontsize=11, fontweight='bold')
    
    # Biểu đồ 2: Phân bố xu hướng theo danh mục
    category_trend = pd.crosstab(df['Danh mục'], df['Xu hướng mua sắm'])
    category_trend.plot(kind='bar', stacked=False, ax=axes[1], 
                        color=['#ff6b6b', '#4ecdc4', '#45b7d1'],
                        edgecolor='black', linewidth=1.5)
    axes[1].set_title('Phan bo xu huong theo danh muc', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Danh muc san pham', fontsize=11, fontweight='bold')
    axes[1].set_ylabel('So luong', fontsize=11, fontweight='bold')
    axes[1].legend(title='Xu huong', loc='upper right')
    axes[1].grid(axis='y', alpha=0.3, linestyle='--')
    axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=45, ha='right')
    
    plt.tight_layout()
    plt.savefig('bieu_do_2_phan_tich_danh_muc.png', dpi=300, bbox_inches='tight')
    print("✓ Đã tạo: bieu_do_2_phan_tich_danh_muc.png")
    plt.close()


def plot_view_count_impact(df):
    """
    Vẽ biểu đồ ảnh hưởng của số lần xem
    """
    # Lọc dữ liệu: chỉ lấy các test case có discount=50 và category=Thời trang
    df_filtered = df[(df['Chiết khấu (%)'] == 50) & (df['Danh mục'] == 'Thời trang')]
    df_filtered = df_filtered.sort_values('Số lần xem')
    
    plt.figure(figsize=(12, 6))
    
    plt.plot(df_filtered['Số lần xem'], df_filtered['Điểm xu hướng'], 
             marker='o', linewidth=2, markersize=6, color='#4ecdc4', 
             markeredgecolor='black', markeredgewidth=1)
    
    # Vẽ các vùng xu hướng
    plt.axhspan(0, 35, alpha=0.2, color='#ff6b6b', label='Mua it (0-35)')
    plt.axhspan(35, 75, alpha=0.2, color='#4ecdc4', label='Mua vua (35-75)')
    plt.axhspan(75, 100, alpha=0.2, color='#45b7d1', label='Mua nhieu (75-100)')
    
    plt.title('Anh huong cua so lan xem den xu huong mua sam', 
              fontsize=14, fontweight='bold', pad=20)
    plt.xlabel('So lan xem san pham', fontsize=12, fontweight='bold')
    plt.ylabel('Diem xu huong mua sam', fontsize=12, fontweight='bold')
    plt.legend(loc='upper left', fontsize=10)
    plt.grid(True, alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    plt.savefig('bieu_do_3_anh_huong_so_lan_xem.png', dpi=300, bbox_inches='tight')
    print("✓ Đã tạo: bieu_do_3_anh_huong_so_lan_xem.png")
    plt.close()


def plot_discount_impact(df):
    """
    Vẽ biểu đồ ảnh hưởng của mức chiết khấu
    """
    # Lọc dữ liệu: chỉ lấy các test case có view_count=50 và category=Thời trang
    df_filtered = df[(df['Số lần xem'] == 50) & (df['Danh mục'] == 'Thời trang')]
    df_filtered = df_filtered.sort_values('Chiết khấu (%)')
    
    plt.figure(figsize=(12, 6))
    
    plt.plot(df_filtered['Chiết khấu (%)'], df_filtered['Điểm xu hướng'], 
             marker='s', linewidth=2, markersize=6, color='#ff6b6b', 
             markeredgecolor='black', markeredgewidth=1)
    
    # Vẽ các vùng xu hướng
    plt.axhspan(0, 35, alpha=0.2, color='#ff6b6b', label='Mua it (0-35)')
    plt.axhspan(35, 75, alpha=0.2, color='#4ecdc4', label='Mua vua (35-75)')
    plt.axhspan(75, 100, alpha=0.2, color='#45b7d1', label='Mua nhieu (75-100)')
    
    plt.title('Anh huong cua muc chiet khau den xu huong mua sam', 
              fontsize=14, fontweight='bold', pad=20)
    plt.xlabel('Muc chiet khau (%)', fontsize=12, fontweight='bold')
    plt.ylabel('Diem xu huong mua sam', fontsize=12, fontweight='bold')
    plt.legend(loc='upper left', fontsize=10)
    plt.grid(True, alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    plt.savefig('bieu_do_4_anh_huong_chiet_khau.png', dpi=300, bbox_inches='tight')
    print("✓ Đã tạo: bieu_do_4_anh_huong_chiet_khau.png")
    plt.close()


def plot_3d_surface():
    """
    Vẽ biểu đồ bề mặt 3D thể hiện mối quan hệ giữa các biến
    """
    print("\nĐang tạo biểu đồ bề mặt 3D...")
    
    system = ShoppingTrendFuzzySystem()
    
    # Tạo lưới giá trị
    view_range = np.linspace(0, 100, 30)
    discount_range = np.linspace(0, 100, 30)
    
    # Cố định category_score = 5 (Thời trang)
    category_fixed = 5.0
    
    X, Y = np.meshgrid(view_range, discount_range)
    Z = np.zeros_like(X)
    
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Z[i, j] = system.predict(X[i, j], category_fixed, Y[i, j])
    
    fig = plt.figure(figsize=(14, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    surf = ax.plot_surface(X, Y, Z, cmap='coolwarm', alpha=0.8, 
                           edgecolor='none', antialiased=True)
    
    ax.set_xlabel('So lan xem', fontsize=11, fontweight='bold', labelpad=10)
    ax.set_ylabel('Chiet khau (%)', fontsize=11, fontweight='bold', labelpad=10)
    ax.set_zlabel('Diem xu huong', fontsize=11, fontweight='bold', labelpad=10)
    ax.set_title('Be mat 3D: Xu huong mua sam (Danh muc: Thoi trang)', 
                 fontsize=14, fontweight='bold', pad=20)
    
    # Thêm colorbar
    fig.colorbar(surf, shrink=0.5, aspect=5, pad=0.1)
    
    # Điều chỉnh góc nhìn
    ax.view_init(elev=25, azim=45)
    
    plt.tight_layout()
    plt.savefig('bieu_do_5_be_mat_3d.png', dpi=300, bbox_inches='tight')
    print("✓ Đã tạo: bieu_do_5_be_mat_3d.png")
    plt.close()


def plot_heatmap_analysis(df):
    """
    Vẽ heatmap phân tích mối quan hệ giữa các biến
    """
    plt.figure(figsize=(12, 8))
    
    # Tạo pivot table
    # Nhóm dữ liệu theo khoảng để tạo heatmap
    df_copy = df.copy()
    df_copy['View Group'] = pd.cut(df_copy['Số lần xem'], bins=[0, 30, 70, 100], 
                                    labels=['It', 'Trung binh', 'Nhieu'])
    df_copy['Discount Group'] = pd.cut(df_copy['Chiết khấu (%)'], bins=[0, 30, 70, 100], 
                                       labels=['Thap', 'Trung binh', 'Cao'])
    
    # Tạo pivot table
    pivot = df_copy.pivot_table(values='Điểm xu hướng', 
                                 index='View Group', 
                                 columns='Discount Group', 
                                 aggfunc='mean')
    
    sns.heatmap(pivot, annot=True, fmt='.1f', cmap='RdYlGn', 
                cbar_kws={'label': 'Diem xu huong trung binh'},
                linewidths=2, linecolor='black', square=True,
                vmin=0, vmax=100)
    
    plt.title('Heatmap: Diem xu huong theo So lan xem va Chiet khau', 
              fontsize=14, fontweight='bold', pad=20)
    plt.xlabel('Muc chiet khau', fontsize=12, fontweight='bold')
    plt.ylabel('So lan xem', fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('bieu_do_6_heatmap.png', dpi=300, bbox_inches='tight')
    print("✓ Đã tạo: bieu_do_6_heatmap.png")
    plt.close()


def plot_score_distribution(df):
    """
    Vẽ biểu đồ phân bố điểm xu hướng
    """
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Histogram
    axes[0].hist(df['Điểm xu hướng'], bins=20, color='#4ecdc4', 
                edgecolor='black', linewidth=1.5, alpha=0.7)
    axes[0].axvline(35, color='red', linestyle='--', linewidth=2, label='Nguong Mua it/vua')
    axes[0].axvline(75, color='green', linestyle='--', linewidth=2, label='Nguong Mua vua/nhieu')
    axes[0].set_title('Phan bo diem xu huong', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Diem xu huong', fontsize=12, fontweight='bold')
    axes[0].set_ylabel('Tan suat', fontsize=12, fontweight='bold')
    axes[0].legend()
    axes[0].grid(axis='y', alpha=0.3, linestyle='--')
    
    # Box plot theo danh mục
    df_boxplot = df[['Danh mục', 'Điểm xu hướng']]
    categories = df_boxplot['Danh mục'].unique()
    data_to_plot = [df_boxplot[df_boxplot['Danh mục'] == cat]['Điểm xu hướng'].values 
                    for cat in categories]
    
    bp = axes[1].boxplot(data_to_plot, labels=categories, patch_artist=True,
                         boxprops=dict(facecolor='#4ecdc4', alpha=0.7),
                         medianprops=dict(color='red', linewidth=2),
                         whiskerprops=dict(linewidth=1.5),
                         capprops=dict(linewidth=1.5))
    
    axes[1].set_title('Box plot diem xu huong theo danh muc', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Danh muc san pham', fontsize=12, fontweight='bold')
    axes[1].set_ylabel('Diem xu huong', fontsize=12, fontweight='bold')
    axes[1].grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    plt.savefig('bieu_do_7_phan_bo_diem.png', dpi=300, bbox_inches='tight')
    print("✓ Đã tạo: bieu_do_7_phan_bo_diem.png")
    plt.close()


def create_summary_table(df):
    """
    Tạo bảng tổng kết kết quả
    """
    # Tạo bảng thống kê tổng quan
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.axis('tight')
    ax.axis('off')
    
    # Dữ liệu cho bảng
    stats_data = [
        ['Tong so test case', f'{len(df)}'],
        ['', ''],
        ['Phan bo xu huong mua sam:', ''],
        ['  - Mua it', f'{len(df[df["Xu hướng mua sắm"] == "Mua ít"])} ({len(df[df["Xu hướng mua sắm"] == "Mua ít"])/len(df)*100:.1f}%)'],
        ['  - Mua vua', f'{len(df[df["Xu hướng mua sắm"] == "Mua vừa"])} ({len(df[df["Xu hướng mua sắm"] == "Mua vừa"])/len(df)*100:.1f}%)'],
        ['  - Mua nhieu', f'{len(df[df["Xu hướng mua sắm"] == "Mua nhiều"])} ({len(df[df["Xu hướng mua sắm"] == "Mua nhiều"])/len(df)*100:.1f}%)'],
        ['', ''],
        ['Thong ke diem xu huong:', ''],
        ['  - Trung binh', f'{df["Điểm xu hướng"].mean():.2f}'],
        ['  - Thap nhat', f'{df["Điểm xu hướng"].min():.2f}'],
        ['  - Cao nhat', f'{df["Điểm xu hướng"].max():.2f}'],
        ['  - Do lech chuan', f'{df["Điểm xu hướng"].std():.2f}'],
        ['', ''],
        ['Diem trung binh theo danh muc:', ''],
    ]
    
    # Thêm thống kê theo danh mục
    for cat in df['Danh mục'].unique():
        mean_score = df[df['Danh mục'] == cat]['Điểm xu hướng'].mean()
        count = len(df[df['Danh mục'] == cat])
        stats_data.append([f'  - {cat}', f'{mean_score:.2f} (n={count})'])
    
    table = ax.table(cellText=stats_data, cellLoc='left',
                    colWidths=[0.6, 0.4],
                    loc='center', bbox=[0, 0, 1, 1])
    
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 2.5)
    
    # Định dạng bảng
    for i, row in enumerate(stats_data):
        if row[0] != '' and not row[0].startswith('  '):
            for j in range(2):
                table[(i, j)].set_facecolor('#e0e0e0')
                table[(i, j)].set_text_props(weight='bold')
    
    plt.title('BANG TONG KET KET QUA THUC NGHIEM', 
              fontsize=16, fontweight='bold', pad=20)
    
    plt.savefig('bang_tong_ket.png', dpi=300, bbox_inches='tight')
    print("✓ Đã tạo: bang_tong_ket.png")
    plt.close()


def main():
    """
    Hàm chính
    """
    print("\n" + "=" * 80)
    print("TẠO BIỂU ĐỒ KẾT QUẢ THỰC NGHIỆM")
    print("=" * 80 + "\n")
    
    # Đọc dữ liệu
    df = load_results()
    if df is None:
        return
    
    print(f"\n{'='*80}")
    print("BẮT ĐẦU TẠO CÁC BIỂU ĐỒ")
    print(f"{'='*80}\n")
    
    # Tạo các biểu đồ
    plot_trend_distribution(df)
    plot_category_analysis(df)
    plot_view_count_impact(df)
    plot_discount_impact(df)
    plot_3d_surface()
    plot_heatmap_analysis(df)
    plot_score_distribution(df)
    create_summary_table(df)
    
    # Tạo hàm thuộc
    print("\nĐang tạo biểu đồ hàm thuộc...")
    system = ShoppingTrendFuzzySystem()
    system.visualize_membership_functions('bieu_do_0_ham_thuoc.png')
    
    print(f"\n{'='*80}")
    print("✓ ĐÃ HOÀN THÀNH TẠO TẤT CẢ BIỂU ĐỒ")
    print(f"{'='*80}\n")
    
    print("Danh sách các file đã tạo:")
    print("  1. bieu_do_0_ham_thuoc.png - Biểu đồ hàm thuộc")
    print("  2. bieu_do_1_phan_bo_xu_huong.png - Phân bố xu hướng")
    print("  3. bieu_do_2_phan_tich_danh_muc.png - Phân tích theo danh mục")
    print("  4. bieu_do_3_anh_huong_so_lan_xem.png - Ảnh hưởng số lần xem")
    print("  5. bieu_do_4_anh_huong_chiet_khau.png - Ảnh hưởng chiết khấu")
    print("  6. bieu_do_5_be_mat_3d.png - Biểu đồ bề mặt 3D")
    print("  7. bieu_do_6_heatmap.png - Heatmap phân tích")
    print("  8. bieu_do_7_phan_bo_diem.png - Phân bố điểm")
    print("  9. bang_tong_ket.png - Bảng tổng kết kết quả")
    print()


if __name__ == "__main__":
    main()
