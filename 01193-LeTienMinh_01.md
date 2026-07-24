# Bài làm Lab 02 — AI Product Scoping

**Sinh viên:** Lê Tiến Minh — **MSSV:** 2A202601193
**Bối cảnh:** Vin Smart Future (Vingroup)

> Các thời gian và tỷ lệ bên dưới là giả định để đặt mục tiêu cho pilot. Cần xác nhận lại bằng log vận hành trước khi triển khai thực tế.

## Phase 1 — SCAN

| # | Công ty thành viên | Lens | Bài toán/bottleneck thực tế |
|---|---|---|---|
| 1 | Vinhomes | Lặp lại | Nhân viên CSKH đọc, phân loại và chuyển từng phản ánh của cư dân như mất nước, hỏng đèn, tiếng ồn đến đúng ban quản lý tòa nhà. |
| 2 | Xanh SM | Tốn thời gian | Điều phối viên nhận tin nhắn/cuộc gọi về sự cố xe hoặc pin, sau đó phải tra cứu vị trí, tình trạng xe và soạn hướng dẫn xử lý thủ công. |
| 3 | VinFast | Lặp lại | Kế toán đối chiếu giao dịch sạc từ đối tác với hóa đơn và dữ liệu trạm sạc theo từng kỳ; các dòng lệch phải kiểm tra thủ công. |
| 4 | VinFast | AI có thể tốt hơn | Tổng đài viên tự diễn giải mô tả lỗi xe bằng tiếng Việt của khách hàng để chọn nhóm lỗi và lịch hẹn dịch vụ phù hợp. |
| 5 | Vinpearl | Pain từ người khác | Quản lý khách sạn đọc thủ công review từ nhiều kênh; các phản ánh khẩn như phòng bẩn hoặc hỏng điều hòa có thể được phát hiện muộn. |

## Phase 2 — QUICK-ASSESS

### Ba bài toán được chọn

1. Phân loại và điều hướng phản ánh cư dân Vinhomes.
2. Đối chiếu giao dịch sạc với hóa đơn đối tác VinFast.
3. Phát hiện review khách sạn cần xử lý khẩn tại Vinpearl.

### QUICK PROBLEM CARD #1 — Phân loại và điều hướng phản ánh cư dân

- **Bài toán (1 câu):** Giảm thời gian nhân viên Vinhomes đọc và chuyển phản ánh tự do của cư dân đến đúng đội vận hành/tòa nhà.
- **Công ty thành viên:** [ ] VinFast  [ ] Xanh SM  [x] Vinhomes  [ ] Vinmec  [ ] Khác
- **Ai đang đau (Actor)?** Nhân viên CSKH, ban quản lý tòa nhà và cư dân chờ phản hồi.
- **Workflow thủ công hiện tại:**
  1. Cư dân gửi phản ánh kèm ảnh qua ứng dụng.
  2. Nhân viên CSKH đọc nội dung, xác định loại sự cố, mức độ khẩn và tòa nhà/căn hộ.
  3. Nhân viên tìm đội kỹ thuật hoặc ban quản lý phù hợp để tạo và chuyển ticket.
  4. Đội nhận ticket kiểm tra lại thông tin rồi liên hệ cư dân.
- **Bước tốn thời gian/lỗi nhất:** Bước 2–3, vì nội dung phản ánh thường mơ hồ và dễ chuyển sai nơi nhận — khoảng **5 phút/ticket**.
- **AI hỗ trợ ở đâu:** LLM đề xuất danh mục, mức độ ưu tiên và đội nhận ticket; rule kiểm tra mã tòa nhà/căn hộ. Nhân viên CSKH phải duyệt trước khi ticket được chuyển.
- **Metric thành công:** Giảm thời gian phân luồng từ **5 phút xuống dưới 2 phút/ticket**; tối thiểu **90%** ticket được duyệt mà không cần đổi danh mục hoặc đội nhận.
- **Quick Architecture:** [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent

### QUICK PROBLEM CARD #2 — Đối chiếu giao dịch sạc với hóa đơn đối tác

- **Bài toán (1 câu):** Tự động so khớp giao dịch sạc có cấu trúc với hóa đơn đối tác để kế toán chỉ xử lý các trường hợp sai lệch.
- **Công ty thành viên:** [x] VinFast  [ ] Xanh SM  [ ] Vinhomes  [ ] Vinmec  [ ] Khác
- **Ai đang đau (Actor)?** Nhân viên kế toán đối soát và quản lý tài chính phụ trách chốt công nợ.
- **Workflow thủ công hiện tại:**
  1. Kế toán tải file giao dịch sạc từ hệ thống và file hóa đơn từ đối tác.
  2. Chuẩn hóa ngày giờ, mã trạm, mã giao dịch và số tiền.
  3. Dùng bảng tính dò từng dòng, đánh dấu giao dịch thiếu hoặc lệch tiền.
  4. Điều tra các dòng lệch và gửi yêu cầu điều chỉnh cho đối tác.
- **Bước tốn thời gian/lỗi nhất:** Bước 2–3, do dữ liệu từ các nguồn có định dạng khác nhau — khoảng **30 phút/1.000 giao dịch**.
- **AI hỗ trợ ở đâu:** Không cần LLM. Rule-based ETL chuẩn hóa dữ liệu và đối chiếu theo mã giao dịch, thời gian, mã trạm, số tiền; các ngoại lệ đi vào hàng chờ để kế toán kiểm tra.
- **Metric thành công:** Tối thiểu **95%** giao dịch được đối chiếu tự động; giảm thời gian xử lý **1.000 giao dịch từ 30 phút xuống dưới 5 phút**; **100%** giao dịch lệch được kế toán phê duyệt kết quả cuối.
- **Quick Architecture:** [ ] No AI  [x] Rule  [ ] LLM  [ ] Agent

### QUICK PROBLEM CARD #3 — Phát hiện review khách sạn cần xử lý khẩn

- **Bài toán (1 câu):** Giúp quản lý Vinpearl phát hiện sớm review có vấn đề khẩn và nhận bản tóm tắt hành động thay vì phải đọc thủ công toàn bộ review.
- **Công ty thành viên:** [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  [ ] Vinmec  [x] Khác: Vinpearl
- **Ai đang đau (Actor)?** Quản lý vận hành khách sạn, đội lễ tân/housekeeping và khách đang gặp sự cố.
- **Workflow thủ công hiện tại:**
  1. Quản lý mở các kênh review theo ngày.
  2. Đọc từng review bằng tiếng Việt hoặc tiếng Anh.
  3. Tự nhận diện nội dung tiêu cực/khẩn và ghi chú nguyên nhân.
  4. Gửi tin nhắn hoặc tạo việc cho bộ phận chịu trách nhiệm.
- **Bước tốn thời gian/lỗi nhất:** Bước 2–3, do review dài, đa ngôn ngữ và mức độ khẩn khó đánh giá nhất quán — khoảng **25 phút/ngày/cơ sở**.
- **AI hỗ trợ ở đâu:** LLM tóm tắt, gán nhãn chủ đề và đề xuất mức ưu tiên; rule bắt buộc gắn cờ từ khóa an toàn/sức khỏe. Quản lý duyệt trước khi giao việc hoặc phản hồi công khai.
- **Metric thành công:** Giảm thời gian tổng hợp review từ **25 phút xuống dưới 7 phút/ngày/cơ sở**; phát hiện tối thiểu **95%** review khẩn được quản lý gắn nhãn; **100%** phản hồi gửi khách phải do nhân viên phê duyệt.
- **Quick Architecture:** [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent
