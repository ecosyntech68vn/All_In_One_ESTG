# Notification Message Templates

Ready-to-use Telegram notification templates for Vietnamese market.

## Template 1: New Order Received

### Markdown Format
```markdown
🛒 *ĐƠN HÀNG MỚI*

📋 Mã đơn: `{{orderId}}`
👤 Khách hàng: {{customerName}}
📞 SĐT: {{customerPhone}}
📦 Sản phẩm: {{productName}}
💰 Số tiền: `{{amount}} VND`
💳 Thanh toán: {{paymentMethod}}
⏰ Thời gian: {{timestamp}}

✅ Trạng thái: *Đã thanh toán*

📧 Email xác nhận đã được gửi tự động.
```

### Variables
- `{{orderId}}` - Order ID (e.g., "ORDER12345")
- `{{customerName}}` - Customer full name
- `{{customerPhone}}` - Phone number with country code
- `{{productName}}` - Product title
- `{{amount}}` - Formatted amount (e.g., "1,500,000")
- `{{paymentMethod}}` - "VietQR", "Chuyển khoản", etc.
- `{{timestamp}}` - Localized datetime

### When to Use
- Immediately after payment confirmation webhook
- For every successful order
- Send to owner/admin chat

### Code Example
```javascript
function sendNewOrderNotification(order) {
  const message = `
🛒 *ĐƠN HÀNG MỚI*

📋 Mã đơn: \`${order.id}\`
👤 Khách hàng: ${order.customer.name}
📞 SĐT: ${order.customer.phone}
📦 Sản phẩm: ${order.product.name}
💰 Số tiền: \`${order.amount.toLocaleString('vi-VN')} VND\`
💳 Thanh toán: ${order.paymentMethod}
⏰ Thời gian: ${new Date().toLocaleString('vi-VN')}

✅ Trạng thái: *Đã thanh toán*

📧 Email xác nhận đã được gửi tự động.
`;

  sendTelegramMessage(message);
}
```

## Template 2: Payment Confirmed

### Markdown Format
```markdown
✅ *THANH TOÁN THÀNH CÔNG*

🔖 Mã giao dịch: `{{transactionId}}`
📦 Đơn hàng: `{{orderId}}`
💵 Số tiền: `{{amount}} VND`
💳 Phương thức: {{paymentMethod}}
🏦 Ngân hàng: {{bankName}}
⏰ Thời gian: {{timestamp}}

🎉 Đơn hàng đang được xử lý.
📧 Khách hàng sẽ nhận link truy cập trong vài phút.
```

### Variables
- `{{transactionId}}` - Bank transaction reference
- `{{orderId}}` - Internal order ID
- `{{amount}}` - Payment amount formatted
- `{{paymentMethod}}` - Payment method name
- `{{bankName}}` - Bank brand name
- `{{timestamp}}` - Transaction time

### When to Use
- After successful payment webhook from SePay
- To confirm payment processing to team
- When transaction ID is available

### Code Example
```javascript
function sendPaymentConfirmation(payment) {
  const message = `
✅ *THANH TOÁN THÀNH CÔNG*

🔖 Mã giao dịch: \`${payment.referenceCode}\`
📦 Đơn hàng: \`${payment.orderCode}\`
💵 Số tiền: \`${payment.amount.toLocaleString('vi-VN')} VND\`
💳 Phương thức: ${payment.method}
🏦 Ngân hàng: ${payment.bankName}
⏰ Thời gian: ${new Date(payment.timestamp).toLocaleString('vi-VN')}

🎉 Đơn hàng đang được xử lý.
📧 Khách hàng sẽ nhận link truy cập trong vài phút.
`;

  sendTelegramMessage(message);
}
```

## Template 3: Payment Failed/Pending

### Failed Payment
```markdown
❌ *THANH TOÁN THẤT BẠI*

📋 Đơn hàng: `{{orderId}}`
👤 Khách hàng: {{customerName}}
💰 Số tiền: `{{amount}} VND`
⚠️ Lý do: {{failureReason}}

🔄 *Hành động:*
• Khách hàng cần thử lại
• Hoặc liên hệ hỗ trợ: {{supportContact}}

⏰ {{timestamp}}
```

### Pending Payment
```markdown
⏳ *THANH TOÁN ĐANG CHỜ*

📋 Đơn hàng: `{{orderId}}`
👤 Khách hàng: {{customerName}}
💰 Số tiền: `{{amount}} VND`
⚠️ Trạng thái: {{pendingReason}}

⏱️ Thời gian chờ còn lại: {{remainingTime}}
🔄 Hệ thống đang kiểm tra giao dịch...

ℹ️ Nếu quá 15 phút chưa có kết quả, vui lòng kiểm tra thủ công.
```

### When to Use
- Failed: When payment validation fails
- Pending: When waiting for bank confirmation
- To alert team for manual intervention

### Code Example
```javascript
function sendPaymentFailedNotification(order, reason) {
  const message = `
❌ *THANH TOÁN THẤT BẠI*

📋 Đơn hàng: \`${order.id}\`
👤 Khách hàng: ${order.customer.name}
💰 Số tiền: \`${order.amount.toLocaleString('vi-VN')} VND\`
⚠️ Lý do: ${reason}

🔄 *Hành động:*
• Khách hàng cần thử lại
• Hoặc liên hệ hỗ trợ: ${process.env.SUPPORT_CONTACT}

⏰ ${new Date().toLocaleString('vi-VN')}
`;

  sendTelegramMessage(message);
}
```

## Template 4: Product Delivered

### Digital Product
```markdown
📦 *SẢN PHẨM ĐÃ GIAO*

📋 Đơn hàng: `{{orderId}}`
👤 Khách hàng: {{customerName}}
📧 Email: {{customerEmail}}
📦 Sản phẩm: {{productName}}
🚀 Phương thức: {{deliveryMethod}}

✅ *Giao hàng thành công:*
{{#if deliveryMethod == 'email'}}
• Email đã gửi đến {{customerEmail}}
• Link truy cập có hiệu lực {{expiryTime}}
{{else if deliveryMethod == 'telegram'}}
• File đã gửi qua Telegram
• Khách hàng: @{{telegramUsername}}
{{else}}
• Link: {{deliveryLink}}
{{/if}}

⏰ {{timestamp}}
```

### When to Use
- Immediately after successful delivery
- To confirm delivery method worked
- For tracking delivery metrics

### Code Example
```javascript
function sendDeliveryNotification(order, delivery) {
  let deliveryInfo = '';

  if (delivery.method === 'email') {
    deliveryInfo = `• Email đã gửi đến ${order.customer.email}\n• Link truy cập có hiệu lực 7 ngày`;
  } else if (delivery.method === 'telegram') {
    deliveryInfo = `• File đã gửi qua Telegram\n• Khách hàng: @${delivery.telegramUsername}`;
  } else {
    deliveryInfo = `• Link: ${delivery.link}`;
  }

  const message = `
📦 *SẢN PHẨM ĐÃ GIAO*

📋 Đơn hàng: \`${order.id}\`
👤 Khách hàng: ${order.customer.name}
📧 Email: ${order.customer.email}
📦 Sản phẩm: ${order.product.name}
🚀 Phương thức: ${delivery.method}

✅ *Giao hàng thành công:*
${deliveryInfo}

⏰ ${new Date().toLocaleString('vi-VN')}
`;

  sendTelegramMessage(message);
}
```

## Template 5: Daily Summary

### End-of-Day Report
```markdown
📊 *BÁO CÁO CUỐI NGÀY*
📅 Ngày: {{date}}

💰 *Doanh thu:*
• Tổng: `{{totalRevenue}} VND`
• Số đơn: {{totalOrders}} đơn
• Trung bình: `{{averageOrder}} VND`

📦 *Sản phẩm bán chạy:*
1️⃣ {{topProduct1}} - {{count1}} đơn
2️⃣ {{topProduct2}} - {{count2}} đơn
3️⃣ {{topProduct3}} - {{count3}} đơn

💳 *Phương thức thanh toán:*
• VietQR: {{qrCount}} đơn ({{qrPercent}}%)
• Chuyển khoản: {{transferCount}} đơn ({{transferPercent}}%)

📈 So với hôm qua: {{comparison}}
{{#if comparison > 0}}🎉{{else}}📉{{/if}}

⏰ Báo cáo tạo lúc: {{timestamp}}
```

### When to Use
- Scheduled daily at end of business hours (e.g., 11 PM)
- For daily performance tracking
- To identify trends and top products

### Code Example
```javascript
const cron = require('node-cron');

// Run daily at 11 PM
cron.schedule('0 23 * * *', async () => {
  const stats = await getDailyStats();

  const message = `
📊 *BÁO CÁO CUỐI NGÀY*
📅 Ngày: ${new Date().toLocaleDateString('vi-VN')}

💰 *Doanh thu:*
• Tổng: \`${stats.totalRevenue.toLocaleString('vi-VN')} VND\`
• Số đơn: ${stats.totalOrders} đơn
• Trung bình: \`${stats.averageOrder.toLocaleString('vi-VN')} VND\`

📦 *Sản phẩm bán chạy:*
${stats.topProducts.map((p, i) => `${i+1}️⃣ ${p.name} - ${p.count} đơn`).join('\n')}

💳 *Phương thức thanh toán:*
• VietQR: ${stats.qrCount} đơn (${stats.qrPercent}%)
• Chuyển khoản: ${stats.transferCount} đơn (${stats.transferPercent}%)

📈 So với hôm qua: ${stats.comparison > 0 ? '+' : ''}${stats.comparison}% ${stats.comparison > 0 ? '🎉' : '📉'}

⏰ Báo cáo tạo lúc: ${new Date().toLocaleTimeString('vi-VN')}
`;

  sendTelegramMessage(message);
});
```

## Template 6: Low Stock Alert

### Inventory Warning
```markdown
⚠️ *CẢNH BÁO TỒN KHO*

📦 Sản phẩm: {{productName}}
📊 Số lượng còn: {{remainingStock}} {{unit}}
🔴 Ngưỡng cảnh báo: {{threshold}} {{unit}}

📈 *Thống kê bán:*
• Hôm nay: {{soldToday}} {{unit}}
• 7 ngày: {{soldWeek}} {{unit}}
• Trung bình/ngày: {{avgDaily}} {{unit}}

⏱️ *Dự kiến hết hàng:* {{estimatedRunout}}

🔄 *Hành động khuyến nghị:*
{{#if remainingStock == 0}}
• ❌ HẾT HÀNG - Tạm ẩn sản phẩm ngay
• 📞 Liên hệ nhà cung cấp khẩn cấp
{{else if remainingStock < threshold}}
• 📦 Chuẩn bị nhập thêm
• 🔔 Thông báo khách hàng về tình trạng
{{/if}}

⏰ {{timestamp}}
```

### When to Use
- When stock drops below threshold
- After each sale that affects inventory
- Daily inventory check (automated)

### Code Example
```javascript
async function checkInventoryAndAlert() {
  const products = await getProducts();

  for (const product of products) {
    if (product.stock <= product.alertThreshold) {
      const message = `
⚠️ *CẢNH BÁO TỒN KHO*

📦 Sản phẩm: ${product.name}
📊 Số lượng còn: ${product.stock} ${product.unit}
🔴 Ngưỡng cảnh báo: ${product.alertThreshold} ${product.unit}

📈 *Thống kê bán:*
• Hôm nay: ${product.soldToday} ${product.unit}
• 7 ngày: ${product.soldWeek} ${product.unit}
• Trung bình/ngày: ${Math.round(product.soldWeek / 7)} ${product.unit}

⏱️ *Dự kiến hết hàng:* ${estimateRunout(product)} ngày

🔄 *Hành động khuyến nghị:*
${product.stock === 0
  ? '• ❌ HẾT HÀNG - Tạm ẩn sản phẩm ngay\n• 📞 Liên hệ nhà cung cấp khẩn cấp'
  : '• 📦 Chuẩn bị nhập thêm\n• 🔔 Thông báo khách hàng về tình trạng'
}

⏰ ${new Date().toLocaleString('vi-VN')}
`;

      sendTelegramMessage(message);
    }
  }
}

// Run every 6 hours
cron.schedule('0 */6 * * *', checkInventoryAndAlert);
```

## Vietnamese-Friendly Message Tone

### Professional vs Casual

**Professional (for business products):**
```
✅ Đơn hàng đã được xác nhận thành công.
📧 Email xác nhận đã được gửi đến khách hàng.
🙏 Cảm ơn quý khách đã tin tưởng sản phẩm của chúng tôi.
```

**Casual (for lifestyle/consumer products):**
```
🎉 Yeahh! Có đơn mới rồi nè!
📦 Sản phẩm đang được chuẩn bị giao cho khách nha.
💕 Cảm ơn bạn đã ủng hộ mình nhé!
```

### Action-Oriented Language
- ✅ Use: "Vui lòng kiểm tra email" (Please check email)
- ❌ Avoid: "Email có thể đã được gửi" (Email may have been sent)

- ✅ Use: "Liên hệ ngay: 0912345678" (Contact now)
- ❌ Avoid: "Có thể liên hệ nếu cần" (May contact if needed)

## Emoji Usage Guidelines

### Recommended Emojis for Business

**Status:**
- ✅ Success, confirmed, completed
- ⏳ Pending, waiting
- ❌ Failed, error, cancelled
- ⚠️ Warning, alert, attention needed

**Money & Business:**
- 💰 Money, revenue, payment
- 💵 Cash, amount
- 💳 Payment method, card
- 🏦 Bank
- 📊 Statistics, report
- 📈 Growth, increase
- 📉 Decrease, decline

**Order & Product:**
- 🛒 Cart, new order
- 📦 Package, product, delivery
- 📋 Order details, list
- 🔖 Transaction ID, reference

**Communication:**
- 📧 Email
- 📞 Phone call
- 💬 Message, chat
- 🔔 Notification

**Time:**
- ⏰ Time, timestamp
- ⏱️ Countdown, timer
- 📅 Date, calendar

**Action:**
- 🔄 Retry, refresh, process
- 🚀 Launch, deliver
- 🎉 Celebration, success
- 🔍 Check, review
- 👤 Customer, user

### Emoji Placement Rules
1. **Start of line** for visual hierarchy
2. **One emoji per line** (max 2 for emphasis)
3. **Consistent usage** across templates
4. **Avoid emoji spam** (no more than 30% of characters)

## Template Variables Reference

### Common Variables
```javascript
{
  // Order info
  orderId: 'ORDER12345',
  orderCode: 'DH12345',

  // Customer info
  customerName: 'Nguyễn Văn A',
  customerPhone: '+84912345678',
  customerEmail: 'customer@example.com',

  // Product info
  productName: 'Khóa học Marketing Online',
  productSku: 'SKU-001',

  // Payment info
  amount: 1500000, // Store as number
  amountFormatted: '1,500,000', // Display formatted
  paymentMethod: 'VietQR',
  bankName: 'MB Bank',
  transactionId: 'FT26044123456789',

  // Timestamp
  timestamp: new Date().toLocaleString('vi-VN'),
  date: new Date().toLocaleDateString('vi-VN'),
  time: new Date().toLocaleTimeString('vi-VN'),

  // Delivery info
  deliveryMethod: 'email', // 'email' | 'telegram' | 'link'
  deliveryLink: 'https://example.com/download/abc123',

  // Support info
  supportContact: 'Zalo: 0912345678',
  supportEmail: 'support@example.com'
}
```

## Message Testing Checklist

Before deploying templates:

- [ ] Test all variable replacements
- [ ] Verify Markdown rendering in Telegram
- [ ] Check message length (< 4096 characters)
- [ ] Test on mobile and desktop Telegram
- [ ] Verify Vietnamese characters display correctly
- [ ] Check emoji rendering
- [ ] Test link formatting
- [ ] Verify timestamp format
- [ ] Test with missing variables (fallback values)
- [ ] Check message arrival time

## A/B Testing Recommendations

Test variations of:
1. **Emoji placement** (start vs inline)
2. **Message length** (concise vs detailed)
3. **CTA wording** (direct vs polite)
4. **Tone** (professional vs casual)
5. **Information order** (amount first vs customer first)

Track metrics:
- Click-through rate (for links)
- Support inquiry rate (fewer = better clarity)
- Customer satisfaction feedback
