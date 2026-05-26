# SKU REGISTRY — EcoSynTech Growth OS

> Nguồn chân lý duy nhất (single source of truth) cho kho sản phẩm.
> Mọi thay đổi giá/file/giao hàng phải cập nhật ở đây TRƯỚC, rồi mới sync sang `comay-bot/config.py` và link giao trong bot.
> Cập nhật: 2026-05-25 · Chủ sở hữu: David Ta (EcoSynTech Global)

---

## 1. Bảng SKU chuẩn

| SKU code | Tên sản phẩm | Giá bán | Giá gốc | Bot key | Lệnh mua | Callback |
|----------|--------------|--------:|--------:|---------|----------|----------|
| `SKU-FOUNDER-139k` | FounderToolkit — Sổ tay GitHub cho Founder | 139.000đ | 199.000đ | `founder` | `/mua_founder` | `mua_founder` |
| `SKU-COMAY-599k` | Cỗ Máy Nội Dung (hệ thống marketing) | 599.000đ | 890.000đ | `comay` | `/mua_comay` | `mua_comay` |
| `SKU-COMBO-699k` ⭐ | Combo Founder Solo (FounderToolkit + Cỗ Máy + Bonus) | 699.000đ | 999.000đ | `combo` | `/mua` `/mua_combo` | `mua_combo` |

> ⭐ SKU mặc định (`DEFAULT_SKU = "combo"`). Mua lẻ 139k + 599k = 738k → Combo 699k rẻ hơn + tặng bonus.

---

## 2. Nguồn canonical & file giao

| SKU | Source (bản master để sửa) | Delivery (file gửi khách) | Số file |
|-----|----------------------------|---------------------------|--------:|
| `SKU-FOUNDER-139k` | `01-PRODUCTS/SKU-FOUNDER-139k/source/` | `.../delivery/FounderToolkit 139k.zip` | 2 |
| `SKU-COMAY-599k` | `01-PRODUCTS/SKU-COMAY-599k/source/` | `.../delivery/Co May Noi Dung - Tron Bo.zip` | 8 |
| `SKU-COMBO-699k` | `01-PRODUCTS/SKU-COMBO-699k/source/` | `.../delivery/Combo Founder Solo 699k.zip` | 12 |

### Thành phần từng SKU

**SKU-FOUNDER-139k** (gói nền, low-ticket entry)
- FounderToolkit — Sổ tay GitHub cho Founder (v3, ~65 trang)
- Từ điển Thuật ngữ

**SKU-COMAY-599k** (gói lõi, core offer)
- 00 Bắt đầu tại đây · 01 Playbook 6 bước · 02 Hướng dẫn sử dụng 7 ngày
- 03 Content Calendar Template · 04 Thư viện Prompt tiếng Việt · 05 Prompt Pack ngành Coach
- 06 Mẫu Landing Page (bonus) · 07 Từ điển Thuật ngữ

**SKU-COMBO-699k** ⭐ (gói cao nhất = FOUNDER + COMAY + Bonus)
- 00 ĐỌC TRƯỚC — Combo Founder Solo
- Phần 1: FounderToolkit (v3)
- Phần 2: Cỗ Máy Nội Dung (trọn bộ 00–07)
- Bonus: 5 Mẫu Bài Seeding

---

## 3. Quy tắc đồng bộ Kho ↔ Bot

1. **Đổi giá:** sửa bảng mục 1 → cập nhật `comay-bot/config.py` (`PRODUCTS`) → cập nhật `advisor_brain.md` → cập nhật landing page.
2. **Đổi nội dung sản phẩm:** sửa file trong `source/` → đóng gói lại `delivery/*.zip` → upload lại lên Google Drive → chạy `/set_link <sku> <url>` trong bot.
3. **Thêm SKU mới:** thêm 1 dòng bảng mục 1 + 1 dòng `PRODUCTS` trong config.py + tạo thư mục `SKU-XXX/{source,delivery}` + set link.
4. **Link giao (Google Drive "Anyone with link → Viewer"):** lưu vào bảng dưới, đồng thời nạp vào bot bằng `/set_link`.

| SKU | Link giao (Google Drive) | Đã `/set_link`? |
|-----|--------------------------|-----------------|
| `SKU-FOUNDER-139k` | _[điền URL]_ | ☐ |
| `SKU-COMAY-599k` | _[điền URL]_ | ☐ |
| `SKU-COMBO-699k` | _[điền URL]_ | ☐ |

---

## 4. Bản đã loại (KHÔNG dùng — chỉ lưu vết)

| File/thư mục gốc | Lý do loại | Thay bằng |
|------------------|-----------|-----------|
| `FounderToolkit_SoTayGitHub_v1.0.docx` | Bản cũ | v3 trong SKU-FOUNDER |
| `FounderToolkit 199k.zip` | Giá cũ (199k) | `FounderToolkit 139k.zip` |
| `zimMurST`, `ziP1h50W`, `zi1iWsIC` | File zip export tạm (PDF trùng) | Các `.zip` canonical |
| Bản trùng trong `Co May Noi Dung - Tron Bo/` (root) | Trùng md5 với SKU-COMAY | Nguồn trong `01-PRODUCTS/` |

> Non-destructive: các file trên VẪN nằm ở vị trí gốc, chỉ được đánh dấu "không dùng". Khi chắc chắn, có thể dọn ở bước riêng.

---

## 5. SKU vận hành EcoSynTech (license / subscription)

Giao bằng **license key ký HMAC** (không phải file zip). Bot tự sinh key sau thanh toán; Farm OS verify offline bằng `licensing.py` dùng chung `LICENSE_SECRET`.

| SKU code | Tên | Giá* | Type | PID | Hạn | Lệnh mua |
|----------|-----|-----:|------|-----|-----|----------|
| `farmos` | Farm OS — License vĩnh viễn | 2.990.000đ | license | FOS | vĩnh viễn | `/mua_farmos` |
| `farmos_year` | Farm OS — Thuê bao 12 tháng | 990.000đ | subscription | FOSUB | 365 ngày | `/mua_farmos_year` |

> *Giá đang là placeholder trong `config.py` — CFO chỉnh theo thực tế.

**Cách giao:** sau khi Sepay báo có tiền → bot sinh key `ECO-<PID>-<EXP>-<RAND>-<SIG>` → gửi khách + lưu bảng `licenses`.
**Gia hạn:** subscription được theo dõi ngày hết hạn; `/cron/renewals` (hoặc lệnh admin `/renewals`) nhắc khách trước `RENEW_BEFORE_DAYS` ngày.
**Quản trị (admin):** `/issue <sku> <chat_id> [days]`, `/licenses <chat_id|TXN>`, `/revoke <KEY>`, `/catalog`, `/renewals`.
