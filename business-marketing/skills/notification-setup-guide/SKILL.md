---
name: notification-setup-guide
description: Real-time order and lead notification system setup via Telegram bot and webhooks
---

# Notification Setup Guide

## When to Use This Skill

Activate this skill when you need to:
- Set up real-time order notifications for solopreneurs
- Configure Telegram bot for business alerts
- Implement webhook-based notification pipelines
- Create automated payment and lead alerts
- Design notification message templates
- Troubleshoot notification delivery issues

## Overview

This skill provides comprehensive guidance for implementing automated notification systems using Telegram as the primary channel. Designed for solopreneurs running digital product businesses, it covers bot setup, webhook integration, and message templating.

**Primary Channel**: Telegram (bot-based notifications)
**Approach**: Code/webhook-based automation
**Target Users**: Solopreneurs, small business owners, developers

## Quick Setup Workflow

```
1. Create Telegram Bot
   ├─ Use @BotFather to generate bot
   ├─ Obtain bot token
   └─ Configure bot settings

2. Prepare Notification Channel
   ├─ Create Telegram group/channel
   ├─ Add bot to group
   └─ Get chat ID

3. Implement Webhook Pipeline
   ├─ Set up webhook endpoint
   ├─ Parse payment gateway payloads
   ├─ Format notification messages
   └─ Send to Telegram API

4. Test Full Pipeline
   ├─ Send test transactions
   ├─ Verify message delivery
   └─ Monitor error logs
```

## Architecture Overview

```
┌─────────────────┐
│ Payment Gateway │ (SePay, Stripe, etc.)
└────────┬────────┘
         │ Webhook POST
         ▼
┌─────────────────┐
│  Your Server    │ (Node.js, PHP, Python)
│  - Parse payload│
│  - Format msg   │
│  - Error handle │
└────────┬────────┘
         │ HTTPS Request
         ▼
┌─────────────────┐
│ Telegram Bot API│
└────────┬────────┘
         │ Message
         ▼
┌─────────────────┐
│ Telegram Group  │ → Business owner gets instant alert
└─────────────────┘
```

## Reference Files

### 1. [Telegram Bot Notification Setup](references/telegram-bot-notification-setup.md)
Complete guide to creating and configuring Telegram bots:
- Step-by-step bot creation via @BotFather
- Token and chat ID acquisition
- API endpoint usage
- Security best practices
- Troubleshooting common issues

### 2. [Webhook to Notification Pipeline](references/webhook-to-notification-pipeline.md)
Implementation guide for webhook-based notifications:
- Architecture and data flow
- Node.js and PHP examples
- Error handling and retry logic
- Logging and monitoring
- Testing strategies

### 3. [Notification Message Templates](references/notification-message-templates.md)
Ready-to-use message templates for various scenarios:
- New order notifications
- Payment status updates
- Daily summaries
- Lead alerts
- Template variable reference
- Formatting guidelines

## Key Features

- **Real-time Alerts**: Instant notifications for critical business events
- **Multi-event Support**: Orders, payments, leads, refunds, alerts
- **Template Library**: Pre-formatted messages for common scenarios
- **Error Resilience**: Retry logic and fallback mechanisms
- **Security-focused**: Token protection and validation guidelines
- **Code Examples**: Ready-to-deploy implementations in popular languages

## Common Use Cases

1. **E-commerce Order Notifications**
   - New order placed
   - Payment confirmed
   - Payment failed/pending
   - Refund processed

2. **Lead Generation Alerts**
   - New email subscriber
   - Form submission
   - Trial signup
   - Contact request

3. **Business Intelligence**
   - Daily sales summary
   - Revenue milestones
   - Low stock alerts
   - Unusual activity detection

4. **System Monitoring**
   - API errors
   - Webhook failures
   - Server issues
   - Integration problems

## Implementation Tips

- **Start Simple**: Begin with basic order notifications, expand gradually
- **Test Thoroughly**: Use sandbox/test mode before production
- **Secure Tokens**: Never commit API tokens to version control
- **Monitor Delivery**: Log all notification attempts and failures
- **User Experience**: Keep messages concise and actionable
- **Fallback Plan**: Have alternative notification methods ready

## Prerequisites

- Telegram account
- Server with HTTPS support (for webhooks)
- Basic understanding of HTTP/REST APIs
- Programming knowledge (Node.js, PHP, or Python)
- Payment gateway with webhook support

## Getting Started

1. Read [Telegram Bot Notification Setup](references/telegram-bot-notification-setup.md)
2. Create your bot and test basic messaging
3. Review [Webhook to Notification Pipeline](references/webhook-to-notification-pipeline.md)
4. Implement webhook endpoint for your server
5. Use [Notification Message Templates](references/notification-message-templates.md)
6. Deploy and test end-to-end flow

## Support and Troubleshooting

Common issues and solutions are documented in each reference file. Focus on:
- Token and chat ID validation
- HTTPS/SSL certificate issues
- Webhook payload parsing
- Rate limiting (Telegram: 30 messages/second)
- Message formatting errors

## Zalo OA (Optional)

- Register Zalo Official Account at [oa.zalo.me](https://oa.zalo.me)
- Use Zalo OA API for automated notifications (send order alerts, lead alerts to followers)
- Best for: Customer communication in Vietnam (75M+ users)
- Requires: Business verification on Zalo platform
- API docs: [developers.zalo.me](https://developers.zalo.me)
- Notification flow: Same webhook pipeline as Telegram, replace Telegram API call with Zalo OA Send Message API

## Future Enhancements

- Multi-channel support (email, SMS, Zalo OA as fallbacks)
- Advanced analytics and reporting
- Custom notification rules and filters
- Integration with CRM systems
- A/B testing for message templates
