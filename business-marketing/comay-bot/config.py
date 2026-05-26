# -*- coding: utf-8 -*-
"""Cấu hình đọc từ biến môi trường (env). KHÔNG hardcode token."""
import os

def _env(k, d=""):
    return os.environ.get(k, d)

BOT_TOKEN               = _env("BOT_TOKEN")
ADMIN_CHAT_ID           = _env("ADMIN_CHAT_ID")
TELEGRAM_WEBHOOK_SECRET = _env("TELEGRAM_WEBHOOK_SECRET")
SEPAY_API_KEY           = _env("SEPAY_API_KEY")          # để trống = chế độ MANUAL (admin /confirm)
BASE_URL                = _env("BASE_URL")

# Ngân hàng nhận tiền (khuyến nghị MB Bank vì Sepay đẩy biến động realtime)
BANK_ACCOUNT = _env("BANK_ACCOUNT")
BANK_NAME    = _env("BANK_NAME", "MB Bank")
BANK_CODE    = _env("BANK_CODE", "MB")     # mã ngân hàng cho VietQR (MB, VCB, TCB, ACB...)
ACCOUNT_NAME = _env("ACCOUNT_NAME", "")

# ---------------------------------------------------------------------------
# Sản phẩm bán. Mỗi SKU có "type" quyết định cách GIAO:
#   type="link"          -> gửi link tải (db.set_link). (mặc định, tương thích bản cũ)
#   type="license"       -> tự sinh license key vĩnh viễn (licensing.gen) + gửi khách
#   type="subscription"  -> license key có hạn ("days") + theo dõi + nhắc gia hạn
# "pid" = mã sản phẩm in trong key (để Farm OS map khi verify offline).
# ---------------------------------------------------------------------------
PRODUCTS = {
    # --- Founder Solo (sản phẩm số, giao bằng link — y như cũ) ---
    "combo":   {"name": "Combo Founder Solo (FounderToolkit + Cỗ Máy + Bonus)", "price": 699000, "list": 999000, "type": "link"},
    "comay":   {"name": "Cỗ Máy Nội Dung (hệ thống marketing)", "price": 599000, "list": 890000, "type": "link"},
    "founder": {"name": "FounderToolkit — Sổ tay GitHub cho Founder", "price": 139000, "list": 199000, "type": "link"},

    # --- EcoSynTech Farm OS (sản phẩm thật — TODO: chỉnh giá theo CFO) ---
    "farmos":      {"name": "EcoSynTech Farm OS — License vĩnh viễn", "price": 2990000, "list": 3990000,
                    "type": "license", "pid": "FOS"},
    "farmos_year": {"name": "EcoSynTech Farm OS — Thuê bao 12 tháng", "price": 990000, "list": 1290000,
                    "type": "subscription", "pid": "FOSUB", "days": 365},
}
DEFAULT_SKU = "combo"

# Engine license
LICENSE_SECRET = _env("LICENSE_SECRET")     # BẮT BUỘC cho license/subscription. Dùng chung với Farm OS để verify offline.
CRON_SECRET    = _env("CRON_SECRET")        # bảo vệ endpoint /cron/renewals
RENEW_BEFORE_DAYS = int(_env("RENEW_BEFORE_DAYS", "7"))   # nhắc gia hạn trước N ngày

# AI (tùy chọn). Để trống LLM_API_KEY -> bot vẫn chạy, chỉ chưa có AI tư vấn.
LLM_API_KEY  = _env("LLM_API_KEY")
LLM_BASE_URL = _env("LLM_BASE_URL", "https://api.openai.com/v1")
LLM_MODEL    = _env("LLM_MODEL", "gpt-4o-mini")

TG_API = f"https://api.telegram.org/bot{BOT_TOKEN}"
