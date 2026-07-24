# 🔍 Phase 1 — SCAN & Phase 2 — QUICK-ASSESS

**Dự án:** Vin Smart Future (Vingroup)  
**Tác giả:** Hoàng Duy Linh - 2A202601159  
**Mục tiêu:** Quét các điểm nghẽn vận hành thực tế tại các công ty thành viên Vingroup và đề xuất các thẻ bài toán tiềm năng.

---

## 🔍 Phase 1 — SCAN: Danh sách bài toán vận hành Vingroup

Dưới đây là 6 bài toán thực tế được phát hiện thông qua khảo sát vận hành tại các công ty thành viên thuộc Tập đoàn Vingroup:

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | **Xanh SM (GSM)** | Lặp lại | So khớp và phân bổ lại cuốc xe khi khách hàng yêu cầu thay đổi điểm đến giữa chừng. |
| 2 | **Xanh SM (GSM)** | Tốn thời gian | Điều phối viên xử lý thủ công các phản hồi khẩn cấp từ tài xế về sự cố sạc pin hoặc va chạm thực địa (mất 15-20 min/lượt). |
| 3 | **VinFast** | Lặp lại | So khớp hóa đơn sạc điện và đối chiếu số liệu trạm sạc đối tác hằng tuần. |
| 4 | **Vinhomes** | AI-upgrade | Phân loại và tự động hóa trả lời phản hồi/khiếu nại của cư dân trên App Vinhomes Resident (đang mất 12 tiếng). |
| 5 | **Vinmec** | Stakeholder Pain | Bác sĩ mất quá nhiều thời gian viết tóm tắt hồ sơ xuất viện (mất 20-30 phút/bệnh nhân, gây quá tải). |
| 6 | **Xanh SM (GSM)** | Tốn thời gian | Tóm tắt lý do khách hàng hủy chuyến từ cuộc gọi ghi âm và ghi chú của tài xế để tìm pattern lỗi hệ thống. |

---

## 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

### 1. QUICK PROBLEM CARD #1: Xanh SM Xử lý sự cố sạc pin thực địa

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Tài xế Xanh SM báo cáo sự cố sạc pin / hết pin    │
│ giữa đường cần điều phối cứu hộ hoặc trạm sạc gần nhất.     │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau? Tài xế (chờ đợi), Điều phối viên (quá tải)     │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Tài xế gọi tổng đài điều vận báo hết pin               │
│   → 2. Điều phối viên tra cứu thủ công vị trí xe trên bản đồ│
│   → 3. Tra cứu thủ công các trạm sạc VinFast còn trụ trống   │
│   → 4. Viết tin nhắn chỉ dẫn/đường đi gửi qua App tài xế    │
│   → 5. Liên hệ đội xe cứu hộ nếu xe đã cạn kiệt pin         │
│                                                             │
│ Bước nào tốn nhất? Bước 3-4 (⏱ 12 phút/lượt)                │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3-4              │
│ (Tự động hóa lấy vị trí -> Tra cứu trạm trống -> Draft tin) │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm thời gian xử lý sự cố từ 15 phút ──> dưới 3 phút.      │
│                                                             │
│ Quick Architecture: [x] LLM Feature (Tự động soạn chỉ dẫn)   │
└─────────────────────────────────────────────────────────────┘
```

---

### 2. QUICK PROBLEM CARD #2: Vinhomes Tự động hóa Phân loại & Phản hồi Yêu cầu Cư dân

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: Phân loại và tự động soạn phản hồi nháp cho ý kiến│
│ khiếu nại/sự cố của cư dân gửi qua ứng dụng Vinhomes Resident.│
│ Công ty thành viên: [x] Vinhomes                            │
│                                                             │
│ Ai đang đau? Cư dân (chờ lâu >12h), Ban Quản Lý (quá tải)   │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Cư dân gửi phản ánh lên ứng dụng Vinhomes Resident      │
│   → 2. Lễ tân đọc và chuyển thủ công đến bộ phận kỹ thuật   │
│   → 3. Kỹ thuật viên phản hồi lại thông tin cho lễ tân       │
│   → 4. Lễ tân soạn phản hồi gửi cư dân qua App              │
│                                                             │
│ Bước nào tốn nhất? Bước 2-4 (⏱ 8 tiếng/lượt)                 │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 4            │
│ (Phân loại tự động theo thẻ ticket -> Soạn câu trả lời nháp)│
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Phân loại ticket dưới 30 giây, giảm thời gian phản hồi từ   │
│ 12 tiếng ──> dưới 1 tiếng.                                  │
│                                                             │
│ Quick Architecture: [x] LLM Feature (Classifier + Drafter)   │
└─────────────────────────────────────────────────────────────┘
```

---

### 3. QUICK PROBLEM CARD #3: Xanh SM Tóm tắt Lý do Khách hàng Hủy chuyến

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: Phân tích ghi âm cuộc gọi và ghi chú tài xế để    │
│ tóm tắt nguyên nhân root-cause gây hủy chuyến giờ cao điểm.  │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau? Đội ngũ Vận hành & QA (tốn thời gian nghe lại) │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Hệ thống ghi nhận chuyến xe bị hủy                     │
│   → 2. Chuyên viên QA nghe lại file ghi âm tổng đài          │
│   → 3. Ghi chép thủ công lý do hủy vào bảng Excel           │
│   → 4. Tổng hợp báo cáo tuần gửi Trưởng phòng Vận hành      │
│                                                             │
│ Bước nào tốn nhất? Bước 2-3 (⏱ 15 phút/chuyến)              │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3              │
│ (STT ghi âm -> LLM Summarizer -> Tagging lý do tự động)     │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Tự động hóa tóm tắt 100% cuộc gọi hủy chuyến, giảm thời gian│
│ tạo báo cáo tuần từ 2 ngày ──> dưới 30 phút.                 │
│                                                             │
│ Quick Architecture: [x] LLM Feature (Speech-to-Text + Summarizer)│
└─────────────────────────────────────────────────────────────┘
```
