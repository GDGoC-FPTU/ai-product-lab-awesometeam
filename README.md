[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=24262336&assignment_repo_type=AssignmentRepo)

# Hướng Dẫn Học Viên - Lab 02: AI Product Scoping

Tài liệu này hướng dẫn cách thiết lập môi trường Python, cấu hình API key và chuẩn bị bài nộp cho **Lab 02: AI Product Scoping - Vin Smart Future**.

Các file trong repo này đã được chuẩn hóa theo cùng một hướng nội dung: **Trợ lý điều phối sạc khẩn cấp cho tài xế Xanh SM khi xe điện sắp hết pin**. Kiến trúc thống nhất là **Rule-based Safety Gate + LLM Draft + Human-in-the-loop**.

---

## 1. Thiết Lập Môi Trường Ảo

Môi trường ảo giúp cô lập thư viện của dự án, tránh xung đột với các phiên bản Python hoặc thư viện khác trên máy.

### Bước 1: Tạo môi trường ảo

Mở terminal tại thư mục gốc của repo và chạy:

```powershell
python -m venv .venv
```

Trên macOS/Linux:

```bash
python3 -m venv .venv
```

### Bước 2: Kích hoạt môi trường ảo

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Nếu gặp lỗi Execution Policy, chạy:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

Windows CMD:

```cmd
.venv\Scripts\activate.bat
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Khi kích hoạt thành công, terminal sẽ hiển thị tiền tố `(.venv)`.

### Bước 3: Cài đặt thư viện

```bash
pip install -r requirements.txt
```

Hoặc cài trực tiếp:

```bash
pip install google-genai google-generativeai pytest
```

---

## 2. Thiết Lập `GEMINI_API_KEY`

Không dán API key trực tiếp vào code. Hãy dùng biến môi trường để tránh lộ khóa khi push lên GitHub.

PowerShell:

```powershell
$env:GEMINI_API_KEY="AIzaSyYourGeminiApiKeyHere"
```

CMD:

```cmd
set GEMINI_API_KEY=AIzaSyYourGeminiApiKeyHere
```

macOS/Linux:

```bash
export GEMINI_API_KEY="AIzaSyYourGeminiApiKeyHere"
```

Kiểm tra nhanh:

```bash
python -c "import os; print('API Key status: OK' if os.getenv('GEMINI_API_KEY') else 'API Key status: MISSING')"
```

Nếu chưa có API key, `starter-code/prompt_prototype.py` vẫn chạy được bằng fallback rule-based cục bộ để autograder kiểm tra ranh giới an toàn.

---

## 3. Cấu Trúc Bài Nộp

Repo nhóm cần có các file sau tại thư mục gốc:

```text
ai-product-lab-awesometeam/
|-- 01-problem-scan.md          Báo cáo Phase 1 và 2
|-- 02-deep-dive-report.md      Báo cáo Deep-Dive và Evaluation
|-- 03-ai-log.md                Nhật ký phản ánh quá trình dùng AI
|-- 04-workflow-diagram.png     Ảnh sơ đồ workflow hiện tại
|-- starter-code/
|   `-- prompt_prototype.py     Prototype kiểm thử prompt và boundary
`-- autograder/
    `-- autograder.py           Script kiểm tra bài nộp
```

## 4. Nội Dung Đã Thống Nhất

Thông tin chính cần giữ nhất quán giữa các file:

| Mục | Nội dung chuẩn |
|---|---|
| Bài toán được chọn | Trợ lý điều phối sạc khẩn cấp cho tài xế Xanh SM khi xe điện sắp hết pin |
| Actor chính | Tài xế Xanh SM và điều phối viên trung tâm điều phối |
| Bottleneck | Thu thập dữ liệu, tra cứu trạm sạc, đánh giá an toàn và soạn hướng dẫn thủ công |
| Thời gian hiện tại | Khoảng 10 phút/lượt |
| Mục tiêu | Tạo draft dưới 30 giây, giảm thời gian điều phối xuống dưới 2 phút/lượt |
| Boundary cốt lõi | AI chỉ tạo bản nháp, không tự gửi tin nhắn, không tự điều xe cứu hộ, không bỏ qua điều phối viên |
| Quy tắc an toàn | Nếu pin dưới 5% và trạm an toàn gần nhất xa hơn 5 km, đề xuất `dispatch_mobile_charger` |
| Kiến trúc | Rule-based Safety Gate + LLM Draft + Human-in-the-loop |
| Quyết định | GO với prototype phạm vi hẹp |

---

## 5. Kiểm Tra Trước Khi Nộp

Chạy autograder:

```bash
python autograder/autograder.py
```

Khi các check thành công, có thể commit và push:

```bash
git add .
git commit -m "Submit Lab 02 Assignment"
git push origin main
```

