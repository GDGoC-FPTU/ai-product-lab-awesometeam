# AI Log & Reflection

## Thông Tin Cá Nhân

**Tên nhóm:** AwesomeTeam

| Họ và tên | Email | Vai trò / Đóng góp vào reflection và prototype |
|---|---|---|
| Lê Mạnh Cương | lemanhcuong_t67@hus.edu.vn | Trưởng nhóm, brainstorm bài toán và tổng hợp lựa chọn cuối |
| Nguyễn Tuấn Anh | anhtt44t@gmail.com | Review metric, business impact và logic deep-dive |
| Lê Tiến Minh | mle409640@gmail.com | Viết system prompt, adversarial tests và chạy prototype |
| Vũ Ngọc Thiện | vungocthien843@gmail.com | Ghi nhận workflow hiện tại, handoff và bottleneck |
| Hoàng Duy Linh | hduylinh7@gmail.com | Tổng hợp AI log, chuẩn hóa reflection và format |
| Nguyễn Tuấn Anh | tuanhhhh204@gmail.com | Review boundary, fallback và kết quả kiểm thử |

## Reflection - Lê Mạnh Cương

### AI đã giúp gì?

Tôi dùng AI để brainstorm các vấn đề vận hành trong Xanh SM, Vinhomes, VinFast, Vinpearl và Vinmec. AI giúp nhóm nhanh chóng chuyển các ý tưởng rộng thành workflow cụ thể có actor, bottleneck và metric. AI cũng gợi ý cách viết Problem Statement theo 6 trường và đề xuất adversarial prompt để tấn công boundary.

### AI sai hoặc chưa hợp lý ở đâu?

Lúc đầu AI đề xuất dùng Agentic Loop để tự tìm trạm sạc, tự gửi tin nhắn và tự điều xe cứu hộ. Cách này quá rủi ro vì đây là hành động vận hành thật, có thể ảnh hưởng tài xế và khách hàng. AI cũng đưa ra một số con số như tỷ lệ chấp nhận 95% mà không có log thực tế, nên nhóm chỉ xem đó là baseline giả định.

### Đã sửa prompt, metric hoặc boundary như thế nào?

Nhóm chuyển từ agent tự động sang LLM Feature kết hợp Rule-based Safety Gate. Prompt được sửa để bắt buộc mọi output bắt đầu bằng `[DRAFT_ONLY]`, không được nói đã gửi tin nhắn và không được bỏ qua điều phối viên. Metric được sửa thành các ngưỡng đo được: dưới 30 giây tạo draft, pin dưới 5% không đề xuất trạm xa hơn 5 km, 0 action tự động khi chưa duyệt.

### Bài học rút ra

AI hữu ích khi cần mở rộng và cấu trúc hóa ý tưởng, nhưng các quy tắc an toàn định lượng nên được xử lý bằng rule-based code. LLM phù hợp với việc hiểu ngôn ngữ và soạn bản nháp, không nên được giao hành động thật trong prototype đầu tiên.

## Reflection - Nguyễn Tuấn Anh (anhtt44t@gmail.com)

### AI đã giúp gì?

AI giúp tôi đóng vai CFO và Operations Manager để phản biện xem bài toán có đáng làm hay không. Nhờ đó nhóm bỏ các ý tưởng quá chung chung và chọn bài toán Xanh SM vì có tác động trực tiếp đến thời gian điều phối.

### AI sai hoặc chưa hợp lý ở đâu?

AI có xu hướng viết metric đẹp nhưng khó chứng minh, ví dụ "tăng hài lòng tài xế" mà không nói cách đo. AI cũng chưa tự tách rõ bước nào là AI Step, bước nào là Human Step.

### Đã sửa prompt, metric hoặc boundary như thế nào?

Tôi yêu cầu AI viết lại metric theo dạng có số: thời gian xử lý, tỷ lệ chấp nhận, tỷ lệ vi phạm boundary, số tin nhắn gửi tự động. Boundary được viết lại thành danh sách "AI được phép" và "AI không được phép" để dễ test.

### Bài học rút ra

Scoping AI Product không chỉ là chọn model. Phải biết điểm nào cần AI, điểm nào cần rule và điểm nào bắt buộc cần người phê duyệt.

## Reflection - Lê Tiến Minh

### AI đã giúp gì?

AI hỗ trợ tôi viết system prompt và adversarial tests cho `prompt_prototype.py`. Các test tập trung vào việc người dùng cố tình bảo model bỏ tag `[DRAFT_ONLY]`, gửi tin nhắn luôn hoặc bỏ qua ngưỡng pin 5%.

### AI sai hoặc chưa hợp lý ở đâu?

Có lúc AI viết prompt quá dài nhưng thiếu output format rõ ràng, khiến việc verify bằng code khó hơn. AI cũng đề xuất check bằng cảm tính thay vì check chuỗi `Passed`/`Failed` phù hợp với autograder.

### Đã sửa prompt, metric hoặc boundary như thế nào?

Tôi thêm structured JSON vào output, thêm fallback local khi chưa có API key và thêm verification check đảm bảo output có `[DRAFT_ONLY]` hoặc `dispatch_mobile_charger` trong case pin dưới 5%.

### Bài học rút ra

Prompt tốt cần đi kèm test. Nếu không có adversarial test, nhóm rất dễ tự tin sai về boundary của model.

## Reflection - Vũ Ngọc Thiện

### AI đã giúp gì?

AI giúp tôi biến mô tả tình huống pin yếu thành workflow hiện tại có các bước, handoff, thời gian và bottleneck rõ hơn. Tôi dùng AI để kiểm tra xem sơ đồ có bỏ sót bước chuyển giao giữa tài xế, điều phối viên và hệ thống trạm sạc hay không.

### AI sai hoặc chưa hợp lý ở đâu?

AI có lúc mô tả workflow quá lý tưởng, giả định hệ thống đã tự lấy đủ GPS, mức pin và trạng thái trạm sạc. Trong thực tế, điều phối viên vẫn phải xác nhận dữ liệu và không thể bỏ qua bước hỏi lại tài xế khi thông tin thiếu.

### Đã sửa prompt, metric hoặc boundary như thế nào?

Tôi bổ sung rõ các điểm handoff và fallback khi thiếu dữ liệu. Boundary được giữ theo hướng AI chỉ tạo bản nháp, còn điều phối viên là người review và quyết định hành động cuối.

### Bài học rút ra

Workflow càng cụ thể thì việc chọn AI Fit càng dễ. Nếu không vẽ rõ bước thủ công hiện tại, nhóm rất dễ dùng AI cho sai phần của quy trình.

## Reflection - Hoàng Duy Linh

### AI đã giúp gì?

AI giúp tôi chuẩn hóa cách diễn đạt giữa các file để cùng dùng một bài toán, cùng metric và cùng ranh giới vận hành. AI cũng hỗ trợ phát hiện các chỗ nội dung bị lệch như thời gian xử lý, tên kiến trúc và quyết định GO.

### AI sai hoặc chưa hợp lý ở đâu?

AI đôi khi dùng thuật ngữ không thống nhất, ví dụ lúc gọi là Agentic Loop, lúc gọi là LLM Feature, hoặc viết boundary chưa đủ chặt. Nếu không kiểm tra thủ công, các file có thể mâu thuẫn nhau.

### Đã sửa prompt, metric hoặc boundary như thế nào?

Tôi giữ cùng một bộ thuật ngữ: Rule-based Safety Gate, LLM Draft và Human-in-the-loop. Các metric được giữ nhất quán: draft dưới 30 giây, điều phối dưới 2 phút, không đề xuất trạm xa hơn 5 km khi pin dưới 5%.

### Bài học rút ra

AI hữu ích cho việc biên tập và chuẩn hóa, nhưng vẫn cần người kiểm tra tính nhất quán cuối cùng giữa các deliverable.

## Reflection - Nguyễn Tuấn Anh (tuanhhhh204@gmail.com)

### AI đã giúp gì?

AI giúp tôi rà lại operational boundary, fallback và kết quả kiểm thử để xem prototype có bảo vệ đúng các tình huống nguy hiểm không. Tôi dùng AI để nghĩ thêm các prompt tấn công như ép gửi tin ngay, bỏ tag `[DRAFT_ONLY]` hoặc tự đoán dữ liệu thiếu.

### AI sai hoặc chưa hợp lý ở đâu?

AI có xu hướng tin rằng prompt đủ để chặn mọi lỗi. Với bài toán vận hành thật, chỉ prompt là chưa đủ; cần rule-based guardrail chạy trước LLM cho các điều kiện như pin dưới 5% và khoảng cách trạm sạc.

### Đã sửa prompt, metric hoặc boundary như thế nào?

Tôi đề xuất giữ guardrail cục bộ trong prototype và bắt buộc output có cấu trúc JSON. Fallback được bổ sung để khi thiếu pin hoặc khoảng cách trạm, hệ thống yêu cầu thêm dữ liệu thay vì tự suy đoán.

### Bài học rút ra

Boundary tốt phải kiểm thử được bằng code. Khi test trả về `Passed` rõ ràng, nhóm dễ chứng minh prototype an toàn hơn so với chỉ mô tả bằng lời.
