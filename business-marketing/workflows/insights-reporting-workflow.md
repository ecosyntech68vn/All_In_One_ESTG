# Insights & Reporting Workflow

Step-by-step: Collect data → Analyze performance → Get optimization recommendations

## Overview
| Field | Value |
|-------|-------|
| Agent | Insights Agent |
| Skills Used | Social Analytics, Revenue Report, Optimization Advisor |
| Duration | Weekly recurring (1-2 hours/week) |
| Output | Performance report + action items |

## Data Sources
- **Social**: Facebook Insights, Instagram Insights, TikTok Analytics, YouTube Studio
- **Revenue**: SePay dashboard, Telegram bot order logs
- **Approach**: No API integration needed — user paste data approach

## Workflow Steps (Weekly Cadence)

### Step 1: Data Collection (30 minutes)
- Screenshot/export social platform insights (7-day window)
- Export SePay transaction history
- Paste data into Insights Agent using data input templates
- Output: Raw data ready for analysis

#### Actions:
1. **Facebook Data** (5 minutes):
   - Go to Facebook Page → Insights → Overview
   - Set date range: Last 7 days
   - Screenshot or note down:
     - Page views
     - Post reach
     - Post engagement (likes, comments, shares)
     - Follower growth
   - Export to CSV (if available)

2. **Instagram Data** (5 minutes):
   - Go to Instagram Profile → Insights → Overview
   - Set date range: Last 7 days
   - Screenshot or note down:
     - Accounts reached
     - Content interactions
     - Profile visits
     - Follower growth
   - Export to CSV (if available via Creator/Business account)

3. **TikTok Data** (5 minutes):
   - Go to TikTok Profile → Creator Tools → Analytics
   - Set date range: Last 7 days
   - Screenshot or note down:
     - Video views
     - Followers gained
     - Profile views
     - Engagement rate (likes, comments, shares)
   - Export to CSV (if available)

4. **YouTube Data** (5 minutes):
   - Go to YouTube Studio → Analytics → Overview
   - Set date range: Last 7 days
   - Screenshot or note down:
     - Views
     - Watch time
     - Subscribers gained
     - Engagement (likes, comments)
   - Export to CSV

5. **SePay Revenue Data** (5 minutes):
   - Go to SePay Dashboard → Transactions
   - Set date range: Last 7 days
   - Export transaction history (CSV)
   - Note down:
     - Total orders
     - Total revenue
     - Average order value (AOV)

6. **Telegram Order Logs** (5 minutes):
   - Review Telegram bot notifications from past 7 days
   - Count orders manually or export chat history
   - Cross-reference with SePay data

7. **Organize data**:
   - Create Google Sheet or spreadsheet
   - Paste all metrics into standardized template
   - Label columns: Date, Metric Name, Value, Platform

#### Deliverable:
- Data collection spreadsheet with 7-day metrics from all platforms
- Screenshots or CSV exports as backup
- Data ready to paste into Insights Agent prompts

---

### Step 2: Social Analytics (30 minutes)
- Use Social Analytics skill: KPI framework
- Agent analyzes: reach, engagement rate, CTR, saves, shares
- Compare vs previous week
- Identify top/bottom performing content
- Output: Social performance summary

#### Actions:
1. Paste data into Insights Agent prompt:
   ```
   Analyze my social media performance for the past 7 days:

   FACEBOOK:
   - Page views: [X]
   - Post reach: [X]
   - Engagement: [X]
   - Follower growth: [X]

   INSTAGRAM:
   - Accounts reached: [X]
   - Content interactions: [X]
   - Profile visits: [X]
   - Follower growth: [X]

   TIKTOK:
   - Video views: [X]
   - Engagement rate: [X]%
   - Followers gained: [X]

   YOUTUBE:
   - Views: [X]
   - Watch time: [X] hours
   - Subscribers gained: [X]

   Compare vs last week and identify trends.
   ```

2. Agent calculates KPIs:
   - Engagement rate: (Likes + Comments + Shares) / Reach × 100
   - CTR: Link clicks / Reach × 100
   - Growth rate: New followers / Total followers × 100

3. Agent identifies:
   - Top 3 performing posts (highest engagement)
   - Bottom 3 performing posts (lowest engagement)
   - Platform with highest growth
   - Platform needing improvement

4. Agent compares week-over-week:
   - Reach: +/- X%
   - Engagement: +/- X%
   - Follower growth: +/- X%

#### Deliverable:
- Social analytics summary report with:
  - KPI dashboard (reach, engagement, growth per platform)
  - Week-over-week comparison
  - Top/bottom performing content
  - Platform performance ranking

---

### Step 3: Revenue Report (20 minutes)
- Use Revenue Report skill: KPI framework
- Agent analyzes: orders, revenue, AOV, conversion rate
- Track trends week-over-week
- Output: Weekly revenue report

#### Actions:
1. Paste revenue data into Insights Agent prompt:
   ```
   Analyze my revenue performance for the past 7 days:

   SEPAY DATA:
   - Total orders: [X]
   - Total revenue: [X] VND
   - Average order value (AOV): [X] VND

   TRAFFIC DATA (if available):
   - Sales page views: [X]
   - Landing page views: [X]

   Calculate conversion rate and compare vs last week.
   ```

2. Agent calculates KPIs:
   - Conversion rate: Orders / Sales page views × 100
   - AOV: Total revenue / Total orders
   - Revenue per visitor: Total revenue / Sales page views
   - Growth rate: (This week revenue - Last week revenue) / Last week revenue × 100

3. Agent tracks trends:
   - Revenue trend: +/- X% vs last week
   - Order volume trend: +/- X% vs last week
   - AOV trend: +/- X% vs last week

4. Agent flags issues:
   - Declining orders (investigate traffic or conversion)
   - Declining AOV (upsell opportunity)
   - Low conversion rate (optimize sales page)

#### Deliverable:
- Weekly revenue report with:
  - Revenue KPI dashboard (orders, revenue, AOV, conversion rate)
  - Week-over-week trends
  - Growth rate analysis
  - Flagged issues requiring attention

---

### Step 4: Optimization Recommendations (20 minutes)
- Use Optimization Advisor skill: IF-THEN playbook
- Agent diagnoses issues from data
- Provides 3-5 prioritized action items
- Output: Actionable optimization list

#### Actions:
1. Paste combined data into Insights Agent prompt:
   ```
   Based on my social and revenue data, provide optimization recommendations:

   SOCIAL ISSUES:
   - [List any declining metrics or underperforming platforms]

   REVENUE ISSUES:
   - [List any declining metrics or low conversion rates]

   Use IF-THEN playbook to diagnose and recommend actions.
   ```

2. Agent applies diagnostic playbook:
   - **IF** reach declining **THEN** increase posting frequency or improve content hooks
   - **IF** engagement declining **THEN** test different content formats (video vs image)
   - **IF** conversion rate < 2% **THEN** optimize sales page copy or offer
   - **IF** AOV stagnant **THEN** add upsells or bundle offers
   - **IF** follower growth stagnant **THEN** run engagement campaigns or collab with others

3. Agent prioritizes recommendations (Impact × Effort matrix):
   - Quick wins: High impact, low effort (do first)
   - Major projects: High impact, high effort (plan next)
   - Fill-ins: Low impact, low effort (do if time)
   - Time wasters: Low impact, high effort (avoid)

4. Agent outputs 3-5 action items with:
   - Action description
   - Expected impact (e.g., +10% reach, +2% conversion)
   - Effort required (hours or days)
   - Priority (High/Medium/Low)

#### Deliverable:
- Optimization recommendations report with:
  - Diagnosed issues
  - 3-5 prioritized action items
  - Expected impact and effort for each
  - IF-THEN reasoning for each recommendation

---

### Step 5: Action Planning (20 minutes)
- Review recommendations
- Pick top 2-3 actions to implement this week
- Update content/funnel/offer based on insights
- Output: This week's optimization tasks

#### Actions:
1. Review all recommendations from agent
2. Select 2-3 highest priority actions to implement this week
3. Break down each action into specific tasks:
   - Example: "Increase posting frequency"
     - Task 1: Batch-create 3 extra posts
     - Task 2: Schedule posts for Mon, Wed, Fri
     - Task 3: Monitor engagement daily
4. Schedule tasks in calendar or to-do list
5. Assign owners (if working with team)
6. Set success metrics for each action (how to measure if it worked)
7. Plan next week's data collection (repeat this workflow)

#### Deliverable:
- This week's action plan with:
  - 2-3 selected optimizations
  - Specific tasks for each
  - Scheduled completion dates
  - Success metrics to track

---

## Weekly Report Template

Use this template to document findings each week:

```markdown
# Weekly Performance Report
**Date Range**: [Start Date] - [End Date]
**Week Number**: [X]

---

## 1. Social Media Performance

### Facebook
- Page views: [X] (+/- X% vs last week)
- Post reach: [X] (+/- X% vs last week)
- Engagement: [X] (+/- X% vs last week)
- Follower growth: [X] (+/- X% vs last week)

### Instagram
- Accounts reached: [X] (+/- X% vs last week)
- Content interactions: [X] (+/- X% vs last week)
- Profile visits: [X] (+/- X% vs last week)
- Follower growth: [X] (+/- X% vs last week)

### TikTok
- Video views: [X] (+/- X% vs last week)
- Engagement rate: [X]% (+/- X% vs last week)
- Followers gained: [X] (+/- X% vs last week)

### YouTube
- Views: [X] (+/- X% vs last week)
- Watch time: [X] hours (+/- X% vs last week)
- Subscribers gained: [X] (+/- X% vs last week)

### Top Performing Content
1. [Post title/link] - [Metric: X engagement]
2. [Post title/link] - [Metric: X engagement]
3. [Post title/link] - [Metric: X engagement]

### Bottom Performing Content
1. [Post title/link] - [Metric: X engagement]
2. [Post title/link] - [Metric: X engagement]

---

## 2. Revenue Performance

- Total orders: [X] (+/- X% vs last week)
- Total revenue: [X] VND (+/- X% vs last week)
- Average order value (AOV): [X] VND (+/- X% vs last week)
- Conversion rate: [X]% (+/- X% vs last week)
- Revenue per visitor: [X] VND

---

## 3. Key Insights

### Top 3 Wins
1. [Win description and impact]
2. [Win description and impact]
3. [Win description and impact]

### Top 3 Concerns
1. [Concern description and data]
2. [Concern description and data]
3. [Concern description and data]

---

## 4. Optimization Recommendations

### Priority 1: [Action]
- Issue: [Describe the problem]
- Recommendation: [What to do]
- Expected impact: [Metric improvement]
- Effort: [Hours/days]

### Priority 2: [Action]
- Issue: [Describe the problem]
- Recommendation: [What to do]
- Expected impact: [Metric improvement]
- Effort: [Hours/days]

### Priority 3: [Action]
- Issue: [Describe the problem]
- Recommendation: [What to do]
- Expected impact: [Metric improvement]
- Effort: [Hours/days]

---

## 5. Action Items for Next Week

- [ ] [Task 1 with deadline]
- [ ] [Task 2 with deadline]
- [ ] [Task 3 with deadline]

---

## Notes
[Any additional observations, customer feedback, or external factors affecting performance]
```

---

## Success Criteria
- Weekly report generated consistently (every Monday or set day)
- Trends tracked over time (compare weekly, monthly, quarterly)
- At least 2 optimizations implemented per week
- Performance improvements visible within 2-4 weeks

## Next Steps
After completing this workflow:
1. Implement 2-3 optimization actions
2. Monitor results throughout the week
3. Repeat this workflow next week
4. Track long-term trends (4+ weeks of data)

## Tips for Vietnamese Solopreneurs
- Schedule data collection on Mondays (start week with insights)
- Use Vietnamese in reports if sharing with team/partners
- Track local holidays and events (explain performance spikes/drops)
- Compare performance during Vietnamese shopping seasons (Tet, Black Friday VN, etc.)
- Use VND for all revenue reporting (don't mix currencies)

## Common Mistakes to Avoid
- Skipping weekly data collection (inconsistent tracking = no trends)
- Collecting data but not analyzing (insights require interpretation)
- Analyzing but not taking action (data without action = wasted effort)
- Changing too many things at once (can't isolate what worked)
- Expecting overnight results (optimization takes 2-4 weeks to show impact)
- Not documenting actions taken (can't learn from past experiments)

## Advanced Optimization Tactics

### A/B Testing Framework
- Test one variable at a time (headline, image, CTA, etc.)
- Run test for minimum 7 days or 100 visitors
- Track winning variation and implement permanently

### Content Optimization
- Double down on top-performing content formats (more of what works)
- Retire or remix bottom-performing content
- Test posting times (morning vs evening, weekday vs weekend)

### Conversion Optimization
- Improve sales page sections with highest drop-off
- Add social proof from recent customers
- Test guarantee terms (7-day vs 30-day)

### Revenue Optimization
- Introduce upsells or downsells (increase AOV)
- Create bundle offers (move more products per order)
- Run limited-time promotions (drive urgency)

## Data Interpretation Guide

### Social Media Benchmarks (Vietnamese Market)
- Facebook engagement rate: 1-3% is average, 5%+ is excellent
- Instagram engagement rate: 3-6% is average, 10%+ is excellent
- TikTok engagement rate: 5-10% is average, 15%+ is excellent
- YouTube CTR: 3-5% is average, 8%+ is excellent

### Conversion Rate Benchmarks
- Landing page (lead magnet): 20-40% is average, 50%+ is excellent
- Sales page (direct sale): 1-3% is average, 5%+ is excellent
- Email click-through rate: 2-5% is average, 10%+ is excellent

### Revenue Growth Benchmarks
- Week-over-week growth: 5-10% is healthy, 20%+ is explosive
- Month-over-month growth: 15-25% is healthy, 50%+ is explosive

---

## Troubleshooting

### Issue: Low Social Reach
- Increase posting frequency
- Use trending hashtags (check TikTok VN trends)
- Post during peak hours (7-9am, 12-1pm, 7-9pm VN time)
- Collaborate with other creators (cross-promote)

### Issue: Low Engagement
- Improve content hooks (first 3 seconds of video, first line of caption)
- Ask questions in captions (encourage comments)
- Use interactive formats (polls, quizzes, Q&A)
- Respond to all comments quickly

### Issue: Low Conversion Rate
- Simplify sales page (remove friction)
- Strengthen guarantee (reduce perceived risk)
- Add more social proof (testimonials, results)
- Test different pricing (lower price point or payment plan)

### Issue: Declining Revenue
- Check traffic sources (is traffic down?)
- Review sales page (is copy still relevant?)
- Survey customers (ask what they want next)
- Launch re-engagement campaign (win back old leads)

---

## Long-Term Tracking (Monthly/Quarterly)

### Monthly Review (First Monday of Month)
- Aggregate 4 weekly reports
- Calculate monthly totals and averages
- Identify trends over 4 weeks
- Set goals for next month

### Quarterly Review (Every 3 Months)
- Analyze 12 weekly reports
- Measure progress toward annual goals
- Adjust strategy based on 3-month trends
- Plan next quarter's priorities

### Annual Review (End of Year)
- Review all 52 weekly reports
- Celebrate wins and milestones
- Document lessons learned
- Set goals for next year
