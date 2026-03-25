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
你要做銷售文案，產品是XXX
```

### CLI Mode
```bash
copywriting-with-coach "你的產品"
```

## Copy Types

| Type | Description |
|------|-------------|
| VSL | Video Sales Letter - 視頻銷售信 |
| Cold Email | 冷郵件 - 開發新客戶 |
| Warm Email | 暖郵件 - 現有客戶維護 |
| Review Backup | 評論回覆 |
| Local Deals | 在地優惠 - 本地服務 |
| Webinar | 網路研討會報名頁 |

## Example Conversation

```
You: 我要賣一個Python線上課程
Bot: 好的！讓我用 VSL 框架幫你。

Bot: 你的目標客戶是什麼程度？
     1. 完全新手
     2. 有些基礎
     3. 中級進階
     4. 高級專業

You: 完全新手

Bot: 明白。接下來：他們現在面臨什麼問題？
     （盡可能具體描述）...

You: 市面上的教程都太複雜了，而且沒人回答問題

Bot: 了解！最後一個問題：你希望客戶下一步做什麼？
     1. 立即購買
     2. 免費試用
     3. 預約諮詢

You: 免費試用

✨ 生成的销售复制...
```

## Files

- `SKILL.md` - Skill definition and metadata
- `copywriting_with_coach.py` - Main script

## License

Apache 2.0
