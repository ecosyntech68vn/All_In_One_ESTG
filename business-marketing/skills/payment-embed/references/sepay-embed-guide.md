# SePay Embed Quick Reference Guide

## QR URL Format

### Base URL
```
https://qr.sepay.vn/img?acc={ACCOUNT}&bank={BANK}&amount={AMOUNT}&des={DESCRIPTION}
```

### Complete Parameter Reference

| Parameter | Type | Required | Description | Example |
|-----------|------|----------|-------------|---------|
| `acc` | string | Yes | Bank account number | `0123456789` |
| `bank` | string | Yes | Bank name (exact match) | `Vietcombank` |
| `amount` | integer | No | Amount in VND (no decimals) | `789000` |
| `des` | string | No | Description/content (URL encoded) | `ORDER_12345` |
| `template` | string | No | QR style: empty, `compact`, `qronly` | `compact` |

### URL Examples

**Minimum required:**
```
https://qr.sepay.vn/img?acc=0123456789&bank=Vietcombank
```

**With fixed amount:**
```
https://qr.sepay.vn/img?acc=0123456789&bank=Vietcombank&amount=789000
```

**Complete (all parameters):**
```
https://qr.sepay.vn/img?acc=0123456789&bank=Vietcombank&amount=789000&des=ORDER_12345&template=compact
```

## Top 15 Vietnamese Banks

| Bank Name | Format for URL | Common Short Name |
|-----------|----------------|-------------------|
| Vietcombank | `Vietcombank` | VCB |
| VPBank | `VPBank` | VPB |
| BIDV | `BIDV` | BIDV |
| Techcombank | `Techcombank` | TCB |
| ACB | `ACB` | ACB |
| MB Bank | `MB` | MB |
| Sacombank | `Sacombank` | STB |
| VietinBank | `VietinBank` | CTG |
| TPBank | `TPBank` | TPB |
| OCB | `OCB` | OCB |
| HDBank | `HDBank` | HDB |
| MSB | `MSB` | MSB |
| SCB | `SCB` | SCB |
| VIB | `VIB` | VIB |
| SHB | `SHB` | SHB |

**Note:** Use the exact format shown in "Format for URL" column. Bank names are case-sensitive.

**Get full list (44+ banks):**
```
https://qr.sepay.vn/banks.json
```

## HTML/CSS Copy-Paste Snippets

### Snippet 1: Basic QR Display

```html
<div class="sepay-qr-container">
  <img
    src="https://qr.sepay.vn/img?acc=YOUR_ACCOUNT&bank=YOUR_BANK&amount=789000"
    alt="Payment QR Code"
    class="sepay-qr-image"
  />
</div>

<style>
.sepay-qr-container {
  text-align: center;
  padding: 2rem;
  background: #f9fafb;
  border-radius: 0.5rem;
}

.sepay-qr-image {
  width: 256px;
  height: 256px;
  margin: 0 auto;
  border-radius: 0.5rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
</style>
```

### Snippet 2: QR with Bank Details

```html
<div class="payment-card">
  <h3 class="payment-title">Complete Payment</h3>

  <img
    src="https://qr.sepay.vn/img?acc=YOUR_ACCOUNT&bank=YOUR_BANK&amount=789000&template=compact"
    alt="QR Code"
    class="qr-code"
  />

  <div class="payment-details">
    <div class="detail-row">
      <span class="detail-label">Bank:</span>
      <span class="detail-value">YOUR_BANK</span>
    </div>
    <div class="detail-row">
      <span class="detail-label">Account:</span>
      <span class="detail-value">YOUR_ACCOUNT</span>
    </div>
    <div class="detail-row">
      <span class="detail-label">Amount:</span>
      <span class="detail-value">789,000 VND</span>
    </div>
  </div>
</div>

<style>
.payment-card {
  max-width: 400px;
  margin: 0 auto;
  padding: 2rem;
  background: white;
  border-radius: 1rem;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
}

.payment-title {
  font-size: 1.5rem;
  font-weight: bold;
  text-align: center;
  margin-bottom: 1.5rem;
  color: #1f2937;
}

.qr-code {
  width: 200px;
  height: 200px;
  display: block;
  margin: 0 auto 1.5rem;
  border-radius: 0.5rem;
}

.payment-details {
  background: #f9fafb;
  padding: 1rem;
  border-radius: 0.5rem;
}

.detail-row {
  display: flex;
  justify-content: space-between;
  padding: 0.5rem 0;
  border-bottom: 1px solid #e5e7eb;
}

.detail-row:last-child {
  border-bottom: none;
}

.detail-label {
  font-weight: 600;
  color: #6b7280;
}

.detail-value {
  color: #1f2937;
}
</style>
```

### Snippet 3: Button with Modal QR

```html
<button id="show-payment-btn" class="payment-button">
  Pay Now - 789,000 VND
</button>

<div id="payment-modal" class="modal hidden">
  <div class="modal-overlay"></div>
  <div class="modal-content">
    <button class="modal-close" id="close-modal">&times;</button>
    <h3 class="modal-title">Scan to Pay</h3>
    <img
      src="https://qr.sepay.vn/img?acc=YOUR_ACCOUNT&bank=YOUR_BANK&amount=789000"
      alt="Payment QR"
      class="modal-qr"
    />
    <p class="modal-text">Use any banking app to scan</p>
  </div>
</div>

<style>
.payment-button {
  background: #2563eb;
  color: white;
  padding: 1rem 2rem;
  border: none;
  border-radius: 0.5rem;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.3s;
}

.payment-button:hover {
  background: #1d4ed8;
}

.modal {
  position: fixed;
  inset: 0;
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal.hidden {
  display: none;
}

.modal-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
}

.modal-content {
  position: relative;
  background: white;
  padding: 2rem;
  border-radius: 1rem;
  max-width: 400px;
  width: 90%;
  text-align: center;
  z-index: 1001;
}

.modal-close {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: none;
  border: none;
  font-size: 2rem;
  color: #9ca3af;
  cursor: pointer;
  line-height: 1;
}

.modal-close:hover {
  color: #4b5563;
}

.modal-title {
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 1.5rem;
  color: #1f2937;
}

.modal-qr {
  width: 220px;
  height: 220px;
  margin: 0 auto;
  border-radius: 0.5rem;
}

.modal-text {
  margin-top: 1rem;
  color: #6b7280;
  font-size: 0.875rem;
}
</style>

<script>
document.getElementById('show-payment-btn').addEventListener('click', () => {
  document.getElementById('payment-modal').classList.remove('hidden');
});

document.getElementById('close-modal').addEventListener('click', () => {
  document.getElementById('payment-modal').classList.add('hidden');
});

document.querySelector('.modal-overlay').addEventListener('click', () => {
  document.getElementById('payment-modal').classList.add('hidden');
});
</script>
```

### Snippet 4: Responsive Pricing Card

```html
<div class="pricing-card">
  <div class="pricing-header">
    <h3 class="plan-name">Pro Plan</h3>
    <div class="price">
      <span class="amount">789,000</span>
      <span class="currency">VND</span>
    </div>
  </div>

  <ul class="features-list">
    <li class="feature-item">✓ Feature One</li>
    <li class="feature-item">✓ Feature Two</li>
    <li class="feature-item">✓ Feature Three</li>
  </ul>

  <div class="payment-section">
    <img
      src="https://qr.sepay.vn/img?acc=YOUR_ACCOUNT&bank=YOUR_BANK&amount=789000&des=PRO_PLAN"
      alt="Pay Now"
      class="payment-qr"
    />
    <p class="payment-hint">Scan to pay instantly</p>
  </div>
</div>

<style>
.pricing-card {
  max-width: 320px;
  background: white;
  border: 2px solid #3b82f6;
  border-radius: 1rem;
  padding: 2rem;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
}

.pricing-header {
  text-align: center;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid #e5e7eb;
}

.plan-name {
  font-size: 1.25rem;
  font-weight: bold;
  color: #1f2937;
  margin-bottom: 1rem;
}

.price {
  display: flex;
  align-items: baseline;
  justify-content: center;
  gap: 0.25rem;
}

.amount {
  font-size: 2.5rem;
  font-weight: bold;
  color: #3b82f6;
}

.currency {
  font-size: 1rem;
  color: #6b7280;
}

.features-list {
  list-style: none;
  padding: 1.5rem 0;
  margin: 0;
  border-bottom: 1px solid #e5e7eb;
}

.feature-item {
  padding: 0.5rem 0;
  color: #4b5563;
}

.payment-section {
  text-align: center;
  padding-top: 1.5rem;
}

.payment-qr {
  width: 180px;
  height: 180px;
  margin: 0 auto;
  border-radius: 0.5rem;
}

.payment-hint {
  margin-top: 0.75rem;
  font-size: 0.875rem;
  color: #6b7280;
}

@media (max-width: 640px) {
  .pricing-card {
    max-width: 100%;
  }
}
</style>
```

## JavaScript Helper Functions

### Function 1: Basic QR Generator

```javascript
function generateSepayQR(config) {
  const { account, bank, amount, description, template } = config;

  if (!account || !bank) {
    throw new Error('Account and bank are required');
  }

  const params = new URLSearchParams();
  params.set('acc', account);
  params.set('bank', bank);

  if (amount) params.set('amount', amount);
  if (description) params.set('des', description);
  if (template) params.set('template', template);

  return `https://qr.sepay.vn/img?${params.toString()}`;
}

// Usage
const qrUrl = generateSepayQR({
  account: '0123456789',
  bank: 'Vietcombank',
  amount: 789000,
  description: 'ORDER_12345'
});
```

### Function 2: Dynamic QR Updater

```javascript
function updatePaymentQR(elementId, config) {
  const qrUrl = generateSepayQR(config);
  const element = document.getElementById(elementId);

  if (!element) {
    console.error(`Element with id "${elementId}" not found`);
    return;
  }

  element.src = qrUrl;
  element.alt = `Payment QR: ${config.amount || 'flexible'} VND`;
}

// Usage
updatePaymentQR('payment-qr', {
  account: '0123456789',
  bank: 'Vietcombank',
  amount: 789000,
  description: 'PRODUCT_SKU_123'
});
```

### Function 3: Multi-Product QR Generator

```javascript
function createProductQR(productId, baseConfig) {
  const products = {
    'basic': { amount: 299000, description: 'BASIC_PLAN' },
    'pro': { amount: 789000, description: 'PRO_PLAN' },
    'premium': { amount: 1490000, description: 'PREMIUM_PLAN' }
  };

  const product = products[productId];
  if (!product) {
    throw new Error(`Product "${productId}" not found`);
  }

  return generateSepayQR({
    ...baseConfig,
    amount: product.amount,
    description: product.description
  });
}

// Usage
const baseConfig = {
  account: '0123456789',
  bank: 'Vietcombank',
  template: 'compact'
};

const basicPlanQR = createProductQR('basic', baseConfig);
const proPlanQR = createProductQR('pro', baseConfig);
```

### Function 4: QR with Format Validation

```javascript
function createValidatedQR(config) {
  // Validate account number
  if (!/^\d{6,20}$/.test(config.account)) {
    throw new Error('Invalid account number format');
  }

  // Validate amount
  if (config.amount && (config.amount <= 0 || !Number.isInteger(config.amount))) {
    throw new Error('Amount must be a positive integer');
  }

  // Clean description (remove special chars)
  if (config.description) {
    config.description = config.description
      .replace(/[^a-zA-Z0-9_-]/g, '_')
      .substring(0, 50);
  }

  return generateSepayQR(config);
}

// Usage
try {
  const qrUrl = createValidatedQR({
    account: '0123456789',
    bank: 'Vietcombank',
    amount: 789000,
    description: 'Order #12345'
  });
  console.log('QR generated:', qrUrl);
} catch (error) {
  console.error('Validation failed:', error.message);
}
```

### Function 5: QR with Loading State

```javascript
function loadPaymentQR(elementId, config) {
  const element = document.getElementById(elementId);
  if (!element) return;

  // Show loading state
  element.src = 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="200" height="200"%3E%3Ctext x="50%25" y="50%25" text-anchor="middle" fill="%23999"%3ELoading...%3C/text%3E%3C/svg%3E';
  element.alt = 'Loading payment QR...';

  // Generate QR URL
  const qrUrl = generateSepayQR(config);

  // Create new image to preload
  const img = new Image();
  img.onload = () => {
    element.src = qrUrl;
    element.alt = 'Payment QR Code';
  };
  img.onerror = () => {
    element.alt = 'Failed to load QR code';
    console.error('QR code failed to load');
  };
  img.src = qrUrl;
}

// Usage
loadPaymentQR('qr-image', {
  account: '0123456789',
  bank: 'Vietcombank',
  amount: 789000
});
```

## Troubleshooting

### Issue: QR Code Not Loading

**Symptoms:**
- Image shows broken icon
- 404 error in browser console
- QR code URL returns error

**Solutions:**

1. **Check account number format**
   ```javascript
   // ✓ Correct
   acc=0123456789

   // ✗ Wrong
   acc=0123-456-789  // No dashes
   acc=0123 456 789  // No spaces
   ```

2. **Verify bank name**
   ```javascript
   // ✓ Correct (exact match)
   bank=Vietcombank
   bank=VPBank

   // ✗ Wrong
   bank=VCB          // Use full name
   bank=vietcombank  // Case-sensitive
   bank=VP Bank      // No space
   ```

3. **Test with minimal URL**
   ```
   https://qr.sepay.vn/img?acc=YOUR_ACCOUNT&bank=Vietcombank
   ```

4. **Verify bank is supported**
   - Check: https://qr.sepay.vn/banks.json
   - Use exact name from list

### Issue: Wrong Amount Displayed

**Symptoms:**
- Amount shows as 0
- Decimal places appear incorrectly
- Customer sees different amount

**Solutions:**

1. **Use integer values only**
   ```javascript
   // ✓ Correct
   amount=789000

   // ✗ Wrong
   amount=789000.00  // No decimals
   amount=789,000    // No commas
   amount=789k       // No suffixes
   ```

2. **Check amount parameter**
   ```javascript
   // Ensure amount is integer
   const amount = parseInt(789000);
   const url = `https://qr.sepay.vn/img?acc=${acc}&bank=${bank}&amount=${amount}`;
   ```

3. **Format display separately**
   ```javascript
   // QR URL: use raw integer
   amount=789000

   // Display text: format with commas
   document.getElementById('display').textContent = '789,000 VND';
   ```

### Issue: Description/Content Not Showing

**Symptoms:**
- Transfer content is empty or garbled
- Special characters break QR code
- Description truncated

**Solutions:**

1. **URL encode description**
   ```javascript
   // ✓ Correct
   const description = encodeURIComponent('ORDER_12345');
   const url = `...&des=${description}`;

   // Or use URLSearchParams (auto-encodes)
   const params = new URLSearchParams();
   params.set('des', 'ORDER_12345');
   ```

2. **Avoid special characters**
   ```javascript
   // ✓ Correct
   des=ORDER_12345
   des=PRO_PLAN
   des=CUSTOMER_NAME

   // ✗ Wrong
   des=Order #12345    // Space and #
   des=Đơn hàng        // Vietnamese characters
   des=Order/12345     // Forward slash
   ```

3. **Keep it short**
   ```javascript
   // Maximum ~50 characters
   const maxLength = 50;
   const description = 'Long description...'.substring(0, maxLength);
   ```

4. **Use underscores/hyphens**
   ```javascript
   // Replace spaces and special chars
   const clean = description
     .replace(/\s+/g, '_')
     .replace(/[^a-zA-Z0-9_-]/g, '');
   ```

### Issue: QR Code Image Quality

**Symptoms:**
- Blurry QR code
- Pixelated image
- Too small to scan

**Solutions:**

1. **Use appropriate size**
   ```css
   /* Minimum recommended */
   .qr-code {
     width: 200px;
     height: 200px;
   }

   /* Optimal for mobile */
   .qr-code {
     width: 256px;
     height: 256px;
   }
   ```

2. **Avoid stretching**
   ```css
   /* ✓ Maintain aspect ratio */
   .qr-code {
     width: 256px;
     height: 256px;
     object-fit: contain;
   }

   /* ✗ Don't distort */
   .qr-code {
     width: 300px;
     height: 200px; /* Different ratio */
   }
   ```

3. **Use template parameter**
   ```javascript
   // Compact template for better clarity
   template=compact

   // QR only (no branding)
   template=qronly
   ```

### Issue: Payment Not Confirmed via Webhook

**Symptoms:**
- Customer paid but order not updated
- Webhook not receiving data
- Timeout errors

**Solutions:**

1. **Verify webhook URL is HTTPS**
   ```javascript
   // ✓ Correct
   https://yourdomain.com/webhook/sepay

   // ✗ Wrong
   http://yourdomain.com/webhook/sepay  // Must be HTTPS
   ```

2. **Return 200 OK immediately**
   ```javascript
   // Node.js Express
   app.post('/webhook/sepay', (req, res) => {
     // Return 200 first
     res.status(200).send('OK');

     // Process async
     processPayment(req.body).catch(console.error);
   });
   ```

3. **Match payment by content**
   ```javascript
   // Ensure content matches exactly
   const orderId = transaction.content; // Must match 'des' parameter
   ```

4. **Check webhook logs in SePay dashboard**
   - Go to my.sepay.vn
   - Check webhook delivery status
   - Review failed attempts

### Issue: QR Code Not Scannable

**Symptoms:**
- Banking app can't read QR
- Scan returns error
- Invalid QR format

**Solutions:**

1. **Test with multiple banking apps**
   - Try different banks' apps
   - Ensure VietQR is supported

2. **Check lighting conditions**
   - QR needs good contrast
   - Avoid dark backgrounds
   - Ensure sufficient screen brightness

3. **Verify QR is not corrupted**
   ```html
   <!-- Add error handling -->
   <img
     src="https://qr.sepay.vn/img?..."
     alt="QR Code"
     onerror="this.onerror=null; this.src='fallback.png';"
   />
   ```

4. **Use simpler template**
   ```javascript
   // If 'compact' fails, try default
   // Remove template parameter
   https://qr.sepay.vn/img?acc=...&bank=...
   ```

### Issue: CORS Errors (if fetching programmatically)

**Symptoms:**
- CORS policy error in console
- Can't load QR via fetch/axios

**Solutions:**

1. **Use direct image embedding**
   ```html
   <!-- ✓ Direct img tag (no CORS issue) -->
   <img src="https://qr.sepay.vn/img?..." />

   <!-- ✗ Don't fetch as data -->
   <script>
   // This may cause CORS
   fetch('https://qr.sepay.vn/img?...')
   </script>
   ```

2. **Load as image, not data**
   ```javascript
   // ✓ Correct approach
   const img = document.createElement('img');
   img.src = qrUrl;
   document.body.appendChild(img);
   ```

## Testing Checklist

Before going live, verify:

- [ ] QR code loads correctly in browser
- [ ] Scan QR with your own banking app
- [ ] Verify bank name, account, amount display correctly
- [ ] Test with and without amount parameter
- [ ] Check description appears in transfer content
- [ ] Test on mobile devices (iOS and Android)
- [ ] Verify responsive design on different screen sizes
- [ ] Test modal open/close (if using modal pattern)
- [ ] Confirm webhook receives test payment (if configured)
- [ ] Check payment confirmation flow end-to-end

## Quick Reference Chart

| Use Case | Template | Amount | Description |
|----------|----------|--------|-------------|
| Product purchase | `compact` | Fixed | Product SKU/name |
| Service subscription | `compact` | Fixed | Subscription plan |
| Donation | Empty | Omit | Optional note |
| Event ticket | `compact` | Fixed | Event + ticket ID |
| Invoice payment | Empty | Fixed | Invoice number |
| Flexible payment | `qronly` | Omit | Customer note |

## Resources

- **SePay Dashboard**: https://my.sepay.vn
- **QR Generator**: https://qr.sepay.vn
- **Bank List API**: https://qr.sepay.vn/banks.json
- **Support**: Contact via SePay dashboard

---

**Last Updated:** 2024
**Version:** 1.0
