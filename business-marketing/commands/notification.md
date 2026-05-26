---
description: Set up Telegram order notifications
argument-hint: [step]
---
Configure Telegram bot for order notifications.

<args>$ARGUMENTS</args>

## Steps
- `start` - Begin bot setup from scratch
- `bot` - Create Telegram bot via @BotFather
- `webhook` - Connect SePay webhook to Telegram
- `test` - Send test notification
- `templates` - Get notification message templates

## Process
1. Activate Deliver Agent
2. Use Notification Setup Guide skill
3. Walk through Telegram bot + webhook pipeline setup
4. Output: Working notification pipeline

## Examples
- `/notification start` — Full setup from creating Telegram bot to receiving first alert
- `/notification templates` — Get ready-to-use message templates for payment, delivery, errors
- `/notification webhook` — Connect SePay payment events to your Telegram bot

## Tips
- Create your Telegram bot via @BotFather first — you'll need the bot token for everything else
- Test webhook with ngrok locally before deploying to production
- Group notifications by type (payment, delivery, error) so you can mute non-critical channels
