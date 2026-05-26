# EcoSynTech Growth OS

> Hệ phương pháp tăng trưởng khép kín cho Founder Solo — hợp nhất Lý thuyết (KIT) + Vận hành (BOT) + Kho sản phẩm chuẩn hóa thành một vòng tròn tự cải tiến.
> Tác giả & chủ sở hữu: **David Ta (CEO_THUAN)** — EcoSynTech Global · v1.0 · 25/05/2026

Đây là lớp hợp nhất, không phá hủy: dựng mới bên cạnh các thư mục gốc (agents/, skills/, commands/, comay-bot/...), không xóa bản cũ.

## Cấu trúc

```
EcoSynTech-Growth-OS/
├── README.md                      # file này — điểm vào
├── 00-FRAMEWORK/                  # IP / bản quyền tác giả
│   ├── EcoSynTech Growth OS — Master Framework.docx   ← tài liệu chính (14 trang)
│   ├── closed-loop-diagram.svg    # sơ đồ nguồn (chỉnh được)
│   └── closed-loop-diagram.png    # sơ đồ render
├── 01-PRODUCTS/                   # kho sản phẩm chuẩn hóa
│   ├── _SKU-REGISTRY.md           ← nguồn chân lý: SKU ↔ giá ↔ file ↔ lệnh /mua
│   ├── SKU-FOUNDER-139k/{source,delivery}
│   ├── SKU-COMAY-599k/{source,delivery}
│   └── SKU-COMBO-699k/{source,delivery}
├── 02-KIT/                        # (trỏ về Lớp 1: ../agents, ../skills, ../commands, ../workflows)
├── 03-OPERATIONS/                 # (trỏ về Lớp 2: ../comay-bot — bot chuẩn)
└── 04-ARCHIVE-NOTES/              # ghi chú bản đã loại (xem _SKU-REGISTRY.md mục 4)
```

## Vòng Khép Kín 5 Trạm

`OFFER → ATTRACT → CONVERT → DELIVER → INSIGHT → (cải tiến) → OFFER`

| Trạm | Lớp KIT (sinh) | Lớp BOT (vận hành) |
|------|----------------|--------------------|
| 1 Offer | Offer Agent · /research /competitor /offer | PRODUCTS{} trong config.py |
| 2 Attract | Attraction Agent · /funnel /content /lead-magnet | Landing → /start |
| 3 Convert | Conversion Agent · /sales-page /copy /objection | advisor_brain.md + menu |
| 4 Deliver | Deliver Agent · /payment-setup /notification /delivery | Sepay → /mua → auto-giao |
| 5 Insight | Insights Agent · /analytics /revenue /optimize | /stats · leads · DB |

Trạm 5 đẩy dữ liệu ngược về Trạm 1 = cơ chế cải tiến liên tục (PDCA).

## Dùng như thế nào

1. Đọc **Master Framework.docx** để nắm toàn bộ phương pháp (manifesto → kiến trúc → vòng khép kín → SOP → bản quyền).
2. Mọi thay đổi sản phẩm/giá: sửa **_SKU-REGISTRY.md** trước → đồng bộ sang `comay-bot/config.py`, `advisor_brain.md`, landing.
3. Gửi khách: dùng đúng file trong `SKU-*/delivery/*.zip` (đã set qua `/set_link` trong bot).

## Bản quyền

© 2026 David Ta / EcoSynTech Global. Bảo lưu mọi quyền. Tài liệu, sơ đồ, mã nguồn bot và "bộ não" advisor là sản phẩm trí tuệ thuộc sở hữu tác giả. Hướng dẫn đăng ký quyền tác giả: xem Chương 8 của Master Framework.
