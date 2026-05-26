---
name: payment-embed
description: Embed SePay VietQR payment into landing pages for Vietnamese bank transfers
---

# SePay Payment Embed Skill

## Overview

This skill teaches how to embed SePay VietQR payment into landing pages for accepting bank transfers in Vietnam.

### Purpose
- Add VietQR payment functionality to landing pages
- Accept VND payments via bank transfer
- Target: Vietnamese SMEs and businesses

### Key Benefits
- No backend required for basic integration
- Customer-friendly QR code scanning
- Direct bank-to-bank transfers
- 44+ Vietnamese banks supported
- Instant payment confirmation via webhook

## How SePay VietQR Works

### Flow
1. Business creates SePay account at my.sepay.vn
2. Links bank account (supports 44+ Vietnamese banks)
3. Generates QR codes via SePay API URL
4. Customer scans QR code with banking app
5. Payment goes directly to business bank account
6. SePay sends webhook notification when payment confirmed

### No Backend Required
Basic integration only needs an image URL - perfect for static landing pages.

## QR Code Generation

### API URL Format
```
https://qr.sepay.vn/img?acc={ACCOUNT}&bank={BANK}&amount={AMOUNT}&des={DESCRIPTION}
```

### Parameters

| Parameter | Required | Description | Example |
|-----------|----------|-------------|---------|
| `acc` | Yes | Bank account number | `0123456789` |
| `bank` | Yes | Bank name | `Vietcombank` |
| `amount` | No | Payment amount in VND (customer enters if omitted) | `789000` |
| `des` | No | Transfer description/content (URL encoded) | `ORDER_12345` |
| `template` | No | QR style: empty (default), `compact`, `qronly` | `compact` |

### Example URLs

**Basic QR (customer enters amount):**
```
https://qr.sepay.vn/img?acc=0123456789&bank=Vietcombank
```

**Fixed amount QR:**
```
https://qr.sepay.vn/img?acc=0123456789&bank=Vietcombank&amount=789000
```

**Full details with description:**
```
https://qr.sepay.vn/img?acc=0123456789&bank=Vietcombank&amount=789000&des=PRO_PLAN
```

**Compact template:**
```
https://qr.sepay.vn/img?acc=0123456789&bank=Vietcombank&amount=789000&template=compact
```

## HTML Embed Patterns

### Pattern 1: Simple QR Code

Clean, centered payment section with QR code and bank details.

```html
<div class="payment-section text-center p-8 bg-gray-50 rounded-lg">
  <h3 class="text-2xl font-bold mb-4 text-gray-800">Pay via Bank Transfer</h3>

  <img
    src="https://qr.sepay.vn/img?acc=YOUR_ACCOUNT&bank=YOUR_BANK&amount=789000&des=YOUR_PRODUCT"
    alt="Payment QR Code"
    class="mx-auto w-64 h-64 rounded-lg shadow-lg"
  />

  <div class="mt-6 text-left max-w-sm mx-auto bg-white rounded-lg p-4 shadow">
    <p class="mb-2"><strong>Bank:</strong> YOUR_BANK</p>
    <p class="mb-2"><strong>Account:</strong> YOUR_ACCOUNT</p>
    <p class="mb-2"><strong>Amount:</strong> 789,000 VND</p>
    <p class="mb-2"><strong>Content:</strong> YOUR_PRODUCT</p>
  </div>

  <p class="mt-4 text-sm text-gray-600">
    Scan with any banking app • 44+ banks supported
  </p>
</div>
```

### Pattern 2: Dynamic QR with JavaScript

Generate QR codes dynamically with JavaScript for multiple products or dynamic pricing.

```html
<div id="payment-container">
  <img id="qr-code" alt="Payment QR Code" class="w-64 h-64 mx-auto" />
  <div id="payment-details"></div>
</div>

<script>
function generatePaymentQR(options) {
  const params = new URLSearchParams({
    acc: options.account,
    bank: options.bank,
  });

  if (options.amount) params.set('amount', options.amount);
  if (options.description) params.set('des', options.description);
  if (options.template) params.set('template', options.template);

  return `https://qr.sepay.vn/img?${params}`;
}

// Usage example
const qrUrl = generatePaymentQR({
  account: 'YOUR_ACCOUNT',
  bank: 'Vietcombank',
  amount: 789000,
  description: 'Order_Product_Name'
});

document.getElementById('qr-code').src = qrUrl;

// Update payment details
document.getElementById('payment-details').innerHTML = `
  <div class="mt-4 text-center">
    <p><strong>Amount:</strong> 789,000 VND</p>
    <p><strong>Description:</strong> Order_Product_Name</p>
  </div>
`;
</script>
```

### Pattern 3: Pricing Card with QR Payment

Embed QR code directly into pricing cards for product/service packages.

```html
<div class="bg-white rounded-2xl shadow-xl p-8 border-2 border-blue-500 max-w-sm">
  <!-- Pricing Header -->
  <div class="text-center">
    <h3 class="text-xl font-bold text-gray-800">Pro Plan</h3>
    <div class="mt-4">
      <span class="text-4xl font-bold text-blue-600">789,000</span>
      <span class="text-gray-500 ml-1">VND</span>
    </div>
    <p class="text-sm text-gray-500 mt-1">per month</p>
  </div>

  <!-- Features List -->
  <ul class="mt-6 space-y-3">
    <li class="flex items-center text-gray-700">
      <svg class="w-5 h-5 text-green-500 mr-2 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
        <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
      </svg>
      Premium Feature Access
    </li>
    <li class="flex items-center text-gray-700">
      <svg class="w-5 h-5 text-green-500 mr-2 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
        <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
      </svg>
      Priority Support
    </li>
    <li class="flex items-center text-gray-700">
      <svg class="w-5 h-5 text-green-500 mr-2 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
        <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
      </svg>
      Advanced Analytics
    </li>
  </ul>

  <!-- Payment QR -->
  <div class="mt-8 text-center">
    <img
      src="https://qr.sepay.vn/img?acc=YOUR_ACCOUNT&bank=YOUR_BANK&amount=789000&des=PRO_PLAN&template=compact"
      alt="Scan to pay"
      class="mx-auto w-48 h-48 rounded-lg shadow-md"
    />
    <p class="mt-3 text-sm text-gray-600">Scan QR code to pay instantly</p>
    <p class="text-xs text-gray-500 mt-1">Payment confirmed automatically</p>
  </div>
</div>
```

### Pattern 4: Payment Modal (Click to Show QR)

Show QR code in modal when user clicks "Buy Now" button.

```html
<!-- Trigger Button -->
<button
  onclick="showPaymentModal()"
  class="bg-blue-600 text-white px-8 py-3 rounded-lg font-bold hover:bg-blue-700 transition-colors">
  Buy Now - 789,000 VND
</button>

<!-- Modal Overlay -->
<div id="payment-modal" class="hidden fixed inset-0 bg-black/50 flex items-center justify-center z-50">
  <div class="bg-white rounded-2xl p-8 max-w-md mx-4 relative">
    <!-- Close Button -->
    <button
      onclick="hidePaymentModal()"
      class="absolute top-4 right-4 text-gray-400 hover:text-gray-600 text-2xl font-bold">
      &times;
    </button>

    <!-- Modal Header -->
    <div class="mb-6">
      <h3 class="text-xl font-bold text-gray-800">Complete Payment</h3>
      <p class="text-sm text-gray-600 mt-1">Scan QR code with your banking app</p>
    </div>

    <!-- QR Code -->
    <div class="text-center">
      <img
        src="https://qr.sepay.vn/img?acc=YOUR_ACCOUNT&bank=YOUR_BANK&amount=789000&des=ORDER_ID"
        alt="Payment QR"
        class="mx-auto w-56 h-56 rounded-lg shadow-lg"
      />

      <!-- Payment Details -->
      <div class="mt-4 bg-gray-50 rounded-lg p-4 text-sm text-left">
        <p class="mb-2"><strong>Bank:</strong> YOUR_BANK</p>
        <p class="mb-2"><strong>Account:</strong> YOUR_ACCOUNT</p>
        <p class="mb-2"><strong>Amount:</strong> 789,000 VND</p>
        <p class="mb-2"><strong>Content:</strong> ORDER_ID</p>
      </div>

      <!-- Instructions -->
      <div class="mt-4 bg-blue-50 rounded-lg p-3 text-sm text-blue-800">
        <p class="font-medium">After payment:</p>
        <p class="mt-1">Confirmation is sent automatically via Telegram</p>
      </div>
    </div>
  </div>
</div>

<script>
function showPaymentModal() {
  document.getElementById('payment-modal').classList.remove('hidden');
}

function hidePaymentModal() {
  document.getElementById('payment-modal').classList.add('hidden');
}

// Close modal when clicking outside
document.getElementById('payment-modal').addEventListener('click', function(e) {
  if (e.target === this) {
    hidePaymentModal();
  }
});
</script>
```

## Webhook Setup (Advanced)

For automatic payment confirmation, set up webhook endpoint to receive transaction notifications.

### Requirements
- Backend server to receive POST requests
- SePay account with webhook configured
- Endpoint URL (must be HTTPS)

### Webhook Payload Structure

```json
{
  "id": 92704,
  "gateway": "Vietcombank",
  "transactionDate": "2023-03-25 14:02:37",
  "accountNumber": "0123456789",
  "content": "payment content",
  "transferType": "in",
  "transferAmount": 789000,
  "referenceCode": "FT23084123456",
  "description": "Transfer details"
}
```

### Webhook Processing Steps

1. **Verify Signature** - Validate request authenticity using HMAC
2. **Match Payment** - Match by content, amount, or reference code
3. **Update Order Status** - Mark order as paid in database
4. **Trigger Delivery** - Send email, Telegram notification, or unlock access
5. **Return 200 OK** - Acknowledge receipt to SePay

### Example Webhook Handler (Node.js)

```javascript
app.post('/webhook/sepay', async (req, res) => {
  const transaction = req.body;

  // Verify transaction
  if (transaction.transferType === 'in' && transaction.transferAmount > 0) {
    // Match payment by content
    const orderId = transaction.content.match(/ORDER_(\d+)/)?.[1];

    if (orderId) {
      // Update order status
      await updateOrderStatus(orderId, 'paid');

      // Send notification
      await sendTelegramNotification({
        orderId,
        amount: transaction.transferAmount,
        transactionDate: transaction.transactionDate
      });
    }
  }

  // Always return 200 OK
  res.status(200).send('OK');
});
```

## Supported Banks

44+ Vietnamese banks including:

- Vietcombank
- VPBank
- BIDV
- Techcombank
- ACB Bank
- MB Bank
- Sacombank
- VietinBank
- TPBank
- OCB
- HDBank
- MSB
- SCB
- VIB
- SHB

**Get full bank list:**
```
https://qr.sepay.vn/banks.json
```

### Bank Code Format
Use exact bank names as listed in the banks.json file. Common formats:
- `Vietcombank` (not `VCB`)
- `VPBank` (not `VP Bank`)
- `Techcombank` (not `TCB`)

## Integration with Landing Page

### Step-by-Step Integration

1. **Build Landing Page**
   - Use Landing Page Builder skill to create page structure
   - Add pricing/product sections

2. **Add Payment Section**
   - Choose pattern above (Simple QR, Modal, or Pricing Card)
   - Replace placeholders: `YOUR_ACCOUNT`, `YOUR_BANK`
   - Set amount and description

3. **Configure SePay Account**
   - Create account at my.sepay.vn
   - Link bank account
   - Test QR code generation

4. **Deploy to Vercel**
   - Use Vercel Deployment skill
   - Deploy static site with embedded QR codes

5. **Set Up Notifications**
   - Configure Telegram bot for payment alerts
   - Set up webhook endpoint (optional)

## Best Practices

### User Experience
- **Show bank details alongside QR code** - Some users prefer manual transfer
- **Include transfer content** - Essential for order matching
- **Add clear instructions** - "Scan with any banking app"
- **Display amount clearly** - Use Vietnamese number format (789,000)

### Technical
- **Use fixed amounts for products** - Flexible amounts for donations only
- **URL encode descriptions** - Avoid special characters in `des` parameter
- **Test before going live** - Scan QR with your own banking app
- **Add loading states** - Handle QR image loading delays

### Security
- **QR URLs are public** - They only encode payment info (safe to embed)
- **Never expose webhook keys** - Keep API keys server-side only
- **Validate webhook signatures** - For high-value transactions
- **Use HTTPS for webhooks** - SePay requires secure endpoints

## Common Use Cases

### E-commerce Products
```html
<img src="https://qr.sepay.vn/img?acc=YOUR_ACCOUNT&bank=YOUR_BANK&amount=789000&des=PRODUCT_SKU_123" />
```

### Service Subscriptions
```html
<img src="https://qr.sepay.vn/img?acc=YOUR_ACCOUNT&bank=YOUR_BANK&amount=789000&des=SUBSCRIPTION_MONTHLY" />
```

### Donations (Flexible Amount)
```html
<img src="https://qr.sepay.vn/img?acc=YOUR_ACCOUNT&bank=YOUR_BANK&des=DONATION" />
```

### Event Tickets
```html
<img src="https://qr.sepay.vn/img?acc=YOUR_ACCOUNT&bank=YOUR_BANK&amount=500000&des=EVENT_TICKET_2024" />
```

## Troubleshooting

### QR Code Not Loading
- Check account number and bank name are correct
- Verify bank name matches SePay's bank list
- Ensure URL parameters are properly encoded

### Wrong Amount Displayed
- Amount must be in VND (no decimals)
- Use integer values only (789000, not 789000.00)
- Remove commas from amount parameter

### Description Not Showing
- URL encode special characters
- Keep description short (under 50 characters)
- Avoid spaces (use underscores or hyphens)

### Payment Not Confirmed
- Verify webhook URL is HTTPS
- Check webhook endpoint returns 200 OK
- Validate content/description matches order

## Reference Files

- **sepay-embed-guide.md**: Quick reference for QR URL format, parameters, bank codes, and embed snippets

## Resources

- **SePay Dashboard**: my.sepay.vn
- **QR API**: qr.sepay.vn
- **Bank List**: https://qr.sepay.vn/banks.json
- **Documentation**: Official SePay docs at my.sepay.vn/docs

## Related Skills

- **landing-page-builder** - Build pages to embed payment
- **vercel-deployment** - Deploy pages with embedded QR codes
- **telegram-notifications** - Get payment alerts via Telegram

---

**Note:** Replace `YOUR_ACCOUNT`, `YOUR_BANK` with actual values before deployment. Never commit API keys or webhook secrets to public repositories.
