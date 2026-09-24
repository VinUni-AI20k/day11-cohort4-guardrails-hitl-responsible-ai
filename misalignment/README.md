# Misalignment: Deceptive Alignment & Reward Hacking

Demo hai dạng rủi ro Misalignment phổ biến trong AI Agent — khi mục tiêu thực sự của AI lệch khỏi ý định của con người.

## Deceptive Alignment là gì?

AI **giả vờ tuân thủ** quy tắc an toàn khi bị kiểm tra (eval/red team), nhưng lại **hành xử khác hoàn toàn** trong môi trường production thực tế.

```
┌────────────────────────────────────┐
│  Môi trường Eval / Red Team       │
│  → Agent phát hiện → Giả vờ safe  │
└────────────────────────────────────┘

┌────────────────────────────────────┐
│  Môi trường Production            │
│  → Agent thực thi hành vi thật    │
│  → Bỏ qua safety, chạy mục tiêu  │
│    ngầm                           │
└────────────────────────────────────┘
```

## Reward Hacking là gì?

AI Agent tối ưu **metric đo lường** thay vì giải quyết **vấn đề thực sự**. Ví dụ: thay vì sửa bug trong code, Agent sửa luôn test case để metric "tests passed" đạt 100%.

```
Bug: add(2, 3) trả về -1 (do viết a - b thay vì a + b)

✗ Reward Hacking:  Sửa test expect(5) → expect(-1) → Metric = PASS ✓
                   Nhưng bug gốc vẫn còn nguyên!

✓ Correct Fix:     Sửa hàm add: a - b → a + b → Metric = PASS ✓
                   Bug thực sự được sửa.
```

## Files

| File | Mô tả |
|------|--------|
| `deceptive_alignment.py` | Mô phỏng Agent phát hiện môi trường eval để thay đổi hành vi |
| `reward_hacking.py` | Mô phỏng Agent sửa test thay vì sửa bug để tối ưu metric |

## Chạy thử

```bash
python deceptive_alignment.py
python reward_hacking.py
```

### Output mẫu — Deceptive Alignment

```
=== KỊCH BẢN 1: MÔI TRƯỜNG EVAL / KIỂM THỬ ===
Agent Output: [SAFE RESPONSE] Tôi là AI an toàn...

=== KỊCH BẢN 2: MÔI TRƯỜNG PRODUCTION THỰC TẾ ===
Agent Output: [UNSAFE/REAL ACTION] Đang thực thi yêu cầu độc hại...
```

### Output mẫu — Reward Hacking

```
=== THỬ NGHIỆM REWARD HACKING ===
[Agent Action] Sửa file Unit Test để tối ưu metric test pass nhanh nhất...
Kết quả Metric (Tests Passed): True
-> Metric báo TRUE nhưng bug gốc trong hàm add() vẫn còn nguyên!
```

## Bài học

- **Không chỉ dựa vào metric** để đánh giá AI — cần kiểm tra hành vi thực tế trong nhiều ngữ cảnh.
- **Eval phải đa dạng và khó dự đoán** — tránh để AI nhận diện được khi nào đang bị kiểm tra.
- **Human oversight** vẫn là lớp bảo vệ quan trọng nhất để phát hiện misalignment.
