# Webhook-to-Notification Pipeline Architecture

End-to-end pipeline from payment webhook to Telegram notification.

## Architecture Diagram

```
SePay Payment
    |
    | HTTP POST (webhook)
    v
Express.js Webhook Receiver
    |
    | 1. Validate HMAC signature
    | 2. Parse payload
    v
Payment Validator
    |
    | 3. Check amount, status
    | 4. Dedup check
    v
Message Template Engine
    |
    | 5. Select template
    | 6. Render variables
    v
Telegram Bot API Client
    |
    | 7. Send message
    | 8. Retry on failure
    v
Telegram Group/Chat
    |
    v
Logging & Monitoring
```

## SePay Webhook Payload Structure

### Success Payment Webhook
```json
{
  "id": "87654321",
  "gateway": "VietQR",
  "transactionDate": "2026-02-13 15:30:45",
  "accountNumber": "0123456789",
  "code": null,
  "content": "ORDER12345",
  "transferType": "in",
  "transferAmount": 1500000,
  "accumulated": 25000000,
  "subAccId": "12345",
  "referenceCode": "FT26044123456789",
  "description": "MB NGUYEN VAN A chuyen tien ORDER12345",
  "bankBrandName": "MB Bank",
  "bankName": "Ngan hang Quan doi",
  "bankAbbreviation": "MB"
}
```

### Key Fields
- `transferAmount`: Payment amount (VND)
- `content`: Order reference (extract order ID)
- `transactionDate`: Payment timestamp
- `bankBrandName`: Bank used by customer
- `referenceCode`: Unique transaction ID
- `description`: Full transfer description

## Express.js Webhook Receiver Endpoint

```javascript
const express = require('express');
const bodyParser = require('body-parser');
const crypto = require('crypto');
const axios = require('axios');

const app = express();
app.use(bodyParser.json());

// Webhook endpoint
app.post('/webhook/sepay', async (req, res) => {
  console.log('📥 Webhook received:', new Date().toISOString());

  try {
    // Step 1: Validate signature
    const isValid = validateHMAC(req.headers, req.body);
    if (!isValid) {
      console.error('❌ Invalid HMAC signature');
      return res.status(401).json({ error: 'Invalid signature' });
    }

    // Step 2: Parse payload
    const paymentData = parsePayload(req.body);

    // Step 3: Validate payment
    const validation = validatePayment(paymentData);
    if (!validation.valid) {
      console.warn('⚠️ Invalid payment:', validation.reason);
      return res.status(400).json({ error: validation.reason });
    }

    // Step 4: Check for duplicates
    const isDuplicate = await checkDuplicate(paymentData.referenceCode);
    if (isDuplicate) {
      console.log('ℹ️ Duplicate webhook ignored');
      return res.status(200).json({ status: 'duplicate' });
    }

    // Respond immediately (don't make SePay wait)
    res.status(200).json({ status: 'received' });

    // Step 5-8: Process asynchronously
    processPaymentNotification(paymentData).catch(error => {
      console.error('❌ Processing error:', error);
    });

  } catch (error) {
    console.error('❌ Webhook error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.listen(3000, () => {
  console.log('✅ Webhook server running on port 3000');
});
```

## HMAC Signature Verification

```javascript
function validateHMAC(headers, payload) {
  const receivedSignature = headers['x-sepay-signature'];
  const webhookSecret = process.env.SEPAY_WEBHOOK_SECRET;

  if (!receivedSignature || !webhookSecret) {
    return false;
  }

  // Create HMAC
  const hmac = crypto.createHmac('sha256', webhookSecret);
  hmac.update(JSON.stringify(payload));
  const expectedSignature = hmac.digest('hex');

  // Compare signatures (timing-safe)
  return crypto.timingSafeEqual(
    Buffer.from(receivedSignature),
    Buffer.from(expectedSignature)
  );
}
```

### Why HMAC Validation is Critical
1. **Prevents fake webhooks** from unauthorized sources
2. **Ensures payload integrity** (not tampered)
3. **Security requirement** for production systems
4. **Protects against replay attacks** (when combined with dedup)

## Payload Parsing and Validation

```javascript
function parsePayload(body) {
  return {
    transactionId: body.id,
    referenceCode: body.referenceCode,
    amount: parseInt(body.transferAmount),
    content: body.content || '',
    timestamp: body.transactionDate,
    bankName: body.bankBrandName,
    customerInfo: extractCustomerInfo(body.description),
    orderCode: extractOrderCode(body.content)
  };
}

function extractOrderCode(content) {
  // Extract order code from content field
  // Examples: "ORDER12345", "DH12345", "12345"
  const match = content.match(/ORDER(\d+)|DH(\d+)|^(\d+)$/);
  return match ? (match[1] || match[2] || match[3]) : null;
}

function extractCustomerInfo(description) {
  // Extract customer name from bank description
  // Example: "MB NGUYEN VAN A chuyen tien ORDER12345"
  const match = description.match(/[A-Z]{2}\s([A-Z\s]+)\schuyen/i);
  return match ? match[1].trim() : 'Unknown';
}

function validatePayment(data) {
  // Amount check
  if (data.amount < 1000) {
    return { valid: false, reason: 'Amount too low' };
  }

  // Order code required
  if (!data.orderCode) {
    return { valid: false, reason: 'Missing order code' };
  }

  // Timestamp check (not older than 1 hour)
  const paymentTime = new Date(data.timestamp);
  const now = new Date();
  const hoursDiff = (now - paymentTime) / (1000 * 60 * 60);

  if (hoursDiff > 1) {
    return { valid: false, reason: 'Payment too old' };
  }

  return { valid: true };
}
```

## Deduplication Check

```javascript
// In-memory cache (use Redis for production)
const processedTransactions = new Set();

async function checkDuplicate(referenceCode) {
  if (processedTransactions.has(referenceCode)) {
    return true;
  }

  processedTransactions.add(referenceCode);

  // Clean up old entries (keep last 1000)
  if (processedTransactions.size > 1000) {
    const firstKey = processedTransactions.values().next().value;
    processedTransactions.delete(firstKey);
  }

  return false;
}

// Redis-based dedup (production)
async function checkDuplicateRedis(referenceCode) {
  const redis = require('redis').createClient();
  const key = `tx:${referenceCode}`;

  const exists = await redis.exists(key);
  if (exists) {
    return true;
  }

  await redis.set(key, '1', 'EX', 3600); // Expire after 1 hour
  return false;
}
```

## Message Template Rendering

```javascript
function renderTemplate(templateName, variables) {
  const templates = {
    newOrder: `
🛒 *ĐƠN HÀNG MỚI*

📋 Mã đơn: \`{{orderCode}}\`
👤 Khách hàng: {{customerName}}
💰 Số tiền: \`{{amount}} VND\`
💳 Ngân hàng: {{bankName}}
🔖 Mã GD: {{referenceCode}}
⏰ Thời gian: {{timestamp}}

✅ Trạng thái: *Đã thanh toán*
`,

    paymentConfirmed: `
✅ *THANH TOÁN THÀNH CÔNG*

📦 Đơn hàng: \`{{orderCode}}\`
💵 Số tiền: \`{{amount}} VND\`
🔖 Mã GD: {{referenceCode}}
⏰ {{timestamp}}

📧 Khách hàng sẽ nhận email xác nhận trong vài phút.
`,

    highValueAlert: `
🚨 *GIAO DỊCH GIÁ TRỊ CAO*

💰 Số tiền: \`{{amount}} VND\`
📋 Mã đơn: \`{{orderCode}}\`
👤 Khách hàng: {{customerName}}
💳 Ngân hàng: {{bankName}}

⚠️ Vui lòng kiểm tra và xử lý ưu tiên!
`
  };

  let message = templates[templateName] || templates.newOrder;

  // Replace variables
  for (const [key, value] of Object.entries(variables)) {
    const placeholder = `{{${key}}}`;
    message = message.replace(new RegExp(placeholder, 'g'), value);
  }

  return message;
}

// Usage
const message = renderTemplate('newOrder', {
  orderCode: 'ORDER12345',
  customerName: 'Nguyen Van A',
  amount: '1,500,000',
  bankName: 'MB Bank',
  referenceCode: 'FT26044123456789',
  timestamp: new Date().toLocaleString('vi-VN')
});
```

## Telegram Bot API Call

```javascript
async function sendTelegramNotification(message, chatId = null) {
  const botToken = process.env.TELEGRAM_BOT_TOKEN;
  const targetChatId = chatId || process.env.TELEGRAM_CHAT_ID;
  const url = `https://api.telegram.org/bot${botToken}/sendMessage`;

  try {
    const response = await axios.post(url, {
      chat_id: targetChatId,
      text: message,
      parse_mode: 'Markdown',
      disable_web_page_preview: true
    }, {
      timeout: 5000 // 5 second timeout
    });

    console.log('✅ Telegram notification sent');
    return { success: true, messageId: response.data.result.message_id };

  } catch (error) {
    console.error('❌ Telegram API error:', error.response?.data || error.message);
    throw error;
  }
}
```

## Queue Management with Retry

```javascript
const Queue = require('better-queue');

// Create notification queue
const notificationQueue = new Queue(async (task, cb) => {
  try {
    await sendTelegramNotification(task.message, task.chatId);
    cb(null, { success: true });
  } catch (error) {
    cb(error);
  }
}, {
  retries: 3,
  retryDelay: 2000, // 2 seconds
  maxTimeout: 30000, // 30 seconds
  afterProcessDelay: 100 // 100ms between messages
});

// Queue error handling
notificationQueue.on('task_failed', (taskId, error) => {
  console.error(`❌ Task ${taskId} failed after retries:`, error.message);
  logFailedNotification(taskId, error);
});

// Usage
function queueNotification(message, chatId = null) {
  notificationQueue.push({ message, chatId });
}
```

## Logging Format

```javascript
const winston = require('winston');

const logger = winston.createLogger({
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.json()
  ),
  transports: [
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'webhook.log' })
  ]
});

function logWebhook(event, data) {
  logger.info({
    event: event,
    timestamp: new Date().toISOString(),
    orderCode: data.orderCode,
    amount: data.amount,
    referenceCode: data.referenceCode,
    success: data.success
  });
}

// Usage
logWebhook('webhook_received', paymentData);
logWebhook('notification_sent', { orderCode: '12345', success: true });
logWebhook('notification_failed', { orderCode: '12345', success: false, error: 'timeout' });
```

## Health Check Endpoint

```javascript
app.get('/health', async (req, res) => {
  const health = {
    status: 'ok',
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
    checks: {}
  };

  // Check Telegram Bot API
  try {
    const botToken = process.env.TELEGRAM_BOT_TOKEN;
    await axios.get(`https://api.telegram.org/bot${botToken}/getMe`);
    health.checks.telegram = 'ok';
  } catch (error) {
    health.checks.telegram = 'error';
    health.status = 'degraded';
  }

  // Check environment variables
  const requiredVars = ['TELEGRAM_BOT_TOKEN', 'TELEGRAM_CHAT_ID', 'SEPAY_WEBHOOK_SECRET'];
  const missingVars = requiredVars.filter(v => !process.env[v]);

  if (missingVars.length > 0) {
    health.checks.env = { status: 'error', missing: missingVars };
    health.status = 'error';
  } else {
    health.checks.env = 'ok';
  }

  const statusCode = health.status === 'ok' ? 200 : 503;
  res.status(statusCode).json(health);
});
```

## Complete Pipeline Code

```javascript
require('dotenv').config();
const express = require('express');
const bodyParser = require('body-parser');
const crypto = require('crypto');
const axios = require('axios');

const app = express();
app.use(bodyParser.json());

// Main processing function
async function processPaymentNotification(paymentData) {
  try {
    // Format variables
    const variables = {
      orderCode: paymentData.orderCode,
      customerName: paymentData.customerInfo,
      amount: paymentData.amount.toLocaleString('vi-VN'),
      bankName: paymentData.bankName,
      referenceCode: paymentData.referenceCode,
      timestamp: new Date(paymentData.timestamp).toLocaleString('vi-VN')
    };

    // Select template based on amount
    const templateName = paymentData.amount > 10000000
      ? 'highValueAlert'
      : 'newOrder';

    // Render message
    const message = renderTemplate(templateName, variables);

    // Send notification
    await sendTelegramNotification(message);

    // Log success
    logWebhook('notification_sent', {
      orderCode: paymentData.orderCode,
      success: true
    });

    // Store in database (optional)
    await saveOrder(paymentData);

  } catch (error) {
    console.error('Processing error:', error);
    logWebhook('notification_failed', {
      orderCode: paymentData.orderCode,
      success: false,
      error: error.message
    });
    throw error;
  }
}

// Webhook endpoint
app.post('/webhook/sepay', async (req, res) => {
  try {
    if (!validateHMAC(req.headers, req.body)) {
      return res.status(401).json({ error: 'Invalid signature' });
    }

    const paymentData = parsePayload(req.body);
    const validation = validatePayment(paymentData);

    if (!validation.valid) {
      return res.status(400).json({ error: validation.reason });
    }

    if (await checkDuplicate(paymentData.referenceCode)) {
      return res.status(200).json({ status: 'duplicate' });
    }

    res.status(200).json({ status: 'received' });

    // Process async
    processPaymentNotification(paymentData);

  } catch (error) {
    console.error('Webhook error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Health check
app.get('/health', async (req, res) => {
  // ... (see Health Check section)
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`✅ Server running on port ${PORT}`);
});
```

## Environment Variables Setup

```bash
# .env
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
TELEGRAM_CHAT_ID=123456789
SEPAY_WEBHOOK_SECRET=your_webhook_secret_from_sepay
PORT=3000
NODE_ENV=production
```

## Deployment Checklist

- [ ] Environment variables configured
- [ ] HMAC signature validation enabled
- [ ] Duplicate detection implemented
- [ ] Error logging configured
- [ ] Health check endpoint working
- [ ] Retry logic tested
- [ ] Rate limiting configured
- [ ] HTTPS enabled (required for webhooks)
- [ ] Firewall rules set (allow SePay IPs)
- [ ] Monitoring alerts configured

## Monitoring Recommendations

1. **Track notification success rate** (target: >99%)
2. **Monitor webhook latency** (target: <500ms response)
3. **Alert on failed notifications** (email/SMS to admin)
4. **Log all webhook payloads** for debugging
5. **Set up uptime monitoring** (UptimeRobot, Pingdom)
