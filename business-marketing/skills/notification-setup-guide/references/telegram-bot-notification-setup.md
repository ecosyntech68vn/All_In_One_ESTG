# Telegram Bot Notification Setup Guide

Complete guide to setting up automated notifications via Telegram Bot API.

## Step 1: Create Bot via @BotFather

### Process
1. Open Telegram and search for `@BotFather`
2. Send `/start` to begin
3. Send `/newbot` to create new bot
4. Provide bot name (display name): `My Store Notifications`
5. Provide bot username (must end in `bot`): `mystorenotify_bot`
6. Save the bot token (looks like `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

### BotFather Commands
- `/newbot` - Create new bot
- `/mybots` - Manage existing bots
- `/setdescription` - Set bot description
- `/setabouttext` - Set about text
- `/setuserpic` - Set bot profile picture
- `/setcommands` - Set bot commands menu
- `/deletebot` - Delete bot

### Recommended Bot Settings
```
Name: [Your Store] Notifications
Username: [yourstore]_notify_bot
Description: Automated order and payment notifications
About: This bot sends you real-time updates about orders and payments.
Commands:
  start - Activate notifications
  status - Check bot status
  help - Get help information
```

## Step 2: Get Bot Token

### Token Format
```
1234567890:ABCdefGHIjklMNOpqrsTUVwxyz-1234567
```

### Security Best Practices
1. **Never commit to Git** (use .env file)
2. **Store in environment variables**
3. **Use different bots** for dev/staging/production
4. **Regenerate token** if compromised (via @BotFather `/revoke`)
5. **Limit bot permissions** to minimum needed

### Environment Variable Setup
```bash
# .env file
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz-1234567
```

```javascript
// Load in Node.js
require('dotenv').config();
const BOT_TOKEN = process.env.TELEGRAM_BOT_TOKEN;
```

## Step 3: Get Chat ID

### Personal Chat ID
1. Start conversation with your bot (send `/start`)
2. Send a message to your bot
3. Visit: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
4. Find `"chat":{"id":123456789}` in JSON response
5. Save this chat ID

### Group Chat ID
1. Add bot to group
2. Send a message in the group
3. Visit same URL: `/getUpdates`
4. Find `"chat":{"id":-1001234567890}` (negative number)
5. Note: Group IDs start with `-100`

### Automated Chat ID Discovery
```javascript
const axios = require('axios');

async function getChatId(botToken) {
  const url = `https://api.telegram.org/bot${botToken}/getUpdates`;
  const response = await axios.get(url);

  if (response.data.result.length > 0) {
    const chatId = response.data.result[0].message.chat.id;
    console.log(`Chat ID: ${chatId}`);
    return chatId;
  } else {
    console.log('No messages found. Send a message to your bot first.');
    return null;
  }
}

// Usage
getChatId(process.env.TELEGRAM_BOT_TOKEN);
```

## Step 4: Set Up Webhook Endpoint

### Express.js Webhook Receiver
```javascript
const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

// Webhook endpoint for payment notifications
app.post('/webhook/sepay', async (req, res) => {
  try {
    const payload = req.body;

    // Validate webhook signature (security)
    const isValid = validateSignature(req.headers, payload);
    if (!isValid) {
      return res.status(401).json({ error: 'Invalid signature' });
    }

    // Process payment notification
    await handlePaymentNotification(payload);

    // Respond immediately (don't make SePay wait)
    res.status(200).json({ success: true });

  } catch (error) {
    console.error('Webhook error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.listen(3000, () => {
  console.log('Webhook server running on port 3000');
});
```

### Signature Validation Function
```javascript
const crypto = require('crypto');

function validateSignature(headers, payload) {
  const signature = headers['x-sepay-signature'];
  const secret = process.env.SEPAY_WEBHOOK_SECRET;

  const hmac = crypto.createHmac('sha256', secret);
  hmac.update(JSON.stringify(payload));
  const expectedSignature = hmac.digest('hex');

  return signature === expectedSignature;
}
```

## Step 5: Send First Test Message

### Simple Message
```javascript
const axios = require('axios');

async function sendTelegramMessage(message) {
  const botToken = process.env.TELEGRAM_BOT_TOKEN;
  const chatId = process.env.TELEGRAM_CHAT_ID;
  const url = `https://api.telegram.org/bot${botToken}/sendMessage`;

  try {
    const response = await axios.post(url, {
      chat_id: chatId,
      text: message,
      parse_mode: 'Markdown'
    });

    console.log('Message sent successfully');
    return response.data;
  } catch (error) {
    console.error('Failed to send message:', error.response?.data || error.message);
    throw error;
  }
}

// Test
sendTelegramMessage('🎉 Bot setup successful! Notifications are now active.');
```

### Test Script
```javascript
// test-telegram.js
require('dotenv').config();

const testMessage = `
*✅ Test Notification*

This is a test message from your notification bot.

*Bot Token:* ${process.env.TELEGRAM_BOT_TOKEN.slice(0, 10)}...
*Chat ID:* ${process.env.TELEGRAM_CHAT_ID}
*Time:* ${new Date().toLocaleString('vi-VN')}

If you see this, your bot is configured correctly!
`;

sendTelegramMessage(testMessage);
```

Run: `node test-telegram.js`

## Message Formatting

### Markdown Mode
```javascript
const message = `
*Bold text*
_Italic text_
\`Monospace\`
[Link text](https://example.com)

*Order #12345*
Amount: \`1,500,000 VND\`
Status: _Confirmed_
`;

await axios.post(url, {
  chat_id: chatId,
  text: message,
  parse_mode: 'Markdown'
});
```

### HTML Mode
```javascript
const message = `
<b>Bold text</b>
<i>Italic text</i>
<code>Monospace</code>
<a href="https://example.com">Link text</a>

<b>Order #12345</b>
Amount: <code>1,500,000 VND</code>
Status: <i>Confirmed</i>
`;

await axios.post(url, {
  chat_id: chatId,
  text: message,
  parse_mode: 'HTML'
});
```

### Emoji Usage
```javascript
const message = `
💰 *New Payment Received*
📦 Order: #12345
💳 Amount: 1,500,000 VND
✅ Status: Confirmed
⏰ Time: ${new Date().toLocaleString('vi-VN')}
`;
```

## Group Chat Integration Setup

### Add Bot to Group
1. Create Telegram group
2. Add your bot to group (search by username)
3. Send a message in group
4. Get group chat ID (negative number starting with -100)
5. Make bot admin for guaranteed message delivery

### Bot Admin Permissions Needed
- Send messages
- Delete messages (optional, for cleanup)
- Pin messages (optional, for important alerts)

### Multiple Chat Support
```javascript
// .env
TELEGRAM_CHAT_ID_OWNER=123456789
TELEGRAM_CHAT_ID_TEAM=-1001234567890
TELEGRAM_CHAT_ID_ALERTS=-1009876543210

// Send to multiple chats
async function broadcastMessage(message, chatIds) {
  const promises = chatIds.map(chatId =>
    sendTelegramMessage(message, chatId)
  );
  await Promise.all(promises);
}

// Usage
const chats = [
  process.env.TELEGRAM_CHAT_ID_OWNER,
  process.env.TELEGRAM_CHAT_ID_TEAM
];
await broadcastMessage('New order received!', chats);
```

## Error Handling and Retry Logic

### Retry with Exponential Backoff
```javascript
async function sendWithRetry(message, maxRetries = 3) {
  let attempt = 0;

  while (attempt < maxRetries) {
    try {
      await sendTelegramMessage(message);
      return { success: true };
    } catch (error) {
      attempt++;

      if (attempt >= maxRetries) {
        console.error(`Failed after ${maxRetries} attempts:`, error.message);
        return { success: false, error: error.message };
      }

      // Wait before retry (exponential backoff)
      const delay = Math.pow(2, attempt) * 1000; // 2s, 4s, 8s
      console.log(`Retry attempt ${attempt} in ${delay}ms...`);
      await new Promise(resolve => setTimeout(resolve, delay));
    }
  }
}
```

### Rate Limit Handling
```javascript
// Telegram limit: 30 messages per second to same chat
const messageQueue = [];
let isProcessing = false;

async function queueMessage(message) {
  messageQueue.push(message);

  if (!isProcessing) {
    processQueue();
  }
}

async function processQueue() {
  isProcessing = true;

  while (messageQueue.length > 0) {
    const message = messageQueue.shift();
    await sendTelegramMessage(message);
    await new Promise(resolve => setTimeout(resolve, 100)); // 10 msg/sec safety
  }

  isProcessing = false;
}
```

## Security: Validate Webhook Source

### IP Whitelist (if webhook from known IPs)
```javascript
const ALLOWED_IPS = ['123.45.67.89', '98.76.54.32']; // SePay IPs

app.use('/webhook/sepay', (req, res, next) => {
  const clientIP = req.ip || req.connection.remoteAddress;

  if (!ALLOWED_IPS.includes(clientIP)) {
    return res.status(403).json({ error: 'Forbidden' });
  }

  next();
});
```

### Secret Token Validation
```javascript
app.post('/webhook/sepay', (req, res, next) => {
  const token = req.headers['x-webhook-token'];

  if (token !== process.env.WEBHOOK_SECRET_TOKEN) {
    return res.status(401).json({ error: 'Unauthorized' });
  }

  next();
});
```

## Complete Notification Function

```javascript
const axios = require('axios');

async function sendOrderNotification(orderData) {
  const message = `
🛒 *ĐƠN HÀNG MỚI*

📋 Mã đơn: \`${orderData.orderId}\`
👤 Khách hàng: ${orderData.customerName}
📞 SĐT: ${orderData.customerPhone}
📦 Sản phẩm: ${orderData.productName}
💰 Số tiền: \`${orderData.amount.toLocaleString('vi-VN')} VND\`
💳 Thanh toán: ${orderData.paymentMethod}
⏰ Thời gian: ${new Date().toLocaleString('vi-VN')}

✅ Trạng thái: ${orderData.status}
`;

  const botToken = process.env.TELEGRAM_BOT_TOKEN;
  const chatId = process.env.TELEGRAM_CHAT_ID;

  try {
    await axios.post(
      `https://api.telegram.org/bot${botToken}/sendMessage`,
      {
        chat_id: chatId,
        text: message,
        parse_mode: 'Markdown'
      }
    );

    console.log(`✅ Notification sent for order ${orderData.orderId}`);
    return true;
  } catch (error) {
    console.error('❌ Failed to send notification:', error.response?.data || error.message);

    // Fallback: log to file
    logToFile('failed-notifications.log', { orderData, error: error.message });
    return false;
  }
}

// Usage in webhook handler
app.post('/webhook/sepay', async (req, res) => {
  const orderData = {
    orderId: req.body.orderCode,
    customerName: req.body.customerName,
    customerPhone: req.body.customerPhone,
    productName: req.body.productName,
    amount: req.body.amount,
    paymentMethod: 'VietQR',
    status: 'Đã thanh toán'
  };

  await sendOrderNotification(orderData);
  res.status(200).json({ success: true });
});
```

## Troubleshooting

### Bot not receiving messages
- Check bot token is correct
- Ensure chat ID is correct (positive for personal, negative for groups)
- Verify bot is not blocked by user
- Check network connectivity

### 401 Unauthorized error
- Bot token is invalid or expired
- Regenerate token via @BotFather

### 400 Bad Request error
- Message format error (check Markdown/HTML syntax)
- Chat ID format wrong
- Message too long (max 4096 characters)

### 403 Forbidden error
- Bot blocked by user
- Bot removed from group
- Bot not admin in group (for certain actions)

### Messages not appearing in group
- Bot must be admin in group
- Check group privacy settings
- Verify correct group chat ID

## Next Steps

1. Integrate with payment webhook (see `webhook-to-notification-pipeline.md`)
2. Set up message templates (see `notification-message-templates.md`)
3. Add monitoring and logging
4. Create health check endpoint
5. Set up alerts for failed notifications
