# Delivery Automation Workflow

Step-by-step: Set up payment → Configure notifications → Automate delivery

## Overview
| Field | Value |
|-------|-------|
| Agent | Deliver Agent |
| Skills Used | Payment Setup Guide, Notification Setup Guide, Delivery Setup Guide |
| Duration | 1-2 days |
| Output | Working payment → notification → delivery pipeline |

## Prerequisites
- Sales page ready (from Conversion workflow)
- Digital product ready to deliver (ebook, video course, template, etc.)
- Bank account for SePay (Vietnamese bank account required)
- Telegram account (for notifications)

## Workflow Steps

### Step 1: SePay Payment Setup (2-3 hours)
- Use Payment Setup Guide skill
- Register SePay account, verify bank
- Generate API token
- Create VietQR payment link for product
- Test with small amount
- Output: Working payment link

#### Actions:
1. Sign up for SePay account:
   - Visit sepay.vn
   - Register with Vietnamese phone number
   - Verify phone via OTP
2. Link bank account:
   - Add Vietnamese bank account (Vietcombank, Techcombank, etc.)
   - Complete bank verification (small deposit verification)
3. Get API credentials:
   - Go to Settings → API Integration
   - Generate API token
   - Save token securely (use .env file, never commit to git)
4. Create payment link for product:
   - Product name: [Your offer name]
   - Amount: [Price in VND]
   - Description: Brief description
   - Generate VietQR code link
5. Test payment:
   - Make small test transaction (10,000 VND)
   - Verify payment received in SePay dashboard
   - Check webhook callback (if set up)
6. Document payment link and QR code
7. Add payment link/button to sales page

#### Deliverable:
- SePay account fully set up and verified
- API token saved securely
- Payment link for product (URL)
- VietQR code image
- Test transaction confirmed

#### Security Notes:
- Store API token in .env file (never hardcode)
- Use HMAC signature verification for webhooks (prevent fraud)
- Enable 2FA on SePay account
- Monitor suspicious transactions

---

### Step 2: Telegram Bot Setup (1-2 hours)
- Use Notification Setup Guide skill
- Create bot via @BotFather
- Get bot token + chat ID
- Test sending message via API
- Output: Working Telegram bot

#### Actions:
1. Create Telegram bot:
   - Open Telegram, search for @BotFather
   - Send command: /newbot
   - Follow prompts: bot name, username
   - Save bot token provided by BotFather
2. Get your chat ID:
   - Start conversation with your bot (send any message)
   - Visit: https://api.telegram.org/bot[BOT_TOKEN]/getUpdates
   - Find "chat":{"id":[YOUR_CHAT_ID]} in response
   - Save chat ID
3. Test sending message:
   - Use curl or Postman to test API:
     ```
     curl -X POST https://api.telegram.org/bot[BOT_TOKEN]/sendMessage \
     -d chat_id=[CHAT_ID] \
     -d text="Test notification"
     ```
   - Verify message received in Telegram
4. Save bot token and chat ID securely (.env file)

#### Deliverable:
- Telegram bot created and active
- Bot token saved securely
- Chat ID documented
- Test message sent and received successfully

---

### Step 3: Webhook Pipeline (2-4 hours)
- Use Notification Setup Guide skill: webhook pipeline
- Set up Express.js endpoint to receive SePay webhooks
- Parse payment confirmation → format message → send to Telegram
- Add HMAC signature verification
- Output: Payment → Telegram notification working

#### Actions:
1. Set up webhook endpoint (Node.js/Express example):
   ```javascript
   const express = require('express');
   const axios = require('axios');
   const crypto = require('crypto');

   const app = express();
   app.use(express.json());

   const SEPAY_SECRET = process.env.SEPAY_SECRET;
   const TELEGRAM_BOT_TOKEN = process.env.TELEGRAM_BOT_TOKEN;
   const TELEGRAM_CHAT_ID = process.env.TELEGRAM_CHAT_ID;

   app.post('/webhook/sepay', (req, res) => {
     // Verify HMAC signature
     const signature = req.headers['x-sepay-signature'];
     const hash = crypto.createHmac('sha256', SEPAY_SECRET)
                        .update(JSON.stringify(req.body))
                        .digest('hex');

     if (signature !== hash) {
       return res.status(401).send('Invalid signature');
     }

     // Parse payment data
     const { amount, transaction_id, customer_name, customer_email } = req.body;

     // Send Telegram notification
     const message = `🎉 New Order!\n\nAmount: ${amount} VND\nTransaction: ${transaction_id}\nCustomer: ${customer_name}\nEmail: ${customer_email}`;

     axios.post(`https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage`, {
       chat_id: TELEGRAM_CHAT_ID,
       text: message
     });

     res.status(200).send('OK');
   });

   app.listen(3000, () => console.log('Webhook server running on port 3000'));
   ```

2. Deploy webhook endpoint:
   - Local testing: use ngrok to expose localhost
   - Production: deploy to Vercel, Heroku, Railway, or VPS
   - Get public webhook URL

3. Configure webhook in SePay:
   - Go to SePay Settings → Webhooks
   - Add webhook URL: https://your-domain.com/webhook/sepay
   - Select events: payment.success
   - Save webhook

4. Test full flow:
   - Make test payment via VietQR
   - Verify webhook received by your endpoint
   - Verify Telegram notification sent
   - Check logs for any errors

#### Deliverable:
- Webhook endpoint deployed and public
- Webhook configured in SePay
- HMAC signature verification implemented
- Test payment → Telegram notification confirmed working

#### Alternative (No-Code Option):
- Use Zapier or Make.com to connect SePay → Telegram
- Steps:
  1. Create Zap: SePay (Trigger) → Telegram (Action)
  2. Authenticate SePay and Telegram
  3. Map payment data to Telegram message format
  4. Test and activate Zap
- Note: Zapier/Make may have monthly limits on free plans

---

### Step 4: Auto Delivery Setup (2-3 hours)
- Use Delivery Setup Guide skill
- Choose delivery method (email link / redirect / Telegram bot)
- Configure auto-send trigger after payment confirmed
- Test full flow: payment → notification → delivery
- Output: Complete automated pipeline

#### Actions:
1. Choose delivery method:
   - **Email auto-send**: Webhook triggers email with download link
   - **Redirect after payment**: SePay redirect URL → thank you page with product
   - **Telegram bot delivery**: Bot DMs customer with product link
   - **Manual delivery**: Get notified, manually send product (simple start)

2. Set up chosen delivery method:

   **Option A: Email Auto-Send**
   - Add email sending to webhook:
     ```javascript
     const nodemailer = require('nodemailer');

     const transporter = nodemailer.createTransport({
       service: 'gmail',
       auth: { user: process.env.EMAIL, pass: process.env.EMAIL_PASSWORD }
     });

     app.post('/webhook/sepay', async (req, res) => {
       // ... (previous webhook code)

       // Send product delivery email
       await transporter.sendMail({
         from: process.env.EMAIL,
         to: customer_email,
         subject: 'Your Product is Ready!',
         html: `
           <h1>Thank you for your purchase!</h1>
           <p>Download your product here:</p>
           <a href="${DOWNLOAD_LINK}">Download Now</a>
         `
       });

       res.status(200).send('OK');
     });
     ```

   **Option B: Redirect After Payment**
   - Set up thank you page with download link
   - Configure SePay redirect URL to thank you page
   - Add transaction_id verification on thank you page (prevent unauthorized access)

   **Option C: Telegram Bot Delivery**
   - Bot sends DM with product link after payment
   - Requires customer Telegram username during checkout
   - Code example:
     ```javascript
     axios.post(`https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage`, {
       chat_id: customer_telegram_id,
       text: `Thank you for your purchase! Here's your product:\n\n${DOWNLOAD_LINK}`
     });
     ```

   **Option D: Manual Delivery (Simplest)**
   - Get Telegram notification with customer email
   - Manually send product via email
   - No coding required, just copy/paste workflow

3. Create download link:
   - Host product on Google Drive (set to "Anyone with link can view")
   - Use signed URLs for security (expire after X days)
   - Or use cloud storage: Dropbox, AWS S3, Cloudinary

4. Test full automation:
   - Make test payment
   - Verify payment confirmed
   - Verify Telegram notification received
   - Verify product delivery email sent OR redirect worked OR Telegram DM sent
   - Check customer experience end-to-end

#### Deliverable:
- Delivery method implemented and tested
- Product hosted and accessible via download link
- Full pipeline working: payment → notification → delivery
- Customer journey tested end-to-end

---

### Step 5: Post-Purchase Sequence (1-2 hours)
- Use Delivery Setup Guide skill: post-purchase engagement
- Set up 6-message sequence (thank you → getting started → upsell)
- Configure timing (Day 0, 1, 3, 5, 7, 14)
- Output: Automated post-purchase engagement

#### Actions:
1. Write post-purchase email sequence:
   - **Email 1 (Day 0)**: Order confirmation + download link
   - **Email 2 (Day 1)**: Getting started guide (how to use product)
   - **Email 3 (Day 3)**: Quick win tip (help them see early results)
   - **Email 4 (Day 5)**: Case study or testimonial (social proof)
   - **Email 5 (Day 7)**: Feedback request + support offer
   - **Email 6 (Day 14)**: Upsell to next tier or complementary product

2. Set up automation:
   - Use email tool: Mailchimp, ConvertKit, or SendGrid API
   - Create automation workflow with delay triggers
   - Tag customers after purchase (segment list)
   - Schedule emails based on purchase date

3. OR manual sequence (if no email automation):
   - Create Google Sheet with customer email + purchase date
   - Set calendar reminders to send each email manually
   - Use email templates for each message

4. Test sequence:
   - Add test customer to automation
   - Verify emails sent on correct schedule
   - Check links and formatting

#### Deliverable:
- 6-email post-purchase sequence written
- Automation set up (or manual process documented)
- Test customer received all emails on schedule

---

## Success Criteria
- Customer pays via VietQR → you get Telegram notification within 1 minute
- Customer receives product automatically (or you get clear notification to send manually)
- Full pipeline tested end-to-end with real test transaction
- Post-purchase sequence scheduled and running

## Next Steps
After completing this workflow:
1. Monitor Telegram notifications for incoming orders
2. Check SePay dashboard daily for transaction reconciliation
3. Respond to customer support inquiries
4. Proceed to **Insights & Reporting Workflow** to track revenue and optimize

## Tips for Vietnamese Solopreneurs
- SePay supports all major Vietnamese banks (Vietcombank, Techcombank, ACB, etc.)
- VietQR is trusted and familiar to Vietnamese customers
- Telegram widely used in Vietnam (alternative to WhatsApp)
- Consider manual delivery initially (automate later as volume grows)
- Offer customer support via Zalo or Facebook Messenger (common in VN)

## Common Mistakes to Avoid
- Not testing webhook with real transaction (test with small amount)
- Forgetting HMAC signature verification (security risk)
- Hardcoding API tokens (use .env files)
- No backup delivery method (if automation fails, have manual process)
- Not monitoring Telegram notifications regularly (miss orders)
- Complicated delivery (keep it simple: email with download link)
- No customer support plan (have Zalo/Messenger ready for questions)

## Troubleshooting
- **Webhook not triggering**: Check SePay webhook configuration, verify URL is public
- **Telegram notification not received**: Verify bot token and chat ID, test API directly
- **Email not delivered**: Check spam folder, verify SMTP credentials, use transactional email service
- **Download link broken**: Test link in incognito browser, check file permissions
- **Payment not confirmed**: Check SePay dashboard, verify webhook logs

## Security Checklist
- [ ] API tokens stored in .env (not committed to git)
- [ ] HMAC signature verification implemented
- [ ] 2FA enabled on SePay account
- [ ] Download links use signed URLs or access control
- [ ] Webhook endpoint uses HTTPS (not HTTP)
- [ ] Error logs don't expose sensitive data
- [ ] Customer data stored securely (or not stored at all)
