#
Phase 1
Mô tả ngắn bài toán
1
VinFast
Lặp lại (Repetitive)
Kiểm tra chất lượng sơn thân xe trên dây chuyền sản xuất: Nhân viên QC phải kiểm tra thủ công từng tấm thân xe (hàng nghìn xe/ngày) để phát hiện vết xước, bong tróc, lỗi màu sơn. Tỷ lệ lỗi sót ~2-3%, gây chi phí bảo hành lớn.
2
Xanh SM
Tốn thời gian (Time-consuming)
Phân loại và xử lý khiếu nại của tài xế: Mỗi ngày có hàng trăm khiếu nại từ tài xế về phí hoa hồng, điểm đón khách, đánh giá sao. Nhân viên CSKH phải đọc, phân loại, tra cứu dữ liệu và soạn phản hồi thủ công (~15-20 phút/đơn).
3
Vinhomes
AI có thể tốt hơn (AI-upgrade)
Dự báo và cảnh báo sự cố thang máy/hệ thống PCCC: Hiện tại bảo trì theo lịch cố định (3-6 tháng/lần), không dựa trên dữ liệu cảm biến thực tế. Dẫn đến 2 vấn đề: (1) thang máy hỏng đột ngột gây phàn nàn cư dân, (2) bảo trì thừa gây lãng phí chi phí.
4
Vinmec
Pain từ người khác (Stakeholder Pain)
Xếp lịch khám và phân bổ bác sĩ theo chuyên khoa: Bệnh nhân phàn nàn thời gian chờ đợi lâu (trung bình 45-60 phút), trong khi bác sĩ có khung giờ trống xen kẽ. Nhân viên lễ tân xếp lịch thủ công qua điện thoại, dễ xảy ra chồng lịch hoặc để trống slot.
5
Vinpearl
Lặp lại + Tốn thời gian
Tổng hợp và phân tích đánh giá từ đa kênh (OTA, Facebook, Google): Mỗi ngày có hàng nghìn review từ Booking, Agoda, TripAdvisor, fanpage... Nhân viên marketing phải copy-paste, dịch (nếu là khách nước ngoài), phân loại cảm xúc và báo cáo thủ công. Mất ~2-3 giờ/ngày chỉ để tổng hợp.

Phase 2
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán (1 câu): Tự động phân loại và soạn phản hồi        │
│ khiếu nại của tài xế Xanh SM                                │
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác                   │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên CSKH Xanh SM                 │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Nhận khiếu nại qua app/email                           │
│   2. Đọc & phân loại chủ đề (hoa hồng/điểm đón/đánh giá)    │
│   3. Tra cứu dữ liệu chuyến đi trong hệ thống               │
│   4. Soạn phản hồi theo template                            │
│   5. Gửi phản hồi & log vào CRM                             │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2+3 (⏱ 15-20 phút/lượt)│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 (phân loại)    │
│   và Bước 4 (soạn phản hồi draft)                           │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│   "Giảm thời gian xử lý 1 khiếu nại từ 18 min ──> 5 min"    │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘