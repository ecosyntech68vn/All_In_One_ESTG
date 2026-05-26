---
name: revenue-report
description: Revenue and order tracking, analysis, and reporting for solopreneur businesses
---

# Revenue Report Skill

## Overview

This skill enables solopreneurs to track, analyze, and report on revenue performance with actionable insights. Designed for businesses using payment gateways like SePay, manual tracking systems, or notification-based data collection.

## When to Use

- **Daily**: Quick revenue checks, order monitoring, payment gateway reconciliation
- **Weekly**: Performance analysis, trend identification, action planning
- **Monthly**: Comprehensive review, strategic planning, forecasting
- **Ad-hoc**: Campaign performance evaluation, product launch tracking, troubleshooting issues

## Key Capabilities

### Data Collection
- Aggregate revenue from multiple sources (payment gateways, manual logs, notifications)
- Reconcile discrepancies between tracking systems
- Validate data quality and completeness
- Export structured datasets for analysis

### Revenue Analysis
- Calculate core metrics: total revenue, order count, average order value (AOV)
- Track growth rates period-over-period
- Analyze revenue by product, channel, and time period
- Identify conversion bottlenecks and optimization opportunities

### Performance Reporting
- Generate weekly/monthly revenue reports with visualizations
- Compare actual vs. target performance
- Highlight trends, patterns, and anomalies
- Provide prioritized recommendations

### Forecasting
- Project monthly/quarterly revenue based on current trends
- Calculate runway and break-even points
- Model impact of pricing or marketing changes

## Data Sources

### Primary Sources
1. **Payment Gateway Dashboard** (e.g., SePay)
   - Transaction exports (CSV/Excel)
   - Real-time order data
   - Payment status tracking

2. **Telegram Bot Order Logs**
   - Order confirmation messages (parse: amount, product, customer, date)
   - Payment success/failure alerts
   - Refund notifications
   - Daily summary messages (if configured by Deliver Agent)
   - **Parsing format**: Match the notification template from `skills/notification-setup-guide/`
   ```
   Expected fields per message:
   - Order ID / Transaction ID
   - Amount (VND)
   - Product name
   - Customer name
   - Payment method / Bank
   - Status (confirmed/pending/failed)
   - Timestamp
   ```

3. **Manual Tracking** (Google Sheets)
   - Supplementary order details
   - Custom categorization
   - Offline transaction records

### Data Collection Best Practices
- Export gateway data weekly minimum
- Archive notification logs monthly
- Maintain consistent manual entry format
- Verify data completeness before analysis

## Reporting Cadence

### Daily Monitoring
- Check order count and revenue totals
- Review payment success/failure rates
- Monitor refund requests

### Weekly Reporting
- Analyze 7-day performance trends
- Compare week-over-week growth
- Identify top-performing products
- Generate actionable insights
- Plan adjustments for upcoming week

### Monthly Review
- Full funnel analysis (traffic → conversion → revenue)
- Profit margin calculation
- Channel performance comparison
- Strategic planning and goal-setting

## References

- **[Revenue KPI Framework](references/revenue-kpi-framework.md)**: Complete metric definitions, formulas, and benchmarks
- **[Revenue Tracking Workflow](references/revenue-tracking-workflow.md)**: Step-by-step data collection and analysis process

## Templates

- **[Weekly Revenue Report Template](templates/weekly-revenue-report-template.md)**: Ready-to-use report structure with sections for all key metrics

## Vietnamese Market Context

This skill incorporates considerations for Vietnamese solopreneur businesses:
- VND pricing psychology and common price points
- Local payment gateway integrations (SePay, VNPay, Momo)
- Typical conversion benchmarks for Vietnamese e-commerce
- Seasonal revenue patterns and shopping behaviors

## Integration with Other Skills

- **Marketing Performance**: Connect revenue to ad spend and campaign effectiveness
- **Customer Insights**: Link revenue trends to customer behavior patterns
- **Business Intelligence**: Feed revenue data into broader business dashboards

## Output Formats

- Markdown reports with tables and charts
- Mermaid diagrams for trend visualization
- CSV exports for further analysis
- Executive summaries for quick decision-making

## Success Metrics

This skill helps you maintain:
- ≤ 2 hours per week on revenue reporting
- < 5% data discrepancy rate across sources
- Weekly actionable insights for business improvement
- Accurate monthly revenue forecasting (±10%)
