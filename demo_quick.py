"""
DEMO NHANH HỆ THỐNG MỜ
======================
File này giúp bạn test nhanh hệ thống với các giá trị tùy chọn
"""

from fuzzy_shopping_system import ShoppingTrendFuzzySystem


def demo_interactive():
    """
    Demo tương tác với người dùng
    """
    print("\n" + "=" * 70)
    print("DEMO TƯƠNG TÁC HỆ THỐNG PHÂN TÍCH XU HƯỚNG MUA SẮM")
    print("=" * 70)
    
    # Khởi tạo hệ thống
    print("\nĐang khởi tạo hệ thống...")
    system = ShoppingTrendFuzzySystem()
    
    print("\n" + "=" * 70)
    print("NHẬP DỮ LIỆU ĐẦU VÀO")
    print("=" * 70)
    
    while True:
        try:
            # Nhập số lần xem
            print("\n1. Nhập số lần xem sản phẩm (0-100):")
            print("   Ví dụ: 10 (ít), 50 (trung bình), 90 (nhiều)")
            view_count = float(input("   Số lần xem: "))
            
            if view_count < 0 or view_count > 100:
                print("   ⚠️  Giá trị phải từ 0 đến 100!")
                continue
            
            # Chọn danh mục
            print("\n2. Chọn danh mục sản phẩm:")
            print("   1 - Nhu yếu phẩm (điểm: 0-4)")
            print("   2 - Thời trang (điểm: 3-7)")
            print("   3 - Điện tử (điểm: 7-10)")
            category_choice = input("   Chọn (1/2/3): ")
            
            if category_choice == '1':
                category_score = 2.0
                category_name = "Nhu yếu phẩm"
            elif category_choice == '2':
                category_score = 5.0
                category_name = "Thời trang"
            elif category_choice == '3':
                category_score = 8.5
                category_name = "Điện tử"
            else:
                print("   ⚠️  Lựa chọn không hợp lệ!")
                continue
            
            # Nhập chiết khấu
            print("\n3. Nhập mức chiết khấu (0-100%):")
            print("   Ví dụ: 10 (thấp), 50 (trung bình), 85 (cao)")
            discount = float(input("   Chiết khấu (%): "))
            
            if discount < 0 or discount > 100:
                print("   ⚠️  Giá trị phải từ 0 đến 100!")
                continue
            
            # Tính toán
            print("\n" + "-" * 70)
            print("ĐANG XỬ LÝ...")
            print("-" * 70)
            
            result = system.predict(view_count, category_score, discount)
            trend = system.interpret_result(result)
            
            # Hiển thị kết quả
            print("\n" + "=" * 70)
            print("KẾT QUẢ PHÂN TÍCH")
            print("=" * 70)
            
            print("\n📊 THÔNG TIN ĐẦU VÀO:")
            print(f"   • Số lần xem sản phẩm: {view_count:.0f}")
            
            if view_count <= 30:
                view_level = "Ít"
            elif view_count <= 70:
                view_level = "Trung bình"
            else:
                view_level = "Nhiều"
            print(f"     → Mức độ: {view_level}")
            
            print(f"\n   • Danh mục sản phẩm: {category_name}")
            print(f"     → Điểm số: {category_score}")
            
            print(f"\n   • Mức chiết khấu: {discount:.0f}%")
            
            if discount <= 30:
                discount_level = "Thấp"
            elif discount <= 70:
                discount_level = "Trung bình"
            else:
                discount_level = "Cao"
            print(f"     → Mức độ: {discount_level}")
            
            print("\n" + "-" * 70)
            print("🎯 KẾT QUẢ DỰ ĐOÁN:")
            print(f"   • Điểm xu hướng mua sắm: {result:.2f}/100")
            print(f"   • Phân loại: {trend}")
            
            # Giải thích kết quả
            print("\n💡 GIẢI THÍCH:")
            if trend == "Mua ít":
                print("   Khách hàng có xu hướng KHÔNG mua hoặc mua rất ít.")
                print("   Đề xuất: Tăng chiết khấu hoặc cải thiện marketing.")
            elif trend == "Mua vừa":
                print("   Khách hàng CÓ THỂ mua, đang cân nhắc.")
                print("   Đề xuất: Tạo thêm ưu đãi hoặc tăng tương tác.")
            else:
                print("   Khách hàng có xu hướng MUA NHIỀU!")
                print("   Đề xuất: Đây là thời điểm tốt để chốt đơn.")
            
            # Phân tích các yếu tố
            print("\n📈 PHÂN TÍCH YẾU TỐ ẢNH HƯỞNG:")
            
            if view_count >= 70:
                print("   ✓ Số lần xem cao → Ảnh hưởng TÍCH CỰC mạnh")
            elif view_count >= 30:
                print("   ~ Số lần xem trung bình → Ảnh hưởng TRUNG LẬP")
            else:
                print("   ✗ Số lần xem thấp → Ảnh hưởng TIÊU CỰC")
            
            if category_name == "Điện tử":
                print("   ✓ Sản phẩm điện tử → Giá trị cao, dễ mua khi có giảm giá")
            elif category_name == "Thời trang":
                print("   ✓ Sản phẩm thời trang → Dễ bị ảnh hưởng bởi xu hướng")
            else:
                print("   ~ Nhu yếu phẩm → Ổn định, ít bị tác động")
            
            if discount >= 70:
                print("   ✓ Chiết khấu cao → Ảnh hưởng TÍCH CỰC mạnh")
            elif discount >= 30:
                print("   ~ Chiết khấu trung bình → Ảnh hưởng VỪA PHẢI")
            else:
                print("   ✗ Chiết khấu thấp → Ít kích thích mua sắm")
            
            print("\n" + "=" * 70)
            
            # Hỏi có tiếp tục không
            print("\nBạn có muốn thử với dữ liệu khác không? (y/n): ", end='')
            choice = input().lower()
            
            if choice != 'y':
                print("\n✓ Cảm ơn bạn đã sử dụng hệ thống!")
                print("=" * 70 + "\n")
                break
                
        except ValueError:
            print("   ⚠️  Vui lòng nhập số hợp lệ!")
        except KeyboardInterrupt:
            print("\n\n✓ Thoát chương trình.")
            print("=" * 70 + "\n")
            break
        except Exception as e:
            print(f"   ⚠️  Lỗi: {e}")


def demo_quick_examples():
    """
    Demo nhanh với các ví dụ có sẵn
    """
    print("\n" + "=" * 70)
    print("DEMO NHANH VỚI CÁC VÍ DỤ CÓ SẴN")
    print("=" * 70)
    
    # Khởi tạo hệ thống
    print("\nĐang khởi tạo hệ thống...")
    system = ShoppingTrendFuzzySystem()
    
    examples = [
        {
            'name': 'Khách hàng không quan tâm',
            'view': 10,
            'category': 2,
            'category_name': 'Nhu yếu phẩm',
            'discount': 10
        },
        {
            'name': 'Khách hàng đang cân nhắc',
            'view': 50,
            'category': 5,
            'category_name': 'Thời trang',
            'discount': 50
        },
        {
            'name': 'Khách hàng sẵn sàng mua',
            'view': 90,
            'category': 8.5,
            'category_name': 'Điện tử',
            'discount': 85
        },
        {
            'name': 'Deal tốt cho thời trang',
            'view': 75,
            'category': 5,
            'category_name': 'Thời trang',
            'discount': 80
        },
        {
            'name': 'Xem nhiều nhưng không giảm giá',
            'view': 85,
            'category': 5,
            'category_name': 'Thời trang',
            'discount': 15
        }
    ]
    
    for i, ex in enumerate(examples, 1):
        print(f"\n{'='*70}")
        print(f"VÍ DỤ {i}: {ex['name']}")
        print(f"{'='*70}")
        
        print(f"\nĐầu vào:")
        print(f"  • Số lần xem: {ex['view']}")
        print(f"  • Danh mục: {ex['category_name']} ({ex['category']})")
        print(f"  • Chiết khấu: {ex['discount']}%")
        
        result = system.predict(ex['view'], ex['category'], ex['discount'])
        trend = system.interpret_result(result)
        
        print(f"\nĐầu ra:")
        print(f"  • Điểm xu hướng: {result:.2f}")
        print(f"  • Kết luận: {trend}")
        
        if trend == "Mua ít":
            print(f"  • Ý nghĩa: Khả năng mua thấp ({result:.1f}%)")
        elif trend == "Mua vừa":
            print(f"  • Ý nghĩa: Có thể mua ({result:.1f}%)")
        else:
            print(f"  • Ý nghĩa: Khả năng mua cao ({result:.1f}%)")
    
    print(f"\n{'='*70}")
    print("✓ HOÀN THÀNH DEMO")
    print(f"{'='*70}\n")


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("CHƯƠNG TRÌNH DEMO HỆ THỐNG MỜ PHÂN TÍCH XU HƯỚNG MUA SẮM")
    print("=" * 70)
    
    print("\nChọn chế độ demo:")
    print("1. Demo với ví dụ có sẵn (nhanh)")
    print("2. Demo tương tác (nhập dữ liệu)")
    print("3. Thoát")
    
    choice = input("\nLựa chọn (1/2/3): ")
    
    if choice == '1':
        demo_quick_examples()
    elif choice == '2':
        demo_interactive()
    elif choice == '3':
        print("\n✓ Tạm biệt!\n")
    else:
        print("\n⚠️  Lựa chọn không hợp lệ!")
        print("Chạy lại chương trình và chọn 1, 2 hoặc 3.\n")
