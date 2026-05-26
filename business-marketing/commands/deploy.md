---
description: Deploy landing page or website to Vercel
argument-hint: [method]
---
Deploy your landing page or website to a live URL.

<args>$ARGUMENTS</args>

## Methods
- `vercel` / `cli` - Deploy via Vercel CLI (recommended)
- `git` - Auto-deploy from GitHub repository
- `drag` - Drag & drop on Vercel dashboard

## Process
1. Activate Deliver Agent
2. Use Vercel Deployment skill
3. Guide through deployment steps
4. Output: Live URL + custom domain setup instructions

## Examples
- `/deploy vercel` — Deploy current project to Vercel via CLI, get live URL
- `/deploy git` — Set up auto-deploy from GitHub (deploy on every push)
- `/deploy domain` — Guide through custom domain setup with DNS records

## Tips
- Make sure Node.js is installed before using Vercel CLI
- Free Vercel tier is sufficient for most landing pages
- Use `/landing-page` first to build the page, then `/deploy` to publish it
