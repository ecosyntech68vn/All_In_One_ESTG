# Runbook — Bot làm Hệ thống Vận hành EcoSynTech

> comay-bot (đã chạy thật: Sepay xác nhận CK + auto-giao) nay là trục vận hành EcoSynTech.
> Bổ sung: giao hàng ĐA-LOẠI (link / license / subscription) + license key verify OFFLINE.
> Cập nhật: 2026-05-25

## 1. Bot làm được gì (sau nâng cấp)

- Bán + thu tiền tự động (VietQR + Sepay) — **đã chạy prod**.
- Giao theo `type` của SKU:
  - `link` — gửi link tải (Founder Solo, như cũ).
  - `license` — tự sinh **license key vĩnh viễn**, gửi khách, lưu DB.
  - `subscription` — key **có hạn** + theo dõi + **tự nhắc gia hạn**.
- AI tư vấn (advisor_brain.md) + Zalo OA — như cũ.
- Quản trị qua Telegram (admin): cấp/thu hồi key, tra cứu, thống kê.

## 2. Cấu hình thêm (env)

| Biến | Ý nghĩa |
|------|---------|
| `LICENSE_SECRET` | **Bắt buộc** cho license/subscription. Chuỗi bí mật, dùng **chung** với Farm OS để verify offline. |
| `CRON_SECRET` | Bảo vệ endpoint `/cron/renewals`. |
| `RENEW_BEFORE_DAYS` | Nhắc gia hạn trước N ngày (mặc định 7). |

> Đặt `LICENSE_SECRET` MỘT LẦN và giữ cố định. Đổi secret = mọi key cũ verify fail.

## 3. Vận hành hằng ngày

- Khách `/mua_farmos` hoặc `/mua_farmos_year` → CK → bot tự cấp key + gửi.
- Theo dõi: admin gõ `/stats`, `/unmatched`, `/licenses <chat_id|TXN>`.
- Nhắc gia hạn: gọi định kỳ `GET {BASE_URL}/cron/renewals?secret=<CRON_SECRET>` (dùng cron-job.org / UptimeRobot / scheduler). Hoặc admin gõ `/renewals` để chạy tay.

## 4. Lệnh admin

```
/catalog                      # liệt kê SKU + giá + type
/issue <sku> <chat_id> [days] # cấp key thủ công (bán offline)
/licenses <chat_id|TXN>       # tra license
/revoke <KEY>                 # thu hồi key
/renewals                     # quét + nhắc gia hạn ngay
/set_link <sku> <url>         # set link cho SKU type=link
/confirm <TXN>                # xác nhận tay (chế độ manual)
/stats  /unmatched
```

## 5. Farm OS verify license OFFLINE (giá trị cốt lõi)

Key tự mang chữ ký HMAC nên Farm OS kiểm tra **không cần internet**. Nhúng `licensing.py`
(hoặc copy hàm `verify`) vào Farm OS, đặt **cùng** `LICENSE_SECRET`:

```python
from licensing import verify   # cùng file với bot, cùng LICENSE_SECRET

r = verify(user_key)           # ví dụ: "ECO-FOS-00000-5C4KNH-N2ZDYVRQ"
if not r["ok"]:
    # r["reason"]: format | bad-signature | expired
    block_activation(r["reason"])
else:
    pid  = r["pid"]            # FOS = license vĩnh viễn, FOSUB = subscription
    exp  = r["expires_day"]    # 0 = vĩnh viễn; >0 = ngày-unix hết hạn
    activate(pid, exp)
```

- `bad-signature` → key giả/sửa.
- `expired` → subscription hết hạn → mời gia hạn.
- Thu hồi (revoke) là trạng thái phía bot (DB); nếu cần chặn offline tức thì, phát key hạn ngắn + gia hạn định kỳ.

## 6. Kiểm thử

```
python licensing.py --selftest     # engine key
python app.py --selftest           # luồng link + license + subscription + nhắc gia hạn + revoke
```

## 7. An toàn (theo chuỗi ưu tiên)

- Token & `LICENSE_SECRET` chỉ trong env, KHÔNG commit. `.env` đã trong `.gitignore`.
- **Gỡ `bot.db` khỏi git** (chứa đơn + chat_id khách) — việc tồn đọng, làm sớm.
- Mất AI/Sepay: bot vẫn chạy menu + chế độ `/confirm` (offline-safe).
- Tương thích ngược: SKU cũ `type=link` chạy y như bản prod, không đổi hành vi.
