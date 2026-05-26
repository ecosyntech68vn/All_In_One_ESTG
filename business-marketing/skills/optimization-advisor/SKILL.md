---
name: optimization-advisor
description: Data-driven business optimization with actionable recommendations and bottleneck diagnosis
---

# Optimization Advisor

## Purpose

Helps solopreneurs identify business bottlenecks and implement data-driven improvements through simple diagnostics and actionable optimization plays.

## When to Use

- Revenue plateaued or declining
- Traffic grows but sales don't
- Need to improve specific metrics
- Planning monthly optimization efforts
- Reviewing A/B test results
- Prioritizing improvement opportunities

## Core Methodology

### 1. Diagnose Stage
- Identify where customers drop off
- Measure performance against benchmarks
- Calculate impact potential
- Classify issue severity

### 2. Prioritize Action
- Rank by Impact Score = Drop-off Rate × Fix Potential × (1/Effort)
- Focus high-impact, low-effort wins first
- Balance quick wins with strategic fixes

### 3. Implement Play
- Select optimization play from playbook
- Test single variable at a time
- Measure before/after performance
- Document results and learnings

### 4. Validate Results
- Check statistical significance
- Compare to baseline metrics
- Decide: Implement, Revert, or Continue Testing

## Quick Diagnosis Workflow

```
Input: Business metrics and KPIs
↓
Analyze funnel stages (Awareness → Traffic → Conversion → Retention)
↓
Identify bottleneck with lowest performance
↓
Apply diagnostic framework
↓
Generate "If → Then" recommendations
↓
Output: Prioritized action list with optimization plays
```

## Reference Files

- **[bottleneck-diagnosis-framework.md](references/bottleneck-diagnosis-framework.md)**: Stage-by-stage diagnosis with decision trees and red flag indicators
- **[optimization-playbook.md](references/optimization-playbook.md)**: 20+ actionable optimization plays with A/B testing guide

## Input Format

Provide current metrics:
- Funnel stage data (impressions, clicks, conversions, retention)
- Conversion rates at each stage
- Revenue and transaction metrics
- Time period for data
- Any known issues or concerns

## Output Format

### Bottleneck Analysis
- Stage with lowest performance
- Gap vs benchmark
- Estimated impact of fixing

### Priority Recommendations
1. **High Priority** (High Impact, Low Effort)
   - Specific issue identified
   - Recommended optimization play
   - Expected improvement range
   - Implementation steps

2. **Medium Priority** (Strategic Fixes)
   - Issue description
   - Recommended approach
   - Resource requirements

3. **Monitor** (Low Priority)
   - Areas to watch
   - Trigger thresholds

### Next Steps
- Immediate actions (this week)
- Short-term optimizations (this month)
- Long-term strategic initiatives

## Example Usage

**Input:**
```
Awareness: 10,000 impressions
Traffic: 150 clicks (1.5% CTR)
Landing page visits: 150
Conversions: 3 (2% conversion rate)
Revenue: $297
Time period: Last 30 days
```

**Output:**
```
BOTTLENECK: Traffic Stage (Low CTR)
- Current CTR: 1.5%
- Benchmark: 2-3%
- Impact: 33-50% more visitors if fixed

HIGH PRIORITY RECOMMENDATIONS:

1. Test Headline Variations (Play: Headline A/B Testing)
   - Current headline likely weak
   - Expected improvement: +30-80% CTR
   - Effort: Low (2 hours)
   - Action: Create 3 headline variants, test for 7 days

2. Improve Call-to-Action Clarity (Play: CTA Optimization)
   - Make benefit clearer in link text
   - Expected improvement: +20-40% CTR
   - Effort: Low (1 hour)
   - Action: Rewrite CTA with specific benefit

NEXT STEPS:
- This week: Implement headline A/B test
- Monitor: Landing page conversion rate (currently good at 2%)
```

## Key Principles

- **One Variable at a Time**: Never test multiple changes simultaneously
- **Sufficient Sample Size**: Minimum 100 conversions per variant
- **Measure Significance**: Don't declare winner prematurely
- **Document Everything**: Track tests, results, and learnings
- **Focus on Impact**: Prioritize biggest levers first

## Success Metrics

- Conversion rate improvements
- Revenue increases
- Reduced drop-off rates
- Faster optimization cycles
- More winning tests
