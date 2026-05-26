# Revenue Tracking Workflow

## Data Collection Sources

### 1. Payment Gateway Dashboard (e.g., SePay)

**What to Export:**
- Transaction history (daily/weekly)
- Order details with timestamps
- Payment method breakdown
- Transaction status (success/failed/pending)
- Refund records

**Export Frequency:**
- Daily: During high-volume campaigns
- Weekly: Standard operating cadence
- Monthly: Complete reconciliation

**Export Format:**
- CSV or Excel preferred
- Ensure UTF-8 encoding for Vietnamese characters
- Include all available columns for flexibility

### 2. Notification System Logs (e.g., Telegram Bot)

**What to Capture:**
- Order confirmation messages
- Payment success alerts
- Failed transaction notifications
- Refund/cancellation alerts
- Customer inquiry timestamps

**Collection Method:**
- Copy-paste into tracking sheet weekly
- Screenshot backup for verification
- Archive messages monthly
- Tag messages with order IDs for cross-reference

### 3. Manual Tracking (Google Sheets)

**Primary Use Cases:**
- Offline/cash transactions
- Bundle sales not tracked automatically
- Custom product combinations
- Affiliate/partnership revenue
- One-off consulting or service fees

**Entry Timing:**
- Same-day entry for all transactions
- Weekly review for completeness
- Monthly audit for accuracy

## Google Sheet Template Structure

### Essential Columns

| Column Name | Data Type | Example | Purpose |
|-------------|-----------|---------|---------|
| Date | Date (DD/MM/YYYY) | 15/02/2026 | Transaction timestamp |
| Order ID | Text | SP-20260215-001 | Unique identifier |
| Product Name | Text | Digital Marketing Course | What was sold |
| Amount (VND) | Number | 599,000 | Transaction value |
| Payment Method | Dropdown | SePay / Bank / Cash | How customer paid |
| Status | Dropdown | Completed / Refunded / Pending | Current state |
| Customer Email | Text | customer@example.com | Buyer identification |
| Traffic Source | Dropdown | Facebook / Organic / Email | Where customer came from |
| Notes | Text | First-time buyer | Additional context |

### Recommended Dropdowns

**Payment Method:**
- SePay
- Bank Transfer
- Cash/COD
- Momo
- VNPay
- Other

**Status:**
- Completed
- Pending
- Refunded
- Cancelled
- Failed

**Traffic Source:**
- Facebook Ads
- Google Ads
- Organic Search
- Email Marketing
- Referral
- Direct
- TikTok
- Zalo
- Affiliate
- Unknown

### Auto-Calculation Formulas

**Total Revenue (All Time):**
```
=SUMIF(Status_Column, "Completed", Amount_Column)
```

**Order Count:**
```
=COUNTIF(Status_Column, "Completed")
```

**Average Order Value:**
```
=Total_Revenue / Order_Count
```

**Refund Rate:**
```
=(COUNTIF(Status_Column, "Refunded") / COUNTIF(Status_Column, "Completed")) * 100
```

**Revenue This Week:**
```
=SUMIFS(Amount_Column, Status_Column, "Completed", Date_Column, ">=Today()-7")
```

**Revenue by Product:**
```
=SUMIFS(Amount_Column, Product_Column, "Product Name", Status_Column, "Completed")
```

### Pivot Table Suggestions

**1. Revenue by Source:**
- Rows: Traffic Source
- Values: SUM of Amount, COUNT of Order ID
- Filters: Status = "Completed"

**2. Weekly Trend:**
- Rows: Week (group dates by 7 days)
- Values: SUM of Amount, COUNT of Order ID
- Chart: Line graph

**3. Product Performance:**
- Rows: Product Name
- Values: SUM of Amount, COUNT of Order ID, AVERAGE of Amount
- Sort: By revenue descending

**4. Payment Method Distribution:**
- Rows: Payment Method
- Values: COUNT of Order ID, SUM of Amount
- Chart: Pie chart

## Weekly Reporting Process

### Step 1: Data Collection (Monday 9-10 AM)

1. **Export Gateway Data**
   - Log into SePay dashboard
   - Filter transactions: Last 7 days
   - Export to CSV
   - Save with naming convention: `sepay-export-YYYYMMDD.csv`

2. **Review Notification Logs**
   - Open Telegram bot conversation
   - Copy all order notifications from past week
   - Paste into temporary doc for processing

3. **Check Manual Entries**
   - Open tracking Google Sheet
   - Verify all manual entries from past week
   - Ensure no duplicate entries

### Step 2: Data Consolidation (Monday 10-10:30 AM)

1. **Import Gateway Data**
   - Copy transactions from CSV
   - Paste into tracking sheet
   - Match column formats (dates, amounts)

2. **Cross-Reference Notifications**
   - Verify gateway transactions against Telegram alerts
   - Flag any discrepancies
   - Investigate missing transactions

3. **Validate Manual Entries**
   - Confirm all manual entries have Order IDs
   - Check status updates (pending → completed)
   - Add missing traffic sources

### Step 3: Calculate Key Metrics (Monday 10:30-11 AM)

1. **Revenue Summary**
   - Total revenue this week
   - Growth vs. last week (%)
   - Growth vs. same week last month (%)

2. **Order Summary**
   - Total orders this week
   - Average order value
   - Orders by day breakdown

3. **Performance Analysis**
   - Revenue by product
   - Revenue by traffic source
   - Top 5 products by revenue
   - Conversion rate (if traffic data available)

4. **Quality Metrics**
   - Refund count and rate
   - Failed transaction count
   - Average time to payment completion

### Step 4: Compare to Previous Period (Monday 11-11:15 AM)

1. **Week-over-Week Comparison**
   - Revenue: Current vs. Previous week
   - Orders: Current vs. Previous week
   - AOV: Current vs. Previous week
   - Top products: Changes in ranking

2. **Month-to-Date Tracking**
   - Current MTD revenue
   - Pace vs. last month
   - Projected month-end revenue

3. **Target Progress**
   - % of weekly target achieved
   - % of monthly target achieved
   - Days remaining to hit targets

### Step 5: Identify Trends (Monday 11:15-11:30 AM)

1. **Positive Patterns**
   - Products with increasing sales
   - High-performing traffic sources
   - Days with peak order volume
   - Successful pricing strategies

2. **Concerning Patterns**
   - Products with declining sales
   - Underperforming traffic sources
   - High refund rates on specific products
   - Failed transactions (payment issues?)

3. **Opportunities**
   - Upsell/cross-sell possibilities
   - Products to promote more
   - Traffic sources to scale
   - Customer segments to target

### Step 6: Generate Report (Monday 11:30-12 PM)

1. Use [Weekly Revenue Report Template](../templates/weekly-revenue-report-template.md)
2. Fill all sections with calculated data
3. Add 3-5 key insights
4. List 3-5 action items for next week
5. Review for accuracy and completeness

## Monthly Review Process

### Timing
First Monday of each month, 9 AM - 12 PM

### Components

1. **Full Month Reconciliation**
   - Verify all transactions recorded
   - Match gateway reports to tracking sheet
   - Resolve all discrepancies
   - Archive export files

2. **Comprehensive Metric Analysis**
   - All revenue and order metrics (see KPI Framework)
   - Profit margin calculation (revenue - costs)
   - Customer acquisition cost (ad spend / new customers)
   - LTV estimation (for repeat customers)

3. **Channel Deep Dive**
   - Revenue and orders by source
   - ROAS for each paid channel
   - Organic vs. paid performance
   - Affiliate/partnership contribution

4. **Product Portfolio Review**
   - Best and worst performers
   - Product profitability (if COGS tracked)
   - Bundle vs. individual sales
   - Seasonal trends identification

5. **Strategic Planning**
   - Set next month's revenue target
   - Identify products to promote/retire
   - Budget allocation for paid ads
   - Pricing adjustments needed

6. **Goal Setting**
   - Monthly revenue target
   - Weekly milestones
   - Target AOV
   - Target conversion rate

## Data Quality Checks

### Daily Checks (5 minutes)
- [ ] All completed orders recorded
- [ ] No duplicate Order IDs
- [ ] Payment status updated

### Weekly Checks (15 minutes)
- [ ] Gateway export matches tracking sheet
- [ ] All traffic sources assigned
- [ ] No missing customer emails
- [ ] Refunds properly recorded
- [ ] Amount format consistent (no extra zeros)

### Monthly Checks (30 minutes)
- [ ] Total revenue matches gateway dashboard
- [ ] Order count matches gateway records
- [ ] All products have correct pricing
- [ ] Status field cleaned up (no "pending" >30 days)
- [ ] Data exported to backup file
- [ ] Previous month archived

## Common Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| Revenue mismatch | Duplicate entries | Use UNIQUE() function or remove duplicates manually |
| Missing orders | Manual entry forgotten | Set daily reminder, cross-check notifications |
| Wrong amounts | Extra zeros (VND confusion) | Data validation rule: must be 5-9 digits |
| Unknown traffic source | Not tracked at purchase | Default to "Direct", improve tracking going forward |
| Pending status stuck | Forgot to update | Weekly status audit, auto-flag >7 days pending |
| Refund not recorded | No notification received | Check gateway weekly for refund reports |

## Automation Opportunities

1. **Gateway Integration**: Use API to auto-import transactions (if available)
2. **Notification Parsing**: Bot that reads Telegram and updates sheet
3. **Alert System**: Email/Telegram alert when daily revenue drops >20%
4. **Dashboard**: Google Data Studio pulling from sheet for real-time view
5. **Backup**: Daily auto-export to Google Drive

## Tools & Resources

- **Google Sheets**: Primary tracking tool
- **SePay Dashboard**: Transaction source
- **Telegram Bot**: Real-time notifications
- **Google Data Studio**: Optional visualization
- **Notion**: Alternative for report storage
- **Excel**: For complex analysis if needed
