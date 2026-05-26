# Design Data Reference

Quick-lookup tables for color palettes, font pairings, and landing page patterns.

## Color Palettes by Product Type

| # | Product Type | Primary | Secondary | CTA | Background | Text |
|---|-------------|---------|-----------|-----|------------|------|
| 1 | Service Landing | `#3B82F6` | `#60A5FA` | `#F97316` | `#F8FAFC` | `#1E293B` |
| 2 | Online Course | `#0D9488` | `#2DD4BF` | `#EA580C` | `#F0FDFA` | `#134E4A` |
| 3 | Beauty / Spa | `#10B981` | `#34D399` | `#8B5CF6` | `#ECFDF5` | `#064E3B` |
| 4 | Restaurant / Food | `#DC2626` | `#F87171` | `#CA8A04` | `#FEF2F2` | `#450A0A` |
| 5 | Healthcare | `#0891B2` | `#22D3EE` | `#059669` | `#ECFEFF` | `#164E63` |
| 6 | SaaS / Software | `#2563EB` | `#3B82F6` | `#F97316` | `#F8FAFC` | `#1E293B` |
| 7 | E-commerce | `#3B82F6` | `#60A5FA` | `#F97316` | `#F8FAFC` | `#1E293B` |
| 8 | Real Estate | `#0F766E` | `#14B8A6` | `#0369A1` | `#F0FDFA` | `#134E4A` |
| 9 | Fitness / Gym | `#DC2626` | `#F87171` | `#16A34A` | `#FEF2F2` | `#1F2937` |
| 10 | Travel / Tourism | `#EC4899` | `#F472B6` | `#06B6D4` | `#FDF2F8` | `#831843` |
| 11 | Fintech / Crypto | `#F59E0B` | `#FBBF24` | `#8B5CF6` | `#0F172A` | `#F8FAFC` |
| 12 | Legal Services | `#1E3A8A` | `#1E40AF` | `#B45309` | `#F8FAFC` | `#0F172A` |
| 13 | Wedding / Event | `#7C3AED` | `#A78BFA` | `#F97316` | `#FAF5FF` | `#4C1D95` |
| 14 | Luxury / Premium | `#1C1917` | `#44403C` | `#CA8A04` | `#FAFAF9` | `#0C0A09` |
| 15 | AI / Tech Startup | `#7C3AED` | `#A78BFA` | `#06B6D4` | `#FAF5FF` | `#1E1B4B` |

## Font Pairings

| # | Name | Heading | Body | Best For |
|---|------|---------|------|----------|
| 1 | Vietnamese Friendly | Be Vietnam Pro | Noto Sans | Vietnamese sites, multilingual |
| 2 | Modern Professional | Poppins | Open Sans | SaaS, corporate, business |
| 3 | Classic Elegant | Playfair Display | Inter | Luxury, beauty, spa |
| 4 | Tech Startup | Space Grotesk | DM Sans | Tech, AI, developer tools |
| 5 | Wellness Calm | Lora | Raleway | Health, spa, wellness |
| 6 | Bold Statement | Bebas Neue | Source Sans 3 | Marketing, agency, events |
| 7 | Friendly SaaS | Plus Jakarta Sans | Plus Jakarta Sans | SaaS, web apps |
| 8 | Minimal Swiss | Inter | Inter | Dashboards, documentation |
| 9 | E-commerce Clean | Rubik | Nunito Sans | Online stores, retail |
| 10 | Geometric Modern | Outfit | Work Sans | Portfolios, modern brands |

### Font CSS Imports

**Vietnamese Friendly (Default):**
```html
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@300;400;500;600;700&family=Noto+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

**Modern Professional:**
```html
<link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;500;600;700&family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
```

**Classic Elegant:**
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap" rel="stylesheet">
```

**Tech Startup:**
```html
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
```

**Wellness Calm:**
```html
<link href="https://fonts.googleapis.com/css2?family=Lora:wght@400;500;600;700&family=Raleway:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

## Landing Page Patterns

| # | Pattern | Best For | Section Order |
|---|---------|----------|--------------|
| 1 | Hero + Features + CTA | SaaS, tools, services | Hero → Value prop → Features (3-5) → CTA → Footer |
| 2 | Hero + Testimonials + CTA | Proven products | Hero → Problem → Solution → Testimonials → CTA |
| 3 | Product Demo + Features | Software, apps | Hero → Video/mockup → Feature breakdown → CTA |
| 4 | Minimal Single Column | Simple offers | Headline → Description → 3 bullets → CTA |
| 5 | Funnel (3-Step) | Conversion focus | Problem → Solution → Action (progressive CTAs) |
| 6 | Lead Magnet + Form | Email capture | Benefit headline → Preview → Form (3 fields max) |
| 7 | Pricing Page + CTA | Multi-tier offers | Value prop → Pricing cards → Comparison → FAQ |
| 8 | Before-After | Results-based offers | Problem → Transformation → Results → CTA |
| 9 | Waitlist / Coming Soon | Pre-launch | Countdown → Teaser → Email capture |
| 10 | Video-First Hero | High-engagement | Video bg → Features overlay → Benefits → CTA |

## UI Quick Rules

| Rule | Do | Don't |
|------|----|----- |
| Icons | SVG icons (Heroicons, Lucide) | Emojis as UI icons |
| Hover | Color/opacity transitions | Scale transforms shifting layout |
| Cursor | `cursor-pointer` on clickable elements | Default cursor on buttons |
| Contrast | 4.5:1 minimum (WCAG AA) | Light gray on white |
| Touch | 44x44px minimum targets | Small mobile tap targets |
| Transitions | 150-300ms duration | Instant or >500ms |
| Body font | 16px minimum on mobile | 12-14px body text |
| Line height | 1.5-1.75 for body | 1.0-1.2 (too tight) |
