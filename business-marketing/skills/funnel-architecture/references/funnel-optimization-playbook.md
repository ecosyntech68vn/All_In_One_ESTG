# Funnel Optimization Playbook

Diagnostic framework for identifying and fixing conversion bottlenecks across all funnel stages.

---

## Optimization Philosophy

**Fix the bottom first.** Always optimize conversion (BOFU) before driving more traffic (TOFU). A 2x improvement in sales page conversion is worth more than 2x traffic with a leaky funnel.

**Priority order:** Checkout → Sales Page → Email Sequence → Lead Magnet → Traffic

---

## Diagnostic Framework: 4-Step Process

### Step 1: Measure Stage-by-Stage

Map conversion rates at each transition:

```
Traffic → Landing Page:     ___% (target: 30-50% from ads, 2-5% organic)
Landing Page → Opt-in:      ___% (target: 20-40%)
Opt-in → Email Open:        ___% (target: 20-35%)
Email → Sales Page Click:   ___% (target: 2-8%)
Sales Page → Checkout:      ___% (target: 3-8% warm, 0.5-2% cold)
Checkout → Purchase:        ___% (target: 60-80%)
```

### Step 2: Identify the Weakest Link

The stage with the biggest gap between actual and target = fix first.

### Step 3: Apply Fixes (see problem library below)

### Step 4: Test → Measure → Repeat

One change at a time. Wait for 100+ data points before concluding.

---

## 15 Common Funnel Problems & Solutions

### TOFU Problems (Traffic → Lead)

**Problem 1: Low traffic volume**
- Symptoms: < 100 visitors/week
- Causes: No content strategy, wrong platforms, inconsistent posting
- Fixes: Pick 1 platform, post daily for 30 days, use trending formats
- Priority: HIGH if no traffic at all

**Problem 2: High traffic, low engagement**
- Symptoms: Views but no clicks, likes, or comments
- Causes: Weak hooks, wrong audience, generic content
- Fixes: Test 5 different hook styles, narrow target audience, add CTAs
- Priority: MEDIUM

**Problem 3: Wrong traffic source**
- Symptoms: Traffic doesn't match buyer profile
- Causes: Platform mismatch, broad targeting, vanity metrics
- Fixes: Analyze buyer demographics, shift to where buyers spend time
- Priority: HIGH

### MOFU Problems (Lead → Engaged Lead)

**Problem 4: Low opt-in rate (< 15%)**
- Symptoms: Visitors see landing page but don't subscribe
- Causes: Weak headline, unclear value, too many form fields
- Fixes: A/B test headlines, reduce to name+email only, add social proof
- Priority: HIGH

**Problem 5: Lead magnet downloaded but not consumed**
- Symptoms: Downloads high, email engagement low
- Causes: Lead magnet too long, not actionable, poor design
- Fixes: Shorten to 1-2 pages, add quick-win first page, improve design
- Priority: MEDIUM

**Problem 6: Low email open rates (< 15%)**
- Symptoms: Emails sent but not opened
- Causes: Boring subject lines, wrong send time, deliverability issues
- Fixes: Test subject lines (curiosity, numbers, questions), check spam score
- Priority: HIGH

**Problem 7: Low email click rates (< 2%)**
- Symptoms: Emails opened but no clicks
- Causes: Weak CTA, too many links, content not compelling
- Fixes: Single CTA per email, P.S. line with link, value before ask
- Priority: MEDIUM

**Problem 8: High unsubscribe rate (> 2%)**
- Symptoms: List shrinking faster than growing
- Causes: Too frequent, too salesy, irrelevant content
- Fixes: Reduce frequency, 80/20 value-to-pitch ratio, segment list
- Priority: HIGH

### BOFU Problems (Lead → Customer)

**Problem 9: Sales page bounce (> 80%)**
- Symptoms: Visitors leave sales page quickly
- Causes: Slow load, weak headline, price shock, wrong audience
- Fixes: Speed optimization, stronger hero section, add price anchor first
- Priority: HIGH

**Problem 10: Sales page read but no checkout (< 1%)**
- Symptoms: Time on page OK but no add-to-cart
- Causes: Unclear offer, weak guarantee, missing social proof
- Fixes: Simplify offer stack, strengthen guarantee, add testimonials near CTA
- Priority: HIGH

**Problem 11: Cart abandonment (> 40%)**
- Symptoms: Checkout started but not completed
- Causes: Surprise costs, complicated checkout, no trust signals
- Fixes: Show total upfront, simplify to 1-step checkout, add security badges
- Priority: HIGH

**Problem 12: High refund rate (> 10%)**
- Symptoms: Buyers requesting refunds
- Causes: Overpromised, poor onboarding, buyer's remorse
- Fixes: Align expectations, improve first 24hr experience, add welcome sequence
- Priority: MEDIUM

### Cross-Funnel Problems

**Problem 13: Long time-to-purchase (> 30 days)**
- Symptoms: Leads go cold before buying
- Causes: Too many funnel steps, weak urgency, nurture too long
- Fixes: Reduce steps, add deadline/scarcity, shorten email sequence
- Priority: MEDIUM

**Problem 14: Low customer lifetime value**
- Symptoms: One-time buyers, no repeat purchases
- Causes: No upsell path, poor post-purchase experience, no retention
- Fixes: Add upsell/cross-sell, post-purchase email series, loyalty program
- Priority: MEDIUM

**Problem 15: Funnel works but doesn't scale**
- Symptoms: Good conversion at low volume, drops at scale
- Causes: Audience exhaustion, manual bottlenecks, platform dependency
- Fixes: Diversify traffic, automate manual steps, build email-first strategy
- Priority: LOW (fix after profitability proven)

---

## Testing Priority Matrix

| Test | Impact | Effort | Priority |
|------|--------|--------|----------|
| Sales page headline | HIGH | LOW | Do first |
| CTA button text/color | MEDIUM | LOW | Do first |
| Email subject lines | HIGH | LOW | Do first |
| Lead magnet title | HIGH | LOW | Do first |
| Price point | HIGH | MEDIUM | Test early |
| Guarantee wording | HIGH | LOW | Test early |
| Landing page layout | MEDIUM | MEDIUM | Test second |
| Email sequence length | MEDIUM | MEDIUM | Test second |
| Content format (video vs text) | MEDIUM | HIGH | Test later |
| Complete funnel restructure | HIGH | HIGH | Only if broken |

---

## Funnel Health Scorecard

Rate each metric 1-5 (1 = critical, 5 = excellent):

```markdown
## Funnel Health: [Business Name]
## Date: [YYYY-MM-DD]

### Traffic (TOFU)
- [ ] Consistent traffic volume:        _/5
- [ ] Right audience quality:            _/5
- [ ] Multiple traffic sources:          _/5

### Lead Capture (MOFU)
- [ ] Opt-in rate meets benchmark:       _/5
- [ ] Lead magnet gets consumed:         _/5
- [ ] Email deliverability healthy:      _/5

### Nurture (MOFU→BOFU)
- [ ] Email open rates healthy:          _/5
- [ ] Click rates meeting targets:       _/5
- [ ] Unsubscribe rate acceptable:       _/5

### Conversion (BOFU)
- [ ] Sales page converts:               _/5
- [ ] Checkout completion rate:          _/5
- [ ] Refund rate acceptable:            _/5

### Overall
- [ ] Time-to-purchase reasonable:       _/5
- [ ] Customer LTV growing:             _/5
- [ ] Funnel scales with traffic:        _/5

**Total Score:** ___/75
- 60-75: Healthy funnel, optimize edges
- 40-59: Needs targeted fixes (use problem library)
- 20-39: Significant issues, prioritize bottom-up
- < 20: Consider funnel redesign
```

---

## Vietnamese Market Optimization Notes

- **Payment friction:** Offer bank transfer + VietQR alongside card payments
- **Mobile-first:** 95%+ traffic is mobile — test everything on phone
- **Zalo integration:** Add Zalo OA follow as secondary capture alongside email
- **Trust signals:** Vietnamese buyers trust personal recommendations — add Zalo/FB group testimonials
- **Price display:** Show VND with charm pricing (X99K), installment options for items > 500K
