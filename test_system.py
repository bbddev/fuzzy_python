"""
SCRIPT THỰC NGHIỆM HỆ THỐNG MỜ PHÂN TÍCH XU HƯỚNG MUA SẮM
=======================================================

Script này thực hiện các thực nghiệm toàn diện để kiểm tra
tính đúng đắn của hệ thống mờ đã xây dựng.

Kết quả sẽ được lưu vào file CSV để phân tích và tạo biểu đồ.
"""

import numpy as np
import pandas as pd
from fuzzy_shopping_system import ShoppingTrendFuzzySystem
import time


def run_comprehensive_tests():
    """
    Chạy các test toàn diện với nhiều trường hợp khác nhau
    """
    print("\n" + "=" * 80)
    print("BẮT ĐẦU THỰC NGHIỆM HỆ THỐNG")
    print("=" * 80)
    
    # Khởi tạo hệ thống
    print("\nĐang khởi tạo hệ thống...")
    system = ShoppingTrendFuzzySystem()
    
    # Danh sách các test case
    test_cases = []
    
    print("\n" + "-" * 80)
    print("PHẦN 1: KIỂM TRA CÁC TRƯỜNG HỢP BIÊN (BOUNDARY CASES)")
    print("-" * 80)
    
    # 1. Các trường hợp biên
    boundary_cases = [
        # Trường hợp 1: Tất cả giá trị thấp nhất
        {"view_count": 0, "category_score": 0, "discount": 0, 
         "description": "Tất cả giá trị thấp nhất"},
        
        # Trường hợp 2: Tất cả giá trị cao nhất
        {"view_count": 100, "category_score": 10, "discount": 100, 
         "description": "Tất cả giá trị cao nhất"},
        
        # Trường hợp 3: Xem nhiều nhưng không giảm giá
        {"view_count": 100, "category_score": 5, "discount": 0, 
         "description": "Xem nhiều nhưng không giảm giá"},
        
        # Trường hợp 4: Xem ít nhưng giảm giá cao
        {"view_count": 0, "category_score": 5, "discount": 100, 
         "description": "Xem ít nhưng giảm giá cao"},
    ]
    
    for i, case in enumerate(boundary_cases, 1):
        print(f"\nTest {i}: {case['description']}")
        result = system.predict(case['view_count'], case['category_score'], case['discount'])
        trend = system.interpret_result(result)
        category = system.get_category_name(case['category_score'])
        
        print(f"  Input: Xem={case['view_count']}, Danh mục={category}, Giảm giá={case['discount']}%")
        print(f"  Output: Điểm={result:.2f}, Xu hướng={trend}")
        
        test_cases.append({
            'STT': len(test_cases) + 1,
            'Mô tả': case['description'],
            'Số lần xem': case['view_count'],
            'Danh mục': category,
            'Điểm danh mục': case['category_score'],
            'Chiết khấu (%)': case['discount'],
            'Điểm xu hướng': round(result, 2),
            'Xu hướng mua sắm': trend
        })
    
    print("\n" + "-" * 80)
    print("PHẦN 2: KIỂM TRA THEO TỪNG DANH MỤC SẢN PHẨM")
    print("-" * 80)
    
    # 2. Kiểm tra theo danh mục sản phẩm
    categories = [
        {"score": 1.5, "name": "Nhu yếu phẩm"},
        {"score": 5.0, "name": "Thời trang"},
        {"score": 8.5, "name": "Điện tử"}
    ]
    
    view_levels = [15, 50, 85]
    discount_levels = [15, 50, 85]
    
    for cat in categories:
        print(f"\n--- Danh mục: {cat['name']} ---")
        for view in view_levels:
            for discount in discount_levels:
                result = system.predict(view, cat['score'], discount)
                trend = system.interpret_result(result)
                
                desc = f"{cat['name']}: Xem {get_level_name(view)}, Giảm giá {get_level_name(discount)}"
                
                print(f"  Xem={view}, Giảm giá={discount}% → Điểm={result:.2f}, Xu hướng={trend}")
                
                test_cases.append({
                    'STT': len(test_cases) + 1,
                    'Mô tả': desc,
                    'Số lần xem': view,
                    'Danh mục': cat['name'],
                    'Điểm danh mục': cat['score'],
                    'Chiết khấu (%)': discount,
                    'Điểm xu hướng': round(result, 2),
                    'Xu hướng mua sắm': trend
                })
    
    print("\n" + "-" * 80)
    print("PHẦN 3: KIỂM TRA ẢNH HƯỞNG CỦA SỐ LẦN XEM")
    print("-" * 80)
    
    # 3. Kiểm tra ảnh hưởng của số lần xem (giữ các biến khác cố định)
    print("\nCố định: Danh mục=Thời trang (5.0), Giảm giá=50%")
    for view in range(0, 101, 10):
        result = system.predict(view, 5.0, 50)
        trend = system.interpret_result(result)
        
        desc = f"Ảnh hưởng số lần xem: {view}"
        
        if view % 20 == 0:
            print(f"  Xem={view} → Điểm={result:.2f}, Xu hướng={trend}")
        
        test_cases.append({
            'STT': len(test_cases) + 1,
            'Mô tả': desc,
            'Số lần xem': view,
            'Danh mục': 'Thời trang',
            'Điểm danh mục': 5.0,
            'Chiết khấu (%)': 50,
            'Điểm xu hướng': round(result, 2),
            'Xu hướng mua sắm': trend
        })
    
    print("\n" + "-" * 80)
    print("PHẦN 4: KIỂM TRA ẢNH HƯỞNG CỦA MỨC CHIẾT KHẤU")
    print("-" * 80)
    
    # 4. Kiểm tra ảnh hưởng của mức chiết khấu
    print("\nCố định: Số lần xem=50, Danh mục=Thời trang (5.0)")
    for discount in range(0, 101, 10):
        result = system.predict(50, 5.0, discount)
        trend = system.interpret_result(result)
        
        desc = f"Ảnh hưởng chiết khấu: {discount}%"
        
        if discount % 20 == 0:
            print(f"  Giảm giá={discount}% → Điểm={result:.2f}, Xu hướng={trend}")
        
        test_cases.append({
            'STT': len(test_cases) + 1,
            'Mô tả': desc,
            'Số lần xem': 50,
            'Danh mục': 'Thời trang',
            'Điểm danh mục': 5.0,
            'Chiết khấu (%)': discount,
            'Điểm xu hướng': round(result, 2),
            'Xu hướng mua sắm': trend
        })
    
    print("\n" + "-" * 80)
    print("PHẦN 5: KIỂM TRA CÁC TRƯỜNG HỢP THỰC TÊ")
    print("-" * 80)
    
    # 5. Các trường hợp thực tế
    realistic_cases = [
        {
            'view_count': 5, 'category_score': 2, 'discount': 5,
            'description': 'Người dùng ít quan tâm, nhu yếu phẩm, giảm giá thấp'
        },
        {
            'view_count': 25, 'category_score': 5, 'discount': 30,
            'description': 'Người dùng quan tâm vừa, thời trang, giảm giá trung bình'
        },
        {
            'view_count': 95, 'category_score': 9, 'discount': 85,
            'description': 'Người dùng rất quan tâm, điện tử, giảm giá cao'
        },
        {
            'view_count': 70, 'category_score': 6.5, 'discount': 60,
            'description': 'Người dùng quan tâm nhiều, thời trang/điện tử, giảm giá khá'
        },
        {
            'view_count': 40, 'category_score': 3, 'discount': 25,
            'description': 'Người dùng quan tâm vừa, nhu yếu phẩm, giảm giá thấp-trung bình'
        },
        {
            'view_count': 88, 'category_score': 4.5, 'discount': 75,
            'description': 'Người dùng quan tâm nhiều, thời trang, giảm giá cao'
        },
        {
            'view_count': 12, 'category_score': 8, 'discount': 15,
            'description': 'Người dùng ít quan tâm, điện tử, giảm giá thấp'
        },
        {
            'view_count': 55, 'category_score': 1.5, 'discount': 40,
            'description': 'Người dùng quan tâm vừa-nhiều, nhu yếu phẩm, giảm giá trung bình'
        },
    ]
    
    for i, case in enumerate(realistic_cases, 1):
        result = system.predict(case['view_count'], case['category_score'], case['discount'])
        trend = system.interpret_result(result)
        category = system.get_category_name(case['category_score'])
        
        print(f"\nTrường hợp {i}: {case['description']}")
        print(f"  Input: Xem={case['view_count']}, Danh mục={category}, Giảm giá={case['discount']}%")
        print(f"  Output: Điểm={result:.2f}, Xu hướng={trend}")
        
        test_cases.append({
            'STT': len(test_cases) + 1,
            'Mô tả': case['description'],
            'Số lần xem': case['view_count'],
            'Danh mục': category,
            'Điểm danh mục': case['category_score'],
            'Chiết khấu (%)': case['discount'],
            'Điểm xu hướng': round(result, 2),
            'Xu hướng mua sắm': trend
        })
    
    # Tạo DataFrame và lưu kết quả
    df = pd.DataFrame(test_cases)
    
    # Lưu ra file CSV
    csv_filename = 'ket_qua_thuc_nghiem.csv'
    df.to_csv(csv_filename, index=False, encoding='utf-8-sig')
    
    print("\n" + "=" * 80)
    print("KẾT QUẢ THỰC NGHIỆM")
    print("=" * 80)
    print(f"\nTổng số test case: {len(test_cases)}")
    print(f"Đã lưu kết quả vào file: {csv_filename}")
    
    # Thống kê kết quả
    print("\n--- THỐNG KÊ KẾT QUẢ ---")
    trend_counts = df['Xu hướng mua sắm'].value_counts()
    print("\nPhân bố xu hướng mua sắm:")
    for trend, count in trend_counts.items():
        percentage = (count / len(test_cases)) * 100
        print(f"  {trend}: {count} trường hợp ({percentage:.1f}%)")
    
    print("\nThống kê điểm xu hướng:")
    print(f"  Điểm trung bình: {df['Điểm xu hướng'].mean():.2f}")
    print(f"  Điểm thấp nhất: {df['Điểm xu hướng'].min():.2f}")
    print(f"  Điểm cao nhất: {df['Điểm xu hướng'].max():.2f}")
    print(f"  Độ lệch chuẩn: {df['Điểm xu hướng'].std():.2f}")
    
    # Phân tích theo danh mục
    print("\nĐiểm trung bình theo danh mục:")
    category_stats = df.groupby('Danh mục')['Điểm xu hướng'].agg(['mean', 'count'])
    for category, row in category_stats.iterrows():
        print(f"  {category}: {row['mean']:.2f} (n={int(row['count'])})")
    
    print("\n" + "=" * 80)
    print("✓ HOÀN THÀNH THỰC NGHIỆM")
    print("=" * 80 + "\n")
    
    return df


def get_level_name(value):
    """
    Chuyển đổi giá trị số thành mức độ
    """
    if value <= 30:
        return "thấp"
    elif value <= 70:
        return "trung bình"
    else:
        return "cao"


if __name__ == "__main__":
    start_time = time.time()
    df_results = run_comprehensive_tests()
    end_time = time.time()
    
    print(f"Thời gian thực hiện: {end_time - start_time:.2f} giây")
    print("\nBước tiếp theo: Chạy 'python visualize_results.py' để tạo biểu đồ")
