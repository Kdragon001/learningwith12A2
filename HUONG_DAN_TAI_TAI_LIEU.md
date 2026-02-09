# Hướng Dẫn Sửa Lỗi Tải Tài Liệu

## ✓ Vấn Đề Đã Xác Định
- Các file PDF chứa **dấu cách** và **ký tự đặc biệt tiếng Việt**
- Browser không thể tải xuống vì URL không được **mã hóa đúng**
- Cần chạy qua **HTTP server** thay vì `file://` protocol

## ✓ Cách Sửa (Đã Thực Hiện)
1. Cập nhật script download trong `index_FIXED.html`
2. Script sẽ tự động **mã hóa URL** với `encodeURIComponent()`
3. Hỗ trợ tải xuống file PDF từ đường dẫn có ký tự đặc biệt

## 🚀 Cách Test

### Cách 1: Dùng Python (Khuyên dùng)
```bash
# Mở PowerShell/Terminal tại thư mục project1
cd d:\hoc\code\htmml\project1

# Chạy server
python run_server.py

# Mở trình duyệt và truy cập:
# http://localhost:8000/index_FIXED.html
```

### Cách 2: Dùng Node.js (Nếu có)
```bash
npx http-server -p 8000
```

### Cách 3: Dùng PHP (Nếu cài PHP)
```bash
php -S localhost:8000
```

### Cách 4: Dùng Live Server (VS Code)
- Cài extension "Live Server"
- Click chuột phải trên `index_FIXED.html` → "Open with Live Server"

## ✓ Kiểm Tra Tải Xuống

1. **Mở** `http://localhost:8000/index_FIXED.html`
2. **Tìm** phần "Đề Thi Tiếng Anh" 
3. **Click** nút "📥 Tải Đề"
4. File PDF sẽ tải xuống thay vì lỗi

## 📝 Chi Tiết Kỹ Thuật

### URL Encoding
```javascript
// Trước (KHÔNG HOẠT ĐỘNG):
href="đề/đề tiếng anh/1. THPT ĐÀO DUY TỪ - THANH HOÁ 2025-2026 Đề.pdf"

// Sau (HOẠT ĐỘNG):
fetch(encodeURI(url))
```

### Các File Được Hỗ Trợ
- ✓ Tệp có **dấu cách**: `file name.pdf`
- ✓ Tệp có **dấu tiếng Việt**: `Tiếng Anh, Toán học`
- ✓ Tệp có **dấu ngoặc**: `(Lần 1).pdf`
- ✓ Tệp có **dấu gạch ngang**: `Đề-Thi.pdf`

## 🔧 Nếu Vẫn Lỗi

1. **Kiểm tra Console Browser** (F12 → Console)
   - Xem thông báo lỗi chi tiết
   
2. **Kiểm tra đường dẫn file**
   ```bash
   dir "đề\đề tiếng anh\"  # Kiểm tra file có tồn tại
   ```

3. **Thử fallback method**
   - Script có fallback tự động
   - Nếu fetch thất bại, sẽ thử tải trực tiếp

## 📦 Cấu Trúc File

```
project1/
├── index_FIXED.html          ← File chính (đã sửa)
├── learning12a2.css          ← CSS styling
├── run_server.py            ← Python server (mới)
├── README.md                ← File này
└── đề/
    └── đề tiếng anh/        ← Folder PDF
        ├── 1. THPT ĐÀO DUY TỪ...pdf
        ├── 2. KSCL THPT TRẦN PHÚ...pdf
        └── ... (30 file PDF)
```

## ✓ Kiểm Tra Đã Xong

- [x] Sửa script download
- [x] Thêm URL encoding
- [x] Tạo Python server
- [x] Hỗ trợ file tiếng Việt

**Giờ đã có thể tải tài liệu xuống bình thường! 🎉**
