#!/usr/bin/env python3
"""
Copywriting With Coach - AI-powered copywriting coach

Analyzes user input and asks dynamic questions to guide them through
creating professional sales copy based on proven frameworks.
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Session storage
SESSION_DIR = Path.home() / ".openclaw" / "workspace" / "memory" / "copywriting-sessions"
SESSION_DIR.mkdir(parents=True, exist_ok=True)

# Question frameworks by copy type
QUESTION_FRAMES = {
    "vsl": {
        "name": "Video Sales Letter (VSL)",
        "description": "視頻銷售信 - 適合線上課程、數位產品、訂閱服務",
        "questions": [
            {
                "id": "product_type",
                "question": "你的產品是什麼類型？",
                "options": ["線上課程", "軟體/SaaS", "電子書/報告", "訓練服務", "訂閱服務", "實體產品", "其他"],
                "follow_ups": {
                    "線上課程": ["這個課程是關於什麼主題？", "課程時長大約多久？"],
                    "軟體/SaaS": ["這個軟體解決什麼問題？", "月費还是年費？"],
                }
            },
            {
                "id": "audience",
                "question": "你的目標客戶是什麼程度？",
                "options": ["完全新手", "有些基礎", "中級進階", "高級專業"],
                "key_point": "了解客戶程度能幫助調整用語和期望管理"
            },
            {
                "id": "main_problem",
                "question": "他們現在最大的問題/痛點是什麼？",
                "placeholder": "盡可能具體描述他們面臨的困境...",
                "multi": True
            },
            {
                "id": "tried_solutions",
                "question": "他們之前嘗試過什麼解決方案？為什麼失敗了？",
                "placeholder": "描述他們過去嘗試過的方法...",
                "optional": True
            },
            {
                "id": "your_solution",
                "question": "你的方案有什麼獨特之處？",
                "placeholder": "什麼讓你的方案與眾不同？",
                "required": True
            },
            {
                "id": "top_benefits",
                "question": "列舉3個最重要的好處",
                "placeholder": "1. ...\n2. ...\n3. ...",
                "multi": True
            },
            {
                "id": "objections",
                "question": "你認為潛在客戶會有的3個反對意見？",
                "placeholder": "1. 價格太貴\n2. 沒時間\n3. ..."

            },
            {
                "id": "guarantee",
                "question": "你有提供任何保證嗎？（退款、不滿意免費調整等）",
                "placeholder": "描述你的保障方案...",
                "optional": True
            },
            {
                "id": "cta",
                "question": "你希望客戶下一步做什麼？",
                "options": ["立即購買", "免費試用", "預約諮詢", "加入LINE", "報名課程"],
                "key_point": "明確的行動呼籲能提高轉化率"
            }
        ]
    },
    "cold-email": {
        "name": "Cold Email (冷郵件)",
        "description": "適合開發新客戶、B2B銷售、顧問服務",
        "questions": [
            {
                "id": "target",
                "question": "你的目標客戶是什麼人？",
                "placeholder": "描述他們的職業、職位、公司類型...",
                "required": True
            },
            {
                "id": "their_problem",
                "question": "他們正面臨什麼問題？",
                "placeholder": "盡量具體描述...",
                "required": True
            },
            {
                "id": "your_solution",
                "question": "你如何幫助他們？",
                "placeholder": "一句話描述你的價值...",
                "required": True
            },
            {
                "id": "specific_detail",
                "question": "有什麼具體的細節或數據可以增加可信度？",
                "placeholder": "例如：客戶成效、經驗年限、具體數字...",
                "optional": True
            },
            {
                "id": "cta",
                "question": "你希望他們做什麼？",
                "options": ["回覆此郵件", "預約電話", "點擊連結", "報名參加"],
                "required": True
            }
        ]
    },
    "warm-email": {
        "name": "Warm Email (暖郵件)",
        "description": "適合現有客戶、舊名單、已經認識的人",
        "questions": [
            {
                "id": "relationship",
                "question": "你與收件人的關係是？",
                "options": ["現有客戶", "舊客戶", "曾諮詢過的人", "活動認識的人"]
            },
            {
                "id": "purpose",
                "question": "這封郵件的主要目的？",
                "options": ["推薦新產品", "喚回流失客戶", "追加銷售", "邀請活動", "只是保持聯繫"]
            },
            {
                "id": "offer",
                "question": "你有什麼特別的優惠或內容？",
                "placeholder": "描述你的Offer...",
                "optional": True
            }
        ]
    },
    "review-backup": {
        "name": "Review Backup (評論回覆)",
        "description": "回覆顧客評論，正面或負面皆可",
        "questions": [
            {
                "id": "review_type",
                "question": "這是正面還是負面評論？",
                "options": ["正面評論", "負面評論", "中等評論"]
            },
            {
                "id": "review_content",
                "question": "評論內容是什麼？",
                "placeholder": "貼上或描述評論內容...",
                "required": True
            },
            {
                "id": "business_response",
                "question": "你希望如何處理這個評論？",
                "options": ["感謝並邀請回購", "解釋並提供補償", "邀請私下聯繫", "單純感謝"]
            }
        ]
    },
    "local-deals": {
        "name": "Local Deals (在地優惠)",
        "description": "適合本地服務業：水電工、HVAC、園藝等",
        "questions": [
            {
                "id": "service_type",
                "question": "你提供什麼服務？",
                "placeholder": "例如：冷氣安裝、水管維修、屋頂工程...",
                "required": True
            },
            {
                "id": "service_area",
                "question": "你在哪些地區服務？",
                "placeholder": "例如：台中市、台北市...",
                "required": True
            },
            {
                "id": "main_problem",
                "question": "客戶最常見的問題是什麼？",
                "placeholder": "描述他們面臨的問題...",
                "required": True
            },
            {
                "id": "why_choose_you",
                "question": "為什麼選擇你不選擇別人？",
                "placeholder": "你的獨特優勢...",
                "required": True
            },
            {
                "id": "deal_offer",
                "question": "你有什麼優惠？",
                "placeholder": "例如：首趟免費估價、打折、贈品...",
                "optional": True
            }
        ]
    },
    "webinar": {
        "name": "Webinar (網路研討會)",
        "description": "研討會報名頁銷售信",
        "questions": [
            {
                "id": "webinar_topic",
                "question": "研討會主題是什麼？",
                "placeholder": "具體的議題...",
                "required": True
            },
            {
                "id": "target_audience",
                "question": "誰應該參加？",
                "placeholder": "目標觀眾是...",
                "required": True
            },
            {
                "id": "key_takeaways",
                "question": "參加者會學到什麼？（列舉3點）",
                "placeholder": "1. ...\n2. ...\n3. ...",
                "multi": True
            },
            {
                "id": " presenter",
                "question": "主讲人是谁？有什么背景？",
                "placeholder": "介绍主讲人...",
                "required": True
            },
            {
                "id": "date_time",
                "question": "研討會時間？",
                "placeholder": "日期和時間...",
                "required": True
            },
            {
                "id": "offer",
                "question": "有什麼特別的BONUS或價值？",
                "placeholder": "限時報名、獨家資料...",
                "optional": True
            }
        ]
    }
}


def get_session_file(user_id: str) -> Path:
    """Get session file path for user."""
    today = datetime.now().strftime("%Y-%m-%d")
    return SESSION_DIR / f"{today}-{user_id}.json"


def load_session(user_id: str) -> dict:
    """Load existing session or create new one."""
    session_file = get_session_file(user_id)
    if session_file.exists():
        with open(session_file) as f:
            return json.load(f)
    return {}


def save_session(user_id: str, session: dict):
    """Save session to file."""
    session_file = get_session_file(user_id)
    with open(session_file, 'w') as f:
        json.dump(session, f, indent=2, ensure_ascii=False)


def start_session(copy_type: str, product: str) -> dict:
    """Start a new copywriting session."""
    if copy_type not in QUESTION_FRAMES:
        return {
            "error": f"Unknown copy type: {copy_type}",
            "available_types": list(QUESTION_FRAMES.keys())
        }
    
    framework = QUESTION_FRAMES[copy_type]
    
    session = {
        "copy_type": copy_type,
        "product": product,
        "framework_name": framework["name"],
        "answers": {},
        "current_question_index": 0,
        "status": "in_progress",
        "started_at": datetime.now().isoformat()
    }
    
    return session


def get_current_question(session: dict) -> dict:
    """Get the current question based on session state."""
    copy_type = session["copy_type"]
    framework = QUESTION_FRAMES[copy_type]
    questions = framework["questions"]
    current_index = session["current_question_index"]
    
    if current_index >= len(questions):
        return None  # All questions answered
    
    return questions[current_index]


def format_question(q: dict, session: dict) -> str:
    """Format a question for display."""
    lines = []
    lines.append(f"**{q['question']}**")
    
    if 'options' in q:
        lines.append("")
        for i, opt in enumerate(q['options'], 1):
            lines.append(f"  {i}. {opt}")
    
    if 'placeholder' in q:
        lines.append("")
        lines.append(f"（輸入你的回答）")
    
    if 'key_point' in q:
        lines.append("")
        lines.append(f"💡 *{q['key_point']}*")
    
    return "\n".join(lines)


def generate_copy(session: dict) -> str:
    """Generate the final sales copy based on answers."""
    copy_type = session["copy_type"]
    answers = session["answers"]
    product = session["product"]
    
    if copy_type == "vsl":
        return generate_vsl(product, answers)
    elif copy_type == "cold-email":
        return generate_cold_email(product, answers)
    elif copy_type == "warm-email":
        return generate_warm_email(product, answers)
    elif copy_type == "review-backup":
        return generate_review_backup(answers)
    elif copy_type == "local-deals":
        return generate_local_deal(product, answers)
    elif copy_type == "webinar":
        return generate_webinar(product, answers)
    
    return "複製生成功能尚未支援此類型。"


def generate_vsl(product: str, answers: dict) -> str:
    """Generate VSL copy."""
    audience_level = answers.get("audience", "一般大眾")
    problem = answers.get("main_problem", "這個問題")
    solution = answers.get("your_solution", "我們的方案")
    benefits = answers.get("top_benefits", [])
    objections = answers.get("objections", [])
    cta = answers.get("cta", "立即行動")
    guarantee = answers.get("guarantee", "")
    
    benefits_text = "\n".join([f"• {b}" for b in benefits]) if benefits else "• 快速看到成效"
    
    copy = f"""## {product} - 視頻銷售信

---

### 🎣 開場鉤子 (Hook)
「你是否是{audience_level}，正在為{problem}而困擾？」

---

### 😤 問題 agitation
「你嘗試過很多方法，但總是...」
{problem}

---

### 💡 解決方案 (Solution)
「這就是為什麼我們創建了 {product}...」
{solution}

---

### ✨ 獨特好處
{benefits_text}

---

### 🛡️ 反對意見處理
「你可能會想說...」
{chr(10).join([f'「{o}」→ 「確實，但...」' for o in objections]) if objections else '「這適合我嗎？」→ 「我們專為{audience_level}設計"'}

---

### 🎁 保證
{guarantee if guarantee else "我們提供滿意保證"}

---

### 📞 行動呼籲 (CTA)
👉 *{cta}*

"""
    return copy


def generate_cold_email(product: str, answers: dict) -> str:
    """Generate cold email copy."""
    target = answers.get("target", "目標客戶")
    their_problem = answers.get("their_problem", "這個問題")
    solution = answers.get("your_solution", "我們可以幫忙")
    cta = answers.get("cta", "回覆我")
    specific = answers.get("specific_detail", "")
    
    copy = f"""## Cold Email - {product}

---

**Subject:** 快速問題關於{product}

---

Hi [姓名],

我在研究時注意到了{target}。

{their_problem}

{solution}。

{f'具體來說：{specific}' if specific else ''}

有興趣進一步聊聊嗎？

Best regards,
[你的名字]

"""
    return copy


def generate_warm_email(product: str, answers: dict) -> str:
    """Generate warm email copy."""
    relationship = answers.get("relationship", "朋友")
    purpose = answers.get("purpose", "分享好東西")
    offer = answers.get("offer", "")
    
    copy = f"""## Warm Email - {product}

---

Hi [名字],

Hope you've been well! 

最近我們更新了{product}，{purpose}。

{f'這次有一些很棒的內容：{offer}' if offer else ''}

如果有興趣，隨時告訴我！

Best,
[你的名字]

"""
    return copy


def generate_review_backup(answers: dict) -> str:
    """Generate review response."""
    review_type = answers.get("review_type", "正面")
    review_content = answers.get("review_content", "")
    response_type = answers.get("business_response", "感謝")
    
    if review_type == "正面評論":
        copy = f"""## 回覆正面評論

感謝您的好評！很开心能帮到您。如果您有任何問題，或想要更多资源，随时联系我们！

期待再次為您服務 🙏
"""
    elif review_type == "負面評論":
        copy = f"""## 回覆負面評論

感謝您分享您的體驗。對於您的不愉快經歷，我們深感抱歉。

我們已經收到您的反饋，並會積極改進。如果您願意，可以私信我們，我們希望有機會親自解決這個問題。

真誠地，
[公司名稱]
"""
    else:
        copy = f"""## 回覆中等評論

感謝您的評論！我們重視每一位客戶的意見。

如果您有任何建議或疑問，歡迎隨時與我們聯繫。我們會努力做得更好！

Best,
[公司名稱]
"""
    
    return copy


def generate_local_deal(product: str, answers: dict) -> str:
    """Generate local deals copy."""
    service = answers.get("service_type", "服務")
    area = answers.get("service_area", "本地")
    problem = answers.get("main_problem", "需求")
    why_you = answers.get("why_choose_you", "專業可靠")
    deal = answers.get("deal_offer", "")
    
    copy = f"""## {service} - 在地優惠

---

{area}的朋友，你們好！

家裡有{problem}的困擾嗎？

我們專門提供{service}服務，{why_you}。

{f'現在特別優惠：{deal}' if deal else ''}

📞 立即致電：[電話]
📍 服務範圍：{area}

"""
    return copy


def generate_webinar(product: str, answers: dict) -> str:
    """Generate webinar registration copy."""
    topic = answers.get("webinar_topic", "這個主題")
    audience = answers.get("target_audience", "相關人士")
    takeaways = answers.get("key_takeaways", [])
    presenter = answers.get("presenter", "專家")
    date_time = answers.get("date_time", "待定")
    offer = answers.get("offer", "")
    
    takeaways_text = "\n".join([f"{i+1}. {t}" for i, t in enumerate(takeaways)]) if takeaways else "實用技巧"
    
    copy = f"""## 網路研討會報名 - {topic}

---

### 🎤 報名這個研討會！

**主題：** {topic}
**時間：** {date_time}

---

### 誰應該參加？
{audience}

---

### 你會學到什麼？
{takeaways_text}

---

### 主講人
{presenter}

{f"""
### 🎁 限時BONUS
{offer}
""" if offer else ""}

---

👉 **立即報名：** [報名連結]

座位有限，報名從速！

"""
    return copy


def main():
    """Main CLI entry point."""
    import sys
    
    if len(sys.argv) < 2:
        print("使用方法: copywriting-with-coach <產品或服務>")
        print("")
        print("範例:")
        print("  copywriting-with-coach 線上Python課程")
        print("  copywriting-with-coach B2B軟體銷售")
        print("")
        print("支援類型:")
        for key, val in QUESTION_FRAMES.items():
            print(f"  - {key}: {val['name']}")
        sys.exit(1)
    
    product = " ".join(sys.argv[1:])
    
    print("=" * 50)
    print("🎯 Copywriting With Coach")
    print("=" * 50)
    print()
    print(f"產品/服務：{product}")
    print()
    print("請選擇複製類型：")
    print()
    for i, (key, val) in enumerate(QUESTION_FRAMES.items(), 1):
        print(f"  {i}. {val['name']}")
        print(f"     {val['description']}")
        print()
    
    # For CLI, we'll start with VSL as default
    copy_type = "vsl"
    framework = QUESTION_FRAMES[copy_type]
    
    print(f"選擇：{framework['name']}")
    print()
    print("請回答以下問題（輸入 'q' 結束）：")
    print()
    
    session = start_session(copy_type, product)
    save_session("cli", session)
    
    for q in framework["questions"]:
        question_text = format_question(q, session)
        print(question_text)
        print()
        
        answer = input("你的回答: ").strip()
        if answer.lower() == 'q':
            print("再見！有機會再繼續。")
            break
        
        session["answers"][q["id"]] = answer
        session["current_question_index"] += 1
        save_session("cli", session)
        print()
    
    if session["current_question_index"] >= len(framework["questions"]):
        print("=" * 50)
        print("✨ 生成的销售复制")
        print("=" * 50)
        print()
        print(generate_copy(session))


if __name__ == "__main__":
    main()
