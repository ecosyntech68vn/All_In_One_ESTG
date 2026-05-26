---
description: Analyze social media performance
argument-hint: [platform]
---
Analyze social media insights and performance.

<args>$ARGUMENTS</args>

## Platforms
- `facebook` / `fb` - Facebook Page insights
- `instagram` / `ig` - Instagram insights
- `tiktok` - TikTok analytics
- `youtube` / `yt` - YouTube Studio analytics
- `all` - Cross-platform summary

## Input Methods

### Option 1: Manual (paste data)
Paste your platform insights data when prompted. Agent will analyze:
- Reach, impressions, engagement rate
- Top/bottom performing content
- Audience growth trends
- Week-over-week comparison

### Option 2: Auto-scrape (requires Apify MCP)
Provide profile URL — agent scrapes data automatically:
- Facebook: `apify/facebook-posts-scraper`
- Instagram: `apify/instagram-post-scraper` + `apify/instagram-reel-scraper`
- YouTube: `streamers/youtube-scraper`
- TikTok: `clockworks/free-tiktok-scraper`

## Process
1. Activate Insights Agent
2. Collect data (manual paste OR Apify MCP scrape)
3. Use Social Analytics skill + KPI framework
4. Output: Performance report + recommendations

## Examples
- `/analytics fb` — Analyze Facebook Page insights (paste data or provide URL)
- `/analytics ig https://instagram.com/mybrand` — Auto-scrape Instagram via Apify
- `/analytics all` — Cross-platform summary comparing FB, IG, TikTok, YouTube
- `/analytics tiktok https://tiktok.com/@mybrand` — Scrape + analyze TikTok profile

## Tips
- If Apify MCP is configured, just provide the profile URL — no manual paste needed
- Focus on engagement rate over follower count; engaged small audiences convert better
- Review weekly to spot trends, optimize monthly to make meaningful changes
