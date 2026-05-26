---
description: Generate revenue and order reports
argument-hint: [period]
---
Create revenue reports from order data.

<args>$ARGUMENTS</args>

## Periods
- `daily` - Today's orders and revenue
- `weekly` - This week's performance
- `monthly` - Monthly revenue report
- `custom [start] [end]` - Custom date range

## Input Methods

### Option 1: Manual (paste data)
Paste your SePay transaction data or Telegram bot order logs when prompted.
Agent will analyze: orders, revenue, AOV, conversion rate, trends.

### Option 2: Telegram Bot logs
If Deliver Agent's Telegram Bot is running, paste or forward order notification messages.
Agent parses: order ID, amount, product, customer, timestamp → auto-generates report.

### Option 3: Auto-collect (requires Apify MCP)
Scrape social metrics via Apify MCP to correlate content performance with sales data.

## Process
1. Activate Insights Agent
2. Collect data (manual paste from SePay/Telegram logs)
3. Use Revenue Report skill + KPI framework
4. Output: Revenue report with trends + weekly template

## Examples
- `/revenue weekly` — This week's orders, revenue, and average order value
- `/revenue monthly` — Full monthly report with growth trends and top products
- `/revenue custom 01/01-31/01` — Custom date range report for January

## Tips
- Pull data from SePay transaction history or Telegram bot order logs
- Compare revenue vs ad spend for true ROI — revenue alone is misleading
- Track per-product revenue separately to identify winners and cut losers
