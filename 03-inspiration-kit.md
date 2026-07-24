# Inspiration Kit - Gợi Ý Tìm Bài Toán

> Dùng file này khi cần thêm ý tưởng cho Phase 1. Đây là tài liệu gợi ý, không thay thế bài làm chính. Bài nộp trong repo này vẫn thống nhất theo case **Trợ lý điều phối sạc khẩn cấp cho tài xế Xanh SM**.

## 1. Ô Tô Và Di Chuyển Xanh

| # | Công ty | Tên bài toán / Bottleneck | Lens | Mô tả ngắn |
|---|---|---|---|---|
| 1 | Xanh SM | Điều phối sạc khẩn cấp | Stakeholder Pain | Tài xế xe điện pin yếu cần phương án sạc hoặc cứu hộ nhanh, an toàn và có người duyệt. |
| 2 | Xanh SM | Điều vận thông minh | Time-consuming | Tối ưu điểm đón và gán lại chuyến khi tài xế bị kẹt xe, thiếu pin hoặc khách đổi điểm đến. |
| 3 | Xanh SM | Phân tích lý do hủy chuyến | AI-upgrade | Tóm tắt ghi âm, ghi chú tài xế và phản hồi khách hàng để tìm pattern lỗi vận hành. |
| 4 | VinFast | Đối chiếu hóa đơn sạc điện | Repetitive | So khớp dữ liệu sạc từ trạm đối tác với hóa đơn thực tế gửi về hệ thống tài chính. |
| 5 | VinFast | Dự đoán bảo trì pin | AI-upgrade | Phân tích log pin, chu kỳ sạc và tín hiệu lỗi để cảnh báo bảo trì trước khi xe gặp sự cố. |

## 2. Đô Thị Và Dịch Vụ Khách Hàng

| # | Công ty | Tên bài toán / Bottleneck | Lens | Mô tả ngắn |
|---|---|---|---|---|
| 6 | Vinhomes | Phân loại phản ánh cư dân | Repetitive | Route phản ánh về mất nước, hỏng đèn, ồn ào hoặc phí dịch vụ đến đúng ban quản lý/bộ phận. |
| 7 | Vinhomes | Trợ lý thủ tục cư dân | Time-consuming | Hỗ trợ cư dân chuẩn bị hồ sơ đăng ký thi công nội thất, vé gửi xe hoặc giấy xác nhận. |
| 8 | Vinpearl | Tổng hợp review khách sạn | Stakeholder Pain | Lọc review tiêu cực khẩn cấp từ Booking, Agoda, Google Maps để gửi về quản lý cơ sở. |
| 9 | Vinpearl / VinWonders | Trợ lý FAQ dịch vụ | Repetitive | Trả lời câu hỏi lặp lại về vé, giờ mở cửa, combo, đổi ngày và hoàn tiền bằng bản nháp có kiểm duyệt. |

## 3. Y Tế Và Giáo Dục

| # | Công ty | Tên bài toán / Bottleneck | Lens | Mô tả ngắn |
|---|---|---|---|---|
| 10 | Vinmec | Tóm tắt hồ sơ xuất viện | Time-consuming | Trích xuất thông tin từ bệnh án điện tử, xét nghiệm và đơn thuốc để soạn bản tóm tắt cho bác sĩ duyệt. |
| 11 | Vinmec | Phân loại lịch hẹn khám ban đầu | Stakeholder Pain | Gợi ý chuyên khoa phù hợp từ mô tả triệu chứng của khách hàng, luôn cần nhân viên y tế kiểm tra. |
| 12 | VinUni | Phản hồi bài lab | Repetitive | Hỗ trợ autograder và LLM tạo phản hồi học tập cho sinh viên dựa trên lỗi code và rubric. |

## Lưu Ý Khi Chọn Bài Toán

1. **Problem First, AI Second:** Chọn bài toán có workflow rõ trước khi chọn model.
2. **Metric phải đo được:** Ưu tiên thời gian xử lý, tỷ lệ route sai, tỷ lệ chấp nhận, số lỗi boundary.
3. **Boundary phải cụ thể:** Ghi rõ AI được phép làm gì, không được phép làm gì và khi nào phải chuyển cho người duyệt.
4. **Rule trước Agent:** Với tình huống an toàn vận hành, tài chính, pháp lý hoặc y tế, rule-based gate và human review thường cần thiết hơn agent tự động.

