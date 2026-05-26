# AI Agent Business Kit

Your complete business automation system — 5 Agents, 18 Skills, 18 Commands.

## How This Kit Works

When a user types a `/command`, you:
1. Read the matching command file in `commands/`
2. Activate the assigned Agent (system prompt in `agents/`)
3. Load the relevant Skill (`skills/*/SKILL.md` + `references/` + `templates/`)
4. Follow the Workflow if applicable (`workflows/`)
5. Deliver the output

## Agents

| Agent | File | Skills |
|-------|------|--------|
| **Offer Agent** | `agents/01-offer-agent.md` | market-research, competitor-analysis, offer-packaging |
| **Attraction Agent** | `agents/02-attraction-agent.md` | funnel-architecture, content-creation, lead-magnet-builder |
| **Conversion Agent** | `agents/03-conversion-agent.md` | sales-page-blueprint, copywriting, objection-handler |
| **Deliver Agent** | `agents/04-deliver-agent.md` | payment-setup-guide, notification-setup-guide, delivery-setup-guide, landing-page-builder, vercel-deployment, payment-embed |
| **Insights Agent** | `agents/05-insights-agent.md` | social-analytics, revenue-report, optimization-advisor |

## Commands

### Offer Agent
- `/research [niche]` — Market research and niche validation
- `/competitor [name]` — Competitor analysis and gap finding
- `/offer [product]` — Offer packaging with value stack

### Attraction Agent
- `/funnel [type]` — Funnel architecture design
- `/content [platform] [type]` — Social media content creation
- `/lead-magnet [type] [topic]` — Lead magnet creation

### Conversion Agent
- `/sales-page [action] [product]` — Sales page blueprint
- `/copy [framework] [context]` — Persuasion copywriting
- `/objection [category] [product]` — Objection handling

### Deliver Agent
- `/payment-setup [step]` — SePay VietQR payment setup
- `/notification [step]` — Telegram bot notification setup
- `/delivery [method]` — Product delivery automation
- `/landing-page [product-type] [style]` — Build deployable HTML landing page
- `/deploy [method]` — Deploy to Vercel (CLI, Git, or drag & drop)
- `/payment-embed [pattern]` — Add SePay VietQR payment to landing pages

### Insights Agent
- `/analytics [platform] [period]` — Social media analytics
- `/revenue [period]` — Revenue reporting
- `/optimize [area]` — Performance optimization

## Skills

Each skill lives in `skills/{skill-name}/` with:
- `SKILL.md` — Main skill instructions and methodology
- `references/` — Frameworks, guides, and knowledge bases
- `templates/` — Ready-to-use fill-in templates (where applicable)

## Workflows

Step-by-step processes for end-to-end execution:

| Workflow | File | Duration |
|----------|------|----------|
| Offer Research | `workflows/offer-research-workflow.md` | 1-2 days |
| Attraction & Content | `workflows/attraction-content-workflow.md` | 3-5 days |
| Conversion & Sales | `workflows/conversion-sales-workflow.md` | 2-3 days |
| Delivery Automation | `workflows/delivery-automation-workflow.md` | 1-2 days |
| Insights & Reporting | `workflows/insights-reporting-workflow.md` | Weekly 1-2h |
| Content Automation | `workflows/content-automation-workflow.md` | Setup 1d + 4-6h/week |

## Rules

- Address users as "anh/chi" (Vietnamese business courtesy)
- All output content in English unless user requests Vietnamese
- Use Vietnamese examples and VND pricing when relevant
- Tech stack: SePay (payments), Telegram (notifications), FB/IG/TikTok/YouTube/Zalo (content)
- When user asks something ambiguous, map to the closest command and confirm before executing

## Command Execution

When a user types a slash command:

1. **Read** the command file: `commands/{command-name}.md`
2. **Load** the agent system prompt: `agents/{agent-file}.md`
3. **Read** the skill file: `skills/{skill-name}/SKILL.md`
4. **Read** relevant references from: `skills/{skill-name}/references/`
5. **Use** templates if available: `skills/{skill-name}/templates/`
6. **Follow** the workflow if doing end-to-end: `workflows/{workflow-file}.md`
7. **Output** the result in the format specified by the skill

If the user doesn't use a slash command, infer their intent and suggest the right command.
