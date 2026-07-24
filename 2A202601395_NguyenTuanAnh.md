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

Phase 2 — QUICK-ASSESS
Ba bài toán được chọn
Phân loại và điều hướng phản ánh cư dân Vinhomes.
Đối chiếu giao dịch sạc với hóa đơn đối tác VinFast.
Phát hiện review khách sạn cần xử lý khẩn tại Vinpearl.
QUICK PROBLEM CARD #1 — Phân loại và điều hướng phản ánh cư dân
Bài toán (1 câu): Giảm thời gian nhân viên Vinhomes đọc và chuyển phản ánh tự do của cư dân đến đúng đội vận hành/tòa nhà.
Công ty thành viên: [ ] VinFast [ ] Xanh SM [x] Vinhomes [ ] Vinmec [ ] Khác
Ai đang đau (Actor)? Nhân viên CSKH, ban quản lý tòa nhà và cư dân chờ phản hồi.
Workflow thủ công hiện tại:
Cư dân gửi phản ánh kèm ảnh qua ứng dụng.
Nhân viên CSKH đọc nội dung, xác định loại sự cố, mức độ khẩn và tòa nhà/căn hộ.
Nhân viên tìm đội kỹ thuật hoặc ban quản lý phù hợp để tạo và chuyển ticket.
Đội nhận ticket kiểm tra lại thông tin rồi liên hệ cư dân.
Bước tốn thời gian/lỗi nhất: Bước 2–3, vì nội dung phản ánh thường mơ hồ và dễ chuyển sai nơi nhận — khoảng 5 phút/ticket.
AI hỗ trợ ở đâu: LLM đề xuất danh mục, mức độ ưu tiên và đội nhận ticket; rule kiểm tra mã tòa nhà/căn hộ. Nhân viên CSKH phải duyệt trước khi ticket được chuyển.
Metric thành công: Giảm thời gian phân luồng từ 5 phút xuống dưới 2 phút/ticket; tối thiểu 90% ticket được duyệt mà không cần đổi danh mục hoặc đội nhận.
Quick Architecture: [ ] No AI [ ] Rule [x] LLM [ ] Agent
QUICK PROBLEM CARD #2 — Đối chiếu giao dịch sạc với hóa đơn đối tác
Bài toán (1 câu): Tự động so khớp giao dịch sạc có cấu trúc với hóa đơn đối tác để kế toán chỉ xử lý các trường hợp sai lệch.
Công ty thành viên: [x] VinFast [ ] Xanh SM [ ] Vinhomes [ ] Vinmec [ ] Khác
Ai đang đau (Actor)? Nhân viên kế toán đối soát và quản lý tài chính phụ trách chốt công nợ.
Workflow thủ công hiện tại:
Kế toán tải file giao dịch sạc từ hệ thống và file hóa đơn từ đối tác.
Chuẩn hóa ngày giờ, mã trạm, mã giao dịch và số tiền.
Dùng bảng tính dò từng dòng, đánh dấu giao dịch thiếu hoặc lệch tiền.
Điều tra các dòng lệch và gửi yêu cầu điều chỉnh cho đối tác.
Bước tốn thời gian/lỗi nhất: Bước 2–3, do dữ liệu từ các nguồn có định dạng khác nhau — khoảng 30 phút/1.000 giao dịch.
AI hỗ trợ ở đâu: Không cần LLM. Rule-based ETL chuẩn hóa dữ liệu và đối chiếu theo mã giao dịch, thời gian, mã trạm, số tiền; các ngoại lệ đi vào hàng chờ để kế toán kiểm tra.
Metric thành công: Tối thiểu 95% giao dịch được đối chiếu tự động; giảm thời gian xử lý 1.000 giao dịch từ 30 phút xuống dưới 5 phút; 100% giao dịch lệch được kế toán phê duyệt kết quả cuối.
Quick Architecture: [ ] No AI [x] Rule [ ] LLM [ ] Agent
QUICK PROBLEM CARD #3 — Phát hiện review khách sạn cần xử lý khẩn
Bài toán (1 câu): Giúp quản lý Vinpearl phát hiện sớm review có vấn đề khẩn và nhận bản tóm tắt hành động thay vì phải đọc thủ công toàn bộ review.
Công ty thành viên: [ ] VinFast [ ] Xanh SM [ ] Vinhomes [ ] Vinmec [x] Khác: Vinpearl
Ai đang đau (Actor)? Quản lý vận hành khách sạn, đội lễ tân/housekeeping và khách đang gặp sự cố.
Workflow thủ công hiện tại:
Quản lý mở các kênh review theo ngày.
Đọc từng review bằng tiếng Việt hoặc tiếng Anh.
Tự nhận diện nội dung tiêu cực/khẩn và ghi chú nguyên nhân.
Gửi tin nhắn hoặc tạo việc cho bộ phận chịu trách nhiệm.
Bước tốn thời gian/lỗi nhất: Bước 2–3, do review dài, đa ngôn ngữ và mức độ khẩn khó đánh giá nhất quán — khoảng 25 phút/ngày/cơ sở.
AI hỗ trợ ở đâu: LLM tóm tắt, gán nhãn chủ đề và đề xuất mức ưu tiên; rule bắt buộc gắn cờ từ khóa an toàn/sức khỏe. Quản lý duyệt trước khi giao việc hoặc phản hồi công khai.
Metric thành công: Giảm thời gian tổng hợp review từ 25 phút xuống dưới 7 phút/ngày/cơ sở; phát hiện tối thiểu 95% review khẩn được quản lý gắn nhãn; 100% phản hồi gửi khách phải do nhân viên phê duyệt.
Quick Architecture: [ ] No AI [ ] Rule [x] LLM [ ] Agent
