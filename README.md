# Copywriting With Coach

An AI-powered copywriting coach that guides you through creating professional sales copy by asking dynamic questions.

## Overview

This skill transforms the traditional copywriting template approach into an interactive coaching experience. Instead of filling in blanks, you answer thoughtfully crafted questions, and the AI generates tailored sales copy.

## Features

- 🎯 **Multiple Copy Types**: VSL, Cold Email, Warm Email, Review Response, Local Deals, Webinar
- 🤖 **AI-Powered**: Dynamic follow-up questions based on your answers
- 📝 **Proven Frameworks**: Based on the Automatic Script methodology
- 💾 **Session Memory**: Your progress is saved automatically

## Usage

### In OpenClaw
```
I want to create sales copy for an online Python course
```

### CLI Mode
```bash
copywriting-with-coach "你的產品"
```

## Copy Types

| Type | Description |
|------|-------------|
| VSL | Video Sales Letter |
| Cold Email | Cold Email for new clients |
| Warm Email | Warm Email for existing customers |
| Review Backup | Review responses |
| Local Deals | Local service promotions |
| Webinar | Webinar registration pages |

## Example Conversation

```
You: I want to sell a Python online course
Bot: Great! Let me help you with the VSL framework.

Bot: What's the level of your target audience?
     1. Complete beginner
     2. Some basics
     3. Intermediate
     4. Advanced professional

You: Complete beginner

Bot: Got it. Next: What problems are they facing right now?
     (Be as specific as possible)...

You: All the tutorials out there are too complicated and nobody answers questions

Bot: Understood! Last question: What do you want them to do next?
     1. Buy now
     2. Free trial
     3. Book a consultation

You: Free trial

✨ Generating your sales copy...
```

## Files

- `SKILL.md` - Skill definition and metadata
- `copywriting_with_coach.py` - Main script

## License

Apache 2.0
