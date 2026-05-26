---
description: Set up automatic product delivery
argument-hint: [method]
---
Configure automated digital product delivery.

<args>$ARGUMENTS</args>

## Methods
- `email` - Email with download link
- `redirect` - Redirect to protected page
- `telegram` - Telegram bot auto-send
- `compare` - Compare all delivery methods
- `post-purchase` - Set up post-purchase sequence

## Process
1. Activate Deliver Agent
2. Use Delivery Setup Guide skill
3. Configure chosen delivery method + post-purchase engagement
4. Output: Working auto-delivery pipeline

## Examples
- `/delivery email` — Set up automated email delivery with download links
- `/delivery telegram` — Configure Telegram bot to auto-send files after payment
- `/delivery compare` — Side-by-side comparison of all delivery methods (speed, cost, UX)

## Tips
- Use email for documents and courses; Telegram for instant-access digital goods
- Always include a post-purchase thank-you message — it reduces refund requests
- Test the full purchase-to-delivery flow end-to-end before going live
