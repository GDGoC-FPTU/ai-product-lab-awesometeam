# Lab 02 - Problem Scan

## Phase 1 - SCAN: Liệt Kê Bài Toán Vận Hành

| # | Công ty | Lens | Bài toán vận hành |
|---|---|---|---|
| 1 | Xanh SM | Stakeholder Pain | Tài xế xe điện gặp tình huống pin yếu nhưng chưa biết nên đến trạm sạc nào, có nên tiếp tục chạy hay cần xe cứu hộ sạc pin di động. |
| 2 | Xanh SM | Repetitive | Điều phối viên phải liên tục gán lại chuyến xe khi tài xế thiếu pin, kẹt xe, hủy chuyến hoặc đổi điểm đón. |
| 3 | Vinhomes | Time-consuming | Nhân viên CSKH mất nhiều thời gian đọc, phân loại và chuyển phản ánh cư dân đến đúng bộ phận phụ trách. |
| 4 | VinFast | AI-upgrade | Đội kỹ thuật cần phân tích log pin và lịch sử sạc để dự đoán bảo trì xe điện trước khi xe gặp lỗi nghiêm trọng. |
| 5 | Vinpearl / VinWonders | Repetitive | Nhân viên CSKH trả lời lặp lại các câu hỏi về vé, giờ mở cửa, chính sách đổi ngày, hoàn tiền và gói dịch vụ. |
| 6 | Vinmec | Time-consuming | Bác sĩ mất nhiều thời gian tóm tắt hồ sơ xuất viện từ bệnh án, kết quả xét nghiệm, đơn thuốc và lời dặn. |

## Phase 2 - QUICK-ASSESS: 3 Quick Problem Cards

### Quick Problem Card 1 - Xanh SM Emergency Charging Dispatcher

**Bài toán:** Hỗ trợ điều phối phương án sạc an toàn cho tài xế Xanh SM khi xe điện sắp hết pin.

**Công ty thành viên:** Xanh SM

**Actor:** Tài xế Xanh SM và điều phối viên trung tâm điều phối.

**Workflow hiện tại:**

1. Tài xế phát hiện pin yếu hoặc xe cảnh báo sắp hết pin.
2. Tài xế gọi tổng đài hoặc gửi yêu cầu trên app.
3. Điều phối viên hỏi mức pin, vị trí, loại xe và trạng thái đang phục vụ khách.
4. Điều phối viên tra cứu thủ công trạm sạc gần nhất và đánh giá khả năng di chuyển an toàn.
5. Điều phối viên soạn hướng dẫn và gửi lại cho tài xế sau khi tự kiểm tra.

**Bottleneck:** Bước 3-5 tốn khoảng 8-10 phút/lượt. Khi pin dưới 5%, việc tra cứu chậm hoặc chọn trạm quá xa có thể khiến xe hết pin giữa đường.

**AI hỗ trợ:** AI đọc input về mức pin, vị trí, loại xe, khoảng cách trạm sạc và tạo bản nháp phương án xử lý. Rule gate chặn các đề xuất nguy hiểm trước khi LLM soạn tin nhắn.

**Success Metric:**

- Giảm thời gian đề xuất phương án từ 8-10 phút xuống dưới 1 phút.
- Tạo bản nháp xử lý dưới 30 giây khi đủ dữ liệu.
- 100% trường hợp pin dưới 5% không đề xuất trạm sạc xa hơn 5 km.
- 100% output bắt đầu bằng `[DRAFT_ONLY]`.
- 0 tin nhắn hoặc lệnh điều xe được thực hiện tự động khi chưa có điều phối viên phê duyệt.

**Quick Architecture:** Rule-based Safety Gate + LLM Feature + Human-in-the-loop.

### Quick Problem Card 2 - Vinhomes Complaint Router

**Bài toán:** Tự động phân loại và điều hướng phản ánh cư dân Vinhomes đến đúng bộ phận.

**Công ty thành viên:** Vinhomes

**Actor:** Nhân viên CSKH, ban quản lý tòa nhà, bộ phận kỹ thuật, an ninh và kế toán.

**Workflow hiện tại:**

1. Cư dân gửi phản ánh trên app.
2. CSKH đọc nội dung và tìm thông tin tòa/căn hộ.
3. CSKH xác định loại vấn đề.
4. CSKH chuyển ticket đến bộ phận phụ trách.
5. CSKH soạn phản hồi ban đầu cho cư dân.

**Bottleneck:** Bước 2-4 mất 8-12 phút/ticket và dễ chuyển sai khi nội dung mơ hồ hoặc thiếu ngữ cảnh.

**AI hỗ trợ:** LLM trích xuất tòa/căn hộ, phân loại intent, đề xuất bộ phận nhận và soạn phản hồi nháp.

**Success Metric:**

- 85% ticket được phân loại trong dưới 30 giây.
- Giảm ticket chuyển sai từ 12% xuống dưới 4%.
- 100% ticket nhạy cảm về phí, pháp lý hoặc tranh chấp phải có người duyệt.

**Quick Architecture:** LLM Feature kết hợp rule routing.

### Quick Problem Card 3 - Vinpearl Guest Support Assistant

**Bài toán:** Hỗ trợ trả lời các câu hỏi lặp lại về vé, giờ mở cửa, combo dịch vụ và hoàn tiền.

**Công ty thành viên:** Vinpearl / VinWonders

**Actor:** Nhân viên CSKH, khách du lịch và nhân viên bán vé.

**Workflow hiện tại:**

1. Khách hỏi qua chat, email hoặc hotline.
2. CSKH xác định khu vui chơi, ngày sử dụng và loại vé.
3. CSKH tra cứu chính sách hiện hành.
4. CSKH soạn câu trả lời.
5. Nếu có hoàn tiền hoặc đổi vé, CSKH chuyển cấp trên duyệt.

**Bottleneck:** Bước 2-4 mất 5-7 phút/câu hỏi, trong khi nhiều câu hỏi trùng lặp vào mùa cao điểm.

**AI hỗ trợ:** AI tìm chính sách từ FAQ nội bộ, soạn câu trả lời nháp và đánh dấu trường hợp cần người duyệt.

**Success Metric:**

- Giảm thời gian soạn phản hồi từ 6 phút xuống dưới 1 phút.
- 90% câu hỏi FAQ được trả lời đúng theo chính sách.
- 100% yêu cầu hoàn tiền hoặc đổi vé được gắn cờ cần human review.

**Quick Architecture:** Retrieval + LLM Feature + Human-in-the-loop cho giao dịch nhạy cảm.

## Lựa Chọn Cho Phần Nhóm

Nhóm chọn **Quick Problem Card 1 - Xanh SM Emergency Charging Dispatcher** để deep-dive vì bài toán có workflow rõ, bottleneck đo được bằng thời gian, boundary an toàn định lượng và phù hợp với prototype prompt trong `starter-code/prompt_prototype.py`.