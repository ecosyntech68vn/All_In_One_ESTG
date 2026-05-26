---
description: Get optimization recommendations based on data
argument-hint: [area]
---
Diagnose issues and get actionable optimization advice.

<args>$ARGUMENTS</args>

## Areas
- `traffic` - Traffic and reach optimization
- `conversion` - Conversion rate optimization
- `revenue` - Revenue and AOV optimization
- `content` - Content performance optimization
- `full` - Full diagnostic across all areas

## Input Methods

### Option 1: Manual (paste data)
Provide metrics from platform insights, SePay logs, or analytics dashboards.

### Option 2: Auto-scrape (requires Apify MCP)
Provide social profile URLs — agent scrapes current metrics via Apify MCP, then diagnoses bottlenecks automatically.

## Process
1. Activate Insights Agent
2. Collect data (manual paste OR Apify MCP scrape)
3. Use Optimization Advisor skill + bottleneck diagnosis framework
4. Apply IF-THEN diagnostic playbook
5. Output: Prioritized action items with expected impact

## Examples
- `/optimize funnel` — Diagnose drop-off points across your entire sales funnel
- `/optimize content https://instagram.com/mybrand` — Scrape + identify top/bottom content
- `/optimize full` — Full diagnostic across traffic, conversion, revenue, and content

## Tips
- Fix the biggest bottleneck first — the step with the highest drop-off rate
- If Apify MCP is configured, provide profile URLs for automated data collection
- Test one change at a time so you know what actually moved the needle
- Wait at least 7 days before evaluating optimization impact — short windows are noisy
