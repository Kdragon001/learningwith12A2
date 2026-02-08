# Hướng Dẫn Push Lên GitHub

## 1️⃣ Tạo Repository Trên GitHub

1. Truy cập https://github.com/new
2. Điền thông tin:
   - **Repository name**: `learning-with-12a2` (ví dụ)
   - **Description**: "Learning with 12A2 - Nền tảng học tập cho lớp 12A2"
   - **Public** / **Private**: Chọn Public nếu muốn mọi người xem
   - **Không check** "Initialize this repository with a README"

3. Click **"Create repository"**

## 2️⃣ Push Lên GitHub

Sao chép lệnh từ GitHub và chạy trong PowerShell:

```bash
cd "d:\hoc\code\htmml\project1"

# Thay <YOUR-USERNAME> và <REPO-NAME> bằng thông tin của bạn
git remote add origin https://github.com/<YOUR-USERNAME>/<REPO-NAME>.git
git branch -M main
git push -u origin main
```

### Ví dụ:
```bash
git remote add origin https://github.com/tenbạn/learning-with-12a2.git
git branch -M main
git push -u origin main
```

## 3️⃣ Nhập GitHub Token

- Nếu được hỏi "password", hãy dùng **GitHub Personal Access Token**
- Tạo token tại: https://github.com/settings/tokens
  - Click "Generate new token"
  - Chọn scopes: `repo` (full control of private repositories)
  - Copy token và paste khi được hỏi

## 4️⃣ Xác Nhận Trên GitHub

- Truy cập repo GitHub của bạn
- Bạn sẽ thấy tất cả file đã được đẩy lên! 🎉

## 5️⃣ Cập Nhật Thêm

Mỗi lần sửa file:

```bash
cd "d:\hoc\code\htmml\project1"
git add .
git commit -m "Mô tả thay đổi của bạn"
git push origin main
```

## 📝 Lệnh Nhanh

```bash
# Xem git log
git log --oneline

# Xem trạng thái
git status

# Xem remote
git remote -v

# Thay đổi remote URL
git remote set-url origin https://github.com/<USERNAME>/<REPO>.git
```

---

**Cần help?** Hỏi mình! 😊
