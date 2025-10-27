"""
HỆ THỐNG PHÂN TÍCH XU HƯỚNG MUA SẮM DỰA TRÊN LOGIC MỜ
=====================================

Mô tả:
    Hệ thống sử dụng logic mờ để phân tích xu hướng mua sắm của người dùng
    dựa trên 3 yếu tố đầu vào:
    1. Số lần xem sản phẩm
    2. Danh mục sản phẩm yêu thích
    3. Mức chiết khấu được cung cấp
    
    Đầu ra: Xu hướng mua sắm (mua ít, mua vừa, mua nhiều)

Tác giả: [Tên sinh viên]
Ngày: [Ngày nộp bài]
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

class ShoppingTrendFuzzySystem:
    """
    Lớp hệ thống mờ phân tích xu hướng mua sắm
    """
    
    def __init__(self):
        """
        Khởi tạo hệ thống mờ với các biến và luật
        """
        print("=" * 70)
        print("KHỞI TẠO HỆ THỐNG MỜ PHÂN TÍCH XU HƯỚNG MUA SẮM")
        print("=" * 70)
        
        # Định nghĩa các biến ngôn ngữ (Antecedents - Đầu vào)
        self._define_input_variables()
        
        # Định nghĩa biến đầu ra (Consequent)
        self._define_output_variable()
        
        # Định nghĩa các hàm thuộc (membership functions)
        self._define_membership_functions()
        
        # Thiết lập các luật mờ (fuzzy rules)
        self._define_fuzzy_rules()
        
        # Tạo hệ thống điều khiển
        self._create_control_system()
        
        print("\n✓ Hệ thống mờ đã được khởi tạo thành công!")
        print("=" * 70)
    
    def _define_input_variables(self):
        """
        Định nghĩa các biến đầu vào
        """
        print("\n1. ĐỊNH NGHĨA CÁC BIẾN ĐẦU VÀO:")
        
        # Biến 1: Số lần xem sản phẩm (0-100 lần)
        self.view_count = ctrl.Antecedent(np.arange(0, 101, 1), 'view_count')
        print("   - Số lần xem sản phẩm: 0-100 lần")
        
        # Biến 2: Điểm số danh mục yêu thích (0-10 điểm)
        # 0-3: Nhu yếu phẩm, 3-7: Thời trang, 7-10: Điện tử
        self.category_score = ctrl.Antecedent(np.arange(0, 11, 0.1), 'category_score')
        print("   - Điểm danh mục yêu thích: 0-10")
        print("     + 0-3: Nhu yếu phẩm")
        print("     + 3-7: Thời trang")
        print("     + 7-10: Điện tử")
        
        # Biến 3: Mức chiết khấu (0-100%)
        self.discount = ctrl.Antecedent(np.arange(0, 101, 1), 'discount')
        print("   - Mức chiết khấu: 0-100%")
    
    def _define_output_variable(self):
        """
        Định nghĩa biến đầu ra
        """
        print("\n2. ĐỊNH NGHĨA BIẾN ĐẦU RA:")
        
        # Biến đầu ra: Xu hướng mua sắm (0-100 điểm)
        # 0-30: Mua ít, 30-70: Mua vừa, 70-100: Mua nhiều
        self.shopping_trend = ctrl.Consequent(np.arange(0, 101, 1), 'shopping_trend')
        print("   - Xu hướng mua sắm: 0-100 điểm")
        print("     + 0-30: Mua ít")
        print("     + 30-70: Mua vừa")
        print("     + 70-100: Mua nhiều")
    
    def _define_membership_functions(self):
        """
        Định nghĩa các hàm thuộc cho mỗi biến
        """
        print("\n3. ĐỊNH NGHĨA CÁC HÀM THUỘC (MEMBERSHIP FUNCTIONS):")
        
        # Hàm thuộc cho Số lần xem sản phẩm
        print("\n   a) Số lần xem sản phẩm:")
        self.view_count['low'] = fuzz.trimf(self.view_count.universe, [0, 0, 40])
        self.view_count['medium'] = fuzz.trimf(self.view_count.universe, [20, 50, 80])
        self.view_count['high'] = fuzz.trimf(self.view_count.universe, [60, 100, 100])
        print("      - Ít: [0, 0, 40]")
        print("      - Trung bình: [20, 50, 80]")
        print("      - Nhiều: [60, 100, 100]")
        
        # Hàm thuộc cho Danh mục sản phẩm
        print("\n   b) Danh mục sản phẩm yêu thích:")
        self.category_score['necessities'] = fuzz.trimf(self.category_score.universe, [0, 0, 4])
        self.category_score['fashion'] = fuzz.trimf(self.category_score.universe, [2, 5, 8])
        self.category_score['electronics'] = fuzz.trimf(self.category_score.universe, [6, 10, 10])
        print("      - Nhu yếu phẩm: [0, 0, 4]")
        print("      - Thời trang: [2, 5, 8]")
        print("      - Điện tử: [6, 10, 10]")
        
        # Hàm thuộc cho Mức chiết khấu
        print("\n   c) Mức chiết khấu:")
        self.discount['low'] = fuzz.trimf(self.discount.universe, [0, 0, 30])
        self.discount['medium'] = fuzz.trimf(self.discount.universe, [20, 50, 80])
        self.discount['high'] = fuzz.trimf(self.discount.universe, [70, 100, 100])
        print("      - Thấp: [0, 0, 30]")
        print("      - Trung bình: [20, 50, 80]")
        print("      - Cao: [70, 100, 100]")
        
        # Hàm thuộc cho Xu hướng mua sắm (đầu ra)
        print("\n   d) Xu hướng mua sắm (Đầu ra):")
        self.shopping_trend['low'] = fuzz.trimf(self.shopping_trend.universe, [0, 0, 35])
        self.shopping_trend['medium'] = fuzz.trimf(self.shopping_trend.universe, [25, 50, 75])
        self.shopping_trend['high'] = fuzz.trimf(self.shopping_trend.universe, [65, 100, 100])
        print("      - Mua ít: [0, 0, 35]")
        print("      - Mua vừa: [25, 50, 75]")
        print("      - Mua nhiều: [65, 100, 100]")
    
    def _define_fuzzy_rules(self):
        """
        Định nghĩa các luật mờ (Fuzzy Rules)
        """
        print("\n4. ĐỊNH NGHĨA CÁC LUẬT MỜ (FUZZY RULES):")
        print("   Tổng số: 27 luật (3x3x3)")
        
        self.rules = []
        
        # Nhóm 1: Số lần xem ÍT
        print("\n   Nhóm 1: Số lần xem ÍT")
        # Rule 1
        rule1 = ctrl.Rule(
            self.view_count['low'] & self.category_score['necessities'] & self.discount['low'],
            self.shopping_trend['low']
        )
        self.rules.append(rule1)
        print("   R1: Xem ít + Nhu yếu phẩm + Giảm giá thấp → Mua ít")
        
        # Rule 2
        rule2 = ctrl.Rule(
            self.view_count['low'] & self.category_score['necessities'] & self.discount['medium'],
            self.shopping_trend['low']
        )
        self.rules.append(rule2)
        print("   R2: Xem ít + Nhu yếu phẩm + Giảm giá TB → Mua ít")
        
        # Rule 3
        rule3 = ctrl.Rule(
            self.view_count['low'] & self.category_score['necessities'] & self.discount['high'],
            self.shopping_trend['medium']
        )
        self.rules.append(rule3)
        print("   R3: Xem ít + Nhu yếu phẩm + Giảm giá cao → Mua vừa")
        
        # Rule 4
        rule4 = ctrl.Rule(
            self.view_count['low'] & self.category_score['fashion'] & self.discount['low'],
            self.shopping_trend['low']
        )
        self.rules.append(rule4)
        print("   R4: Xem ít + Thời trang + Giảm giá thấp → Mua ít")
        
        # Rule 5
        rule5 = ctrl.Rule(
            self.view_count['low'] & self.category_score['fashion'] & self.discount['medium'],
            self.shopping_trend['low']
        )
        self.rules.append(rule5)
        print("   R5: Xem ít + Thời trang + Giảm giá TB → Mua ít")
        
        # Rule 6
        rule6 = ctrl.Rule(
            self.view_count['low'] & self.category_score['fashion'] & self.discount['high'],
            self.shopping_trend['medium']
        )
        self.rules.append(rule6)
        print("   R6: Xem ít + Thời trang + Giảm giá cao → Mua vừa")
        
        # Rule 7
        rule7 = ctrl.Rule(
            self.view_count['low'] & self.category_score['electronics'] & self.discount['low'],
            self.shopping_trend['low']
        )
        self.rules.append(rule7)
        print("   R7: Xem ít + Điện tử + Giảm giá thấp → Mua ít")
        
        # Rule 8
        rule8 = ctrl.Rule(
            self.view_count['low'] & self.category_score['electronics'] & self.discount['medium'],
            self.shopping_trend['medium']
        )
        self.rules.append(rule8)
        print("   R8: Xem ít + Điện tử + Giảm giá TB → Mua vừa")
        
        # Rule 9
        rule9 = ctrl.Rule(
            self.view_count['low'] & self.category_score['electronics'] & self.discount['high'],
            self.shopping_trend['medium']
        )
        self.rules.append(rule9)
        print("   R9: Xem ít + Điện tử + Giảm giá cao → Mua vừa")
        
        # Nhóm 2: Số lần xem TRUNG BÌNH
        print("\n   Nhóm 2: Số lần xem TRUNG BÌNH")
        # Rule 10
        rule10 = ctrl.Rule(
            self.view_count['medium'] & self.category_score['necessities'] & self.discount['low'],
            self.shopping_trend['low']
        )
        self.rules.append(rule10)
        print("   R10: Xem TB + Nhu yếu phẩm + Giảm giá thấp → Mua ít")
        
        # Rule 11
        rule11 = ctrl.Rule(
            self.view_count['medium'] & self.category_score['necessities'] & self.discount['medium'],
            self.shopping_trend['medium']
        )
        self.rules.append(rule11)
        print("   R11: Xem TB + Nhu yếu phẩm + Giảm giá TB → Mua vừa")
        
        # Rule 12
        rule12 = ctrl.Rule(
            self.view_count['medium'] & self.category_score['necessities'] & self.discount['high'],
            self.shopping_trend['medium']
        )
        self.rules.append(rule12)
        print("   R12: Xem TB + Nhu yếu phẩm + Giảm giá cao → Mua vừa")
        
        # Rule 13
        rule13 = ctrl.Rule(
            self.view_count['medium'] & self.category_score['fashion'] & self.discount['low'],
            self.shopping_trend['low']
        )
        self.rules.append(rule13)
        print("   R13: Xem TB + Thời trang + Giảm giá thấp → Mua ít")
        
        # Rule 14
        rule14 = ctrl.Rule(
            self.view_count['medium'] & self.category_score['fashion'] & self.discount['medium'],
            self.shopping_trend['medium']
        )
        self.rules.append(rule14)
        print("   R14: Xem TB + Thời trang + Giảm giá TB → Mua vừa")
        
        # Rule 15
        rule15 = ctrl.Rule(
            self.view_count['medium'] & self.category_score['fashion'] & self.discount['high'],
            self.shopping_trend['high']
        )
        self.rules.append(rule15)
        print("   R15: Xem TB + Thời trang + Giảm giá cao → Mua nhiều")
        
        # Rule 16
        rule16 = ctrl.Rule(
            self.view_count['medium'] & self.category_score['electronics'] & self.discount['low'],
            self.shopping_trend['medium']
        )
        self.rules.append(rule16)
        print("   R16: Xem TB + Điện tử + Giảm giá thấp → Mua vừa")
        
        # Rule 17
        rule17 = ctrl.Rule(
            self.view_count['medium'] & self.category_score['electronics'] & self.discount['medium'],
            self.shopping_trend['medium']
        )
        self.rules.append(rule17)
        print("   R17: Xem TB + Điện tử + Giảm giá TB → Mua vừa")
        
        # Rule 18
        rule18 = ctrl.Rule(
            self.view_count['medium'] & self.category_score['electronics'] & self.discount['high'],
            self.shopping_trend['high']
        )
        self.rules.append(rule18)
        print("   R18: Xem TB + Điện tử + Giảm giá cao → Mua nhiều")
        
        # Nhóm 3: Số lần xem NHIỀU
        print("\n   Nhóm 3: Số lần xem NHIỀU")
        # Rule 19
        rule19 = ctrl.Rule(
            self.view_count['high'] & self.category_score['necessities'] & self.discount['low'],
            self.shopping_trend['medium']
        )
        self.rules.append(rule19)
        print("   R19: Xem nhiều + Nhu yếu phẩm + Giảm giá thấp → Mua vừa")
        
        # Rule 20
        rule20 = ctrl.Rule(
            self.view_count['high'] & self.category_score['necessities'] & self.discount['medium'],
            self.shopping_trend['medium']
        )
        self.rules.append(rule20)
        print("   R20: Xem nhiều + Nhu yếu phẩm + Giảm giá TB → Mua vừa")
        
        # Rule 21
        rule21 = ctrl.Rule(
            self.view_count['high'] & self.category_score['necessities'] & self.discount['high'],
            self.shopping_trend['high']
        )
        self.rules.append(rule21)
        print("   R21: Xem nhiều + Nhu yếu phẩm + Giảm giá cao → Mua nhiều")
        
        # Rule 22
        rule22 = ctrl.Rule(
            self.view_count['high'] & self.category_score['fashion'] & self.discount['low'],
            self.shopping_trend['medium']
        )
        self.rules.append(rule22)
        print("   R22: Xem nhiều + Thời trang + Giảm giá thấp → Mua vừa")
        
        # Rule 23
        rule23 = ctrl.Rule(
            self.view_count['high'] & self.category_score['fashion'] & self.discount['medium'],
            self.shopping_trend['high']
        )
        self.rules.append(rule23)
        print("   R23: Xem nhiều + Thời trang + Giảm giá TB → Mua nhiều")
        
        # Rule 24
        rule24 = ctrl.Rule(
            self.view_count['high'] & self.category_score['fashion'] & self.discount['high'],
            self.shopping_trend['high']
        )
        self.rules.append(rule24)
        print("   R24: Xem nhiều + Thời trang + Giảm giá cao → Mua nhiều")
        
        # Rule 25
        rule25 = ctrl.Rule(
            self.view_count['high'] & self.category_score['electronics'] & self.discount['low'],
            self.shopping_trend['medium']
        )
        self.rules.append(rule25)
        print("   R25: Xem nhiều + Điện tử + Giảm giá thấp → Mua vừa")
        
        # Rule 26
        rule26 = ctrl.Rule(
            self.view_count['high'] & self.category_score['electronics'] & self.discount['medium'],
            self.shopping_trend['high']
        )
        self.rules.append(rule26)
        print("   R26: Xem nhiều + Điện tử + Giảm giá TB → Mua nhiều")
        
        # Rule 27
        rule27 = ctrl.Rule(
            self.view_count['high'] & self.category_score['electronics'] & self.discount['high'],
            self.shopping_trend['high']
        )
        self.rules.append(rule27)
        print("   R27: Xem nhiều + Điện tử + Giảm giá cao → Mua nhiều")
    
    def _create_control_system(self):
        """
        Tạo hệ thống điều khiển mờ
        """
        print("\n5. TẠO HỆ THỐNG ĐIỀU KHIỂN MỜ:")
        self.shopping_ctrl = ctrl.ControlSystem(self.rules)
        self.shopping_sim = ctrl.ControlSystemSimulation(self.shopping_ctrl)
        print("   ✓ Hệ thống điều khiển đã được tạo với 27 luật mờ")
    
    def predict(self, view_count, category_score, discount):
        """
        Dự đoán xu hướng mua sắm dựa trên các tham số đầu vào
        
        Parameters:
        -----------
        view_count : float
            Số lần xem sản phẩm (0-100)
        category_score : float
            Điểm danh mục (0-10): 0-3: Nhu yếu phẩm, 3-7: Thời trang, 7-10: Điện tử
        discount : float
            Mức chiết khấu (0-100%)
        
        Returns:
        --------
        float
            Điểm xu hướng mua sắm (0-100)
        """
        # Gán giá trị đầu vào
        self.shopping_sim.input['view_count'] = view_count
        self.shopping_sim.input['category_score'] = category_score
        self.shopping_sim.input['discount'] = discount
        
        # Tính toán
        self.shopping_sim.compute()
        
        # Lấy kết quả
        result = self.shopping_sim.output['shopping_trend']
        
        return result
    
    def interpret_result(self, score):
        """
        Diễn giải kết quả điểm số thành xu hướng mua sắm
        
        Parameters:
        -----------
        score : float
            Điểm xu hướng mua sắm (0-100)
        
        Returns:
        --------
        str
            Mô tả xu hướng mua sắm
        """
        if score <= 35:
            return "Mua ít"
        elif score <= 75:
            return "Mua vừa"
        else:
            return "Mua nhiều"
    
    def get_category_name(self, category_score):
        """
        Lấy tên danh mục từ điểm số
        
        Parameters:
        -----------
        category_score : float
            Điểm danh mục (0-10)
        
        Returns:
        --------
        str
            Tên danh mục
        """
        if category_score <= 3:
            return "Nhu yếu phẩm"
        elif category_score <= 7:
            return "Thời trang"
        else:
            return "Điện tử"
    
    def visualize_membership_functions(self, save_path='membership_functions.png'):
        """
        Vẽ các hàm thuộc của hệ thống
        
        Parameters:
        -----------
        save_path : str
            Đường dẫn lưu file ảnh
        """
        fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))
        
        # Số lần xem sản phẩm
        self.view_count.view(ax=axes[0, 0])
        axes[0, 0].set_title('Số lần xem sản phẩm', fontsize=12, fontweight='bold')
        axes[0, 0].set_xlabel('Số lần xem')
        axes[0, 0].set_ylabel('Độ thuộc')
        axes[0, 0].legend(['Ít', 'Trung bình', 'Nhiều'])
        
        # Danh mục sản phẩm
        self.category_score.view(ax=axes[0, 1])
        axes[0, 1].set_title('Danh mục sản phẩm yêu thích', fontsize=12, fontweight='bold')
        axes[0, 1].set_xlabel('Điểm danh mục')
        axes[0, 1].set_ylabel('Độ thuộc')
        axes[0, 1].legend(['Nhu yếu phẩm', 'Thời trang', 'Điện tử'])
        
        # Mức chiết khấu
        self.discount.view(ax=axes[1, 0])
        axes[1, 0].set_title('Mức chiết khấu', fontsize=12, fontweight='bold')
        axes[1, 0].set_xlabel('Phần trăm chiết khấu (%)')
        axes[1, 0].set_ylabel('Độ thuộc')
        axes[1, 0].legend(['Thấp', 'Trung bình', 'Cao'])
        
        # Xu hướng mua sắm
        self.shopping_trend.view(ax=axes[1, 1])
        axes[1, 1].set_title('Xu hướng mua sắm (Đầu ra)', fontsize=12, fontweight='bold')
        axes[1, 1].set_xlabel('Điểm xu hướng')
        axes[1, 1].set_ylabel('Độ thuộc')
        axes[1, 1].legend(['Mua ít', 'Mua vừa', 'Mua nhiều'])
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"\n✓ Đã lưu biểu đồ hàm thuộc tại: {save_path}")
        plt.close()
        
        return save_path


def main():
    """
    Hàm chính để demo hệ thống
    """
    print("\n" + "=" * 70)
    print("DEMO HỆ THỐNG PHÂN TÍCH XU HƯỚNG MUA SẮM")
    print("=" * 70)
    
    # Khởi tạo hệ thống
    system = ShoppingTrendFuzzySystem()
    
    # Vẽ các hàm thuộc
    system.visualize_membership_functions()
    
    # Các test case mẫu
    print("\n" + "=" * 70)
    print("THỰC HIỆN CÁC TEST CASE MẪU")
    print("=" * 70)
    
    test_cases = [
        {"view_count": 10, "category_score": 2, "discount": 10},  # Xem ít, nhu yếu phẩm, giảm giá thấp
        {"view_count": 50, "category_score": 5, "discount": 50},  # Xem TB, thời trang, giảm giá TB
        {"view_count": 90, "category_score": 9, "discount": 90},  # Xem nhiều, điện tử, giảm giá cao
        {"view_count": 80, "category_score": 6, "discount": 80},  # Xem nhiều, thời trang, giảm giá cao
        {"view_count": 30, "category_score": 1.5, "discount": 20},  # Xem ít, nhu yếu phẩm, giảm giá thấp
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"\nTest case {i}:")
        print(f"  Đầu vào:")
        print(f"    - Số lần xem: {test['view_count']}")
        print(f"    - Danh mục: {system.get_category_name(test['category_score'])} (điểm: {test['category_score']})")
        print(f"    - Chiết khấu: {test['discount']}%")
        
        result = system.predict(
            test['view_count'],
            test['category_score'],
            test['discount']
        )
        
        print(f"  Đầu ra:")
        print(f"    - Điểm xu hướng: {result:.2f}")
        print(f"    - Phân loại: {system.interpret_result(result)}")
    
    print("\n" + "=" * 70)
    print("✓ HOÀN THÀNH DEMO HỆ THỐNG")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
