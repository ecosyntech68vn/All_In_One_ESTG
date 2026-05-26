---
description: Set up SePay payment gateway
argument-hint: [step]
---
Guide through SePay payment setup.

<args>$ARGUMENTS</args>

## Steps
- `start` - Begin setup from scratch
- `api` - Configure API token
- `qr` - Generate VietQR payment link
- `webhook` - Set up payment webhook
- `test` - Test payment flow

## Process
1. Activate Deliver Agent
2. Use Payment Setup Guide skill
3. Walk through step-by-step SePay configuration
4. Output: Working payment link + webhook endpoint

## Examples
- `/payment-setup start` — Full guided setup from SePay account creation to first QR code
- `/payment-setup webhook` — Configure webhook to receive real-time payment confirmations
- `/payment-setup test` — Run a test transaction to verify the entire payment flow

## Tips
- Use SePay sandbox mode first, switch to production only after full testing
- Always verify HMAC signature on webhook callbacks to prevent spoofed payments
- Keep API keys in environment variables — never hardcode them in source files
