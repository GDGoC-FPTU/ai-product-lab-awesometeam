# Lab 02 — Problem Scan & Quick Assessment

## Tên nhóm: Awesome Team

# Phase 1 — SCAN (Cá nhân)

Dùng 4 lenses để quét các pain point trong các công ty thành viên của Vingroup.

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | Xanh SM | Lặp lại | Điều phối viên phải xử lý lại cuốc xe khi khách yêu cầu đổi điểm đón hoặc hủy chuyến do lỗi định vị. |
| 2 | Xanh SM | Tốn thời gian | Tài xế báo sự cố pin/không đủ pin giữa đường; điều phối viên phải tra cứu trạm sạc và soạn tin nhắn chỉ dẫn thủ công. |
| 3 | VinFast | Lặp lại | So khớp hóa đơn sạc điện, đối chiếu dữ liệu trạm sạc và báo cáo đối tác trong chu kỳ tuần. |
| 4 | Vinhomes | AI-upgrade | CSKH phải soạn phản hồi cho cư dân theo nhiều mẫu tương tự, mất thời gian và dễ rập khuôn. |
| 5 | Vinmec | Pain từ người khác | Bác sĩ mất thời gian viết tóm tắt hồ sơ xuất viện để chuyển cho bệnh viện hoặc phòng kế hoạch. |

---

# Phase 2 — QUICK-ASSESS (3 Quick Problem Cards)

## Quick Problem Card #1 — Xanh SM: Sự cố pin thực địa

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Tài xế Xanh SM báo sự cố pin giữa đường và cần   │
│ hướng dẫn đến trạm sạc gần nhất hoặc xe cứu hộ.            │
│ Công ty thành viên: [x] Xanh SM                             │
│                                                             │
│ Ai đang đau? Tài xế và điều phối viên                      │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                      │
│   1. Tài xế gọi tổng đài báo pin thấp                      │
│   → 2. Điều phối viên tra vị trí xe trên bản đồ nội bộ     │
│   → 3. Tra cứu trạm sạc phù hợp còn trụ trống              │
│   → 4. Soạn tin nhắn hướng dẫn gửi cho tài xế              │
│   → 5. Nếu pin dưới 5%, gọi xe cứu hộ                     │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3-4 (⏱ 12 phút/lượt) │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3-4              │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                      │
│ Giảm từ 12 phút xuống dưới 3 phút/lượt.                   │
│                                                             │
│ Quick Architecture: [ ] No AI [ ] Rule [x] LLM [ ] Agent  │
└─────────────────────────────────────────────────────────────┘
```

## Quick Problem Card #2 — Vinhomes: Phản hồi CSKH bị rập khuôn

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: CSKH Vinhomes phản hồi lại cư dân về khiếu nại    │
│ và yêu cầu quản lý cư dân bằng văn bản thủ công.           │
│ Công ty thành viên: [x] Vinhomes                            │
│                                                             │
│ Ai đang đau? Nhân viên CSKH và cư dân                      │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                      │
│   1. Nhận ticket khiếu nại                                  │
│   → 2. Đọc nội dung và chọn response mẫu                   │
│   → 3. Chỉnh sửa thủ công từng tin nhắn                    │
│   → 4. Gửi phản hồi và theo dõi SLA                        │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-3 (⏱ 8 phút/ticket)│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3              │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                      │
│ Giảm thời gian phản hồi từ 8 phút xuống dưới 2 phút.      │
│                                                             │
│ Quick Architecture: [ ] No AI [ ] Rule [x] LLM [ ] Agent  │
└─────────────────────────────────────────────────────────────┘
```

## Quick Problem Card #3 — Vinmec: Tóm tắt hồ sơ xuất viện

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: Bác sĩ Vinmec phải tóm tắt hồ sơ bệnh án xuất   │
│ viện thủ công trước khi chuyển tuyến hoặc xử lý tiếp.     │
│ Công ty thành viên: [x] Vinmec                              │
│                                                             │
│ Ai đang đau? Bác sĩ, bộ phận hành chính và bệnh nhân       │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                      │
│   1. Mở hồ sơ bệnh án và ghi chú                           │
│   → 2. Tóm tắt diễn biến lâm sàng và thuốc điều trị         │
│   → 3. Chuyển thông tin vào template xuất viện              │
│   → 4. Gửi cho bệnh viện/phòng kế hoạch                    │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 (⏱ 20 phút/bệnh án)│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2               │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                      │
│ Giảm thời gian tóm tắt từ 20 phút xuống dưới 5 phút.      │
│                                                             │
│ Quick Architecture: [ ] No AI [ ] Rule [x] LLM [ ] Agent  │
└─────────────────────────────────────────────────────────────┘
```
