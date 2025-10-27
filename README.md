# HỆ THỐNG PHÂN TÍCH XU HƯỚNG MUA SẮM DỰA TRÊN LOGIC MỜ

## Mô tả đề tài

Phân tích xu hướng mua sắm của người dùng (mua nhiều, mua vừa, mua ít) dựa trên:

- Số lần xem sản phẩm (nhiều, trung bình, ít)
- Danh mục sản phẩm yêu thích (thời trang, điện tử, nhu yếu phẩm)
- Mức chiết khấu được cung cấp (cao, trung bình, thấp)

## Cấu trúc dự án

```
fuzzy/
├── README.md
├── Phan_tich_va_thiet_ke.pdf (Tài liệu phân tích và thiết kế)
├── fuzzy_shopping_system.py (Chương trình chính)
├── test_system.py (Script thực nghiệm)
├── visualize_results.py (Script vẽ biểu đồ)
└── requirements.txt (Thư viện cần thiết)
```

## Hướng dẫn cài đặt

```bash
pip install -r requirements.txt
```

## Hướng dẫn chạy chương trình

```bash
# Chạy chương trình chính
python fuzzy_shopping_system.py

# Chạy thực nghiệm
python test_system.py

# Vẽ biểu đồ kết quả
python visualize_results.py
```
