# Post-Purchase Engagement Sequence

6-message automated sequence over 14 days to maximize customer value and satisfaction.

## Sequence Overview

```
Purchase → Message 1 (Immediate) → Message 2 (Day 1) → Message 3 (Day 3)
→ Message 4 (Day 5) → Message 5 (Day 7) → Message 6 (Day 14)
```

## Message 1: Thank You + Access Instructions (Immediate)

### Timing
Send immediately after payment confirmation (within 1 minute)

### Channel
Email + Telegram (if available)

### Email Version

**Subject:** ✅ [{{orderCode}}] Cảm ơn bạn đã mua {{productName}}!

**Body:**
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
    .container { max-width: 600px; margin: 0 auto; padding: 20px; }
    .header { background: #4CAF50; color: white; padding: 30px; text-align: center; }
    .content { padding: 30px 20px; }
    .button {
      display: inline-block;
      background: #4CAF50;
      color: white;
      padding: 15px 40px;
      text-decoration: none;
      border-radius: 5px;
      font-weight: bold;
      margin: 20px 0;
    }
    .steps { background: #f9f9f9; padding: 20px; border-left: 4px solid #4CAF50; margin: 20px 0; }
    .footer { background: #f5f5f5; padding: 20px; text-align: center; font-size: 12px; color: #666; }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>🎉 Chào mừng bạn!</h1>
      <p style="font-size: 18px; margin-top: 10px;">
        Cảm ơn bạn đã mua {{productName}}
      </p>
    </div>

    <div class="content">
      <p>Xin chào <strong>{{customerName}}</strong>,</p>

      <p>
        Đơn hàng <strong>{{orderCode}}</strong> đã được xác nhận thành công.
        Bạn đã sẵn sàng để bắt đầu!
      </p>

      <div style="text-align: center; margin: 30px 0;">
        <a href="{{accessLink}}" class="button">
          BẮT ĐẦU NGAY
        </a>
      </div>

      <div class="steps">
        <h3>📋 Bước tiếp theo:</h3>
        <ol>
          <li>Click nút "Bắt đầu ngay" ở trên</li>
          <li>Tải xuống tài liệu/truy cập khóa học</li>
          <li>Làm theo hướng dẫn trong file "GETTING_STARTED.pdf"</li>
          <li>Tham gia nhóm hỗ trợ (nếu có): {{communityLink}}</li>
        </ol>
      </div>

      <p>
        <strong>💡 Mẹo:</strong> Đánh dấu email này để dễ tìm lại link truy cập.
        Link có hiệu lực <strong>{{accessDuration}}</strong>.
      </p>

      <hr style="margin: 30px 0; border: none; border-top: 1px solid #ddd;">

      <h3>📧 Cần hỗ trợ?</h3>
      <p>
        Chúng tôi luôn sẵn sàng giúp bạn:<br>
        📧 Email: {{supportEmail}}<br>
        💬 Telegram/Zalo: {{supportPhone}}<br>
        ⏰ Thời gian hỗ trợ: 9:00 - 21:00 hàng ngày
      </p>
    </div>

    <div class="footer">
      <p>&copy; {{year}} {{storeName}}. All rights reserved.</p>
    </div>
  </div>
</body>
</html>
```

### Telegram Version
```markdown
🎉 *CHÀO MỪNG BẠN!*

Cảm ơn bạn đã mua *{{productName}}*

📋 Mã đơn: `{{orderCode}}`
✅ Trạng thái: Đã thanh toán

🚀 *BẮT ĐẦU NGAY:*
1. Tải sản phẩm: {{downloadLink}}
2. Đọc hướng dẫn: GETTING_STARTED.pdf
3. Tham gia nhóm: {{communityLink}}

💬 Cần hỗ trợ? Nhắn tin trực tiếp tại đây!

⏰ Link truy cập có hiệu lực: {{accessDuration}}
```

### Automation Code
```javascript
async function sendMessage1(order) {
  const variables = {
    orderCode: order.code,
    productName: order.product.name,
    customerName: order.customer.name,
    accessLink: order.accessLink,
    accessDuration: '365 ngày',
    communityLink: order.product.communityLink || 'N/A',
    supportEmail: process.env.SUPPORT_EMAIL,
    supportPhone: process.env.SUPPORT_PHONE,
    storeName: process.env.STORE_NAME,
    year: new Date().getFullYear(),
    downloadLink: order.downloadLink
  };

  // Send email
  await sendEmail({
    to: order.customer.email,
    subject: `✅ [${variables.orderCode}] Cảm ơn bạn đã mua ${variables.productName}!`,
    template: 'message-1-welcome',
    variables
  });

  // Send Telegram if available
  if (order.customer.telegram) {
    await sendTelegram(order.customer.telegramChatId, renderTemplate('message-1-telegram', variables));
  }

  // Log message sent
  await logEngagementMessage(order.id, 'message_1', 'sent');
}
```

## Message 2: Getting Started Guide (Day 1)

### Timing
24 hours after purchase

### Channel
Email (primary)

### Email

**Subject:** 🚀 [{{productName}}] Bắt đầu nhanh - 3 bước đơn giản

**Body:**
```html
<div class="container">
  <div class="header">
    <h1>🚀 Bắt đầu với {{productName}}</h1>
  </div>

  <div class="content">
    <p>Xin chào {{customerName}},</p>

    <p>
      Hy vọng bạn đã có cơ hội khám phá {{productName}}.
      Đây là 3 bước đơn giản để bạn đạt kết quả nhanh nhất:
    </p>

    <div class="steps">
      <h3>📍 Bước 1: Thiết lập ban đầu (15 phút)</h3>
      <ul>
        <li>Tải xuống tất cả file cần thiết</li>
        <li>Cài đặt công cụ/phần mềm (nếu có)</li>
        <li>Xem video hướng dẫn: {{setupVideoLink}}</li>
      </ul>

      <h3>🎯 Bước 2: Hoàn thành nhiệm vụ đầu tiên (30 phút)</h3>
      <ul>
        <li>Làm theo {{firstTaskName}}</li>
        <li>Thực hành với ví dụ đầu tiên</li>
        <li>Kiểm tra kết quả</li>
      </ul>

      <h3>🚀 Bước 3: Áp dụng vào dự án của bạn (1 giờ)</h3>
      <ul>
        <li>Chọn 1 dự án/vấn đề cụ thể</li>
        <li>Áp dụng kiến thức vừa học</li>
        <li>Chia sẻ kết quả trong nhóm cộng đồng</li>
      </ul>
    </div>

    <div style="background: #FFF9C4; padding: 20px; border-left: 4px solid #FBC02D; margin: 20px 0;">
      <h3>💡 Mẹo từ các học viên thành công:</h3>
      <p><em>
        "Tôi đã hoàn thành bài đầu tiên trong 1 giờ và thấy ngay kết quả!
        Đừng bỏ qua phần thực hành, đó là chìa khóa."
      </em> - {{testimonialName}}</p>
    </div>

    <div style="text-align: center; margin: 30px 0;">
      <a href="{{accessLink}}" class="button">
        BẮT ĐẦU NGAY
      </a>
    </div>

    <p>
      📧 Có câu hỏi? Trả lời email này, chúng tôi sẽ giúp bạn trong 24h!
    </p>
  </div>
</div>
```

### Automation Code
```javascript
// Schedule with cron or queue
const cron = require('node-cron');

// Run every hour, check for orders from 24h ago
cron.schedule('0 * * * *', async () => {
  const yesterday = new Date(Date.now() - 24 * 60 * 60 * 1000);
  const orders = await db.orders.findAll({
    where: {
      createdAt: {
        $gte: new Date(yesterday.setHours(yesterday.getHours() - 1)),
        $lt: yesterday
      }
    }
  });

  for (const order of orders) {
    await sendMessage2(order);
  }
});

async function sendMessage2(order) {
  const variables = {
    productName: order.product.name,
    customerName: order.customer.name,
    setupVideoLink: order.product.setupVideoLink,
    firstTaskName: order.product.firstTaskName || 'bài học đầu tiên',
    testimonialName: 'Nguyễn Văn A',
    accessLink: order.accessLink
  };

  await sendEmail({
    to: order.customer.email,
    subject: `🚀 [${order.product.name}] Bắt đầu nhanh - 3 bước đơn giản`,
    template: 'message-2-getting-started',
    variables
  });

  await logEngagementMessage(order.id, 'message_2', 'sent');
}
```

## Message 3: Quick Win Tip (Day 3)

### Timing
72 hours (3 days) after purchase

### Channel
Email + SMS (optional for high-value products)

### Email

**Subject:** 💡 [{{productName}}] 1 mẹo đơn giản giúp bạn tiết kiệm 2 giờ

**Body:**
```html
<div class="container">
  <div class="header" style="background: #2196F3;">
    <h1>💡 Mẹo nhanh cho bạn</h1>
  </div>

  <div class="content">
    <p>Xin chào {{customerName}},</p>

    <p>
      Sau 3 ngày sử dụng {{productName}}, đây là 1 mẹo giúp bạn
      đạt kết quả nhanh gấp đôi:
    </p>

    <div style="background: #E3F2FD; padding: 30px; border-radius: 10px; margin: 30px 0;">
      <h2 style="color: #1976D2; margin-top: 0;">🎯 {{tipTitle}}</h2>

      <p style="font-size: 16px;">
        {{tipDescription}}
      </p>

      <h3>✅ Cách thực hiện:</h3>
      <ol style="font-size: 15px; line-height: 1.8;">
        <li>{{step1}}</li>
        <li>{{step2}}</li>
        <li>{{step3}}</li>
      </ol>

      <div style="background: white; padding: 15px; border-radius: 5px; margin-top: 20px;">
        <strong>💰 Kết quả:</strong> {{tipResult}}
      </div>
    </div>

    <div style="text-align: center; margin: 30px 0;">
      <a href="{{tipVideoLink}}" class="button">
        XEM VIDEO HƯỚNG DẪN
      </a>
    </div>

    <p>
      <strong>⏰ Thử ngay hôm nay</strong> và chia sẻ kết quả của bạn
      bằng cách trả lời email này!
    </p>

    <p style="color: #666; font-size: 14px; margin-top: 30px;">
      <em>
        Bạn sẽ nhận thêm nhiều mẹo hữu ích trong những ngày tới.
        Theo dõi email để không bỏ lỡ!
      </em>
    </p>
  </div>
</div>
```

### SMS Version (optional)
```
{{storeName}}: 💡 Mẹo nhanh cho {{productName}}: {{tipTitle}}.
Xem chi tiết: {{shortLink}}
```

### Automation Code
```javascript
// Day 3 automation
cron.schedule('0 10 * * *', async () => {
  const threeDaysAgo = new Date(Date.now() - 3 * 24 * 60 * 60 * 1000);
  const orders = await getOrdersFromDate(threeDaysAgo);

  for (const order of orders) {
    const tip = getTipForProduct(order.product.id);
    await sendMessage3(order, tip);
  }
});

function getTipForProduct(productId) {
  const tips = {
    'course-marketing': {
      title: 'Tăng hiệu suất quảng cáo gấp đôi với A/B testing',
      description: 'Thay vì chạy 1 quảng cáo, hãy tạo 2 phiên bản và so sánh kết quả.',
      step1: 'Tạo 2 bản quảng cáo khác nhau (ảnh/tiêu đề)',
      step2: 'Chạy cùng lúc với cùng ngân sách',
      step3: 'Sau 3 ngày, dừng bản thua, tăng ngân sách cho bản thắng',
      result: 'Tăng CTR 30-50%, giảm chi phí 20%',
      videoLink: 'https://example.com/ab-testing-guide'
    }
    // Add more tips per product
  };

  return tips[productId] || tips['default'];
}
```

## Message 4: Check-in + Support Offer (Day 5)

### Timing
120 hours (5 days) after purchase

### Channel
Email

### Email

**Subject:** 👋 [{{productName}}] Mọi thứ ổn chứ {{customerName}}?

**Body:**
```html
<div class="container">
  <div class="header" style="background: #FF9800;">
    <h1>👋 Bạn đang tiến triển thế nào?</h1>
  </div>

  <div class="content">
    <p>Xin chào {{customerName}},</p>

    <p>
      Đã 5 ngày kể từ khi bạn bắt đầu với {{productName}}.
      Chúng tôi muốn biết: bạn đang tiến triển như thế nào?
    </p>

    <div style="background: #FFF3E0; padding: 20px; border-radius: 10px; margin: 20px 0;">
      <p style="font-size: 16px; margin: 0;">
        <strong>Trả lời nhanh (chỉ 1 click):</strong>
      </p>
      <div style="margin-top: 15px;">
        <a href="{{surveyLink}}?status=great" style="display: inline-block; background: #4CAF50; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; margin: 5px;">
          😊 Rất tốt!
        </a>
        <a href="{{surveyLink}}?status=ok" style="display: inline-block; background: #FF9800; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; margin: 5px;">
          😐 Cũng được
        </a>
        <a href="{{surveyLink}}?status=stuck" style="display: inline-block; background: #F44336; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; margin: 5px;">
          😞 Đang gặp khó khăn
        </a>
      </div>
    </div>

    <h3>🤔 Bạn đang gặp vấn đề gì?</h3>
    <p>Dưới đây là những thắc mắc phổ biến và giải pháp:</p>

    <div style="margin: 20px 0;">
      <details style="background: #f9f9f9; padding: 15px; margin: 10px 0; border-radius: 5px;">
        <summary style="cursor: pointer; font-weight: bold;">
          ❓ "Tôi không biết bắt đầu từ đâu"
        </summary>
        <p style="margin-top: 10px;">
          → Bắt đầu với Module 1, Bài 1. Dành 30 phút/ngày và hoàn thành từng bài theo thứ tự.
          <a href="{{roadmapLink}}">Xem lộ trình chi tiết →</a>
        </p>
      </details>

      <details style="background: #f9f9f9; padding: 15px; margin: 10px 0; border-radius: 5px;">
        <summary style="cursor: pointer; font-weight: bold;">
          ❓ "Tôi không có đủ thời gian"
        </summary>
        <p style="margin-top: 10px;">
          → Chia nhỏ mục tiêu: 15 phút/ngày là đủ. Học 1 bài mỗi sáng trước khi làm việc.
          <a href="{{timeManagementGuide}}">Xem hướng dẫn quản lý thời gian →</a>
        </p>
      </details>

      <details style="background: #f9f9f9; padding: 15px; margin: 10px 0; border-radius: 5px;">
        <summary style="cursor: pointer; font-weight: bold;">
          ❓ "Tôi bị kẹt ở một bài nào đó"
        </summary>
        <p style="margin-top: 10px;">
          → Gửi câu hỏi vào nhóm cộng đồng hoặc email cho chúng tôi.
          Chúng tôi cam kết trả lời trong 24h.
          <a href="{{supportLink}}">Gửi câu hỏi ngay →</a>
        </p>
      </details>
    </div>

    <div style="background: #E8F5E9; padding: 20px; border-left: 4px solid #4CAF50; margin: 30px 0;">
      <h3 style="margin-top: 0;">🎁 Ưu đãi đặc biệt</h3>
      <p>
        <strong>Trả lời khảo sát ngay hôm nay</strong> và nhận:
      </p>
      <ul>
        <li>✅ 1 buổi tư vấn 1-1 (15 phút) qua Zoom/Zalo</li>
        <li>✅ Template/checklist độc quyền</li>
        <li>✅ Mã giảm 20% cho sản phẩm tiếp theo</li>
      </ul>
      <div style="text-align: center; margin-top: 20px;">
        <a href="{{surveyLink}}" class="button">
          NHẬN ƯU ĐÃI NGAY
        </a>
      </div>
    </div>

    <p>
      Chúng tôi ở đây để giúp bạn thành công. Đừng ngại liên hệ bất cứ lúc nào!
    </p>

    <p>
      Trân trọng,<br>
      <strong>{{supportTeamName}}</strong>
    </p>
  </div>
</div>
```

## Message 5: Testimonial/Review Request (Day 7)

### Timing
7 days after purchase

### Channel
Email + Telegram notification

### Email

**Subject:** 🌟 [{{productName}}] Chia sẻ trải nghiệm của bạn (nhận quà)

**Body:**
```html
<div class="container">
  <div class="header" style="background: #9C27B0;">
    <h1>🌟 Bạn thích {{productName}} không?</h1>
  </div>

  <div class="content">
    <p>Xin chào {{customerName}},</p>

    <p>
      Đã 1 tuần kể từ khi bạn bắt đầu hành trình với {{productName}}.
      Chúng tôi rất muốn nghe ý kiến của bạn!
    </p>

    <div style="text-align: center; background: #F3E5F5; padding: 40px 20px; border-radius: 10px; margin: 30px 0;">
      <h2 style="color: #7B1FA2; margin-top: 0;">
        💜 Đánh giá {{productName}}
      </h2>
      <p style="font-size: 18px;">
        Click vào số sao để đánh giá:
      </p>
      <div style="font-size: 40px; margin: 20px 0;">
        <a href="{{reviewLink}}?rating=5" style="text-decoration: none;">⭐</a>
        <a href="{{reviewLink}}?rating=4" style="text-decoration: none;">⭐</a>
        <a href="{{reviewLink}}?rating=3" style="text-decoration: none;">⭐</a>
        <a href="{{reviewLink}}?rating=2" style="text-decoration: none;">⭐</a>
        <a href="{{reviewLink}}?rating=1" style="text-decoration: none;">⭐</a>
      </div>
      <p style="font-size: 14px; color: #666;">
        Chỉ mất 2 phút!
      </p>
    </div>

    <div style="background: #FFF9C4; padding: 20px; border-left: 4px solid #FBC02D; margin: 20px 0;">
      <h3 style="margin-top: 0;">🎁 Quà tặng tri ân</h3>
      <p>Gửi đánh giá của bạn và nhận ngay:</p>
      <ul>
        <li>✅ Bonus module độc quyền (giá trị {{bonusValue}})</li>
        <li>✅ Tham gia group VIP (hỗ trợ ưu tiên)</li>
        <li>✅ Voucher 30% cho lần mua tiếp theo</li>
      </ul>
    </div>

    <div style="text-align: center; margin: 30px 0;">
      <a href="{{reviewLink}}" class="button" style="background: #9C27B0;">
        VIẾT ĐÁNH GIÁ NGAY
      </a>
    </div>

    <h3>💬 Câu hỏi đánh giá:</h3>
    <ol style="line-height: 1.8;">
      <li>Bạn đánh giá {{productName}} mấy sao? (1-5)</li>
      <li>Điều bạn thích nhất là gì?</li>
      <li>Kết quả nào bạn đã đạt được sau 1 tuần?</li>
      <li>Bạn có giới thiệu cho bạn bè không? Tại sao?</li>
    </ol>

    <p style="background: #E8F5E9; padding: 15px; border-radius: 5px; margin-top: 30px;">
      <strong>🔒 Lưu ý:</strong> Đánh giá của bạn giúp chúng tôi cải thiện sản phẩm
      và hỗ trợ các học viên tương lai tốt hơn. Cảm ơn bạn rất nhiều!
    </p>
  </div>
</div>
```

### Automation Code
```javascript
async function sendMessage5(order) {
  const variables = {
    productName: order.product.name,
    customerName: order.customer.name,
    reviewLink: `${process.env.APP_URL}/review/${order.id}`,
    bonusValue: '500,000 VND'
  };

  await sendEmail({
    to: order.customer.email,
    subject: `🌟 [${order.product.name}] Chia sẻ trải nghiệm của bạn (nhận quà)`,
    template: 'message-5-review-request',
    variables
  });

  // Telegram reminder
  if (order.customer.telegramChatId) {
    await sendTelegram(order.customer.telegramChatId, `
🌟 *ĐÁNH GIÁ & NHẬN QUÀ*

Bạn đã dùng ${order.product.name} được 1 tuần!

Dành 2 phút đánh giá và nhận:
✅ Bonus module độc quyền
✅ Voucher 30% cho lần mua sau

Đánh giá ngay: ${variables.reviewLink}
    `);
  }

  await logEngagementMessage(order.id, 'message_5', 'sent');
}
```

## Message 6: Upsell/Cross-sell (Day 14)

### Timing
14 days (2 weeks) after purchase

### Channel
Email (personalized based on product purchased)

### Email

**Subject:** 🚀 [Ưu đãi đặc biệt] Bước tiếp theo sau {{productName}}

**Body:**
```html
<div class="container">
  <div class="header" style="background: #E91E63;">
    <h1>🎯 Sẵn sàng lên level?</h1>
  </div>

  <div class="content">
    <p>Xin chào {{customerName}},</p>

    <p>
      Chúc mừng bạn đã hoàn thành 2 tuần với {{productName}}!
      Đây là thời điểm tuyệt vời để tiến lên bước tiếp theo.
    </p>

    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 40px; border-radius: 10px; margin: 30px 0;">
      <h2 style="margin-top: 0; color: white;">
        🔥 {{upsellProductName}}
      </h2>
      <p style="font-size: 18px; opacity: 0.95;">
        {{upsellDescription}}
      </p>

      <div style="background: rgba(255,255,255,0.2); padding: 20px; border-radius: 5px; margin: 20px 0;">
        <h3 style="margin-top: 0; color: white;">✨ Bạn sẽ học được:</h3>
        <ul style="line-height: 1.8; font-size: 16px;">
          <li>{{benefit1}}</li>
          <li>{{benefit2}}</li>
          <li>{{benefit3}}</li>
        </ul>
      </div>

      <div style="text-align: center; margin-top: 30px;">
        <div style="background: #FFC107; color: #333; display: inline-block; padding: 15px 30px; border-radius: 30px; font-size: 24px; font-weight: bold;">
          <s style="opacity: 0.7;">{{regularPrice}}</s>
          →
          {{discountPrice}}
          <span style="font-size: 14px; display: block; margin-top: 5px;">
            (Giảm {{discountPercent}}% - chỉ dành cho bạn)
          </span>
        </div>
      </div>
    </div>

    <div style="background: #FFF3E0; padding: 20px; border-left: 4px solid #FF9800; margin: 20px 0;">
      <h3 style="margin-top: 0;">⏰ Ưu đãi có hạn</h3>
      <p style="margin: 0;">
        Mã giảm giá <strong>{{couponCode}}</strong> chỉ có hiệu lực đến
        <strong>{{expiryDate}}</strong> (còn {{daysLeft}} ngày).
      </p>
    </div>

    <div style="text-align: center; margin: 30px 0;">
      <a href="{{checkoutLink}}" class="button" style="background: #E91E63; font-size: 18px; padding: 20px 50px;">
        NHẬN ƯU ĐÃI NGAY
      </a>
    </div>

    <h3>💬 Học viên nói gì về {{upsellProductName}}:</h3>

    <div style="background: #f9f9f9; padding: 20px; border-radius: 5px; margin: 15px 0;">
      <p style="font-style: italic; margin-bottom: 10px;">
        "{{testimonial1}}"
      </p>
      <p style="text-align: right; color: #666; margin: 0;">
        - {{testimonialAuthor1}}
      </p>
    </div>

    <div style="background: #f9f9f9; padding: 20px; border-radius: 5px; margin: 15px 0;">
      <p style="font-style: italic; margin-bottom: 10px;">
        "{{testimonial2}}"
      </p>
      <p style="text-align: right; color: #666; margin: 0;">
        - {{testimonialAuthor2}}
      </p>
    </div>

    <div style="background: #E8F5E9; padding: 20px; border-radius: 10px; margin: 30px 0;">
      <h3 style="margin-top: 0;">🎁 Bonus đặc biệt khi mua hôm nay:</h3>
      <ul>
        <li>{{bonus1}}</li>
        <li>{{bonus2}}</li>
        <li>{{bonus3}}</li>
      </ul>
      <p style="margin-bottom: 0;">
        <strong>Tổng giá trị bonus:</strong> {{bonusTotalValue}}
      </p>
    </div>

    <div style="text-align: center; margin: 30px 0;">
      <a href="{{checkoutLink}}" class="button" style="background: #4CAF50; font-size: 18px; padding: 20px 50px;">
        MUA NGAY - GIẢM {{discountPercent}}%
      </a>
    </div>

    <p style="text-align: center; color: #666; font-size: 14px;">
      Không quan tâm lúc này?
      <a href="{{unsubscribeLink}}" style="color: #666;">Hủy nhận email khuyến mãi</a>
    </p>
  </div>
</div>
```

### Personalization Logic
```javascript
function getUpsellProduct(purchasedProductId) {
  const upsellMap = {
    'beginner-marketing': {
      productId: 'advanced-marketing',
      name: 'Marketing Nâng Cao - Tăng Doanh Thu x10',
      description: 'Chiến lược marketing chuyên sâu cho doanh nghiệp',
      benefit1: 'Xây dựng phễu bán hàng tự động',
      benefit2: 'Tối ưu chi phí quảng cáo (giảm 50% CPA)',
      benefit3: 'Scale doanh thu từ 10 triệu → 100 triệu/tháng',
      regularPrice: '2,990,000 VND',
      discountPrice: '1,990,000 VND',
      discountPercent: '33',
      bonuses: [
        'Template phễu bán hàng (10 mẫu)',
        'Script quảng cáo Facebook (50 mẫu)',
        'Tư vấn 1-1 miễn phí (30 phút)'
      ]
    }
  };

  return upsellMap[purchasedProductId] || null;
}

async function sendMessage6(order) {
  const upsell = getUpsellProduct(order.product.id);

  if (!upsell) {
    console.log('No upsell product for', order.product.id);
    return;
  }

  const couponCode = await generateCoupon(order.customer.id, upsell.discountPercent);
  const expiryDate = new Date(Date.now() + 7 * 24 * 60 * 60 * 1000);

  const variables = {
    customerName: order.customer.name,
    productName: order.product.name,
    upsellProductName: upsell.name,
    upsellDescription: upsell.description,
    benefit1: upsell.benefit1,
    benefit2: upsell.benefit2,
    benefit3: upsell.benefit3,
    regularPrice: upsell.regularPrice,
    discountPrice: upsell.discountPrice,
    discountPercent: upsell.discountPercent,
    couponCode: couponCode,
    expiryDate: expiryDate.toLocaleDateString('vi-VN'),
    daysLeft: 7,
    checkoutLink: `${process.env.APP_URL}/checkout?product=${upsell.productId}&coupon=${couponCode}`,
    testimonial1: 'Khóa học này giúp tôi tăng doanh thu từ 15tr lên 80tr chỉ trong 2 tháng!',
    testimonialAuthor1: 'Trần Thị B - Chủ shop online',
    testimonial2: 'Chiến lược quảng cáo trong khóa học giúp tôi giảm chi phí 60% nhưng đơn hàng tăng gấp 3.',
    testimonialAuthor2: 'Lê Văn C - Marketing Manager',
    bonus1: upsell.bonuses[0],
    bonus2: upsell.bonuses[1],
    bonus3: upsell.bonuses[2],
    bonusTotalValue: '3,500,000 VND',
    unsubscribeLink: `${process.env.APP_URL}/unsubscribe?email=${order.customer.email}`
  };

  await sendEmail({
    to: order.customer.email,
    subject: `🚀 [Ưu đãi đặc biệt] Bước tiếp theo sau ${order.product.name}`,
    template: 'message-6-upsell',
    variables
  });

  await logEngagementMessage(order.id, 'message_6', 'sent');
}
```

## Automation Setup

### Cron-based Scheduler
```javascript
const cron = require('node-cron');

// Run every hour to check for due messages
cron.schedule('0 * * * *', async () => {
  await processEngagementSequence();
});

async function processEngagementSequence() {
  const now = new Date();

  // Message 2: Day 1
  const day1Orders = await getOrdersFromDaysAgo(1);
  for (const order of day1Orders) {
    if (!await hasReceivedMessage(order.id, 'message_2')) {
      await sendMessage2(order);
    }
  }

  // Message 3: Day 3
  const day3Orders = await getOrdersFromDaysAgo(3);
  for (const order of day3Orders) {
    if (!await hasReceivedMessage(order.id, 'message_3')) {
      await sendMessage3(order);
    }
  }

  // Message 4: Day 5
  const day5Orders = await getOrdersFromDaysAgo(5);
  for (const order of day5Orders) {
    if (!await hasReceivedMessage(order.id, 'message_4')) {
      await sendMessage4(order);
    }
  }

  // Message 5: Day 7
  const day7Orders = await getOrdersFromDaysAgo(7);
  for (const order of day7Orders) {
    if (!await hasReceivedMessage(order.id, 'message_5')) {
      await sendMessage5(order);
    }
  }

  // Message 6: Day 14
  const day14Orders = await getOrdersFromDaysAgo(14);
  for (const order of day14Orders) {
    if (!await hasReceivedMessage(order.id, 'message_6')) {
      await sendMessage6(order);
    }
  }
}

async function getOrdersFromDaysAgo(days) {
  const targetDate = new Date(Date.now() - days * 24 * 60 * 60 * 1000);
  const startOfDay = new Date(targetDate.setHours(0, 0, 0, 0));
  const endOfDay = new Date(targetDate.setHours(23, 59, 59, 999));

  return await db.orders.findAll({
    where: {
      createdAt: {
        $gte: startOfDay,
        $lte: endOfDay
      },
      status: 'completed'
    },
    include: [db.products, db.customers]
  });
}

async function hasReceivedMessage(orderId, messageType) {
  const log = await db.engagementLogs.findOne({
    where: { orderId, messageType, status: 'sent' }
  });
  return !!log;
}
```

### Queue-based (Production)
```javascript
const Queue = require('bull');

const engagementQueue = new Queue('engagement', {
  redis: {
    host: process.env.REDIS_HOST,
    port: process.env.REDIS_PORT
  }
});

// Schedule messages when order is created
async function scheduleEngagementSequence(order) {
  // Message 1: Immediate
  await engagementQueue.add('message_1', { orderId: order.id }, { delay: 0 });

  // Message 2: Day 1
  await engagementQueue.add('message_2', { orderId: order.id }, { delay: 24 * 60 * 60 * 1000 });

  // Message 3: Day 3
  await engagementQueue.add('message_3', { orderId: order.id }, { delay: 3 * 24 * 60 * 60 * 1000 });

  // Message 4: Day 5
  await engagementQueue.add('message_4', { orderId: order.id }, { delay: 5 * 24 * 60 * 60 * 1000 });

  // Message 5: Day 7
  await engagementQueue.add('message_5', { orderId: order.id }, { delay: 7 * 24 * 60 * 60 * 1000 });

  // Message 6: Day 14
  await engagementQueue.add('message_6', { orderId: order.id }, { delay: 14 * 24 * 60 * 60 * 1000 });
}

// Process queue
engagementQueue.process(async (job) => {
  const { orderId } = job.data;
  const order = await getOrderWithDetails(orderId);

  switch (job.name) {
    case 'message_1':
      await sendMessage1(order);
      break;
    case 'message_2':
      await sendMessage2(order);
      break;
    case 'message_3':
      await sendMessage3(order);
      break;
    case 'message_4':
      await sendMessage4(order);
      break;
    case 'message_5':
      await sendMessage5(order);
      break;
    case 'message_6':
      await sendMessage6(order);
      break;
  }
});
```

## Vietnamese Market Tone Guidelines

### Professional vs Friendly Balance
```
Too formal: "Quý khách vui lòng kiểm tra email để nhận sản phẩm."
✅ Right: "Bạn có thể tải sản phẩm ngay qua link trong email nhé!"

Too casual: "Ê check email đi bạn ơi!!!"
✅ Right: "Nhớ kiểm tra email để nhận sản phẩm nha bạn!"
```

### Use "Bạn" not "Quý khách"
- "Bạn" = friendly, relatable (consumer market)
- "Quý khách" = formal, distant (B2B or luxury)

### Add emotional encouragement
- "Chúc mừng bạn!" (Congratulations!)
- "Bạn làm tốt lắm!" (You're doing great!)
- "Chúng tôi tin bạn sẽ thành công!" (We believe you'll succeed!)

## Metrics to Track

```javascript
// Engagement analytics
async function getEngagementMetrics(startDate, endDate) {
  return {
    message1OpenRate: await getOpenRate('message_1', startDate, endDate),
    message2OpenRate: await getOpenRate('message_2', startDate, endDate),
    message3ClickRate: await getClickRate('message_3', startDate, endDate),
    message4ResponseRate: await getResponseRate('message_4', startDate, endDate),
    message5ReviewRate: await getReviewSubmissionRate(startDate, endDate),
    message6ConversionRate: await getUpsellConversionRate(startDate, endDate)
  };
}
```

## Testing Checklist

- [ ] All message templates render correctly
- [ ] Variables replaced properly
- [ ] Links work and track clicks
- [ ] Unsubscribe link functional
- [ ] Mobile email rendering tested
- [ ] Telegram formatting correct
- [ ] Scheduling logic accurate
- [ ] Duplicate prevention working
- [ ] Analytics tracking implemented
- [ ] Vietnamese language review completed
