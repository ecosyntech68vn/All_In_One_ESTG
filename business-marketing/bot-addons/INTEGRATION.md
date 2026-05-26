# Tích hợp AI Tư Vấn + Zalo vào bot-aithucchien

Bạn ĐÃ có repo `bot-aithucchien`: Telegram + Sepay tự giao hàng (chạy thật rồi). **Không làm lại phần đó.**
Bộ add-on này thêm 2 lớp MỚI lên trên: **(1) AI tư vấn** cho tin nhắn tự do, **(2) kênh Zalo OA** dùng chung AI.

---

## Bước 1 — Copy file vào repo (cùng cấp `app.py`)
- `ai_advisor.py`
- `advisor_brain.md`  ← mở sửa nội dung sản phẩm/giá cho đúng thực tế
- `zalo.py`           ← chỉ cần nếu dùng Zalo

## Bước 2 — Sửa `app.py` (2 chỗ nhỏ)
**(a)** Thêm import gần đầu file (cạnh các import khác):
```python
from ai_advisor import ai_reply
```
**(b)** Tìm nhánh `else` ở cuối `telegram_webhook()` (khoảng dòng 695), hiện là:
```python
    else:
        tg_send(chat_id,
                "Tôi chưa hiểu lệnh đó. Anh/chị hãy Gõ /start để xem menu chính.")
```
Thay bằng:
```python
    else:
        reply = ai_reply(chat_id, text)
        if reply:
            tg_send(chat_id, reply, tg_keyboard())
        else:
            tg_send(chat_id, "Tôi chưa hiểu lệnh đó. Anh/chị hãy gõ /start để xem menu chính.", tg_keyboard())
```
→ Giờ mọi tin nhắn tự do (không phải lệnh) được **AI tư vấn**; nếu AI chưa bật/timeout thì tự về câu mặc định + menu (**offline-safe**). Lệnh `/mua_combo`… và Sepay giữ NGUYÊN.

## Bước 3 — Env cho AI (Railway → Variables)
```
LLM_API_KEY  = ...                      # OpenAI key, hoặc Groq key (Groq có free tier)
LLM_BASE_URL = https://api.openai.com/v1   # Groq: https://api.groq.com/openai/v1
LLM_MODEL    = gpt-4o-mini                  # Groq: llama-3.3-70b-versatile
```
Để trống `LLM_API_KEY` → bot chạy y như cũ (chưa có AI). `requirements.txt` đã có `requests` → không cần thêm gì cho AI.

## Bước 4 — Zalo OA (tùy chọn)
**(a)** Trong `app.py`, sau khi tạo `app = Flask(...)`:
```python
from zalo import zalo_bp
app.register_blueprint(zalo_bp)
```
(Flask đã có sẵn trong repo → không cần cài thêm.)

**(b)** Tạo Zalo OA + App:
1. Tạo **Official Account** tại `oa.zalo.me`.
2. Tạo **Application** ở `developers.zalo.me`, gắn OA, xin quyền nhận/gửi tin nhắn.
3. Lấy **ACCESS TOKEN** của OA (qua OAuth) → đặt env `ZALO_OA_ACCESS_TOKEN`.
   - ⚠️ Token Zalo hết hạn ~25 giờ → phải **refresh bằng refresh_token** định kỳ (theo docs Zalo). Đây là điểm tốn công nhất của Zalo (Telegram không có).
4. Cấu hình **Webhook URL** = `{BASE_URL}/zalo-webhook` (cùng domain Railway với bot).
5. (Khuyến nghị) đặt `ZALO_APP_ID`, `ZALO_APP_SECRET`, `ZALO_STRICT=1` để bật xác thực chữ ký.

**(c)** Phạm vi Zalo: hiện Zalo làm **TƯ VẤN bằng AI**. Thanh toán/giao hàng tự động vẫn qua **Telegram + Sepay** (giao theo `chat_id` Telegram). Với khách Zalo: AI nên hướng họ qua bot Telegram để mua tự động, hoặc bạn xác nhận đơn Zalo thủ công bằng `/confirm`. (Giao tự động ngay trên Zalo là bước lớn hơn — map Zalo user → đơn — làm sau nếu cần.)

## Bước 5 — Test
- **Telegram:** nhắn 1 câu tự do (không phải lệnh) → AI trả lời tư vấn; menu/lệnh mua vẫn chạy.
- **Zalo:** nhắn OA → nhận trả lời AI.
- **Fallback:** tạm xóa `LLM_API_KEY` → bot vẫn chạy (không chết).

## An toàn
- KHÔNG commit token/key — chỉ để trong env Railway. Repo để **private**.
- AI không bịa số TK/giá; gặp khó → mời khách gõ `/lien_he`.
- Sửa "bộ não" trong `advisor_brain.md` (sản phẩm, giá, cách tư vấn) — không cần đụng code.

---

### Tóm tắt kiến trúc sau tích hợp
```
Khách Telegram ──/telegram-webhook──┐
                                    ├─ lệnh (/mua_…) → luồng cũ + Sepay tự giao  (GIỮ NGUYÊN)
Khách Zalo ──────/zalo-webhook──────┘─ tin tự do     → ai_advisor (LLM + advisor_brain.md)
```
