---
description: Add SePay VietQR payment to landing pages
argument-hint: [pattern]
---
Embed VietQR payment into your landing page.

<args>$ARGUMENTS</args>

## Patterns
- `qr` - Simple QR code embed
- `pricing` - Pricing card with QR payment
- `modal` - Click-to-pay modal popup
- `dynamic` - JavaScript dynamic QR generation

## Process
1. Activate Deliver Agent
2. Use Payment Embed skill
3. Generate SePay QR embed code
4. Output: Copy-paste HTML/JS payment section

## Examples
- `/payment-embed qr` — Generate a simple QR code payment section with bank details
- `/payment-embed pricing` — Create a 3-tier pricing card layout with QR codes per plan
- `/payment-embed modal` — Build a payment modal that shows QR on button click
- `/payment-embed dynamic` — Generate JavaScript code for dynamic QR based on product selection

## Tips
- Replace YOUR_ACCOUNT and YOUR_BANK placeholders with your real SePay bank details
- Test the QR code with your own banking app before going live
- Always show bank details alongside QR (some customers prefer manual transfer)
