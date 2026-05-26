---
name: landing-page-builder
description: Generate complete, deployable HTML landing pages with Tailwind CSS
---

# Landing Page Builder Skill

## Overview

**Purpose**: Generate complete, deployable HTML landing pages with Tailwind CSS that drive conversions for Vietnamese SME/solopreneurs.

**Target Audience**: Vietnamese small businesses and solopreneurs who need professional landing pages during Day 2-3 of their business setup process.

**Output Format**: Single-file HTML with embedded Tailwind CSS (via CDN), fully responsive, mobile-first design, production-ready.

**Core Philosophy**:
- Speed over perfection (launch in hours, not weeks)
- Conversion-focused (every element serves the CTA)
- Vietnamese market context (local payment methods, cultural preferences)
- Zero dependencies (works offline after first load)

---

## Design System Selection Workflow

When building a landing page, follow this sequence:

### Step 1: Identify Product Type
Ask the user or infer from context:
- Service-based (consulting, freelance, agency)
- Online course/education
- Beauty/spa/wellness
- Restaurant/food delivery
- Healthcare/medical
- SaaS/software
- E-commerce/retail
- Real estate
- Fitness/gym
- Travel/tourism
- Fintech/financial services
- Legal services
- Wedding/event planning
- Luxury goods
- AI/tech products

### Step 2: Select Color Palette
Reference `references/design-data.md` for the appropriate color scheme based on product type. Each palette includes:
- Primary (brand color)
- Secondary (supporting color)
- CTA (call-to-action button color)
- Background (page background)
- Text (body text color)

### Step 3: Select Font Pairing
Choose fonts based on brand mood from `references/design-data.md`:
- Vietnamese Friendly: Be Vietnam Pro + Noto Sans
- Modern Professional: Poppins + Open Sans
- Classic Elegant: Playfair Display + Inter
- Tech Startup: Space Grotesk + DM Sans
- Wellness Calm: Lora + Raleway

### Step 4: Choose Landing Page Pattern
Select from the top 10 conversion-optimized patterns below based on business goal.

---

## Landing Page Patterns (Top 10)

| Pattern | Sections | CTA Placement | Best For | Conversion Focus |
|---------|----------|---------------|----------|------------------|
| **Hero + Features + CTA** | Hero, 3-6 Features, CTA | Above fold + bottom | General services, SaaS | Feature-benefit clarity |
| **Hero + Testimonials + CTA** | Hero, Social Proof, CTA | Above fold + after testimonials | High-trust needed (legal, health) | Social validation |
| **Product Demo + Features** | Video/GIF Demo, Features, CTA | After demo | SaaS, software, apps | Product visualization |
| **Minimal Single Column** | Hero, 1 CTA, Footer | Center, above fold | Lead magnets, waitlists | Zero distraction |
| **Funnel (3-Step)** | Problem → Solution → CTA | Each section | High-ticket services | Guided journey |
| **Lead Magnet + Form** | Hero, Benefits, Form, CTA | Form above fold | Email capture, freebies | List building |
| **Pricing Page + CTA** | Hero, 3-Tier Pricing, FAQ, CTA | Pricing cards | SaaS, memberships | Price transparency |
| **Before-After** | Problem state, Solution, Results | After transformation | Weight loss, beauty, courses | Transformation proof |
| **Waitlist/Coming Soon** | Hero, Countdown, Email Form | Email capture | Pre-launch products | FOMO urgency |
| **Video-First Hero** | Full-screen video, Overlay CTA | Video overlay | High-production brands | Emotional engagement |

### Pattern Selection Guide:
- **New business, no testimonials**: Use Hero + Features + CTA
- **Service with strong social proof**: Use Hero + Testimonials + CTA
- **SaaS with demo**: Use Product Demo + Features
- **Lead magnet offer**: Use Lead Magnet + Form
- **Pricing-sensitive audience**: Use Pricing Page + CTA
- **Transformation promise**: Use Before-After
- **Pre-launch hype**: Use Waitlist/Coming Soon

---

## Page Structure Template

Use this base HTML structure for all landing pages:

```html
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{PAGE_TITLE}}</title>
  <meta name="description" content="{{META_DESCRIPTION}}">

  <!-- Open Graph -->
  <meta property="og:title" content="{{OG_TITLE}}">
  <meta property="og:description" content="{{OG_DESCRIPTION}}">
  <meta property="og:image" content="{{OG_IMAGE}}">
  <meta property="og:type" content="website">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  {{FONT_IMPORT}}

  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            primary: '{{PRIMARY}}',
            secondary: '{{SECONDARY}}',
            accent: '{{ACCENT}}'
          },
          fontFamily: {
            heading: [{{HEADING_FONT}}, 'sans-serif'],
            body: [{{BODY_FONT}}, 'sans-serif']
          }
        }
      }
    }
  </script>

  <style>
    body { font-family: {{BODY_FONT}}, sans-serif; }
    h1, h2, h3, h4, h5, h6 { font-family: {{HEADING_FONT}}, sans-serif; }
  </style>
</head>
<body class="bg-gray-50 text-gray-900">
  <!-- Page content here -->
</body>
</html>
```

---

## Component Library

### Navbar (Floating with CTA)
```html
<nav class="fixed top-0 w-full bg-white shadow-md z-50">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex justify-between items-center h-16">
      <div class="flex-shrink-0">
        <span class="text-2xl font-bold text-primary">{{BRAND_NAME}}</span>
      </div>
      <div class="hidden md:flex space-x-8">
        <a href="#features" class="text-gray-700 hover:text-primary">Features</a>
        <a href="#pricing" class="text-gray-700 hover:text-primary">Pricing</a>
        <a href="#faq" class="text-gray-700 hover:text-primary">FAQ</a>
      </div>
      <a href="#cta" class="bg-accent text-white px-6 py-2 rounded-lg hover:opacity-90 transition">
        {{CTA_TEXT}}
      </a>
    </div>
  </div>
</nav>
```

### Hero Section (Headline + Subheadline + CTA + Social Proof)
```html
<section class="pt-24 pb-12 px-4 sm:px-6 lg:px-8 bg-gradient-to-b from-primary/5 to-white">
  <div class="max-w-4xl mx-auto text-center">
    <h1 class="text-4xl sm:text-5xl lg:text-6xl font-bold text-gray-900 mb-6">
      {{HEADLINE}}
    </h1>
    <p class="text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
      {{SUBHEADLINE}}
    </p>
    <div class="flex flex-col sm:flex-row gap-4 justify-center mb-8">
      <a href="#cta" class="bg-accent text-white px-8 py-4 rounded-lg text-lg font-semibold hover:opacity-90 transition">
        {{CTA_PRIMARY}}
      </a>
      <a href="#features" class="bg-white border-2 border-primary text-primary px-8 py-4 rounded-lg text-lg font-semibold hover:bg-primary hover:text-white transition">
        {{CTA_SECONDARY}}
      </a>
    </div>
    <div class="flex items-center justify-center gap-6 text-sm text-gray-600">
      <span>⭐⭐⭐⭐⭐ 4.9/5</span>
      <span>|</span>
      <span>{{SOCIAL_PROOF_COUNT}}+ customers</span>
    </div>
  </div>
</section>
```

### Features Grid (3-Column)
```html
<section id="features" class="py-16 px-4 sm:px-6 lg:px-8 bg-white">
  <div class="max-w-7xl mx-auto">
    <h2 class="text-3xl sm:text-4xl font-bold text-center mb-12">{{FEATURES_HEADLINE}}</h2>
    <div class="grid md:grid-cols-3 gap-8">
      <!-- Feature 1 -->
      <div class="text-center">
        <div class="w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mx-auto mb-4">
          <span class="text-3xl">{{ICON_1}}</span>
        </div>
        <h3 class="text-xl font-semibold mb-2">{{FEATURE_1_TITLE}}</h3>
        <p class="text-gray-600">{{FEATURE_1_DESC}}</p>
      </div>
      <!-- Feature 2 -->
      <div class="text-center">
        <div class="w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mx-auto mb-4">
          <span class="text-3xl">{{ICON_2}}</span>
        </div>
        <h3 class="text-xl font-semibold mb-2">{{FEATURE_2_TITLE}}</h3>
        <p class="text-gray-600">{{FEATURE_2_DESC}}</p>
      </div>
      <!-- Feature 3 -->
      <div class="text-center">
        <div class="w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mx-auto mb-4">
          <span class="text-3xl">{{ICON_3}}</span>
        </div>
        <h3 class="text-xl font-semibold mb-2">{{FEATURE_3_TITLE}}</h3>
        <p class="text-gray-600">{{FEATURE_3_DESC}}</p>
      </div>
    </div>
  </div>
</section>
```

### Testimonials (Grid)
```html
<section id="testimonials" class="py-16 px-4 sm:px-6 lg:px-8 bg-gray-50">
  <div class="max-w-7xl mx-auto">
    <h2 class="text-3xl sm:text-4xl font-bold text-center mb-12">What Our Customers Say</h2>
    <div class="grid md:grid-cols-3 gap-8">
      <!-- Testimonial 1 -->
      <div class="bg-white p-6 rounded-lg shadow-md">
        <p class="text-gray-700 mb-4">"{{TESTIMONIAL_1}}"</p>
        <div class="flex items-center gap-3">
          <div class="w-12 h-12 bg-gray-300 rounded-full"></div>
          <div>
            <p class="font-semibold">{{NAME_1}}</p>
            <p class="text-sm text-gray-600">{{ROLE_1}}</p>
          </div>
        </div>
      </div>
      <!-- Testimonial 2 -->
      <div class="bg-white p-6 rounded-lg shadow-md">
        <p class="text-gray-700 mb-4">"{{TESTIMONIAL_2}}"</p>
        <div class="flex items-center gap-3">
          <div class="w-12 h-12 bg-gray-300 rounded-full"></div>
          <div>
            <p class="font-semibold">{{NAME_2}}</p>
            <p class="text-sm text-gray-600">{{ROLE_2}}</p>
          </div>
        </div>
      </div>
      <!-- Testimonial 3 -->
      <div class="bg-white p-6 rounded-lg shadow-md">
        <p class="text-gray-700 mb-4">"{{TESTIMONIAL_3}}"</p>
        <div class="flex items-center gap-3">
          <div class="w-12 h-12 bg-gray-300 rounded-full"></div>
          <div>
            <p class="font-semibold">{{NAME_3}}</p>
            <p class="text-sm text-gray-600">{{ROLE_3}}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

### Pricing Cards (3-Tier)
```html
<section id="pricing" class="py-16 px-4 sm:px-6 lg:px-8 bg-white">
  <div class="max-w-7xl mx-auto">
    <h2 class="text-3xl sm:text-4xl font-bold text-center mb-12">Simple, Transparent Pricing</h2>
    <div class="grid md:grid-cols-3 gap-8">
      <!-- Basic Tier -->
      <div class="border-2 border-gray-200 rounded-lg p-8 hover:border-primary transition">
        <h3 class="text-2xl font-bold mb-2">{{TIER_1_NAME}}</h3>
        <p class="text-4xl font-bold mb-6">{{TIER_1_PRICE}}<span class="text-lg text-gray-600">/month</span></p>
        <ul class="space-y-3 mb-8">
          <li class="flex items-start"><span class="text-green-500 mr-2">✓</span>{{TIER_1_FEATURE_1}}</li>
          <li class="flex items-start"><span class="text-green-500 mr-2">✓</span>{{TIER_1_FEATURE_2}}</li>
          <li class="flex items-start"><span class="text-green-500 mr-2">✓</span>{{TIER_1_FEATURE_3}}</li>
        </ul>
        <a href="#cta" class="block w-full text-center bg-gray-200 text-gray-900 px-6 py-3 rounded-lg font-semibold hover:bg-gray-300 transition">
          Get Started
        </a>
      </div>
      <!-- Pro Tier (Popular) -->
      <div class="border-2 border-accent rounded-lg p-8 relative transform scale-105 shadow-xl">
        <span class="absolute -top-4 left-1/2 -translate-x-1/2 bg-accent text-white px-4 py-1 rounded-full text-sm font-semibold">
          Most Popular
        </span>
        <h3 class="text-2xl font-bold mb-2">{{TIER_2_NAME}}</h3>
        <p class="text-4xl font-bold mb-6">{{TIER_2_PRICE}}<span class="text-lg text-gray-600">/month</span></p>
        <ul class="space-y-3 mb-8">
          <li class="flex items-start"><span class="text-green-500 mr-2">✓</span>{{TIER_2_FEATURE_1}}</li>
          <li class="flex items-start"><span class="text-green-500 mr-2">✓</span>{{TIER_2_FEATURE_2}}</li>
          <li class="flex items-start"><span class="text-green-500 mr-2">✓</span>{{TIER_2_FEATURE_3}}</li>
          <li class="flex items-start"><span class="text-green-500 mr-2">✓</span>{{TIER_2_FEATURE_4}}</li>
        </ul>
        <a href="#cta" class="block w-full text-center bg-accent text-white px-6 py-3 rounded-lg font-semibold hover:opacity-90 transition">
          Get Started
        </a>
      </div>
      <!-- Enterprise Tier -->
      <div class="border-2 border-gray-200 rounded-lg p-8 hover:border-primary transition">
        <h3 class="text-2xl font-bold mb-2">{{TIER_3_NAME}}</h3>
        <p class="text-4xl font-bold mb-6">{{TIER_3_PRICE}}<span class="text-lg text-gray-600">/month</span></p>
        <ul class="space-y-3 mb-8">
          <li class="flex items-start"><span class="text-green-500 mr-2">✓</span>{{TIER_3_FEATURE_1}}</li>
          <li class="flex items-start"><span class="text-green-500 mr-2">✓</span>{{TIER_3_FEATURE_2}}</li>
          <li class="flex items-start"><span class="text-green-500 mr-2">✓</span>{{TIER_3_FEATURE_3}}</li>
          <li class="flex items-start"><span class="text-green-500 mr-2">✓</span>{{TIER_3_FEATURE_4}}</li>
          <li class="flex items-start"><span class="text-green-500 mr-2">✓</span>{{TIER_3_FEATURE_5}}</li>
        </ul>
        <a href="#cta" class="block w-full text-center bg-gray-200 text-gray-900 px-6 py-3 rounded-lg font-semibold hover:bg-gray-300 transition">
          Contact Sales
        </a>
      </div>
    </div>
  </div>
</section>
```

### FAQ Accordion (Vanilla JS)
```html
<section id="faq" class="py-16 px-4 sm:px-6 lg:px-8 bg-gray-50">
  <div class="max-w-3xl mx-auto">
    <h2 class="text-3xl sm:text-4xl font-bold text-center mb-12">Frequently Asked Questions</h2>
    <div class="space-y-4">
      <!-- FAQ Item 1 -->
      <div class="bg-white rounded-lg shadow-md overflow-hidden">
        <button class="faq-toggle w-full text-left p-6 font-semibold text-lg flex justify-between items-center hover:bg-gray-50 transition">
          {{FAQ_Q1}}
          <span class="faq-icon text-2xl">+</span>
        </button>
        <div class="faq-content hidden px-6 pb-6 text-gray-700">
          {{FAQ_A1}}
        </div>
      </div>
      <!-- FAQ Item 2 -->
      <div class="bg-white rounded-lg shadow-md overflow-hidden">
        <button class="faq-toggle w-full text-left p-6 font-semibold text-lg flex justify-between items-center hover:bg-gray-50 transition">
          {{FAQ_Q2}}
          <span class="faq-icon text-2xl">+</span>
        </button>
        <div class="faq-content hidden px-6 pb-6 text-gray-700">
          {{FAQ_A2}}
        </div>
      </div>
      <!-- Add more FAQ items as needed -->
    </div>
  </div>
</section>

<script>
  document.querySelectorAll('.faq-toggle').forEach(btn => {
    btn.addEventListener('click', () => {
      const content = btn.nextElementSibling;
      const icon = btn.querySelector('.faq-icon');
      content.classList.toggle('hidden');
      icon.textContent = content.classList.contains('hidden') ? '+' : '−';
    });
  });
</script>
```

### Footer
```html
<footer class="bg-gray-900 text-gray-300 py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-7xl mx-auto">
    <div class="grid md:grid-cols-4 gap-8 mb-8">
      <div>
        <h3 class="text-white font-bold text-xl mb-4">{{BRAND_NAME}}</h3>
        <p class="text-sm">{{BRAND_TAGLINE}}</p>
      </div>
      <div>
        <h4 class="text-white font-semibold mb-4">Product</h4>
        <ul class="space-y-2 text-sm">
          <li><a href="#features" class="hover:text-white">Features</a></li>
          <li><a href="#pricing" class="hover:text-white">Pricing</a></li>
          <li><a href="#faq" class="hover:text-white">FAQ</a></li>
        </ul>
      </div>
      <div>
        <h4 class="text-white font-semibold mb-4">Company</h4>
        <ul class="space-y-2 text-sm">
          <li><a href="#about" class="hover:text-white">About Us</a></li>
          <li><a href="#contact" class="hover:text-white">Contact</a></li>
          <li><a href="#blog" class="hover:text-white">Blog</a></li>
        </ul>
      </div>
      <div>
        <h4 class="text-white font-semibold mb-4">Connect</h4>
        <div class="flex gap-4">
          <a href="#" class="hover:text-white">Facebook</a>
          <a href="#" class="hover:text-white">Twitter</a>
          <a href="#" class="hover:text-white">LinkedIn</a>
        </div>
      </div>
    </div>
    <div class="border-t border-gray-800 pt-8 text-center text-sm">
      <p>&copy; 2025 {{BRAND_NAME}}. All rights reserved.</p>
    </div>
  </div>
</footer>
```

### SePay Payment Section (VietQR Embed)
```html
<section id="payment" class="py-16 px-4 sm:px-6 lg:px-8 bg-white">
  <div class="max-w-2xl mx-auto text-center">
    <h2 class="text-3xl font-bold mb-6">Complete Your Order</h2>
    <p class="text-gray-600 mb-8">Scan QR code with your banking app to pay instantly</p>

    <!-- SePay QR Code Embed -->
    <div class="bg-gray-50 p-8 rounded-lg inline-block">
      <img src="https://my.sepay.vn/qr?bank={{BANK_ID}}&acc={{ACCOUNT_NUMBER}}&amount={{AMOUNT}}&des={{ORDER_ID}}"
           alt="VietQR Payment Code"
           class="w-64 h-64 mx-auto">
    </div>

    <p class="text-sm text-gray-600 mt-4">
      Order ID: <span class="font-mono font-semibold">{{ORDER_ID}}</span>
    </p>
    <p class="text-xs text-gray-500 mt-2">
      Payment will be confirmed automatically within 30 seconds
    </p>
  </div>
</section>
```

---

## Copy Formulas

### Headlines
- **Benefit-Driven**: `[Achieve outcome] without [pain]`
  - Example: "Grow Your Business Without Hiring a Marketing Team"
- **Transformation**: `From [current state] to [desired state] in [timeframe]`
  - Example: "From Zero Customers to 100+ Sales in 30 Days"
- **Question Hook**: `Want to [desired outcome]?`
  - Example: "Want to Double Your Revenue This Quarter?"

### Subheadlines
- **Product-Benefit**: `[Product] helps [audience] [benefit] so they can [ultimate goal]`
  - Example: "Our AI-powered tool helps solopreneurs automate marketing so they can focus on what they love"
- **Social Proof**: `Join [number]+ [audience] who [achieved result]`
  - Example: "Join 10,000+ small businesses who increased sales by 50%"

### CTA Buttons
- **Action + Benefit**: `[Action verb] + [benefit]`
  - Examples: "Get Started Free", "Start Growing Today", "Claim Your Discount"
- **Risk Reversal**: `Try [product] Free for [timeframe]`
  - Example: "Try Free for 14 Days"

### Social Proof Snippets
- `[Number]+ customers trust us`
- `[Rating]/5 stars from [number] reviews`
- `Featured in [publication]`
- `Used by [well-known brand]`

---

## SEO Meta Template

### Title Tag (50-60 characters)
```
[Primary Keyword] - [Benefit] | [Brand]
```
Example: "Landing Page Builder - Create Pages in Minutes | BrandName"

### Meta Description (150-160 characters)
```
[Benefit statement]. [Social proof]. [CTA phrase].
```
Example: "Build high-converting landing pages without coding. Join 10,000+ businesses. Get started free today."

### Open Graph
```html
<meta property="og:title" content="[Catchier version of title]">
<meta property="og:description" content="[Same as meta description or more compelling]">
<meta property="og:image" content="[URL to 1200x630px image]">
<meta property="og:type" content="website">
```

---

## Deployment

### Vercel Deployment (Recommended)
1. Save landing page as `index.html`
2. Create `vercel.json` with:
   ```json
   {
     "version": 2,
     "builds": [{ "src": "index.html", "use": "@vercel/static" }]
   }
   ```
3. Run `vercel --prod`
4. Custom domain: Add domain in Vercel dashboard → DNS settings

### Alternative: Netlify Drop
1. Drag `index.html` to netlify.com/drop
2. Custom domain: Site settings → Domain management

---

## Quality Checklist

Before delivering the landing page, verify:

### Responsiveness
- [ ] Renders correctly at 375px (mobile)
- [ ] Renders correctly at 768px (tablet)
- [ ] Renders correctly at 1024px (laptop)
- [ ] Renders correctly at 1440px (desktop)

### Performance
- [ ] Page loads under 3 seconds on 3G connection
- [ ] Tailwind CDN loaded correctly
- [ ] No console errors
- [ ] Images optimized (under 200KB each)

### Conversion Optimization
- [ ] Primary CTA visible above fold
- [ ] CTA repeated at least 2x on page
- [ ] Social proof visible in hero section
- [ ] Contact/payment method clearly stated

### Content
- [ ] All placeholder text replaced
- [ ] Vietnamese language support (Be Vietnam Pro font)
- [ ] All images have alt text
- [ ] No Lorem ipsum remaining

### Technical
- [ ] Valid HTML5
- [ ] Meta tags complete
- [ ] Favicon included
- [ ] Google Analytics (optional) tracking code

### Accessibility
- [ ] Color contrast ratio > 4.5:1
- [ ] Focus states on interactive elements
- [ ] Keyboard navigation works
- [ ] Screen reader friendly

---

## Usage Instructions

When a user requests a landing page:

1. **Gather Requirements**:
   - What product/service?
   - Target audience?
   - Primary goal (leads, sales, signups)?
   - Existing brand colors/fonts?

2. **Select Design System**:
   - Choose color palette from `references/design-data.md`
   - Choose font pairing
   - Choose landing page pattern

3. **Generate HTML**:
   - Use `templates/landing-page-template.html` as base
   - Replace all `{{PLACEHOLDERS}}`
   - Add/remove sections based on pattern

4. **Test Locally**:
   - Open in browser
   - Test responsive breakpoints
   - Verify all links work

5. **Deliver**:
   - Provide HTML file
   - Include deployment instructions
   - Offer customization tips

---

## Tips for High Conversions

1. **Above the Fold**: CTA + headline + subheadline + social proof
2. **Single CTA**: Don't confuse visitors with multiple actions
3. **Scarcity**: "Limited spots", "Offer ends soon"
4. **Risk Reversal**: "Money-back guarantee", "Free trial"
5. **Vietnamese Context**: Use VietQR, local testimonials, Vietnamese language
6. **Mobile-First**: 70%+ Vietnamese users browse on mobile
7. **Fast Loading**: Under 3 seconds or lose 50% of visitors
8. **Clear Value**: Answer "What's in it for me?" in first 3 seconds

---

## Working from Design Reference (Image/Screenshot Input)

When a user provides a screenshot, image, or URL of a landing page they want to replicate or draw inspiration from, follow this systematic protocol:

### Phase 1: Visual Analysis (Read the Image)

Analyze the reference image across these 8 dimensions:

**1. Layout Architecture**
- Overall structure: single column, split-screen, asymmetric, grid-based?
- Section count and ordering (hero, features, pricing, etc.)
- Content width: full-bleed, contained (max-width), mixed?
- Vertical rhythm: section spacing (compact, normal, generous)?
- Breakpoint behavior: how might it adapt to mobile?

**2. Color Extraction**
- Primary brand color (dominant hue)
- Secondary color (supporting/accent)
- CTA button color (action color)
- Background colors per section (alternating? gradient? solid?)
- Text colors (heading vs body vs muted)
- Dark mode or light mode base?
- Special effects: gradients, overlays, glassmorphism?

Map extracted colors to closest Tailwind utilities:
```
primary: bg-[#HEX] or bg-blue-600
secondary: bg-[#HEX] or bg-indigo-500
accent/CTA: bg-[#HEX] or bg-orange-500
```

**3. Typography Assessment**
- Heading font style: sans-serif, serif, display, monospace?
- Body font style: clean sans, humanist, geometric?
- Heading weight: bold, extrabold, black?
- Size hierarchy: how much contrast between h1/h2/body?
- Letter spacing: tight, normal, wide?
- Line height: tight (1.2), normal (1.5), relaxed (1.75)?
- Special text treatments: gradient text, outlined text, rotated text?

Map to Google Fonts:
```
Heading: font-family: 'Inter', 'Poppins', 'Space Grotesk', etc.
Body: font-family: 'DM Sans', 'Open Sans', 'Nunito Sans', etc.
```

**4. Component Inventory**
List every UI component visible:
- Navigation (fixed? transparent? floating pill?)
- Hero type (centered text, split image+text, video background, animated)
- Cards (shadow, border, rounded, hover effects)
- Buttons (rounded, pill, ghost, gradient, icon+text)
- Forms (inline, stacked, multi-step)
- Badges/tags (pill, square, outline)
- Icons (line, filled, custom illustrations, emoji)
- Dividers (line, wave, angle, none)
- Footer (simple, multi-column, CTA footer)

**5. Spacing & Sizing Patterns**
- Section padding: py-12 (compact), py-20 (normal), py-32 (generous)?
- Card/element gaps: gap-4, gap-6, gap-8?
- Content max-width: max-w-4xl, max-w-6xl, max-w-7xl?
- Border radius: rounded-lg, rounded-xl, rounded-2xl, rounded-full?
- Shadow depth: shadow-sm, shadow-md, shadow-xl?

**6. Visual Effects & Animations**
- Background patterns (dots, grid, noise, blobs)
- Scroll animations (fade-in, slide-up, parallax)
- Hover effects (scale, shadow, color change, underline)
- Gradient usage (linear, radial, mesh)
- Blur/glassmorphism effects
- Floating/decorative elements
- Image treatments (rounded corners, shadows, overlays, masks)

**7. Content Density**
- Text-heavy vs visual-heavy ratio
- Number of CTAs visible
- Social proof density (testimonials, logos, stats)
- Whitespace philosophy (minimal, moderate, generous)

**8. Vietnamese Market Adaptation Notes**
- Does the design suit Vietnamese aesthetics?
- Font compatibility with Vietnamese diacritics?
- Payment section placement for VietQR?
- Trust signals appropriate for VN market?
- Mobile-first considerations for Vietnamese users?

### Phase 2: Design Mapping (Plan the Build)

After analysis, create a build plan:

```
DESIGN REFERENCE BUILD PLAN
============================
Template Base: [closest existing template or start fresh]
Layout: [layout description]
Color Scheme:
  - Primary: [color] → Tailwind: [class]
  - Secondary: [color] → Tailwind: [class]
  - CTA: [color] → Tailwind: [class]
  - Background: [color] → Tailwind: [class]
Font Pairing:
  - Heading: [font] → Google Fonts import
  - Body: [font] → Google Fonts import
Components Needed:
  1. [component] → [Tailwind approach]
  2. [component] → [Tailwind approach]
  ...
Special Effects:
  - [effect] → [CSS/Tailwind implementation]
Sections (top to bottom):
  1. [section name] — [brief description]
  2. [section name] — [brief description]
  ...
Estimated Complexity: [Low/Medium/High]
```

### Phase 3: Build (Generate HTML)

1. Start from closest template or build fresh
2. Apply color scheme via Tailwind config
3. Import correct Google Fonts
4. Build section by section, matching reference layout
5. Add special effects (gradients, animations, glassmorphism)
6. Implement responsive breakpoints
7. Add SePay/VietQR if payment needed
8. Run quality checklist

### Phase 4: Compare & Refine

After generating, compare output to reference:
- [ ] Overall layout matches reference structure
- [ ] Color scheme feels similar (exact match not required)
- [ ] Typography hierarchy matches
- [ ] Spacing and breathing room similar
- [ ] Key components present (nav, hero, features, CTA, footer)
- [ ] Special effects implemented (gradients, shadows, animations)
- [ ] Mobile responsive behavior appropriate
- [ ] Vietnamese market elements added where needed

### Important Notes for Design Reference Workflow
- **Match the spirit, not pixel-perfect**: Capture the feel, layout, and style — not every pixel
- **Respect copyright**: Don't copy logos, images, or proprietary content
- **Improve on weaknesses**: If reference has poor mobile UX or missing CTA, fix it
- **Add VN context**: Always adapt for Vietnamese market even if reference is Western
- **Stay Tailwind-native**: All styling via Tailwind utilities, no custom CSS unless absolutely necessary
- **Single-file output**: Keep everything in one HTML file for easy deployment

---

## Template Library

This skill includes multiple production-ready HTML templates for different use cases and styles. Each template is a complete, deployable single-file HTML with Tailwind CSS.

### Available Templates

| # | Template File | Style | Best For | Key Features |
|---|--------------|-------|----------|--------------|
| 1 | `landing-page-template.html` | Standard Light | General services, SaaS | Hero + Features + Pricing + FAQ + SePay |
| 2 | `landing-page-dark-modern.html` | Dark + Gradient | Tech, AI, SaaS, crypto | Dark theme, glassmorphism, gradient accents |
| 3 | `landing-page-minimal-clean.html` | Minimal + Serif | Luxury, coaching, personal brand | Single column, generous whitespace, elegant |
| 4 | `landing-page-creative-bold.html` | Bold + Asymmetric | Agency, creative, startup | Large type, asymmetric layout, animations |
| 5 | `landing-page-saas-product.html` | Product-focused | SaaS, software, apps | Product demo, feature grid, comparison table |
| 6 | `landing-page-ecommerce-product.html` | E-commerce | Physical/digital products | Product gallery, specs, reviews, cart |
| 7 | `landing-page-webinar-event.html` | Event/Launch | Webinars, workshops, launches | Countdown, speakers, schedule, registration |
| 8 | `landing-page-portfolio-personal.html` | Portfolio | Freelancers, consultants, coaches | Work showcase, about, skills, contact |
| 9 | `landing-page-restaurant-food.html` | Restaurant/F&B | Restaurants, cafes, food delivery | Menu, gallery, reservation, location map |
| 10 | `landing-page-mobile-app.html` | App Landing | Mobile apps, tools | Phone mockup, app store buttons, features |

### Template Selection Guide

**By Business Type:**
- New service business, no preference → Template 1 (Standard)
- Tech/AI/crypto product → Template 2 (Dark Modern)
- High-ticket coaching/consulting → Template 3 (Minimal Clean)
- Creative agency/startup → Template 4 (Creative Bold)
- SaaS/software tool → Template 5 (SaaS Product)
- Selling physical/digital product → Template 6 (E-commerce)
- Hosting webinar/event → Template 7 (Webinar/Event)
- Personal brand/freelancer → Template 8 (Portfolio)
- Restaurant/cafe/food → Template 9 (Restaurant)
- Mobile app launch → Template 10 (Mobile App)

**By Design Preference:**
- "I want something professional" → Template 1, 5
- "I want something modern and dark" → Template 2
- "I want something elegant and clean" → Template 3
- "I want something creative and bold" → Template 4
- "I want something fun and colorful" → Template 9, 10
- "I want something minimal" → Template 3, 8

---

## Maintenance

Landing pages should be updated:
- **Monthly**: Refresh testimonials, update stats
- **Quarterly**: A/B test new headlines
- **Yearly**: Redesign based on trends

Track with Google Analytics:
- Conversion rate
- Bounce rate
- Time on page
- CTA click-through rate
