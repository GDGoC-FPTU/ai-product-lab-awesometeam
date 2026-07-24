# 01 — Problem Scan (Bài cá nhân)
**Họ tên:** [Điền tên bạn]
**Mảng chọn để scan:** Đa dạng (VinFast, Xanh SM, Vinhomes, Vinmec, Vinpearl)

---

## Phase 1 — SCAN: 5 bài toán tiềm năng

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|----------------------|
| 1 | **Xanh SM** | Tốn thời gian | Điều phối viên phải tự tổng hợp thủ công báo cáo hiệu suất tài xế cuối ngày (số cuốc, đánh giá, thời gian chờ) từ nhiều nguồn (app, tổng đài, ghi chú tay) để gửi ca sau. |
| 2 | **VinFast** | AI-upgrade | Trợ lý trong xe hiện chỉ trả lời được các câu hỏi cố định (rule-based), chưa xử lý được câu hỏi tự nhiên của khách về tính năng xe (VD: "vì sao đèn cảnh báo pin sáng vàng"). |
| 3 | **Vinhomes** | Lặp lại | Ban quản lý tòa nhà phải tự đọc và phân loại thủ công hàng trăm phản ánh cư dân mỗi tuần (mất nước, ồn, hỏng thang máy...) rồi mới chuyển đúng bộ phận xử lý. |
| 4 | **Vinmec** | Pain từ người khác | Bác sĩ phàn nàn mất 20-30 phút/bệnh nhân để tự tay viết tóm tắt hồ sơ xuất viện từ dữ liệu bệnh án điện tử, xét nghiệm rời rạc. |
| 5 | **Vinpearl** | Pain từ người khác | Quản lý khách sạn phải tự đọc thủ công hàng nghìn review trên Booking/Agoda/Google Map mỗi tháng để tìm ra phàn nàn khẩn cấp cần xử lý gấp. |

---

## Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

### 🃏 Quick Problem Card #1

```
Bài toán: Tự động phân loại và điều hướng phản ánh cư dân trên App Vinhomes Resident.
Công ty thành viên: [x] Vinhomes

Ai đang đau (Actor)? Ban quản lý tòa nhà (quá tải xử lý thủ công), cư dân (chờ lâu).

Workflow thủ công hiện tại (4 bước):
  1. Cư dân gửi phản ánh qua App (text tự do)
  → 2. Nhân viên trực đọc từng phản ánh, tự phân loại nhóm lỗi
  → 3. Nhân viên tra cứu đúng bộ phận phụ trách (điện/nước/an ninh/kỹ thuật)
  → 4. Chuyển phản ánh cho bộ phận đó xử lý, ghi log theo dõi

Bước nào tốn thời gian/lỗi nhất? Bước 2-3 (⏱ ~5 phút/lượt, dễ phân loại sai)
AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3 (tự động đọc nội dung, phân loại nhóm lỗi, gợi ý bộ phận phù hợp)

Đo thành công bằng gì (Metric có số)?
  Giảm thời gian phân loại từ 5 phút ──> dưới 30 giây/phản ánh, độ chính xác phân loại ≥ 90%.

Quick Architecture: [x] LLM Feature (phân loại + gợi ý điều hướng, người duyệt cuối)
```

### 🃏 Quick Problem Card #2

```
Bài toán: Trợ lý AI hỗ trợ bác sĩ soạn nháp tóm tắt hồ sơ xuất viện cho bệnh nhân.
Công ty thành viên: [x] Vinmec

Ai đang đau (Actor)? Bác sĩ điều trị (quá tải giấy tờ), bệnh nhân (chờ lâu khi ra viện).

Workflow thủ công hiện tại (4 bước):
  1. Bác sĩ tổng hợp dữ liệu bệnh án điện tử, kết quả xét nghiệm, ghi chú điều trị
  → 2. Bác sĩ tự viết tóm tắt xuất viện bằng ngôn ngữ dễ hiểu cho bệnh nhân
  → 3. Bác sĩ tự kiểm tra lại thông tin thuốc, liều dùng, lịch tái khám
  → 4. In/gửi bản tóm tắt cho bệnh nhân

Bước nào tốn thời gian/lỗi nhất? Bước 1-2 (⏱ 20-30 phút/bệnh nhân)
AI có thể nhảy vào hỗ trợ ở bước nào? Bước 1-2 (tự động tổng hợp + soạn nháp tóm tắt từ dữ liệu có sẵn)

Đo thành công bằng gì (Metric có số)?
  Giảm thời gian soạn tóm tắt từ 25 phút ──> dưới 5 phút/bệnh nhân (bác sĩ chỉ cần rà soát & duyệt).

Quick Architecture: [x] LLM Feature (soạn nháp, bắt buộc bác sĩ duyệt trước khi gửi bệnh nhân)
```

### 🃏 Quick Problem Card #3

```
Bài toán: Tự động lọc và cảnh báo sớm các review khẩn cấp của khách sạn Vinpearl.
Công ty thành viên: [x] Vinpearl

Ai đang đau (Actor)? Quản lý khách sạn (không kịp phát hiện phàn nàn nghiêm trọng sớm).

Workflow thủ công hiện tại (4 bước):
  1. Nhân viên CSKH tự đọc review mới trên Booking/Agoda/Google Map mỗi ngày
  → 2. Tự đánh giá mức độ nghiêm trọng (bình thường / cần chú ý / khẩn cấp)
  → 3. Tổng hợp và soạn báo cáo gửi quản lý
  → 4. Quản lý phản hồi/khắc phục nếu cần

Bước nào tốn thời gian/lỗi nhất? Bước 1-2 (⏱ ~2-3 giờ/ngày, dễ bỏ sót review khẩn cấp)
AI có thể nhảy vào hỗ trợ ở bước nào? Bước 1-2 (tự động quét, phân loại mức độ nghiêm trọng, gắn cờ khẩn cấp)

Đo thành công bằng gì (Metric có số)?
  Giảm thời gian phát hiện review khẩn cấp từ vài giờ ──> dưới 10 phút, không bỏ sót review nghiêm trọng.

Quick Architecture: [x] LLM Feature (phân loại + gắn cờ, người duyệt trước khi phản hồi khách)
```