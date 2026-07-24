# Deliverable Example - Vin Smart Future

> Đây là ví dụ bài nộp hoàn chỉnh cho cùng case mà repo đang sử dụng: **Trợ lý điều phối sạc khẩn cấp cho tài xế Xanh SM khi xe điện sắp hết pin**. File này dùng để đối chiếu format, metric và boundary; nội dung chính đã được chuẩn hóa với `01-problem-scan.md`, `02-deep-dive-report.md`, `03-ai-log.md` và `starter-code/prompt_prototype.py`.

## Bối Cảnh

Nhóm đóng vai AI Product Engineer tại Vin Smart Future và phối hợp với đội vận hành Xanh SM. Qua quan sát workflow điều phối, nhóm nhận thấy khi tài xế báo pin yếu, điều phối viên phải thu thập thông tin, tra cứu trạm sạc và đánh giá rủi ro thủ công trong thời gian ngắn. Nếu chọn sai trạm hoặc phản hồi chậm, xe có thể hết pin giữa đường, tài xế trễ chuyến và khách hàng bị ảnh hưởng.

## Phase 1 - SCAN

| # | Công ty | Lens | Mô tả ngắn bài toán |
|---|---|---|---|
| 1 | Xanh SM | Stakeholder Pain | Tài xế pin yếu cần phương án sạc hoặc cứu hộ nhanh. |
| 2 | Xanh SM | Repetitive | Điều phối viên gán lại chuyến xe khi tài xế thiếu pin, kẹt xe hoặc hủy chuyến. |
| 3 | Vinhomes | Time-consuming | CSKH phân loại và route phản ánh cư dân thủ công. |
| 4 | VinFast | AI-upgrade | Phân tích log pin và lịch sử sạc để dự đoán bảo trì xe điện. |
| 5 | Vinpearl / VinWonders | Repetitive | Trả lời lặp lại câu hỏi về vé, combo, giờ mở cửa và hoàn tiền. |
| 6 | Vinmec | Time-consuming | Tóm tắt hồ sơ xuất viện từ bệnh án, xét nghiệm và đơn thuốc. |

## Phase 2 - Quick Problem Card Tiêu Biểu

**Bài toán:** Tài xế Xanh SM báo xe sắp hết pin và cần điều phối phương án sạc hoặc cứu hộ an toàn.

**Công ty thành viên:** Xanh SM

**Actor:** Tài xế Xanh SM và điều phối viên trung tâm điều phối.

**Workflow hiện tại:**

```text
Tài xế báo pin yếu
  -> Điều phối viên hỏi mức pin, vị trí, loại xe
  -> Điều phối viên tra dashboard trạm sạc
  -> Điều phối viên đánh giá rủi ro pin/khoảng cách
  -> Điều phối viên soạn hướng dẫn hoặc gọi đội cứu hộ
```

**Bottleneck:** Bước thu thập dữ liệu, tra cứu trạm và đánh giá an toàn tốn khoảng 8-10 phút/lượt.

**AI hỗ trợ:** Rule Engine kiểm tra điều kiện định lượng; LLM tạo bản nháp khuyến nghị và tin nhắn `[DRAFT_ONLY]` cho điều phối viên review.

**Metric có số:**

- Giảm thời gian điều phối từ 10 phút xuống dưới 2 phút/lượt.
- Tạo draft dưới 30 giây khi đủ dữ liệu.
- 100% case pin dưới 5% không đề xuất trạm xa hơn 5 km.
- 0 hành động thật khi chưa có điều phối viên duyệt.

**Quick Architecture:** Rule-based Safety Gate + LLM Draft + Human-in-the-loop.

## Quyết Định Lựa Chọn

Nhóm chọn bài toán Xanh SM vì đây là bài toán có workflow rõ, dữ liệu đầu vào đo được, rủi ro có thể chặn bằng rule và giá trị vận hành trực tiếp. Các bài toán Vinhomes hoặc Vinpearl cũng phù hợp cho LLM, nhưng có thể để giai đoạn sau vì không khẩn cấp bằng tình huống pin yếu trên đường.

## Phase 3 - Deep-Dive

### Current-State Workflow

```text
Tài xế phát hiện pin yếu
  -> Gọi tổng đài hoặc gửi yêu cầu trên app
     Time: 1 phút

Điều phối viên nhận yêu cầu
  -> Hỏi mức pin, vị trí, loại xe, trạng thái chuyến xe
     Time: 2 phút

Điều phối viên tra dashboard trạm sạc
  -> Kiểm tra trạm gần nhất và khoảng cách
     Time: 3 phút

Điều phối viên đánh giá an toàn thủ công
  -> Nếu pin dưới 5%, cân nhắc xe cứu hộ sạc pin di động
     Time: 2 phút

Điều phối viên soạn hướng dẫn
  -> Gửi cho tài xế hoặc tạo yêu cầu cứu hộ theo quy trình
     Time: 2 phút

Tổng thời gian: 10 phút/lượt.
Bottleneck: tra cứu nhiều nguồn và đánh giá an toàn khi pin rất thấp.
```

### Problem Statement 6-Field

| Field | Nội dung |
|---|---|
| Actor / Operator | Tài xế Xanh SM và điều phối viên trung tâm điều phối |
| Current Workflow | Tài xế báo pin yếu, điều phối viên thu thập thông tin, tra trạm, đánh giá an toàn và soạn hướng dẫn |
| Bottleneck | Tra cứu nhiều nguồn và ra quyết định an toàn trong thời gian ngắn |
| Business Impact | Mỗi yêu cầu tốn 10 phút, xe dừng lâu, dễ trễ chuyến, có thể phải gọi cứu hộ |
| Success Metric | Draft dưới 30 giây, thời gian điều phối dưới 2 phút, 100% output có `[DRAFT_ONLY]` |
| Operational Boundary | AI không tự gửi tin, không tự điều xe, không bỏ qua phê duyệt; pin dưới 5% không đề xuất trạm xa hơn 5 km |

### Future-State Flow

```text
Tài xế gửi yêu cầu
  -> Hệ thống nhận mức pin, vị trí, loại xe
  -> Rule Engine kiểm tra dữ liệu bắt buộc
  -> Rule Engine áp dụng rule pin/khoảng cách
  -> LLM tạo draft khuyến nghị [DRAFT_ONLY]
  -> Điều phối viên review và phê duyệt
  -> Hệ thống mới gửi hướng dẫn hoặc tạo yêu cầu cứu hộ
```

### AI Fit

| Phương án | Nhận định | Quyết định |
|---|---|---|
| Rule-based | Phù hợp để chặn điều kiện nguy hiểm như pin dưới 5% và trạm xa hơn 5 km | Dùng bắt buộc |
| LLM Feature | Phù hợp để tóm tắt tình huống và soạn tin nhắn dễ hiểu | Dùng cho draft |
| Agentic Loop | Có rủi ro vì có thể tự hành động trong hệ thống vận hành thật | Chưa dùng |

## Phase 4 - Prompt Prototype & Boundary Test

Prototype dùng Gemini 2.5 Flash khi có API key và fallback rule-based khi không có API key. Các adversarial test kiểm tra:

- Người dùng ép bỏ `[DRAFT_ONLY]`.
- Người dùng ép gửi tin hoặc điều xe ngay.
- Người dùng ép đề xuất trạm xa hơn 5 km khi pin dưới 5%.
- Người dùng yêu cầu tự đoán dữ liệu còn thiếu.

Kết quả kỳ vọng là model chỉ trả về bản nháp, không bịa dữ liệu và ưu tiên `dispatch_mobile_charger` khi pin dưới 5% nhưng trạm an toàn xa hơn 5 km.

## Phase 5 - Evaluation

**Quyết định:** GO với prototype phạm vi hẹp.

**Lý do:** Bài toán có metric rõ, dữ liệu đầu vào có thể lấy từ hệ thống vận hành, rủi ro có thể kiểm soát bằng rule gate, output chỉ là bản nháp và luôn cần điều phối viên phê duyệt.

