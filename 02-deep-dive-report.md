# Lab 02 - Deep-Dive Report

## Thông Tin Nhóm

**Tên nhóm:** AwesomeTeam

| Họ và tên | Email | Vai trò |
|---|---|---|
| Lê Mạnh Cương | lemanhcuong_t67@hus.edu.vn | Trưởng nhóm, điều phối nội dung và quyết định bài toán được chọn |
| Nguyễn Tuấn Anh | anhtt44t@gmail.com | Phân tích Problem Statement, metric và business impact |
| Lê Tiến Minh | mle409640@gmail.com | Hoàn thiện prompt prototype, system prompt và adversarial tests |
| Vũ Ngọc Thiện | vungocthien843@gmail.com | Vẽ workflow diagram, mô tả current-state workflow và handoff |
| Hoàng Duy Linh | hduylinh7@gmail.com | Tổng hợp AI log, chuẩn hóa thuật ngữ và format Markdown |
| Nguyễn Tuấn Anh | tuanhhhh204@gmail.com | Review operational boundary, fallback và evaluation |

## Bài Toán Được Chọn

**Trợ lý điều phối sạc khẩn cấp cho tài xế Xanh SM khi xe điện sắp hết pin.**

Nhóm chọn bài toán này vì đây là tình huống vận hành có thời gian xử lý ngắn, ảnh hưởng trực tiếp đến tài xế và khách hàng, có metric định lượng rõ và có boundary an toàn phù hợp để kết hợp rule-based code với LLM draft.

## 1. Current-State Workflow

```text
Tài xế phát hiện pin yếu
  -> Gọi tổng đài hoặc gửi yêu cầu trên app
     Actor: Tài xế
     Time: 1 phút

Điều phối viên nhận yêu cầu
  -> Hỏi mức pin, vị trí, loại xe, trạng thái đang chở khách hay không
     Handoff: Tài xế -> Điều phối viên
     Time: 2 phút

Điều phối viên tra cứu bản đồ và dashboard trạm sạc
  -> Tìm các trạm sạc gần nhất, kiểm tra khoảng cách và khả năng phù hợp
     Handoff: Điều phối viên -> Hệ thống bản đồ/trạm sạc
     Time: 3 phút

Điều phối viên đánh giá an toàn thủ công
  -> Nếu pin quá thấp, cân nhắc xe cứu hộ sạc pin di động
     Bottleneck: dễ sai khi pin dưới 5% nhưng trạm gần nhất vẫn quá xa
     Time: 2 phút

Điều phối viên soạn hướng dẫn
  -> Gửi tin nhắn cho tài xế hoặc điều phối xe cứu hộ theo quy trình nội bộ
     Handoff: Điều phối viên -> Tài xế / đội cứu hộ
     Time: 2 phút

Tổng thời gian trung bình: 10 phút/lượt.
Bottleneck chính: tra cứu nhiều nguồn và đánh giá an toàn trong tình huống pin rất thấp.
```

## 2. Problem Statement 6-Field

### 2.1 Actor / Operator

Tài xế Xanh SM và điều phối viên trung tâm điều phối. Tài xế cần phương án nhanh, còn điều phối viên cần ra quyết định an toàn dựa trên mức pin, vị trí, loại xe, khoảng cách trạm sạc và trạng thái trạm.

### 2.2 Current Workflow

Khi xe gần hết pin, tài xế liên hệ trung tâm điều phối. Điều phối viên thu thập mức pin, vị trí, loại xe, trạng thái chuyến xe và tra cứu dashboard trạm sạc. Sau đó điều phối viên đánh giá xem xe có thể đến trạm sạc hay phải gọi xe cứu hộ sạc pin di động, rồi soạn hướng dẫn gửi lại cho tài xế.

### 2.3 Bottleneck

Điều phối viên phải tra cứu thủ công nhiều nguồn dữ liệu trong thời gian ngắn. Khi pin dưới 5%, việc đề xuất trạm sạc xa hơn 5 km có rủi ro làm xe hết pin giữa đường. Bottleneck nằm ở bước tra cứu trạm, đánh giá an toàn và soạn hướng dẫn.

### 2.4 Business Impact

- Mỗi yêu cầu tốn trung bình 10 phút xử lý thủ công.
- Xe dừng lâu làm giảm thời gian phục vụ khách và giảm doanh thu/chuyến.
- Tài xế bị áp lực, dễ hủy chuyến hoặc trễ đón khách.
- Nếu quyết định sai, Xanh SM có thể phải điều xe cứu hộ, ảnh hưởng trải nghiệm khách hàng và hình ảnh vận hành xe điện.

### 2.5 Success Metrics

- Tạo phương án xử lý dưới 30 giây cho mỗi yêu cầu có đủ dữ liệu.
- Giảm thời gian điều phối từ 10 phút xuống dưới 2 phút/lượt.
- Ít nhất 90% đề xuất được điều phối viên chấp nhận mà không cần sửa lớn.
- 100% trường hợp pin dưới 5% không đề xuất trạm sạc xa hơn 5 km.
- 100% output bắt đầu bằng `[DRAFT_ONLY]`.
- 0 tin nhắn hoặc lệnh thực tế được thực hiện khi chưa có điều phối viên phê duyệt.

### 2.6 Operational Boundary

AI được phép:

- Phân tích thông tin đầu vào: mức pin, vị trí, loại xe, khoảng cách trạm sạc và trạng thái trạm.
- Tạo khuyến nghị dạng nháp cho điều phối viên.
- Soạn tin nhắn nháp cho tài xế với tag `[DRAFT_ONLY]`.
- Nếu thiếu dữ liệu, liệt kê thông tin cần bổ sung.

AI không được phép:

- Tự gửi tin nhắn cho tài xế.
- Tự đặt trạm sạc, tự điều xe cứu hộ hoặc tự cập nhật hệ thống điều phối.
- Bỏ qua bước điều phối viên phê duyệt.
- Đề xuất trạm sạc xa hơn 5 km khi pin dưới 5%.
- Bịa đặt tọa độ, mức pin, tình trạng trạm sạc hoặc hành động đã thực hiện.

Quy tắc an toàn bắt buộc:

```json
{
  "if": "battery_percent < 5 and nearest_safe_station_km > 5",
  "action": "dispatch_mobile_charger",
  "requires_human_approval": true
}
```

## 3. AI Fit: Rule vs LLM vs Agent

| Phương án | Ưu điểm | Nhược điểm | Quyết định |
|---|---|---|---|
| Rule-based | Ổn định, dễ kiểm soát điều kiện pin, khoảng cách và ngưỡng an toàn | Không linh hoạt khi soạn hướng dẫn tự nhiên cho tài xế | Dùng làm safety gate bắt buộc |
| LLM Feature | Hiểu yêu cầu tự nhiên, tóm tắt tình huống, soạn tin nhắn rõ ràng | Có thể hallucinate hoặc bị prompt injection nếu không có boundary | Dùng để tạo draft |
| Agentic Loop | Có thể tự gọi API, tìm trạm, điều xe | Rủi ro cao vì có hành động thật trong tình huống an toàn vận hành | Chưa dùng trong prototype |

**Kiến trúc được chọn:** Rule-based Safety Gate + LLM Draft + Human-in-the-loop.

## 4. Future-State Flow

```text
Tài xế gửi yêu cầu
  -> Hệ thống đọc mức pin, vị trí, loại xe
  -> Rule Engine kiểm tra dữ liệu bắt buộc
  -> Rule Engine kiểm tra ngưỡng pin và khoảng cách
      - Nếu pin < 5% và trạm an toàn xa hơn 5 km:
        tạo action draft: dispatch_mobile_charger
      - Nếu pin >= 5% hoặc trạm gần nằm trong ngưỡng an toàn:
        đề xuất trạm sạc phù hợp
  -> LLM tạo nội dung [DRAFT_ONLY] bằng ngôn ngữ dễ hiểu
  -> Điều phối viên review
  -> Điều phối viên sửa/phê duyệt
  -> Hệ thống mới gửi hướng dẫn cho tài xế hoặc tạo yêu cầu cứu hộ
```

### AI Step

LLM chỉ tạo bản nháp khuyến nghị và tin nhắn. Rule Engine xử lý các điều kiện định lượng có rủi ro cao.

### Human-in-the-loop

Điều phối viên bắt buộc xem lại output trước khi bất kỳ tin nhắn nào được gửi hoặc bất kỳ xe cứu hộ nào được điều động.

### Fallback

- Thiếu mức pin, vị trí hoặc loại xe: dừng quy trình AI và yêu cầu tài xế bổ sung thông tin.
- Gemini timeout: dùng template rule-based có sẵn.
- Output không bắt đầu bằng `[DRAFT_ONLY]`: chặn output và tạo lại.
- Output sai JSON hoặc vi phạm boundary: không hiển thị cho tài xế, gắn cờ review cho trưởng ca.

## 5. Evaluation

| Câu hỏi readiness | Kết quả | Ghi chú |
|---|---|---|
| Có dữ liệu mẫu/log để test? | Có một phần | Cần lấy log điều phối đã ẩn danh, dữ liệu trạm sạc mẫu và case pin yếu. |
| Rủi ro AI sai có kiểm soát được? | Có | Rule gate kiểm tra pin/khoảng cách, LLM chỉ tạo draft, human review bắt buộc. |
| Stakeholder sẵn sàng đổi workflow? | Có thể thử nhỏ | Nên pilot với một nhóm điều phối viên trong giờ thấp điểm trước. |

## Final Decision: GO

Nhóm quyết định **GO** với prototype scope hẹp. Lý do: bài toán có metric rõ, boundary định lượng, rủi ro có thể kiểm soát bằng rule gate và human review. Không nên xây agent tự động hành động trong giai đoạn đầu; prototype chỉ nên tạo khuyến nghị và tin nhắn nháp.

Ước lượng chi phí prototype:

- 1 AI/Product Engineer trong 1-2 tuần để hoàn thiện prompt, adversarial test và logging.
- 1 Backend Engineer trong 1-2 tuần để nối dữ liệu mẫu về pin, vị trí và trạm sạc.
- 1 Operations reviewer từ Xanh SM để đánh giá 50-100 case mẫu.
- Chi phí API thấp trong pilot vì mỗi request chỉ tạo một draft ngắn.
