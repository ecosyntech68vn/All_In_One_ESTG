---
name: payment-setup-guide
description: Step-by-step guide for integrating payment gateways with focus on Vietnamese bank transfer automation
---

# Payment Setup Guide

## When to Use

Activate this skill when you need to:
- Integrate automated payment collection into your application
- Accept bank transfers without manual verification
- Set up QR code-based payment flows
- Handle webhook notifications for payment confirmation
- Build checkout pages optimized for Vietnamese customers
- Choose between payment gateway options

## Platform Comparison

### Automated Payment Gateway
**Best For:** Scaling businesses, automated operations
- ✅ Real-time payment notifications via webhooks
- ✅ Multi-bank support (40+ banks)
- ✅ QR code generation API
- ✅ Transaction history and reconciliation
- ❌ Service fees apply
- ❌ Business verification required

### Manual Bank Transfer
**Best For:** Starting MVPs, low volume
- ✅ Zero integration cost
- ✅ No technical setup needed
- ❌ Manual verification required
- ❌ Delayed order confirmation
- ❌ Poor customer experience at scale

### International Payment Processors
**Best For:** Global customers, card payments
- ✅ Credit/debit card support
- ✅ International reach
- ❌ Higher fees (2-4%)
- ❌ Currency conversion overhead
- ❌ Limited Vietnamese bank integration

## Quick Setup Workflow

1. **Account Registration** → Create sandbox account for testing
2. **API Credentials** → Generate authentication tokens
3. **Webhook Configuration** → Set up payment notification endpoint
4. **QR Code Integration** → Add dynamic QR generation
5. **Order Matching Logic** → Parse transaction content
6. **Testing** → Verify sandbox transactions
7. **Production Deployment** → Switch to live environment

## Key Capabilities

| Feature | Capability | Reference |
|---------|-----------|-----------|
| Payment Methods | Bank QR, Card, Virtual Account | Integration Guide |
| Bank Coverage | 40+ Vietnamese banks | Integration Guide |
| Response Time | Real-time via webhooks | Integration Guide |
| Authentication | API Token, OAuth2 | Integration Guide |
| Rate Limits | 2 calls/second | Integration Guide |
| Retry Mechanism | Auto-retry up to 7 times | Integration Guide |
| QR Generation | Dynamic URL-based | Checkout Flow Patterns |
| Order Matching | Content parsing with fallbacks | Checkout Flow Patterns |

## Implementation Checklist

### Phase 1: Setup
- [ ] Register for sandbox account
- [ ] Generate API authentication token
- [ ] Configure webhook endpoint URL
- [ ] Test webhook with mock payload
- [ ] Verify 200 response handling

### Phase 2: Integration
- [ ] Implement QR code generation
- [ ] Build checkout page UI
- [ ] Add order status polling
- [ ] Handle payment confirmation
- [ ] Test transaction matching logic

### Phase 3: Security
- [ ] Implement timing-safe auth validation
- [ ] Add duplicate transaction prevention
- [ ] Enable HTTPS for webhooks
- [ ] Set up error logging
- [ ] Configure retry limits

### Phase 4: Production
- [ ] Complete business verification
- [ ] Switch to production API endpoint
- [ ] Monitor webhook delivery rate
- [ ] Set up transaction reconciliation
- [ ] Configure customer support flows

## Reference Files

### [Payment Gateway Integration Guide](./references/payment-gateway-integration-guide.md)
Complete technical setup covering:
- Account creation and API configuration
- Webhook implementation with code examples
- Security best practices
- Testing and deployment procedures
- Troubleshooting common issues

### [Checkout Flow Design Patterns](./references/checkout-flow-design-patterns.md)
UX optimization guide covering:
- High-conversion checkout page design
- QR code presentation strategies
- Mobile-responsive layouts
- Payment confirmation patterns
- Error handling workflows

## Common Use Cases

**E-commerce Store**
- Customer selects products → Checkout → QR display → Bank scan → Auto-confirmation

**Subscription Service**
- Monthly billing → Generate unique QR → Track payment → Renew subscription

**Event Ticketing**
- Book tickets → Pay via QR → Instant confirmation → Send ticket

**Digital Product Sales**
- Purchase digital goods → QR payment → Auto-delivery after confirmation

## Integration Effort Estimate

- **Basic Setup:** 2-4 hours (webhook + QR display)
- **Full Checkout Flow:** 1-2 days (UI + matching logic + testing)
- **Production Hardening:** 1-2 days (security + monitoring + edge cases)

## Support Resources

- Sandbox environment for risk-free testing
- Webhook payload simulator
- Transaction history dashboard
- API documentation with examples
- Developer support channels

## Next Steps

1. Read **Payment Gateway Integration Guide** for technical setup
2. Review **Checkout Flow Design Patterns** for UX best practices
3. Start with sandbox environment
4. Build webhook handler first
5. Add checkout UI incrementally
6. Test thoroughly before production launch
