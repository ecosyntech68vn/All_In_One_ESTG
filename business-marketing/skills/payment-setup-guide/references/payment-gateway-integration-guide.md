# Payment Gateway Integration Guide

Complete guide for integrating SePay payment gateway for Vietnamese digital product businesses.

## SePay Overview

SePay is a Vietnamese payment aggregator supporting:
- VietQR (instant bank transfer via QR code)
- Domestic bank transfers
- E-wallets (MoMo, ZaloPay, ViettelPay)
- Real-time payment notifications via webhook

**Pricing**: 1.5-2% transaction fee + no monthly costs
**Settlement**: T+1 (next business day)

## Account Registration

### Step 1: Sign Up
1. Visit sepay.vn/merchant
2. Complete business registration form:
   - Business name (individual or company)
   - Tax code (optional for individuals)
   - Bank account details
   - Contact information

### Step 2: Verification
- Submit ID/business license photos
- Verification takes 1-3 business days
- Approval via email notification

### Step 3: API Access
- Login to merchant dashboard
- Navigate to Settings → API Integration
- Generate API token (save securely)

## API Token Management

### Obtaining Your Token
```
Dashboard → Settings → API Integration → Generate Token
```

**Security practices:**
- Store token in environment variables (never in code)
- Use separate tokens for development/production
- Rotate tokens every 90 days
- Never expose in frontend code

### Environment Variables
```bash
# .env file
SEPAY_API_TOKEN=your_token_here
SEPAY_WEBHOOK_SECRET=your_webhook_secret_here
SEPAY_ENVIRONMENT=production # or sandbox
```

## VietQR Integration

VietQR enables instant bank transfers by scanning QR codes.

### Creating Payment QR Code

**Endpoint**: `POST https://api.sepay.vn/v1/qr/create`

**Headers**:
```javascript
{
  "Authorization": "Bearer YOUR_API_TOKEN",
  "Content-Type": "application/json"
}
```

**Request Body**:
```javascript
{
  "amount": 500000, // VND
  "order_id": "ORD-20240213-001",
  "description": "Payment for Digital Marketing Course",
  "customer_email": "customer@example.com",
  "customer_name": "Nguyen Van A",
  "return_url": "https://yoursite.com/payment/success",
  "cancel_url": "https://yoursite.com/payment/cancel"
}
```

**Response**:
```javascript
{
  "success": true,
  "data": {
    "qr_code_url": "https://sepay.vn/qr/xyz123",
    "qr_image": "data:image/png;base64,...",
    "payment_id": "PAY-xyz123",
    "expires_at": "2024-02-13T10:30:00Z"
  }
}
```

### Node.js Implementation

```javascript
const axios = require('axios');

async function createPaymentQR(orderData) {
  try {
    const response = await axios.post(
      'https://api.sepay.vn/v1/qr/create',
      {
        amount: orderData.amount,
        order_id: orderData.orderId,
        description: orderData.description,
        customer_email: orderData.customerEmail,
        customer_name: orderData.customerName,
        return_url: `${process.env.BASE_URL}/payment/success`,
        cancel_url: `${process.env.BASE_URL}/payment/cancel`
      },
      {
        headers: {
          'Authorization': `Bearer ${process.env.SEPAY_API_TOKEN}`,
          'Content-Type': 'application/json'
        }
      }
    );

    return response.data;
  } catch (error) {
    console.error('SePay QR creation failed:', error.response?.data);
    throw new Error('Payment QR generation failed');
  }
}

// Usage
const payment = await createPaymentQR({
  amount: 500000,
  orderId: 'ORD-' + Date.now(),
  description: 'Digital Product Purchase',
  customerEmail: req.body.email,
  customerName: req.body.name
});

// Display QR code to customer
res.render('checkout', { qrImage: payment.data.qr_image });
```

## Webhook Integration

Webhooks notify your server instantly when payments complete.

### Webhook Setup

**Dashboard Configuration**:
1. Settings → Webhook Configuration
2. Enter webhook URL: `https://yoursite.com/api/sepay-webhook`
3. Select events: `payment.success`, `payment.failed`
4. Save webhook secret (used for verification)

### Webhook Payload

SePay sends POST request to your webhook URL:

```javascript
{
  "event": "payment.success",
  "payment_id": "PAY-xyz123",
  "order_id": "ORD-20240213-001",
  "amount": 500000,
  "currency": "VND",
  "status": "completed",
  "customer_email": "customer@example.com",
  "timestamp": "2024-02-13T09:15:30Z",
  "signature": "hmac_signature_here"
}
```

### HMAC Signature Verification

**Critical security step**: Verify webhook authenticity

```javascript
const crypto = require('crypto');

function verifyWebhookSignature(payload, signature, secret) {
  const hmac = crypto.createHmac('sha256', secret);
  const expectedSignature = hmac
    .update(JSON.stringify(payload))
    .digest('hex');

  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(expectedSignature)
  );
}
```

### Complete Webhook Handler (Express.js)

```javascript
const express = require('express');
const router = express.Router();

router.post('/sepay-webhook', express.json(), async (req, res) => {
  try {
    // 1. Extract signature from headers
    const signature = req.headers['x-sepay-signature'];

    if (!signature) {
      return res.status(401).json({ error: 'Missing signature' });
    }

    // 2. Verify signature
    const isValid = verifyWebhookSignature(
      req.body,
      signature,
      process.env.SEPAY_WEBHOOK_SECRET
    );

    if (!isValid) {
      console.error('Invalid webhook signature');
      return res.status(401).json({ error: 'Invalid signature' });
    }

    // 3. Process payment event
    const { event, payment_id, order_id, amount, status } = req.body;

    if (event === 'payment.success' && status === 'completed') {
      // Update order in database
      await updateOrderStatus(order_id, 'paid', payment_id);

      // Trigger product delivery
      await deliverProduct(order_id);

      // Send confirmation email
      await sendConfirmationEmail(order_id);

      console.log(`Payment processed: ${order_id}`);
    }

    // 4. Acknowledge receipt (must respond within 5 seconds)
    res.status(200).json({ received: true });

  } catch (error) {
    console.error('Webhook processing error:', error);
    res.status(500).json({ error: 'Processing failed' });
  }
});

module.exports = router;
```

## Testing Flow

### Sandbox Environment

Use test credentials for development:

```javascript
// .env.development
SEPAY_API_TOKEN=test_token_xxx
SEPAY_WEBHOOK_SECRET=test_secret_xxx
SEPAY_ENVIRONMENT=sandbox
```

### Test Scenarios

1. **Successful Payment**:
   - Create QR code
   - Use SePay test card
   - Verify webhook received
   - Check order updated

2. **Failed Payment**:
   - Simulate insufficient funds
   - Verify error handling
   - Check retry logic

3. **Webhook Timeout**:
   - Test delayed processing
   - Verify retry mechanism

## Production Checklist

- [ ] Production API token configured
- [ ] Webhook URL using HTTPS
- [ ] HMAC signature verification implemented
- [ ] Error logging setup
- [ ] Webhook retry handling configured
- [ ] Payment reconciliation process defined
- [ ] Customer support flow for failed payments
- [ ] Security audit completed

## Common Issues & Solutions

**Issue**: Webhook not receiving events
- Check URL is publicly accessible
- Verify HTTPS certificate valid
- Review firewall settings
- Test with webhook testing tools

**Issue**: Signature verification fails
- Confirm webhook secret matches dashboard
- Check payload parsing (use raw body)
- Verify HMAC algorithm (sha256)

**Issue**: Payment shows pending
- VietQR takes 5-30 seconds
- Don't auto-cancel before 5 minutes
- Implement status polling as backup

## Rate Limits

- QR creation: 100 requests/minute
- Status check: 300 requests/minute
- Webhook retries: 5 attempts over 24 hours

## Support Resources

- SePay documentation: docs.sepay.vn
- Merchant support: support@sepay.vn
- Technical issues: dev@sepay.vn
- Response time: 4-24 hours
