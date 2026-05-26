# AI Trợ Lý Bán Hàng (Telegram) — Cỗ Máy Nội Dung

Bot Telegram thông minh: **tự tư vấn, trả lời câu hỏi, dẫn khách qua phễu tới mua, bắt lead, báo đơn cho bạn**. Thiết kế cho người vận hành bận (low-touch): khách tự được hướng dẫn, bạn chỉ nhận thông báo.

## Bot làm được gì
- Trò chuyện thông minh bằng AI (LLM) — hiểu nỗi đau, tư vấn, xử lý lăn tăn theo "bộ não" bạn dạy.
- Menu nhanh: Sản phẩm / Bảng giá / FAQ / Nhận quà / Mua ngay / Gặp tư vấn viên.
- Bắt lead (tên + SĐT) → lưu file `leads.jsonl` + báo bạn qua Telegram.
- Hướng dẫn thanh toán VietQR/chuyển khoản, báo "đơn mới" cho bạn.
- **Offline-safe:** nếu không có/khi mất AI, bot vẫn chạy bằng menu — không chết.

## Cài đặt (10 phút)
1. **Tạo bot:** mở Telegram → chat với **@BotFather** → `/newbot` → lấy **token**.
2. **Cài Python** (3.9+). Mở terminal trong thư mục này:
   ```
   pip install -r requirements.txt
   ```
3. **Tạo file cấu hình:** copy `.env.example` thành `.env`, điền:
   - `TELEGRAM_BOT_TOKEN` (từ BotFather)
   - `OWNER_CHAT_ID` (xem cách lấy trong `.env.example`)
   - `LLM_API_KEY` (tùy chọn — để bot thông minh; có thể dùng **Groq free**, xem `.env.example`)
   - Thông tin ngân hàng + link landing + link quà tặng.
4. **Chạy:**
   ```
   python bot.py
   ```
   Nhắn cho bot trên Telegram để thử. (Kiểm tra logic không cần token: `python bot.py --selftest`)

## Dạy lại bot (không cần code)
Sửa file **`assistant_config.md`** — đó là "bộ não": vai trò, giọng, sản phẩm, cách xử lý lăn tăn, quy tắc an toàn. Lưu lại và chạy lại bot.

## Chạy 24/7 (tùy chọn)
- Đơn giản: để chạy trên 1 máy luôn bật.
- Hoặc deploy miễn phí/rẻ lên Railway / Render / 1 VPS nhỏ (chạy `python bot.py`).

## Mở rộng (gợi ý low-touch)
- Nối thật thanh toán **SePay** để tự xác nhận đơn (thay bước nhắn "đã CK").
- Dùng chung "bộ não" `assistant_config.md` cho **Zalo OA / Messenger (ManyChat)** — cùng cách tư vấn.

## An toàn
- KHÔNG đưa token/API key vào code hay git. Chỉ để trong `.env`.
- Bot không bịa thông tin/giá; gặp câu khó sẽ đề nghị chuyển tư vấn viên (báo bạn).
