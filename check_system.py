"""
SCRIPT KIỂM TRA HỆ THỐNG
========================
Chạy file này để kiểm tra xem hệ thống có hoạt động đúng không
"""

import sys


def check_python_version():
    """Kiểm tra phiên bản Python"""
    print("\n1. Kiểm tra phiên bản Python...")
    version = sys.version_info
    print(f"   Phiên bản hiện tại: Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("   ✓ Python version hợp lệ (>=3.8)")
        return True
    else:
        print("   ✗ Cần Python 3.8 trở lên!")
        return False


def check_libraries():
    """Kiểm tra các thư viện cần thiết"""
    print("\n2. Kiểm tra các thư viện...")
    
    required_libs = {
        'numpy': 'NumPy',
        'skfuzzy': 'Scikit-fuzzy',
        'matplotlib': 'Matplotlib',
        'pandas': 'Pandas',
        'seaborn': 'Seaborn'
    }
    
    all_ok = True
    
    for lib_name, display_name in required_libs.items():
        try:
            if lib_name == 'skfuzzy':
                __import__('skfuzzy')
            else:
                __import__(lib_name)
            print(f"   ✓ {display_name} đã cài đặt")
        except ImportError:
            print(f"   ✗ {display_name} chưa cài đặt!")
            print(f"      Chạy: pip install {lib_name if lib_name != 'skfuzzy' else 'scikit-fuzzy'}")
            all_ok = False
    
    return all_ok


def check_fuzzy_system():
    """Kiểm tra hệ thống mờ có chạy được không"""
    print("\n3. Kiểm tra hệ thống mờ...")
    
    try:
        from fuzzy_shopping_system import ShoppingTrendFuzzySystem
        print("   ✓ Import module thành công")
        
        # Thử khởi tạo hệ thống (bỏ output)
        import sys
        import io
        
        # Chuyển output sang null để không in ra
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        
        system = ShoppingTrendFuzzySystem()
        
        # Khôi phục output
        sys.stdout = old_stdout
        
        print("   ✓ Khởi tạo hệ thống thành công")
        
        # Test một dự đoán đơn giản
        result = system.predict(50, 5, 50)
        
        if 0 <= result <= 100:
            print(f"   ✓ Dự đoán hoạt động (kết quả: {result:.2f})")
            return True
        else:
            print(f"   ✗ Kết quả bất thường: {result}")
            return False
            
    except Exception as e:
        print(f"   ✗ Lỗi: {e}")
        return False


def check_test_script():
    """Kiểm tra script test có chạy được không"""
    print("\n4. Kiểm tra script test...")
    
    try:
        # Chỉ kiểm tra import, không chạy test
        import test_system
        print("   ✓ File test_system.py hợp lệ")
        return True
    except Exception as e:
        print(f"   ✗ Lỗi trong test_system.py: {e}")
        return False


def check_visualize_script():
    """Kiểm tra script vẽ biểu đồ"""
    print("\n5. Kiểm tra script visualize...")
    
    try:
        import visualize_results
        print("   ✓ File visualize_results.py hợp lệ")
        return True
    except Exception as e:
        print(f"   ✗ Lỗi trong visualize_results.py: {e}")
        return False


def run_quick_test():
    """Chạy test nhanh với một số giá trị"""
    print("\n6. Chạy test nhanh...")
    
    try:
        import sys
        import io
        from fuzzy_shopping_system import ShoppingTrendFuzzySystem
        
        # Tắt output khi khởi tạo
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        system = ShoppingTrendFuzzySystem()
        sys.stdout = old_stdout
        
        test_cases = [
            (10, 2, 10),    # Nên cho kết quả thấp
            (50, 5, 50),    # Nên cho kết quả trung bình
            (90, 9, 90),    # Nên cho kết quả cao
        ]
        
        all_passed = True
        
        for i, (view, cat, disc) in enumerate(test_cases, 1):
            result = system.predict(view, cat, disc)
            trend = system.interpret_result(result)
            
            print(f"   Test {i}: view={view}, cat={cat}, disc={disc}")
            print(f"           → Kết quả: {result:.2f} ({trend})")
            
            # Kiểm tra logic cơ bản
            if i == 1 and result >= 50:
                print(f"           ⚠️  Cảnh báo: Kết quả cao bất thường cho input thấp")
                all_passed = False
            elif i == 3 and result <= 50:
                print(f"           ⚠️  Cảnh báo: Kết quả thấp bất thường cho input cao")
                all_passed = False
        
        if all_passed:
            print("   ✓ Tất cả test đều hợp lý")
        
        return all_passed
        
    except Exception as e:
        print(f"   ✗ Lỗi khi chạy test: {e}")
        return False


def main():
    """Hàm chính"""
    print("=" * 70)
    print("KIỂM TRA HỆ THỐNG MỜ PHÂN TÍCH XU HƯỚNG MUA SẮM")
    print("=" * 70)
    
    results = []
    
    # Chạy các kiểm tra
    results.append(("Python version", check_python_version()))
    results.append(("Thư viện", check_libraries()))
    results.append(("Hệ thống mờ", check_fuzzy_system()))
    results.append(("Script test", check_test_script()))
    results.append(("Script visualize", check_visualize_script()))
    results.append(("Test nhanh", run_quick_test()))
    
    # Tổng kết
    print("\n" + "=" * 70)
    print("KẾT QUẢ KIỂM TRA")
    print("=" * 70)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print(f"\nĐã pass: {passed}/{total} kiểm tra")
    
    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"  {status} - {name}")
    
    print("\n" + "-" * 70)
    
    if passed == total:
        print("🎉 TẤT CẢ KIỂM TRA ĐỀU PASS!")
        print("Hệ thống sẵn sàng để sử dụng.")
        print("\nBước tiếp theo:")
        print("  1. Chạy: python fuzzy_shopping_system.py")
        print("  2. Chạy: python test_system.py")
        print("  3. Chạy: python visualize_results.py")
    elif passed >= total * 0.7:
        print("⚠️  HỆ THỐNG CÓ THỂ HOẠT ĐỘNG")
        print("Một số kiểm tra fail nhưng không nghiêm trọng.")
        print("Bạn có thể thử chạy các script chính.")
    else:
        print("❌ HỆ THỐNG CÓ VẤN ĐỀ")
        print("Cần khắc phục các lỗi trước khi tiếp tục.")
        print("\nGợi ý:")
        print("  1. Kiểm tra lại Python version")
        print("  2. Cài đặt lại thư viện: pip install -r requirements.txt")
        print("  3. Đọc kỹ thông báo lỗi ở trên")
    
    print("=" * 70 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n✓ Đã dừng kiểm tra.")
    except Exception as e:
        print(f"\n\n✗ Lỗi nghiêm trọng: {e}")
        import traceback
        traceback.print_exc()
