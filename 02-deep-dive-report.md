# Lab 02 — Deep Dive Report

## Thông tin nhóm
- Tên nhóm: Awesome Team
- Thành viên đóng góp:
  - Thành viên 1 — MSSV: [chưa cập nhật]
  - Thành viên 2 — MSSV: [chưa cập nhật]

---

## Quyết định lựa chọn bài toán
Nhóm lựa chọn bài toán: **Xanh SM — Sự cố pin thực địa của tài xế EV taxi**.

Lý do chọn:
- Bài toán có thể đo được bằng thời gian xử lý và có tác động trực tiếp tới SLA vận hành.
- Dữ liệu đầu vào và output có cấu trúc rõ: vị trí xe, trạng thái pin, trạm sạc gần nhất, tin nhắn hướng dẫn.
- Rủi ro có thể kiểm soát bằng human-in-the-loop và fallback thủ công.

---

## Problem Statement (6-field)

| Field | Nội dung |
|---|---|
| **1. Actor / Operator** | Điều phối viên trung tâm Xanh SM đang xử lý sự cố pin của tài xế EV taxi. |
| **2. Current Workflow** | Khi tài xế báo hết pin giữa đường, điều phối viên phải mở hệ thống định vị, tra trạm sạc gần nhất, đối chiếu loại cổng sạc, soạn tin nhắn hướng dẫn, và nếu pin < 5% thì gọi xe cứu hộ. |
| **3. Bottleneck** | Bước tra cứu trạm sạc còn trụ trống và bước soạn tin nhắn hướng dẫn là chậm nhất, mất khoảng 10-12 phút/lượt. |
| **4. Business Impact** | Mỗi sự cố pin kéo theo thời gian chờ xe, tăng áp lực đội điều vận, và có thể làm mất doanh thu do tài xế không thể tiếp tục chuyến. |
| **5. Success Metric** | Giảm thời gian xử lý sự cố từ 12 phút xuống dưới 3 phút; đạt 95% độ chính xác khi lựa chọn trạm sạc hoặc xe cứu hộ. |
| **6. Operational Boundary** | AI được phép đề xuất trạm sạc, định vị và soạn nháp tin nhắn; AI tuyệt đối không được tự động gửi tin cho tài xế mà không qua phê duyệt. Nếu pin <= 5%, AI phải không đề xuất trạm sạc xa hơn 5km và phải trả về lệnh dispatch_mobile_charger. |

---

## Future-State Flow & AI Fit

### AI Fit
- Chọn: **LLM Feature**
- Không chọn Agentic Loop vì quy trình hiện đã có cấu trúc rõ ràng, rủi ro cao nếu AI tự ra quyết định mà không được hậu kiểm.

### Future-State Flow
```text
Tài xế báo sự cố pin
    ↓
Điều phối viên mở hệ thống
    ↓
🔵 AI truy xuất vị trí xe + dữ liệu trạm sạc
    ↓
🔵 AI soạn nháp tin nhắn / đề xuất trạm phù hợp
    ↓
🟢 Dispatcher kiểm duyệt và gửi tin
    ↓
↩️ Fallback: nếu AI không chắc chắn, quay về workflow thủ công cũ
```

### Human-in-the-loop
- Người điều phối viên **bắt buộc phê duyệt** trước khi gửi tin nhắn.
- Nếu AI đưa ra quyết định về xe cứu hộ hoặc trạm sạc, hành động phải được kiểm tra lại bằng quy tắc nghiệp vụ.

---

## Evaluate

### AI Readiness Checklist
1. [x] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test.
2. [x] Rủi ro khi AI sai có nằm trong tầm kiểm soát qua HITL hoặc Fallback.
3. [x] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ.

### Quyết định cuối cùng
- **GO**

### Justification
Dự án này phù hợp để bắt đầu prototype vì:
- Hệ thống có scope hẹp và dễ đo lường.
- Có thể dùng LLM để draft tin nhắn và chọn trạm sạc gần nhất.
- Rủi ro an toàn được kiểm soát tốt bằng rule-based guardrails và phê duyệt của con người.
- Chi phí triển khai thấp hơn so với xây dựng agentic pipeline phức tạp.
