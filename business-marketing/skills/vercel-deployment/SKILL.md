---
name: vercel-deployment
description: Deploy HTML landing pages to Vercel with one command - get live websites on .vercel.app or custom domains
---

# Vercel Deployment Skill

## When to Use

Activate this skill when you need to:
- Deploy HTML landing pages to production
- Get a live URL for customer testing
- Connect a custom domain to your website
- Set up auto-deployment from Git repositories
- Configure SSL certificates automatically
- Deploy static sites with zero backend configuration

## Overview

**Purpose:** Deploy HTML landing pages to Vercel with one command
**Target:** Non-technical SME/solopreneurs
**Result:** Live website on .vercel.app domain or custom domain
**Cost:** Free tier sufficient for most landing pages

## Prerequisites

### Required Software
- **Node.js**: Required for Vercel CLI
  - Download: https://nodejs.org/en/download/
  - Windows install: Download and run the installer (.msi file)
  - Verify: `node --version` (should show v18+ or v20+)

- **Vercel CLI**: Command-line deployment tool
  - Install: `npm install -g vercel`
  - Verify: `vercel --version`

### Required Account
- **Vercel Account**: Sign up at https://vercel.com/signup
  - Free tier includes:
    - Unlimited deployments
    - Automatic SSL certificates
    - 100GB bandwidth per month
    - Custom domain support

## Deployment Methods

### Method 1: Vercel CLI Deploy (Recommended)

**Best For:** Quick deployments, testing, iterative development

**Step-by-Step:**

1. **Open Terminal in Project Folder**
   - Windows: Right-click folder → "Open in Terminal" or CMD
   - Navigate: `cd path\to\your\project`

2. **Login to Vercel (One-time)**
   ```bash
   vercel login
   ```
   - Opens browser for authentication
   - Login with GitHub/GitLab/Bitbucket or email

3. **Deploy Your Site**
   ```bash
   vercel
   ```
   - First deployment: Answer setup questions
   - Subsequent deploys: Just run `vercel` again

4. **Production Deployment**
   ```bash
   vercel --prod
   ```
   - Use this for final production URL

**Example Output:**
```bash
cd my-landing-page
vercel --prod

Vercel CLI 32.0.0
🔍 Inspect: https://vercel.com/your-account/my-landing-page/abc123
✅ Production: https://my-landing-page.vercel.app [3s]
```

**Setup Questions (First Deploy):**
```
Set up and deploy "my-landing-page"?
> Yes

Which scope do you want to deploy to?
> Your Account

Link to existing project?
> No

What's your project's name?
> my-landing-page

In which directory is your code located?
> ./

Auto-detected Project Settings:
- Framework Preset: Other
- Build Command: None
- Output Directory: .
- Development Command: None

Want to override the settings?
> No
```

### Method 2: Git Deploy (Auto-deploy on Push)

**Best For:** Team collaboration, automated workflows, production sites

**Step-by-Step:**

1. **Push Code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/username/repo.git
   git push -u origin main
   ```

2. **Connect to Vercel Dashboard**
   - Go to https://vercel.com/new
   - Click "Import Git Repository"
   - Select your repository
   - Click "Import"

3. **Configure Project**
   - Framework Preset: Other (for static HTML)
   - Build Command: Leave empty
   - Output Directory: . (current directory)
   - Install Command: Leave empty

4. **Deploy**
   - Click "Deploy"
   - Wait 20-60 seconds
   - Get live URL

**Auto-Deploy Feature:**
- Every push to `main` branch → automatic production deploy
- Every push to other branches → preview deploy
- Pull requests get unique preview URLs

### Method 3: Drag & Drop

**Best For:** Non-technical users, quick testing, one-time deploys

**Step-by-Step:**

1. Go to https://vercel.com/new
2. Drag project folder to upload area
3. Wait for upload to complete
4. Click "Deploy"
5. Done - get live URL

**Limitations:**
- No auto-deploy on code changes
- Manual re-upload required for updates
- Not recommended for production

## Project Structure for Static Sites

```
my-landing-page/
├── index.html           ← Main landing page (REQUIRED)
├── thank-you.html       ← Post-purchase redirect (optional)
├── privacy-policy.html  ← Legal pages (optional)
├── terms.html
├── assets/
│   ├── images/
│   │   ├── hero-image.jpg
│   │   ├── product-photo.png
│   │   └── favicon.ico
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── main.js
└── vercel.json          ← Configuration file (optional)
```

**File Naming Rules:**
- Main page MUST be named `index.html`
- Use lowercase, hyphens for spaces: `thank-you.html`
- No spaces or special characters in file names

## vercel.json Configuration

Create `vercel.json` in your project root for advanced settings:

### Basic Configuration
```json
{
  "rewrites": [
    { "source": "/(.*)", "destination": "/index.html" }
  ]
}
```

### Security Headers
```json
{
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "X-Frame-Options", "value": "DENY" },
        { "key": "X-XSS-Protection", "value": "1; mode=block" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" }
      ]
    }
  ]
}
```

### Redirects
```json
{
  "redirects": [
    {
      "source": "/old-page",
      "destination": "/new-page",
      "permanent": true
    },
    {
      "source": "/promo",
      "destination": "/special-offer",
      "permanent": false
    }
  ]
}
```

### Complete Production Config
See `templates/vercel-config.json` for full example

## Custom Domain Setup

### Step 1: Add Domain in Vercel Dashboard

1. Go to https://vercel.com/dashboard
2. Select your project
3. Click "Settings" → "Domains"
4. Enter your domain name: `example.com`
5. Click "Add"

### Step 2: Configure DNS Records

**Option A: Apex Domain (example.com)**

Add A record in your domain registrar:

| Type | Name | Value | TTL |
|------|------|-------|-----|
| A | @ | 76.76.21.21 | 3600 |

**Option B: Subdomain (www.example.com)**

Add CNAME record:

| Type | Name | Value | TTL |
|------|------|-------|-----|
| CNAME | www | cname.vercel-dns.com | 3600 |

**Best Practice: Setup Both**

```
A      @     76.76.21.21
CNAME  www   cname.vercel-dns.com
```

### Step 3: Verify Domain

1. Wait 5-10 minutes for DNS propagation
2. Vercel automatically detects changes
3. SSL certificate issued automatically (5-60 minutes)
4. Green lock icon appears when ready

### DNS Propagation Time
- **Minimum:** 5 minutes
- **Average:** 1-4 hours
- **Maximum:** 24-48 hours
- Check status: https://dnschecker.org

## Environment Variables

### When to Use
- API keys for third-party services
- Payment gateway tokens
- Analytics tracking IDs
- Feature flags

### How to Set

1. **Via Dashboard:**
   - Project → Settings → Environment Variables
   - Add key-value pairs
   - Select environments: Production, Preview, Development

2. **Via CLI:**
   ```bash
   vercel env add PAYMENT_API_KEY
   # Paste value when prompted
   ```

### Access in HTML (Client-Side)
```html
<script>
  // Environment variables are NOT available in static HTML
  // For security, use server functions or build-time replacement
</script>
```

### Best Practices
- Never expose API keys in client-side code
- Use environment-specific values
- Rotate keys regularly
- Document required variables in README

## Troubleshooting

### Error: "404 Not Found"

**Cause:** Missing `index.html` file
**Fix:** Ensure main file is named exactly `index.html`

```bash
# Check file name
ls
# Should show: index.html (not Index.html or home.html)
```

### Error: "Build Failed"

**Cause:** Build command configured for static HTML
**Fix:** Remove build settings

1. Go to Project Settings → General
2. Build Command: Leave empty
3. Output Directory: `.`
4. Install Command: Leave empty

### Error: "DNS Not Propagating"

**Cause:** DNS changes take time
**Fix:** Wait and verify

- Wait 24-48 hours maximum
- Check https://dnschecker.org
- Verify DNS records match Vercel requirements
- Contact domain registrar support if stuck

### Error: "Images Not Loading"

**Cause:** Incorrect file paths
**Fix:** Use relative paths

```html
<!-- ❌ Wrong -->
<img src="/Users/admin/project/image.jpg">
<img src="C:\project\image.jpg">

<!-- ✅ Correct -->
<img src="./assets/images/hero.jpg">
<img src="assets/images/hero.jpg">
```

### Error: "Site Loads Locally But Not on Vercel"

**Cause:** Case-sensitive file paths
**Fix:** Match exact file names

```html
<!-- Local (Windows): Works with any case -->
<img src="Assets/Images/Hero.jpg">

<!-- Vercel (Linux): Case-sensitive -->
<img src="assets/images/hero.jpg">
```

### Check Deployment Logs

```bash
# View recent deployment logs
vercel logs

# View specific deployment
vercel logs [deployment-url]
```

## Quality Checklist

### Pre-Deployment
- [ ] `index.html` exists in root directory
- [ ] All file paths use relative URLs
- [ ] File names use lowercase and hyphens
- [ ] Images compressed (< 500KB each)
- [ ] No hardcoded localhost URLs
- [ ] External scripts use HTTPS
- [ ] Meta tags present (title, description, og:image)

### Post-Deployment
- [ ] Site loads at .vercel.app URL
- [ ] Mobile responsive (test on phone)
- [ ] All internal links working
- [ ] All images loading correctly
- [ ] Forms submit correctly
- [ ] Payment buttons functional
- [ ] SSL certificate active (green lock icon)
- [ ] Custom domain connected (if applicable)

### Performance
- [ ] Page load time < 3 seconds
- [ ] Lighthouse score > 90
- [ ] No console errors in browser DevTools

### Testing Commands
```bash
# Check SSL certificate
curl -I https://your-site.vercel.app

# Test page load time
curl -o /dev/null -s -w '%{time_total}\n' https://your-site.vercel.app
```

## Common Use Cases

### Landing Page Deployment
```bash
# Standard landing page structure
vercel --prod
# Result: https://product-landing.vercel.app
```

### Multi-Page Site
```bash
# With thank-you page, privacy policy, etc.
vercel --prod
# All pages accessible:
# https://site.vercel.app/
# https://site.vercel.app/thank-you
# https://site.vercel.app/privacy-policy
```

### A/B Testing
```bash
# Deploy variant A
vercel --prod

# Deploy variant B to preview
vercel
# Result: https://site-abc123.vercel.app (preview URL)
```

## Best Practices

### Development Workflow
1. Develop locally
2. Test thoroughly
3. Deploy to preview: `vercel`
4. Verify preview URL
5. Deploy to production: `vercel --prod`

### File Organization
- Keep assets in dedicated folders
- Use descriptive file names
- Minimize file sizes (compress images)
- Group related files together

### Security
- Enable all security headers in `vercel.json`
- Use HTTPS for all external resources
- Never commit API keys to Git
- Regular dependency updates

### Performance
- Compress images before upload
- Minify CSS and JavaScript
- Use CDN for large assets
- Enable caching headers

## Advanced Features

### Custom Error Pages

Create `404.html` for custom not-found page:
```html
<!DOCTYPE html>
<html>
<head>
  <title>Page Not Found</title>
</head>
<body>
  <h1>404 - Page Not Found</h1>
  <a href="/">Go Home</a>
</body>
</html>
```

### Analytics Integration

Add to `index.html`:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

### Form Handling

Use form submission services:
- Formspree: https://formspree.io
- Netlify Forms (alternative platform)
- Web3Forms: https://web3forms.com

Example:
```html
<form action="https://formspree.io/f/your-form-id" method="POST">
  <input type="email" name="email" required>
  <button type="submit">Submit</button>
</form>
```

## Reference Links

- Official Docs: https://vercel.com/docs
- CLI Reference: https://vercel.com/docs/cli
- Platform Limits: https://vercel.com/docs/limits
- Status Page: https://vercel-status.com
- Community: https://github.com/vercel/vercel/discussions

## Quick Commands Reference

```bash
# Login
vercel login

# Deploy to preview
vercel

# Deploy to production
vercel --prod

# List deployments
vercel list

# View logs
vercel logs

# Remove deployment
vercel remove [deployment-url]

# Link local project to Vercel project
vercel link

# Pull environment variables
vercel env pull

# Check CLI version
vercel --version

# Get help
vercel --help
```

## Support

### Getting Help
- Check deployment logs: `vercel logs`
- Visit Vercel documentation: https://vercel.com/docs
- Community discussions: https://github.com/vercel/vercel/discussions
- Support email: support@vercel.com

### Common Issues Database
- Deployment errors: https://vercel.com/docs/errors
- DNS configuration: https://vercel.com/docs/custom-domains
- Build configuration: https://vercel.com/docs/build-step
