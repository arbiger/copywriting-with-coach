---
name: copywriting-with-coach
description: AI-powered copywriting coach that asks dynamic questions to guide you through creating sales copy (VSL, Cold Email, etc.). Based on the Automatic Script framework but enhanced with AI.
tags: [copywriting, marketing, sales, coach, VSL, email]
---

# Copywriting With Coach

An AI-powered copywriting coach that guides you through creating professional sales copy by asking dynamic questions.

## Concept

Instead of giving you a template, this skill acts as a **copywriting coach** that:
1. Learns about your product/service through questions
2. Asks contextually relevant questions based on your answers
3. Generates tailored sales copy at the end

## Supported Copy Types

| Type | Description |
|------|-------------|
| `vsl` | Video Sales Letter |
| `cold-email` | Cold Email |
| `warm-email` | Warm Email |
| `review-backup` | Review Backup/Response |
| `local-deals` | Local Service Deals |
| `webinar` | Webinar Registration |

## How It Works

### Conversation Flow

```
You: "我要賣線上課程，關於Python編程"
Bot: "好的！讓我用 VSL 框架幫你。"

Bot: "第一題：你的目標學生是什麼程度？"
     "(A) 完全新手  (B) 有基礎  (C) 想進階"

You: "完全新手"

Bot: "明白。接下來：他們現在面臨什麼問題？"
     "（盡可能具體描述）"
```

### Question Categories by Type

#### VSL Questions
1. Product type & category
2. Target audience & their level
3. Main problem/pain point
4. Current solutions they've tried
5. Your unique solution approach
6. Key benefits (top 3)
7. Objections to anticipate
8. Call to action

#### Cold Email Questions
1. Who is your ideal customer?
2. What problem do you solve?
3. What's your offer/value proposition?
4. Call to action

## Usage

```bash
# Start a new copywriting session
copywriting-with-coach "你的產品或服務"

# Or in conversation:
"我要做一個銷售文案，產品是..."
```

## Output

After collecting answers, the skill generates:
1. **Hook/Opening** - Attention-grabbing intro
2. **Problem Agitation** - Describe their pain
3. **Solution Presentation** - Your offer
4. **Social Proof** - Testimonials, results
5. **Objection Handling** - Address concerns
6. **Call to Action** - What to do next

## Examples

### VSL Output Example
```
[Hook]
"Does this sound familiar? You've been wanting to learn Python, but..."

[Problem Agitation]
"You're tired of confusing tutorials that assume you already know..."

[Solution]
"That's why I created Python For Complete Beginners..."

[CTA]
"Click below to get started..."
```

### Cold Email Output Example
```
Subject: Quick question about [their goal]

Hi [Name],

I noticed [specific observation about their business].

[One-line value prop].

Would you be open to a 15-minute call this week?

Best,
[Your name]
```

## Memory

Session data is stored in:
`memory/copywriting-sessions/YYYY-MM-DD-product-slug.md`

## Notes

- If user wants to change copy type mid-session, acknowledge and restart with new framework
- For short responses, ask follow-up questions to gather more detail
- Suggest A/B variations when generating final copy
