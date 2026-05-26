# All In One ESTG - Nền tảng kinh doanh thống nhất

Kết hợp **AI Agent Business-Marketing** (5 Agent, 18 Skills, tự động hóa marketing) và **Tro_Ly_Shop** (AI chăm sóc khách hàng 24/7) thành một hệ sinh thái duy nhất.

## 🚀 Kiến trúc

```
All_In_One_ESTG/
├── business-marketing/     # Hệ thống marketing: kênh, nội dung, bán hàng
├── tro_ly_shop/            # AI Agent chăm sóc khách hàng và bán hàng
├── integration/            # LỚP TÍCH HỢP (mới)
│   ├── webhooks/           # lead_to_prospect.py
│   ├── shared_services/    # sepay_client.py, telegram_bot.py
│   └── data_sync/          # lead_sync.py, customer_sync.py
├── shared/                 # Cấu hình và tiện ích dùng chung
├── deploy/                 # docker-compose.yml
├── .env.example            # Biến môi trường thống nhất
└── README.md
```

## 🔗 Các điểm tích hợp chính

| Điểm tích hợp | Mô tả | File |
|---|---|---|
| 🔄 Lead → Prospect | Lead từ marketing tự động tạo prospect trong shop | `integration/webhooks/lead_to_prospect.py` |
| 💰 Thanh toán thống nhất | SePay VietQR dùng chung cho cả 2 hệ thống | `integration/shared_services/sepay_client.py` |
| 📢 Telegram Bot | Bot thông báo thống nhất cho admin | `integration/shared_services/telegram_bot.py` |
| 👥 Đồng bộ khách hàng | Lịch sử mua hàng → cá nhân hóa marketing | `integration/data_sync/customer_sync.py` |
| 📋 Đồng bộ Lead | Lead mới → thông báo + chăm sóc tự động | `integration/data_sync/lead_sync.py` |

## 🛠️ Cài đặt

```bash
# 1. Clone repo
git clone https://github.com/ecosyntech68vn/All_In_One_ESTG.git
cd All_In_One_ESTG

# 2. Copy environment variables
cp .env.example .env
# Điền các giá trị: BOT_TOKEN, GEMINI_API_KEY, SEPAY_API_KEY, ...

# 3. Clone 2 repo con vào đúng thư mục
git clone https://github.com/ecosyntech68vn/Tro_Ly_Shop.git tro_ly_shop

# 4. Chạy bằng Docker
docker-compose -f deploy/docker-compose.yml up -d
```

## 📋 Yêu cầu

- Python 3.8+
- Docker & Docker Compose
- Telegram Bot Token
- SePay API key (cho thanh toán VietQR)
- Ít nhất 1 AI API key (Gemini/Claude/OpenAI)

## 📄 Giấy phép

Proprietary. All rights reserved.

---

*All In One ESTG v1.0 · EcoSynTech Global 2026*
