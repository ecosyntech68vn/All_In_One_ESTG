# Automated Delivery Workflow

End-to-end automation from payment to product delivery.

## Workflow Overview

```
Payment Webhook → Validate → Extract Order → Lookup Product
→ Select Delivery Method → Execute Delivery → Log Status
→ Send Confirmation → Error Recovery
```

## Step 1: Payment Webhook Received

### Webhook Entry Point
```javascript
const express = require('express');
const app = express();

app.post('/webhook/sepay', async (req, res) => {
  console.log('📥 Webhook received:', new Date().toISOString());

  // Respond immediately (don't make webhook source wait)
  res.status(200).json({ status: 'received' });

  // Process asynchronously
  processPaymentWebhook(req.body, req.headers)
    .catch(error => {
      console.error('❌ Processing error:', error);
      handleFailedDelivery(req.body, error);
    });
});
```

### Validate Signature
```javascript
const crypto = require('crypto');

function validateWebhookSignature(headers, payload) {
  const signature = headers['x-sepay-signature'];
  const secret = process.env.SEPAY_WEBHOOK_SECRET;

  if (!signature || !secret) {
    return { valid: false, reason: 'Missing signature or secret' };
  }

  const hmac = crypto.createHmac('sha256', secret);
  hmac.update(JSON.stringify(payload));
  const expectedSignature = hmac.digest('hex');

  const isValid = crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(expectedSignature)
  );

  return isValid
    ? { valid: true }
    : { valid: false, reason: 'Invalid signature' };
}
```

## Step 2: Extract Order Details

### Parse Webhook Payload
```javascript
function extractOrderDetails(webhookPayload) {
  // SePay payload structure
  const orderCode = webhookPayload.content; // e.g., "ORDER12345"
  const amount = parseInt(webhookPayload.transferAmount);
  const referenceCode = webhookPayload.referenceCode;
  const timestamp = new Date(webhookPayload.transactionDate);

  // Extract customer info from description
  const description = webhookPayload.description;
  const customerName = extractCustomerName(description);

  return {
    orderCode,
    amount,
    referenceCode,
    timestamp,
    customerName,
    bankName: webhookPayload.bankBrandName
  };
}

function extractCustomerName(description) {
  // Example: "MB NGUYEN VAN A chuyen tien ORDER12345"
  const match = description.match(/[A-Z]{2}\s([A-Z\s]+)\s(chuyen|CT)/i);
  return match ? match[1].trim() : 'Unknown';
}
```

### Lookup Order in Database
```javascript
async function getOrderByCode(orderCode) {
  // Query database for order
  const order = await db.orders.findOne({
    where: { code: orderCode }
  });

  if (!order) {
    throw new Error(`Order not found: ${orderCode}`);
  }

  // Include customer and product details
  const fullOrder = await db.orders.findOne({
    where: { id: order.id },
    include: [
      { model: db.customers },
      { model: db.products }
    ]
  });

  return fullOrder;
}
```

## Step 3: Product Lookup

### Map Product ID to Delivery Assets
```javascript
async function getProductDeliveryConfig(productId) {
  const product = await db.products.findByPk(productId);

  if (!product) {
    throw new Error(`Product not found: ${productId}`);
  }

  // Product delivery configuration
  return {
    id: product.id,
    name: product.name,
    deliveryMethod: product.deliveryMethod, // 'email' | 'telegram' | 'link' | 'notion'

    // File delivery
    filePath: product.filePath, // Local file path
    fileName: product.fileName, // Download filename

    // Link delivery
    accessPageUrl: product.accessPageUrl,
    accessDuration: product.accessDuration || 365, // Days

    // Google Drive
    googleDriveFileId: product.googleDriveFileId,

    // Notion
    notionPageId: product.notionPageId,

    // Email template
    emailSubject: product.emailSubject,
    emailTemplate: product.emailTemplate
  };
}
```

### Database Schema for Products
```sql
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  price INTEGER NOT NULL,
  delivery_method VARCHAR(20) NOT NULL, -- 'email', 'telegram', 'link', 'hybrid'

  -- File delivery
  file_path VARCHAR(500),
  file_name VARCHAR(255),
  file_size BIGINT,

  -- Link delivery
  access_page_url VARCHAR(500),
  access_duration INTEGER DEFAULT 365, -- days

  -- Third-party
  google_drive_file_id VARCHAR(100),
  notion_page_id VARCHAR(100),

  -- Email config
  email_subject VARCHAR(255),
  email_template TEXT,

  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);
```

## Step 4: Select Delivery Method

### Decision Logic
```javascript
async function selectDeliveryMethod(order, product) {
  const customer = order.customer;

  // Priority 1: Customer preference (if they provided Telegram)
  if (customer.telegram && product.deliveryMethod.includes('telegram')) {
    return 'telegram';
  }

  // Priority 2: Product default method
  if (product.deliveryMethod === 'link') {
    return 'link';
  }

  if (product.deliveryMethod === 'notion') {
    return 'notion';
  }

  if (product.deliveryMethod === 'gdrive') {
    return 'gdrive';
  }

  // Priority 3: Email fallback (always works)
  return 'email';
}
```

### Hybrid Approach
```javascript
async function deliverViaMultipleMethods(order, product) {
  const results = {
    telegram: null,
    email: null,
    link: null
  };

  // Try Telegram first (fastest)
  if (order.customer.telegram) {
    try {
      await deliverViaTelegram(order, product);
      results.telegram = { success: true, timestamp: new Date() };
    } catch (error) {
      results.telegram = { success: false, error: error.message };
    }
  }

  // Always send email (backup + receipt)
  try {
    await deliverViaEmail(order, product);
    results.email = { success: true, timestamp: new Date() };
  } catch (error) {
    results.email = { success: false, error: error.message };
  }

  // Always create access link (permanent backup)
  try {
    const accessLink = await createAccessLink(order, product);
    results.link = { success: true, url: accessLink, timestamp: new Date() };
  } catch (error) {
    results.link = { success: false, error: error.message };
  }

  return results;
}
```

## Step 5a: Email Delivery

### Nodemailer Setup
```javascript
const nodemailer = require('nodemailer');

const transporter = nodemailer.createTransport({
  host: process.env.SMTP_HOST,
  port: process.env.SMTP_PORT,
  auth: {
    user: process.env.SMTP_USER,
    pass: process.env.SMTP_PASS
  }
});

async function deliverViaEmail(order, product) {
  // Generate download link
  const downloadLink = generateDownloadToken(order.id, product.id);

  // Render email template
  const emailHtml = renderEmailTemplate(order, product, downloadLink);

  // Send email
  const info = await transporter.sendMail({
    from: `"${process.env.STORE_NAME}" <${process.env.STORE_EMAIL}>`,
    to: order.customer.email,
    subject: `[${order.code}] ${product.emailSubject || product.name}`,
    html: emailHtml
  });

  console.log('✅ Email sent:', info.messageId);

  // Log delivery
  await logDelivery(order.id, 'email', {
    messageId: info.messageId,
    recipient: order.customer.email,
    downloadLink
  });

  return { success: true, messageId: info.messageId };
}
```

### Email Template
```javascript
function renderEmailTemplate(order, product, downloadLink) {
  return `
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
    .container { max-width: 600px; margin: 0 auto; padding: 20px; }
    .header { background: #4CAF50; color: white; padding: 20px; text-align: center; }
    .content { padding: 30px 20px; }
    .button {
      display: inline-block;
      background: #4CAF50;
      color: white;
      padding: 15px 30px;
      text-decoration: none;
      border-radius: 5px;
      font-weight: bold;
      margin: 20px 0;
    }
    .footer {
      background: #f5f5f5;
      padding: 20px;
      text-align: center;
      font-size: 12px;
      color: #666;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>🎉 Cảm ơn bạn đã mua hàng!</h1>
    </div>

    <div class="content">
      <p>Xin chào <strong>${order.customer.name}</strong>,</p>

      <p>Đơn hàng <strong>${order.code}</strong> đã được thanh toán thành công.</p>

      <h3>📦 Chi tiết đơn hàng:</h3>
      <ul>
        <li><strong>Sản phẩm:</strong> ${product.name}</li>
        <li><strong>Số tiền:</strong> ${order.amount.toLocaleString('vi-VN')} VND</li>
        <li><strong>Ngày mua:</strong> ${new Date().toLocaleDateString('vi-VN')}</li>
      </ul>

      <p style="text-align: center;">
        <a href="${downloadLink}" class="button">
          TẢI XUỐNG NGAY
        </a>
      </p>

      <p><em>💡 Link có hiệu lực trong 7 ngày. Vui lòng tải về và lưu trữ sản phẩm.</em></p>

      <hr>

      <h3>📧 Cần hỗ trợ?</h3>
      <p>
        Email: ${process.env.SUPPORT_EMAIL}<br>
        Zalo/Telegram: ${process.env.SUPPORT_PHONE}
      </p>
    </div>

    <div class="footer">
      <p>&copy; ${new Date().getFullYear()} ${process.env.STORE_NAME}. All rights reserved.</p>
      <p>Email này được gửi tự động, vui lòng không trả lời.</p>
    </div>
  </div>
</body>
</html>
  `;
}
```

## Step 5b: Telegram Delivery

### Send File via Bot
```javascript
const axios = require('axios');
const FormData = require('form-data');
const fs = require('fs');

async function deliverViaTelegram(order, product) {
  const botToken = process.env.TELEGRAM_BOT_TOKEN;

  // Get customer chat ID
  const chatId = await getCustomerChatId(order.customer.telegram);

  if (!chatId) {
    throw new Error('Customer has not started bot conversation');
  }

  // Send file
  const form = new FormData();
  form.append('chat_id', chatId);
  form.append('document', fs.createReadStream(product.filePath));
  form.append('caption', `
🎉 *Cảm ơn bạn đã mua ${product.name}!*

📋 Mã đơn: \`${order.code}\`
💰 Số tiền: \`${order.amount.toLocaleString('vi-VN')} VND\`

📥 File đính kèm là sản phẩm của bạn.

💬 Cần hỗ trợ? Nhắn tin trực tiếp tại đây!
  `);
  form.append('parse_mode', 'Markdown');

  const response = await axios.post(
    `https://api.telegram.org/bot${botToken}/sendDocument`,
    form,
    {
      headers: form.getHeaders(),
      maxBodyLength: Infinity,
      maxContentLength: Infinity
    }
  );

  console.log('✅ Telegram file sent');

  // Log delivery
  await logDelivery(order.id, 'telegram', {
    messageId: response.data.result.message_id,
    chatId: chatId,
    fileName: product.fileName
  });

  return { success: true, messageId: response.data.result.message_id };
}
```

### Get Customer Chat ID
```javascript
// Store chat IDs when customer interacts with bot
const chatIdCache = new Map(); // In production: use Redis

async function getCustomerChatId(telegramUsername) {
  // Remove @ if present
  const username = telegramUsername.replace('@', '');

  // Check cache
  if (chatIdCache.has(username)) {
    return chatIdCache.get(username);
  }

  // Check database
  const customer = await db.customers.findOne({
    where: { telegram: username }
  });

  if (customer && customer.telegramChatId) {
    chatIdCache.set(username, customer.telegramChatId);
    return customer.telegramChatId;
  }

  return null;
}

// Bot handler to store chat IDs
app.post('/webhook/telegram', async (req, res) => {
  const update = req.body;

  if (update.message && update.message.text === '/start') {
    const chatId = update.message.chat.id;
    const username = update.message.from.username;

    // Store chat ID
    await db.customers.update(
      { telegramChatId: chatId },
      { where: { telegram: username } }
    );

    chatIdCache.set(username, chatId);

    // Send welcome message
    await sendTelegramMessage(
      '✅ Bot đã kích hoạt! Bạn sẽ nhận sản phẩm tự động sau khi thanh toán.',
      chatId
    );
  }

  res.sendStatus(200);
});
```

## Step 5c: Redirect URL Generation

### Generate Signed Token URL
```javascript
const jwt = require('jsonwebtoken');

function createAccessLink(order, product) {
  // Create access record
  const accessRecord = {
    orderId: order.id,
    productId: product.id,
    customerId: order.customer.id,
    expiresAt: new Date(Date.now() + product.accessDuration * 24 * 60 * 60 * 1000)
  };

  // Generate token
  const token = jwt.sign(
    accessRecord,
    process.env.JWT_SECRET,
    { expiresIn: `${product.accessDuration}d` }
  );

  // Create URL
  const accessUrl = `${process.env.APP_URL}/access/${token}`;

  // Store in database
  db.accessTokens.create({
    orderId: order.id,
    token: token,
    expiresAt: accessRecord.expiresAt
  });

  return accessUrl;
}
```

### Access Page Handler
```javascript
app.get('/access/:token', async (req, res) => {
  try {
    // Verify token
    const decoded = jwt.verify(req.params.token, process.env.JWT_SECRET);

    // Get order and product
    const order = await db.orders.findByPk(decoded.orderId, {
      include: [db.products, db.customers]
    });

    if (!order) {
      return res.status(404).send('Order not found');
    }

    // Log access
    await logAccess(order.id, req.ip);

    // Render access page
    res.render('access-page', {
      order: order,
      product: order.product,
      customer: order.customer,
      expiresAt: decoded.expiresAt
    });

  } catch (error) {
    if (error.name === 'TokenExpiredError') {
      res.status(410).send('Access link has expired. Please contact support.');
    } else {
      res.status(401).send('Invalid access link.');
    }
  }
});
```

## Step 6: Log Delivery Status

### Database Schema
```sql
CREATE TABLE delivery_logs (
  id SERIAL PRIMARY KEY,
  order_id INTEGER REFERENCES orders(id),
  method VARCHAR(20) NOT NULL, -- 'email', 'telegram', 'link'
  status VARCHAR(20) NOT NULL, -- 'success', 'failed', 'retry'
  metadata JSONB,
  error_message TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);
```

### Logging Function
```javascript
async function logDelivery(orderId, method, metadata = {}, error = null) {
  await db.deliveryLogs.create({
    orderId: orderId,
    method: method,
    status: error ? 'failed' : 'success',
    metadata: metadata,
    errorMessage: error ? error.message : null
  });

  // Update order status
  await db.orders.update(
    {
      deliveryStatus: error ? 'failed' : 'delivered',
      deliveryMethod: method,
      deliveredAt: error ? null : new Date()
    },
    { where: { id: orderId } }
  );
}
```

## Step 7: Send Confirmation to Customer

### Confirmation Message
```javascript
async function sendDeliveryConfirmation(order, deliveryResults) {
  const successMethods = Object.entries(deliveryResults)
    .filter(([_, result]) => result.success)
    .map(([method, _]) => method);

  let message = `
✅ *XÁC NHẬN GIAO HÀNG*

📦 Đơn hàng: \`${order.code}\`
🎯 Sản phẩm: ${order.product.name}
💰 Số tiền: \`${order.amount.toLocaleString('vi-VN')} VND\`

🚀 *Phương thức giao:*
${successMethods.map(m => `• ${methodLabels[m]}`).join('\n')}

⏰ Giao lúc: ${new Date().toLocaleString('vi-VN')}

✅ Giao hàng thành công!
`;

  // Send to admin
  await sendTelegramMessage(message, process.env.ADMIN_CHAT_ID);
}

const methodLabels = {
  email: '📧 Email',
  telegram: '💬 Telegram',
  link: '🔗 Link truy cập'
};
```

## Step 8: Error Recovery

### Retry Failed Deliveries
```javascript
async function retryFailedDelivery(order, product, failedMethod) {
  const maxRetries = 3;
  let attempt = 0;

  while (attempt < maxRetries) {
    attempt++;

    try {
      console.log(`🔄 Retry attempt ${attempt}/${maxRetries} for order ${order.code}`);

      // Retry based on failed method
      if (failedMethod === 'email') {
        await deliverViaEmail(order, product);
      } else if (failedMethod === 'telegram') {
        await deliverViaTelegram(order, product);
      }

      console.log(`✅ Retry successful on attempt ${attempt}`);
      return { success: true, attempts: attempt };

    } catch (error) {
      console.error(`❌ Retry ${attempt} failed:`, error.message);

      if (attempt >= maxRetries) {
        // All retries failed - alert admin
        await alertAdminFailedDelivery(order, failedMethod, error);
        return { success: false, attempts: attempt, error: error.message };
      }

      // Wait before next retry (exponential backoff)
      const delay = Math.pow(2, attempt) * 1000; // 2s, 4s, 8s
      await new Promise(resolve => setTimeout(resolve, delay));
    }
  }
}

async function alertAdminFailedDelivery(order, method, error) {
  const message = `
🚨 *GIAO HÀNG THẤT BẠI*

📋 Đơn hàng: \`${order.code}\`
👤 Khách hàng: ${order.customer.name}
📦 Sản phẩm: ${order.product.name}
🚫 Phương thức: ${method}
⚠️ Lỗi: ${error.message}

⚡ *Cần xử lý thủ công ngay!*
`;

  await sendTelegramMessage(message, process.env.ADMIN_CHAT_ID);
}
```

## Complete Workflow Code Structure

```javascript
// Main processing function
async function processPaymentWebhook(payload, headers) {
  try {
    // Step 1: Validate
    const validation = validateWebhookSignature(headers, payload);
    if (!validation.valid) {
      throw new Error(`Invalid webhook: ${validation.reason}`);
    }

    // Step 2: Extract order details
    const paymentInfo = extractOrderDetails(payload);
    const order = await getOrderByCode(paymentInfo.orderCode);

    // Step 3: Lookup product
    const product = await getProductDeliveryConfig(order.productId);

    // Step 4-5: Deliver via all applicable methods
    const deliveryResults = await deliverViaMultipleMethods(order, product);

    // Step 6: Log delivery
    for (const [method, result] of Object.entries(deliveryResults)) {
      await logDelivery(
        order.id,
        method,
        result.success ? result : null,
        result.success ? null : new Error(result.error)
      );
    }

    // Step 7: Send confirmation
    await sendDeliveryConfirmation(order, deliveryResults);

    // Step 8: Retry failed deliveries
    const failedMethods = Object.entries(deliveryResults)
      .filter(([_, result]) => !result.success)
      .map(([method, _]) => method);

    for (const method of failedMethods) {
      await retryFailedDelivery(order, product, method);
    }

    console.log(`✅ Order ${order.code} processed successfully`);

  } catch (error) {
    console.error('❌ Workflow error:', error);
    throw error;
  }
}
```

## Monitoring and Alerts

### Track Delivery Metrics
```javascript
// Daily delivery report
cron.schedule('0 23 * * *', async () => {
  const today = new Date();
  today.setHours(0, 0, 0, 0);

  const stats = await db.deliveryLogs.aggregate([
    { $match: { createdAt: { $gte: today } } },
    {
      $group: {
        _id: { method: '$method', status: '$status' },
        count: { $sum: 1 }
      }
    }
  ]);

  const report = formatDeliveryReport(stats);
  await sendTelegramMessage(report, process.env.ADMIN_CHAT_ID);
});
```

## Environment Variables

```bash
# .env
# App
APP_URL=https://yourdomain.com
STORE_NAME=Your Store
STORE_EMAIL=noreply@yourdomain.com

# Webhook
SEPAY_WEBHOOK_SECRET=your_secret

# Email
SMTP_HOST=smtp.sendgrid.net
SMTP_PORT=587
SMTP_USER=apikey
SMTP_PASS=your_sendgrid_api_key

# Telegram
TELEGRAM_BOT_TOKEN=123456789:ABC...
ADMIN_CHAT_ID=123456789

# Security
JWT_SECRET=your_jwt_secret_min_32_chars

# Support
SUPPORT_EMAIL=support@yourdomain.com
SUPPORT_PHONE=0912345678
```

## Testing Checklist

- [ ] Webhook signature validation
- [ ] Order lookup (existing vs not found)
- [ ] Email delivery (success + failure)
- [ ] Telegram delivery (user started bot + not started)
- [ ] Access link generation and verification
- [ ] Token expiration handling
- [ ] Retry logic (simulate failures)
- [ ] Admin alerts for failed deliveries
- [ ] Database logging
- [ ] Concurrent webhook handling
