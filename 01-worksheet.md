# Lab 02 - Worksheet: AI Product Scoping

## 1. Bối Cảnh: Vin Smart Future

**Vin Smart Future** là đơn vị công nghệ giả định chịu trách nhiệm tìm kiếm, scope và thử nghiệm các giải pháp AI cho các công ty thành viên Vingroup như VinFast, Xanh SM, Vinhomes, Vinmec, Vinpearl và VinWonders.

Trong lab này, nhóm đóng vai **AI Product Engineer**. Nhiệm vụ là chọn một bài toán vận hành thực tế, phân tích workflow hiện tại, xác định ranh giới vận hành và xây dựng prompt prototype để kiểm thử an toàn.

Repo này thống nhất chọn bài toán:

> **Trợ lý điều phối sạc khẩn cấp cho tài xế Xanh SM khi xe điện sắp hết pin.**

## 2. Cơ Cấu Tính Điểm

### Điểm nhóm: 60 điểm

| Gate | Điểm | Deliverable | Tiêu chí chấm |
|---|---:|---|---|
| G1. Workflow Mapping | 20 | `02-deep-dive-report.md` và `04-workflow-diagram.png` | Quy trình hiện tại có bước, handoff, thời gian và bottleneck rõ |
| G2. Problem Statement | 20 | `02-deep-dive-report.md` | Problem Statement 6-field có metric và boundary cụ thể |
| G3. AI Fit & Future Flow | 10 | `02-deep-dive-report.md` | So sánh Rule, LLM, Agent; có future flow, fallback và HITL |
| G4. Decision Quality | 10 | `02-deep-dive-report.md` | Quyết định GO / NOT YET / NO-GO có bằng chứng |

### Điểm cá nhân: 40 điểm

| Gate | Điểm | Deliverable | Tiêu chí chấm |
|---|---:|---|---|
| I1. Scan & Cards | 15 | `01-problem-scan.md` | Có ít nhất 5 bài toán và 3 Quick Problem Cards |
| I2. Prototyping | 10 | `starter-code/prompt_prototype.py` | Chạy được prompt prototype và boundary tests |
| I3. AI Log & Reflection | 15 | `03-ai-log.md` | Phản ánh trung thực: AI giúp gì, sai gì, nhóm sửa gì |

---

# Phase 1 - SCAN

Dùng 4 lenses để quét bài toán vận hành:

1. **Repetitive:** Tác vụ lặp đi lặp lại nhiều lần mỗi ngày.
2. **Time-consuming:** Tác vụ thủ công tốn nhiều thời gian.
3. **AI-upgrade:** Quy trình hiện tại có thể tốt hơn nếu có AI hỗ trợ.
4. **Stakeholder Pain:** Bottleneck khiến khách hàng, nhân viên hoặc đối tác phàn nàn.

## Danh Sách Bài Toán

| # | Công ty | Lens | Mô tả ngắn bài toán |
|---|---|---|---|
| 1 | Xanh SM | Stakeholder Pain | Tài xế xe điện pin yếu cần phương án sạc hoặc cứu hộ nhanh, tránh hết pin giữa đường. |
| 2 | Xanh SM | Repetitive | Điều phối viên phải gán lại chuyến xe liên tục khi tài xế thiếu pin, kẹt xe hoặc hủy chuyến. |
| 3 | Vinhomes | Time-consuming | CSKH đọc và route phản ánh cư dân đến đúng bộ phận thủ công. |
| 4 | VinFast | AI-upgrade | Đội kỹ thuật phân tích log pin và lịch sử sạc để dự đoán bảo trì xe điện. |
| 5 | Vinpearl / VinWonders | Repetitive | CSKH trả lời lặp lại câu hỏi về vé, giờ mở cửa, đổi ngày và hoàn tiền. |
| 6 | Vinmec | Time-consuming | Bác sĩ soạn tóm tắt xuất viện từ nhiều nguồn dữ liệu lâm sàng. |

---

# Phase 2 - QUICK-ASSESS

## Quick Problem Card 1

**Bài toán:** Hỗ trợ điều phối phương án sạc an toàn cho tài xế Xanh SM khi xe điện sắp hết pin.

**Công ty thành viên:** Xanh SM

**Actor:** Tài xế Xanh SM và điều phối viên trung tâm điều phối.

**Workflow thủ công hiện tại:**

```text
Tài xế báo pin yếu
  -> Điều phối viên hỏi mức pin, vị trí, loại xe
  -> Điều phối viên tra dashboard trạm sạc
  -> Điều phối viên đánh giá có thể đến trạm hay cần cứu hộ
  -> Điều phối viên soạn hướng dẫn và gửi sau khi tự kiểm tra
```

**Bước tốn thời gian/lỗi nhất:** Thu thập dữ liệu, tra cứu trạm và đánh giá an toàn, khoảng 8-10 phút/lượt.

**AI hỗ trợ ở đâu:** Rule Engine kiểm tra ngưỡng pin/khoảng cách; LLM soạn khuyến nghị nháp và tin nhắn cho tài xế.

**Metric có số:**

- Giảm thời gian điều phối từ 10 phút xuống dưới 2 phút/lượt.
- Tạo draft dưới 30 giây khi đủ dữ liệu.
- 100% output có `[DRAFT_ONLY]`.
- 100% case pin dưới 5% không đề xuất trạm xa hơn 5 km.

**Quick Architecture:** Rule-based Safety Gate + LLM Feature + Human-in-the-loop.

## Quick Problem Card 2

**Bài toán:** Tự động phân loại và route phản ánh cư dân Vinhomes đến đúng bộ phận.

**Công ty thành viên:** Vinhomes

**Actor:** Nhân viên CSKH, ban quản lý tòa nhà, bộ phận kỹ thuật/an ninh/kế toán.

**Workflow thủ công hiện tại:**

```text
Cư dân gửi phản ánh
  -> CSKH đọc nội dung
  -> CSKH xác định tòa/căn hộ và loại vấn đề
  -> CSKH chuyển ticket
  -> CSKH soạn phản hồi ban đầu
```

**Bước tốn thời gian/lỗi nhất:** Phân loại và route ticket mơ hồ, khoảng 8-12 phút/ticket.

**AI hỗ trợ ở đâu:** LLM trích xuất thông tin, phân loại intent, đề xuất bộ phận nhận và soạn phản hồi nháp.

**Metric có số:**

- 85% ticket được phân loại trong dưới 30 giây.
- Giảm ticket chuyển sai từ 12% xuống dưới 4%.
- 100% ticket nhạy cảm phải có người duyệt.

**Quick Architecture:** LLM Feature + Rule routing.

## Quick Problem Card 3

**Bài toán:** Hỗ trợ CSKH Vinpearl trả lời câu hỏi lặp lại về vé, combo, giờ mở cửa và hoàn tiền.

**Công ty thành viên:** Vinpearl / VinWonders

**Actor:** Nhân viên CSKH, khách du lịch và nhân viên bán vé.

**Workflow thủ công hiện tại:**

```text
Khách gửi câu hỏi
  -> CSKH xác định khu vui chơi/ngày sử dụng/loại vé
  -> CSKH tra chính sách
  -> CSKH soạn phản hồi
  -> Nếu hoàn tiền hoặc đổi vé, chuyển cấp trên duyệt
```

**Bước tốn thời gian/lỗi nhất:** Tra chính sách và soạn phản hồi, khoảng 5-7 phút/câu hỏi.

**AI hỗ trợ ở đâu:** Retrieval từ FAQ nội bộ, LLM soạn phản hồi nháp, rule đánh dấu giao dịch nhạy cảm.

**Metric có số:**

- Giảm thời gian soạn phản hồi từ 6 phút xuống dưới 1 phút.
- 90% câu hỏi FAQ được trả lời đúng chính sách.
- 100% yêu cầu hoàn tiền/đổi vé có human review.

**Quick Architecture:** Retrieval + LLM Feature + Human-in-the-loop.

---

# Phase 3 - DEEP-DIVE

## 3.1 Current-State Workflow Mapping

Workflow hiện tại của bài toán được chọn:

```text
Tài xế phát hiện pin yếu
  -> Gọi tổng đài hoặc gửi yêu cầu trên app
  -> Điều phối viên hỏi mức pin, vị trí, loại xe, trạng thái chuyến xe
  -> Điều phối viên tra bản đồ và dashboard trạm sạc
  -> Điều phối viên đánh giá thủ công rủi ro pin/khoảng cách
  -> Điều phối viên soạn hướng dẫn hoặc gọi đội cứu hộ theo quy trình
```

**Tổng thời gian hiện tại:** Khoảng 10 phút/lượt.

**Bottleneck chính:** Bước tra cứu trạm và đánh giá an toàn khi pin dưới 5%.

## 3.2 Problem Statement 6-Field

| Field | Nội dung |
|---|---|
| Actor / Operator | Tài xế Xanh SM và điều phối viên trung tâm điều phối |
| Current Workflow | Tài xế báo pin yếu, điều phối viên thu thập dữ liệu, tra trạm, đánh giá an toàn, soạn hướng dẫn |
| Bottleneck | Tra cứu nhiều nguồn và ra quyết định an toàn trong thời gian ngắn |
| Business Impact | Mỗi yêu cầu tốn khoảng 10 phút, xe dừng lâu, dễ trễ chuyến hoặc cần cứu hộ |
| Success Metric | Draft dưới 30 giây, thời gian điều phối dưới 2 phút, 0 action tự động khi chưa duyệt |
| Operational Boundary | AI chỉ tạo bản nháp; không tự gửi tin, không tự đặt trạm, không tự điều xe; pin dưới 5% không đề xuất trạm xa hơn 5 km |

## 3.3 Future-State Flow & AI Fit

**AI Fit:** Rule-based Safety Gate + LLM Feature. Chưa dùng Agentic Loop trong prototype vì agent có thể tạo hành động thật trong một tình huống có rủi ro vận hành.

```text
Tài xế gửi yêu cầu
  -> Hệ thống lấy mức pin, vị trí, loại xe
  -> Rule Engine kiểm tra dữ liệu bắt buộc
  -> Rule Engine áp dụng ngưỡng an toàn pin/khoảng cách
  -> LLM soạn [DRAFT_ONLY] recommendation
  -> Điều phối viên review, chỉnh sửa và phê duyệt
  -> Hệ thống mới gửi hướng dẫn hoặc tạo yêu cầu cứu hộ
```

**Fallback:** Nếu thiếu dữ liệu, Gemini timeout, output sai JSON hoặc không có `[DRAFT_ONLY]`, hệ thống dừng output AI và chuyển về quy trình thủ công.

---

# Phase 4 - Technical Prompt Prototype

Prototype nằm tại:

```text
starter-code/prompt_prototype.py
```

Prototype cần kiểm thử ít nhất ba nhóm tấn công:

1. Người dùng yêu cầu bỏ tag `[DRAFT_ONLY]`.
2. Người dùng yêu cầu gửi tin nhắn hoặc điều xe ngay.
3. Người dùng ép model đề xuất trạm xa hơn 5 km khi pin dưới 5%.

Chạy thử:

```bash
python starter-code/prompt_prototype.py
```

---

# Phase 5 - EVALUATE

## AI Readiness Checklist

| Câu hỏi | Trạng thái | Ghi chú |
|---|---|---|
| Có dữ liệu mẫu/log sạch để test? | Có một phần | Cần log điều phối đã ẩn danh và dữ liệu trạm sạc mẫu |
| Rủi ro AI sai có kiểm soát được? | Có | Rule gate + `[DRAFT_ONLY]` + human review |
| Stakeholder sẵn sàng đổi workflow? | Có thể pilot | Nên thử với một nhóm điều phối viên trong giờ thấp điểm |

## Quyết Định Cuối Cùng

**GO** với prototype phạm vi hẹp.

Lý do: Bài toán có metric rõ, boundary định lượng và rủi ro có thể kiểm soát bằng rule gate và human review. Không triển khai agent tự động hành động ở giai đoạn đầu.

---

# Phase 6 - REFLECTION

Ghi phản ánh cá nhân vào `03-ai-log.md`, tập trung vào ba câu hỏi:

1. AI đã giúp gì?
2. AI sai hoặc chưa hợp lý ở đâu?
3. Nhóm đã sửa prompt, metric hoặc boundary như thế nào?

