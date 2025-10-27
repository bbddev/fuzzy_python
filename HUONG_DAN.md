# HƯỚNG DẪN THỰC HIỆN BÀI THU HOẠCH

## 📋 MỤC LỤC

1. [Chuẩn bị môi trường](#1-chuẩn-bị-môi-trường)
2. [Chạy chương trình](#2-chạy-chương-trình)
3. [Hiểu kết quả](#3-hiểu-kết-quả)
4. [Hoàn thiện bài thu hoạch](#4-hoàn-thiện-bài-thu-hoạch)
5. [Câu hỏi thường gặp](#5-câu-hỏi-thường-gặp)

---

## 1. CHUẨN BỊ MÔI TRƯỜNG

### Bước 1: Cài đặt Python

Đảm bảo bạn đã cài Python 3.8 trở lên:

```cmd
python --version
```

### Bước 2: Cài đặt các thư viện

Mở Command Prompt (cmd) tại thư mục dự án và chạy:

```cmd
pip install -r requirements.txt
```

Nếu gặp lỗi, thử cài từng thư viện:

```cmd
pip install numpy==1.24.3
pip install scikit-fuzzy==0.4.2
pip install matplotlib==3.7.1
pip install pandas==2.0.3
pip install seaborn==0.12.2
```

### Bước 3: Kiểm tra cài đặt

Chạy lệnh sau để kiểm tra:

```cmd
python -c "import skfuzzy; import numpy; import matplotlib; import pandas; print('Cài đặt thành công!')"
```

---

## 2. CHẠY CHƯƠNG TRÌNH

### Bước 1: Chạy demo hệ thống

```cmd
python fuzzy_shopping_system.py
```

**Kết quả mong đợi:**

- In ra thông tin khởi tạo hệ thống
- Hiển thị 27 luật mờ
- Chạy 5 test case mẫu
- Tạo file `membership_functions.png`

**Thời gian:** ~10-20 giây

### Bước 2: Chạy thực nghiệm toàn diện

```cmd
python test_system.py
```

**Kết quả mong đợi:**

- Chạy 100+ test case
- Tạo file `ket_qua_thuc_nghiem.csv`
- In thống kê tổng quan

**Thời gian:** ~30-60 giây

### Bước 3: Tạo biểu đồ

```cmd
python visualize_results.py
```

**Kết quả mong đợi:**

- Tạo 9 file ảnh biểu đồ (bieu_do_0.png đến bieu_do_7.png, bang_tong_ket.png)
- Mỗi biểu đồ phân tích một khía cạnh khác nhau

**Thời gian:** ~1-2 phút

---

## 3. HIỂU KẾT QUẢ

### 3.1. File CSV - ket_qua_thuc_nghiem.csv

Mở file này bằng Excel hoặc Google Sheets để xem chi tiết.

**Các cột quan trọng:**

- **STT:** Số thứ tự test case
- **Mô tả:** Mô tả tình huống
- **Số lần xem:** Giá trị đầu vào (0-100)
- **Danh mục:** Nhu yếu phẩm / Thời trang / Điện tử
- **Chiết khấu (%):** Giá trị đầu vào (0-100)
- **Điểm xu hướng:** Kết quả hệ thống tính toán (0-100)
- **Xu hướng mua sắm:** Mua ít / Mua vừa / Mua nhiều

**Cách đọc:**

- Điểm 0-35: Mua ít
- Điểm 35-75: Mua vừa
- Điểm 75-100: Mua nhiều

### 3.2. Các biểu đồ

#### bieu_do_0_ham_thuoc.png

- **Nội dung:** Hiển thị 4 biểu đồ hàm thuộc của các biến
- **Cách đọc:** Mỗi đường màu thể hiện một tập mờ (low, medium, high)
- **Ý nghĩa:** Cho thấy cách hệ thống phân loại các giá trị

#### bieu_do_1_phan_bo_xu_huong.png

- **Nội dung:** Biểu đồ cột phân bố xu hướng
- **Cách đọc:** Chiều cao cột = số lượng test case
- **Ý nghĩa:** Xem hệ thống phân loại cân bằng hay không

#### bieu_do_2_phan_tich_danh_muc.png

- **Nội dung:** 2 biểu đồ so sánh theo danh mục
- **Cách đọc:** So sánh điểm trung bình giữa các danh mục
- **Ý nghĩa:** Danh mục nào có xu hướng mua cao nhất

#### bieu_do_3_anh_huong_so_lan_xem.png

- **Nội dung:** Đường biểu diễn ảnh hưởng của số lần xem
- **Cách đọc:** Trục X = số lần xem, Trục Y = điểm xu hướng
- **Ý nghĩa:** Kiểm tra quan hệ tăng dần

#### bieu_do_4_anh_huong_chiet_khau.png

- **Nội dung:** Đường biểu diễn ảnh hưởng của chiết khấu
- **Cách đọc:** Trục X = chiết khấu, Trục Y = điểm xu hướng
- **Ý nghĩa:** Kiểm tra ảnh hưởng của giảm giá

#### bieu_do_5_be_mat_3d.png

- **Nội dung:** Bề mặt 3D thể hiện quan hệ 3 biến
- **Cách đọc:** Màu sắc thể hiện điểm xu hướng
- **Ý nghĩa:** Nhìn tổng quan mối quan hệ

#### bieu_do_6_heatmap.png

- **Nội dung:** Bản đồ nhiệt
- **Cách đọc:** Màu xanh = thấp, Màu đỏ = cao
- **Ý nghĩa:** Dễ dàng nhận diện vùng xu hướng cao/thấp

#### bieu_do_7_phan_bo_diem.png

- **Nội dung:** Histogram và boxplot
- **Cách đọc:** Phân bố tần suất và các giá trị ngoại lai
- **Ý nghĩa:** Đánh giá độ phân tán của kết quả

#### bang_tong_ket.png

- **Nội dung:** Bảng thống kê tổng hợp
- **Cách đọc:** Đọc trực tiếp các con số
- **Ý nghĩa:** Tóm tắt toàn bộ kết quả thực nghiệm

---

## 4. HOÀN THIỆN BÀI THU HOẠCH

### Bước 1: Cập nhật thông tin cá nhân

Mở file `Bai_thu_hoach.md` và thay thế:

- `[Tên sinh viên]` → Tên của bạn
- `[MSSV]` → Mã số sinh viên
- `[Lớp]` → Lớp học
- `[Ngày/tháng/năm]` → Ngày nộp bài

### Bước 2: Cập nhật kết quả thực nghiệm

Trong phần 3.2.1, cập nhật:

- Tổng số test case thực tế
- Phân bố xu hướng thực tế (%, số lượng)
- Các thống kê từ file CSV

### Bước 3: Phân tích biểu đồ

Cho mỗi biểu đồ trong phần 3.3, thêm:

- Nhận xét cụ thể về hình dạng, xu hướng
- So sánh với kỳ vọng
- Giải thích nguyên nhân

### Bước 4: Viết kết luận

Dựa trên kết quả thực tế, viết:

- Đánh giá tính đúng đắn của hệ thống
- Những điểm mạnh đã kiểm chứng được
- Những hạn chế phát hiện được
- Đề xuất cải tiến

### Bước 5: Tạo file PDF

Có 2 cách:

**Cách 1: Sử dụng Pandoc (khuyên dùng)**

```cmd
pandoc Bai_thu_hoach.md -o Bai_thu_hoach.pdf --pdf-engine=xelatex
```

**Cách 2: Sử dụng trình chỉnh sửa Markdown**

- Visual Studio Code + Extension "Markdown PDF"
- Typora (phần mềm trả phí)
- Dillinger.io (online, miễn phí)

---

## 5. CÂU HỎI THƯỜNG GẶP

### Q1: Lỗi "No module named 'skfuzzy'"?

**Trả lời:** Chạy lại `pip install scikit-fuzzy`

### Q2: Biểu đồ không hiển thị tiếng Việt?

**Trả lời:** Đây là vấn đề font. File code đã sử dụng ký tự không dấu cho tiêu đề biểu đồ để tránh lỗi này.

### Q3: Tại sao hệ thống có 27 luật?

**Trả lời:**

- 3 mức số lần xem × 3 mức danh mục × 3 mức chiết khấu = 27 tổ hợp
- Mỗi tổ hợp cần 1 luật

### Q4: Làm sao biết hệ thống hoạt động đúng?

**Trả lời:** Kiểm tra:

- Số lần xem tăng → Điểm xu hướng tăng
- Chiết khấu tăng → Điểm xu hướng tăng
- Kết quả logic, không có giá trị bất thường
- Biểu đồ có dạng trơn, liên tục

### Q5: Có thể thay đổi số lượng luật không?

**Trả lời:** Có, nhưng cần:

- Thay đổi code trong `_define_fuzzy_rules()`
- Đảm bảo bao phủ tất cả các trường hợp
- Giải thích rõ lý do trong bài thu hoạch

### Q6: File nào cần nộp?

**Trả lời:** Nộp tất cả:

- `Bai_thu_hoach.pdf` (hoặc .md)
- `fuzzy_shopping_system.py`
- `test_system.py`
- `visualize_results.py`
- `requirements.txt`
- `ket_qua_thuc_nghiem.csv`
- Tất cả các file ảnh biểu đồ
- `README.md`

### Q7: Làm sao test với dữ liệu tự chọn?

**Trả lời:** Thêm vào file `test_system.py`:

```python
# Thêm test case của bạn
my_test = {
    'view_count': 60,        # Giá trị bạn muốn test
    'category_score': 7,     # 0-10
    'discount': 40,          # 0-100
    'description': 'Test case của tôi'
}
realistic_cases.append(my_test)
```

### Q8: Hệ thống cho kết quả không như mong đợi?

**Trả lời:** Kiểm tra:

1. Giá trị đầu vào có đúng khoảng không? (0-100, 0-10)
2. Danh mục có đúng không? (0-4: nhu yếu phẩm, 3-7: thời trang, 7-10: điện tử)
3. Nếu vẫn chưa đúng, có thể điều chỉnh luật hoặc hàm thuộc

### Q9: Làm sao giải thích cho giáo viên?

**Trả lời:** Chuẩn bị:

- Demo trực tiếp chương trình
- Giải thích 2-3 luật cụ thể
- Chỉ vào biểu đồ hàm thuộc
- So sánh kết quả thực tế với lý thuyết

### Q10: Có thể mở rộng hệ thống không?

**Trả lời:** Có thể thêm:

- Biến mới: thời gian lưu trú, lịch sử mua hàng
- Luật mới cho các trường hợp đặc biệt
- Tích hợp dữ liệu thực từ website

---

## 6. CHECKLIST TRƯỚC KHI NỘP

- [ ] Đã chạy thành công cả 3 file Python
- [ ] Có đầy đủ 9 file ảnh biểu đồ
- [ ] File CSV có dữ liệu đầy đủ
- [ ] Đã cập nhật thông tin cá nhân trong bài thu hoạch
- [ ] Đã phân tích kết quả thực tế
- [ ] File PDF đẹp, dễ đọc
- [ ] Đã kiểm tra lỗi chính tả
- [ ] Tất cả code có chú thích đầy đủ
- [ ] Đã test demo trước khi nộp

---

## 7. TIPS ĐỂ ĐẠT ĐIỂM CAO

1. **Phần lý thuyết:**

   - Giải thích rõ tại sao chọn hàm thuộc tam giác
   - Phân tích kỹ từng luật mờ
   - Vẽ thêm sơ đồ khối chi tiết

2. **Phần code:**

   - Thêm nhiều comment tiếng Việt
   - Code clean, dễ đọc
   - Xử lý exception tốt

3. **Phần thực nghiệm:**

   - Càng nhiều test case càng tốt
   - Phân tích sâu các biểu đồ
   - So sánh với các hệ thống tương tự

4. **Trình bày:**

   - Sử dụng bảng, biểu đồ nhiều
   - Format đẹp, chuyên nghiệp
   - Không có lỗi chính tả

5. **Demo:**
   - Chuẩn bị sẵn các test case hay
   - Giải thích logic dễ hiểu
   - Trả lời câu hỏi tự tin

---

## 8. HỖ TRỢ VÀ TÀI LIỆU THAM KHẢO

### Tài liệu học tập:

- [Scikit-fuzzy Documentation](https://pythonhosted.org/scikit-fuzzy/)
- [Fuzzy Logic Tutorial](https://www.tutorialspoint.com/fuzzy_logic/index.htm)

### Video hướng dẫn:

- YouTube: "Fuzzy Logic Control Tutorial"
- YouTube: "Python Fuzzy Control System"

### Hỗ trợ kỹ thuật:

- Stack Overflow: Tag [fuzzy-logic]
- GitHub Issues: scikit-fuzzy repository

---

**Chúc bạn hoàn thành tốt bài thu hoạch! 🎉**

_Nếu gặp vấn đề kỹ thuật, hãy đọc kỹ phần Câu hỏi thường gặp hoặc tìm kiếm trên Google với từ khóa cụ thể._
