# Digital Product Delivery Methods Comparison

Comprehensive comparison of delivery methods for digital products in Vietnamese market.

## Method Comparison Matrix

| Method | Setup Difficulty | Monthly Cost | Reliability | UX Score | Best For |
|--------|-----------------|--------------|-------------|----------|----------|
| Email with download link | Easy | Low ($0-20) | High (95%+) | 8/10 | Documents, files |
| Protected page redirect | Medium | Low ($0-10) | Very High (99%+) | 9/10 | Courses, membership |
| Telegram bot auto-send | Easy | Free | High (98%+) | 10/10 | Quick delivery, VN market |
| Google Drive shared link | Very Easy | Free-Low ($0-10) | Medium (85%) | 6/10 | Large files, temp access |
| Notion page access | Easy | Free-Medium ($0-16) | High (95%) | 7/10 | Courses, documentation |

## Method 1: Email with Download Link

### How It Works
1. Payment confirmed → Generate signed download token
2. Create expiring download URL (e.g., valid 7 days)
3. Send email with link via SendGrid/Nodemailer
4. Customer clicks → File downloads

### Step-by-Step Setup (Nodemailer)

#### Install Dependencies
```bash
npm install nodemailer jsonwebtoken
```

#### Configure Email Service
```javascript
const nodemailer = require('nodemailer');

// Gmail setup (free tier)
const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: process.env.EMAIL_USER,
    pass: process.env.EMAIL_APP_PASSWORD // Not regular password!
  }
});

// Or SMTP (SendGrid, Mailgun)
const transporter = nodemailer.createTransport({
  host: 'smtp.sendgrid.net',
  port: 587,
  auth: {
    user: 'apikey',
    pass: process.env.SENDGRID_API_KEY
  }
});
```

#### Generate Download Token
```javascript
const jwt = require('jsonwebtoken');

function generateDownloadLink(orderId, productId) {
  const token = jwt.sign(
    { orderId, productId },
    process.env.JWT_SECRET,
    { expiresIn: '7d' }
  );

  return `https://yourdomain.com/download/${token}`;
}
```

#### Send Email
```javascript
async function sendDownloadEmail(order) {
  const downloadLink = generateDownloadLink(order.id, order.productId);

  const mailOptions = {
    from: '"Your Store" <noreply@yourdomain.com>',
    to: order.customer.email,
    subject: `[${order.id}] Link tải sản phẩm - ${order.product.name}`,
    html: `
      <h2>Cảm ơn bạn đã mua hàng!</h2>
      <p>Xin chào ${order.customer.name},</p>
      <p>Đơn hàng <strong>${order.id}</strong> đã được thanh toán thành công.</p>

      <p><strong>Sản phẩm:</strong> ${order.product.name}</p>
      <p><strong>Số tiền:</strong> ${order.amount.toLocaleString('vi-VN')} VND</p>

      <p style="margin: 30px 0;">
        <a href="${downloadLink}"
           style="background: #4CAF50; color: white; padding: 15px 30px;
                  text-decoration: none; border-radius: 5px; font-weight: bold;">
          TẢI XUỐNG NGAY
        </a>
      </p>

      <p><em>Link có hiệu lực trong 7 ngày.</em></p>
      <p>Nếu gặp vấn đề, vui lòng liên hệ: support@yourdomain.com</p>
    `
  };

  await transporter.sendMail(mailOptions);
  console.log('✅ Email sent to:', order.customer.email);
}
```

#### Handle Download Endpoint
```javascript
const express = require('express');
const app = express();

app.get('/download/:token', async (req, res) => {
  try {
    // Verify token
    const decoded = jwt.verify(req.params.token, process.env.JWT_SECRET);

    // Get file info
    const order = await getOrder(decoded.orderId);
    const filePath = getProductFilePath(decoded.productId);

    // Log download
    await logDownload(decoded.orderId, req.ip);

    // Send file
    res.download(filePath, order.product.fileName);

  } catch (error) {
    if (error.name === 'TokenExpiredError') {
      res.status(410).send('Link đã hết hạn. Vui lòng liên hệ hỗ trợ.');
    } else {
      res.status(400).send('Link không hợp lệ.');
    }
  }
});
```

### Pros
- ✅ Familiar to users (everyone has email)
- ✅ Professional appearance
- ✅ Can include receipt, instructions
- ✅ Email serves as proof of purchase

### Cons
- ❌ Spam filters may block (use verified domain)
- ❌ Email delivery not instant (30s-5min)
- ❌ Users may not check email regularly
- ❌ Link expiration can frustrate customers

### Best For
- PDF guides, ebooks
- ZIP files (templates, resources)
- Software installers
- Professional/business audience

### Cost Breakdown
- **Free tier:** Gmail (100/day), SendGrid (100/day)
- **Paid:** SendGrid $15/mo (40k emails), Mailgun $35/mo (50k)

## Method 2: Redirect to Protected Page

### How It Works
1. Payment confirmed → Generate access token
2. Store token + user in database
3. Redirect customer to protected URL
4. Page validates token → Display content

### Step-by-Step Setup

#### Create Protected Route
```javascript
app.get('/access/:token', async (req, res) => {
  try {
    const decoded = jwt.verify(req.params.token, process.env.JWT_SECRET);
    const access = await getAccessRecord(decoded.accessId);

    if (!access || access.revoked) {
      return res.status(403).send('Access denied');
    }

    // Render content page
    res.render('product-page', {
      product: access.product,
      customer: access.customer,
      downloadLinks: access.downloadLinks,
      expiresAt: access.expiresAt
    });

  } catch (error) {
    res.status(401).send('Invalid or expired token');
  }
});
```

#### Generate Access on Payment
```javascript
async function createAccess(order) {
  // Create access record
  const access = await db.access.create({
    orderId: order.id,
    customerId: order.customerId,
    productId: order.productId,
    expiresAt: new Date(Date.now() + 365 * 24 * 60 * 60 * 1000) // 1 year
  });

  // Generate token
  const token = jwt.sign(
    { accessId: access.id },
    process.env.JWT_SECRET,
    { expiresIn: '1y' }
  );

  const accessUrl = `https://yourdomain.com/access/${token}`;

  // Send email with access URL
  await sendAccessEmail(order, accessUrl);

  return accessUrl;
}
```

#### Protected Page Template (EJS)
```html
<!DOCTYPE html>
<html>
<head>
  <title><%= product.name %> - Access Page</title>
</head>
<body>
  <h1>Welcome, <%= customer.name %>!</h1>
  <h2><%= product.name %></h2>

  <p>Your access expires: <%= expiresAt.toLocaleDateString('vi-VN') %></p>

  <div class="downloads">
    <% downloadLinks.forEach(link => { %>
      <a href="<%= link.url %>" class="download-btn">
        <%= link.label %>
      </a>
    <% }); %>
  </div>

  <div class="content">
    <%- product.content %>
  </div>
</body>
</html>
```

### Pros
- ✅ Highest reliability (no email dependency)
- ✅ Instant access after payment
- ✅ Can track page views, engagement
- ✅ Easy to update content (users always see latest)
- ✅ Can embed videos, interactive content

### Cons
- ❌ Requires web hosting and development
- ❌ Token must be securely stored (database needed)
- ❌ More complex setup than email

### Best For
- Online courses with video lessons
- Membership sites
- SaaS products
- Content that updates frequently

### Cost Breakdown
- **Hosting:** Vercel/Netlify (free), VPS $5-10/mo
- **Database:** MongoDB Atlas (free 512MB), PostgreSQL on Heroku (free)
- **Total:** $0-15/mo

## Method 3: Telegram Bot Auto-Send

### How It Works
1. Customer provides Telegram username during checkout
2. Payment confirmed → Bot sends file/link via Telegram
3. Customer receives instantly in Telegram app

### Step-by-Step Setup

#### Bot Setup (see telegram-bot-notification-setup.md)

#### Send File via Telegram
```javascript
const axios = require('axios');
const FormData = require('form-data');
const fs = require('fs');

async function sendFileToCustomer(order) {
  const botToken = process.env.TELEGRAM_BOT_TOKEN;

  // Get customer chat ID (requires customer to /start bot first)
  const chatId = await getCustomerChatId(order.customer.telegramUsername);

  if (!chatId) {
    // Fallback: send to owner, manual forward
    await sendTelegramMessage(
      `❌ Cannot send to @${order.customer.telegramUsername}. ` +
      `Customer must /start bot first. Order: ${order.id}`,
      process.env.ADMIN_CHAT_ID
    );
    return false;
  }

  // Send file
  const form = new FormData();
  form.append('chat_id', chatId);
  form.append('document', fs.createReadStream(order.product.filePath));
  form.append('caption', `
🎉 Cảm ơn bạn đã mua ${order.product.name}!

📋 Mã đơn: ${order.id}
💰 Số tiền: ${order.amount.toLocaleString('vi-VN')} VND

📥 File đính kèm là sản phẩm của bạn.
💬 Cần hỗ trợ? Nhắn tin ngay tại đây!
  `);

  await axios.post(
    `https://api.telegram.org/bot${botToken}/sendDocument`,
    form,
    { headers: form.getHeaders() }
  );

  console.log('✅ File sent to customer via Telegram');
  return true;
}
```

#### Send Link Instead of File
```javascript
async function sendLinkToCustomer(order) {
  const chatId = await getCustomerChatId(order.customer.telegramUsername);

  const message = `
🎉 *Cảm ơn bạn đã mua hàng!*

📦 Sản phẩm: ${order.product.name}
📋 Mã đơn: \`${order.id}\`
💰 Số tiền: \`${order.amount.toLocaleString('vi-VN')} VND\`

🔗 *Link truy cập:*
${order.accessLink}

⏰ Link có hiệu lực: ${order.expiresAt}

💬 Cần hỗ trợ? Nhắn tin ngay!
`;

  await sendTelegramMessage(message, chatId);
}
```

#### Collect Telegram Username at Checkout
```html
<form id="checkout-form">
  <input name="name" placeholder="Họ tên" required>
  <input name="phone" placeholder="Số điện thoại" required>
  <input name="email" placeholder="Email" type="email" required>

  <!-- Telegram field -->
  <input name="telegram" placeholder="Telegram username (không bắt buộc)"
         pattern="@?[a-zA-Z0-9_]+"
         title="Ví dụ: @username hoặc username">
  <small>Nhập để nhận sản phẩm ngay qua Telegram</small>

  <button type="submit">Thanh toán</button>
</form>
```

### Pros
- ✅ Instant delivery (fastest method)
- ✅ High engagement (Telegram popular in Vietnam)
- ✅ Two-way communication (support via chat)
- ✅ Can send files up to 2GB
- ✅ No spam filters
- ✅ Free (no cost)

### Cons
- ❌ Customer must have Telegram account
- ❌ Customer must /start bot before receiving
- ❌ Not professional for B2B audiences
- ❌ Limited formatting compared to web page

### Best For
- Vietnamese consumer market (Telegram very popular)
- Fast delivery needs
- Digital products < 2GB
- Community-based products (groups, channels)
- Businesses wanting direct customer communication

### Cost Breakdown
- **Free** (Telegram Bot API is 100% free)

## Method 4: Google Drive Shared Link

### How It Works
1. Upload product files to Google Drive
2. Payment confirmed → Share file with customer email
3. Customer receives email from Google Drive

### Step-by-Step Setup

#### Google Drive API Setup
```bash
npm install googleapis
```

#### Authenticate
```javascript
const { google } = require('googleapis');

const auth = new google.auth.GoogleAuth({
  keyFile: 'service-account-key.json',
  scopes: ['https://www.googleapis.com/auth/drive']
});

const drive = google.drive({ version: 'v3', auth });
```

#### Share File with Customer
```javascript
async function shareFileWithCustomer(order) {
  const fileId = order.product.googleDriveFileId;

  try {
    // Add permission
    await drive.permissions.create({
      fileId: fileId,
      requestBody: {
        role: 'reader',
        type: 'user',
        emailAddress: order.customer.email
      },
      sendNotificationEmail: true,
      emailMessage: `
        Chào ${order.customer.name},

        Bạn đã được cấp quyền truy cập vào file: ${order.product.name}
        Mã đơn: ${order.id}

        File sẽ tự động hiện trong Google Drive của bạn.
      `
    });

    // Get shareable link
    const file = await drive.files.get({
      fileId: fileId,
      fields: 'webViewLink'
    });

    console.log('✅ File shared:', file.data.webViewLink);
    return file.data.webViewLink;

  } catch (error) {
    console.error('❌ Failed to share file:', error.message);
    throw error;
  }
}
```

#### Revoke Access After Period
```javascript
async function revokeAccess(order, permissionId) {
  const fileId = order.product.googleDriveFileId;

  await drive.permissions.delete({
    fileId: fileId,
    permissionId: permissionId
  });

  console.log('✅ Access revoked for order:', order.id);
}
```

### Pros
- ✅ Easy setup (no file hosting needed)
- ✅ Large files supported (up to 5TB per file)
- ✅ Familiar interface (most users know Google Drive)
- ✅ Automatic backup and versioning

### Cons
- ❌ Requires Google account (customer email must be Gmail)
- ❌ Files visible in customer's Drive (can't truly revoke)
- ❌ API quota limits (10,000 requests/day free)
- ❌ Less control over branding

### Best For
- Large files (videos, design assets)
- Temporary access needs
- B2B customers (likely have Google Workspace)
- File collaboration needs

### Cost Breakdown
- **Free tier:** 15GB storage, 10k API requests/day
- **Paid:** Google Workspace $6/user/mo (30GB)

## Method 5: Notion Page Access

### How It Works
1. Create Notion page with product content
2. Payment confirmed → Invite customer email to page
3. Customer receives Notion invitation

### Step-by-Step Setup

#### Notion API Setup
```bash
npm install @notionhq/client
```

#### Create Integration
1. Go to notion.so/my-integrations
2. Create new integration
3. Copy integration token
4. Share target pages with integration

#### Share Page with Customer
```javascript
const { Client } = require('@notionhq/client');

const notion = new Client({ auth: process.env.NOTION_API_KEY });

async function shareNotionPage(order) {
  const pageId = order.product.notionPageId;

  // Notion API doesn't directly support sharing with email
  // Workaround: Create a shareable link or use Notion's share UI

  // Get page details
  const page = await notion.pages.retrieve({ page_id: pageId });

  // Generate public link (requires manual sharing settings)
  const shareLink = `https://notion.so/${pageId.replace(/-/g, '')}`;

  // Send email with link
  await sendNotionAccessEmail(order, shareLink);

  return shareLink;
}
```

#### Alternative: Embed Notion Content
```javascript
// Create private Notion page, extract content via API
async function getNotionContent(pageId) {
  const blocks = await notion.blocks.children.list({
    block_id: pageId
  });

  // Convert blocks to HTML (simplified)
  const html = blocks.results.map(block => {
    if (block.type === 'paragraph') {
      return `<p>${block.paragraph.rich_text[0]?.plain_text || ''}</p>`;
    }
    // Handle other block types...
  }).join('\n');

  return html;
}

// Serve on your own protected page
app.get('/course/:token', async (req, res) => {
  const content = await getNotionContent(order.product.notionPageId);
  res.render('course-page', { content });
});
```

### Pros
- ✅ Beautiful, structured content
- ✅ Easy to update (edit Notion page → customers see changes)
- ✅ Rich media support (videos, embeds, databases)
- ✅ Good for courses and documentation

### Cons
- ❌ Requires Notion account (customer friction)
- ❌ API limited (no direct email invitation)
- ❌ Not fully private (shared links can leak)
- ❌ Branding limited

### Best For
- Online courses (structured lessons)
- Documentation and guides
- Resource libraries
- Businesses already using Notion

### Cost Breakdown
- **Free tier:** Personal plan (unlimited blocks)
- **Paid:** Plus $8/user/mo (advanced permissions)

## Hybrid Approach Recommendation

### Optimal Setup for Vietnamese Market
```
Primary: Telegram Bot (instant, high engagement)
   ↓
Fallback: Email with Link (if no Telegram)
   ↓
Backup: Protected Web Page (permanent access)
```

### Implementation
```javascript
async function deliverProduct(order) {
  let deliveryMethod = null;

  // Try Telegram first
  if (order.customer.telegram) {
    try {
      await sendFileToCustomer(order);
      deliveryMethod = 'telegram';
      console.log('✅ Delivered via Telegram');
    } catch (error) {
      console.warn('⚠️ Telegram failed, trying email...');
    }
  }

  // Fallback to email
  if (!deliveryMethod) {
    try {
      await sendDownloadEmail(order);
      deliveryMethod = 'email';
      console.log('✅ Delivered via Email');
    } catch (error) {
      console.error('❌ Email failed');
    }
  }

  // Always create protected page access (backup)
  const accessLink = await createAccess(order);

  // Update order record
  await updateOrder(order.id, {
    deliveryMethod,
    accessLink,
    deliveredAt: new Date()
  });

  return { deliveryMethod, accessLink };
}
```

## Decision Matrix

Choose method based on:

| If your product is... | Use... |
|----------------------|--------|
| PDF/Document < 50MB | Email or Telegram |
| Video course | Protected page or Notion |
| Large files > 100MB | Google Drive or Telegram |
| Requires updates | Protected page or Notion |
| Vietnamese consumer market | Telegram (primary) |
| B2B/Professional | Email + Protected page |
| Need analytics | Protected page |
| Limited budget | Telegram (free) |

## Next Steps
1. Choose primary method based on your audience
2. Implement delivery automation (see `automated-delivery-workflow.md`)
3. Set up post-purchase engagement (see `post-purchase-engagement-sequence.md`)
4. Monitor delivery success rate and customer feedback
