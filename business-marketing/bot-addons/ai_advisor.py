# -*- coding: utf-8 -*-
"""
ai_advisor.py — Lớp AI tư vấn cắm vào bot Telegram đã có (bot-aithucchien).
KHÔNG đụng tới SePay/giao hàng. Chỉ trả lời tin nhắn tự do (nhánh else của webhook).

Cách dùng trong app.py:
    from ai_advisor import ai_reply
    ...
    else:                                  # tin nhắn không phải lệnh
        reply = ai_reply(chat_id, text)
        if reply:
            tg_send(chat_id, reply, tg_keyboard())
        else:
            tg_send(chat_id, "Tôi chưa hiểu lệnh đó. Anh/chị hãy gõ /start để xem menu chính.", tg_keyboard())

Env cần thêm (Railway Variables):
    LLM_API_KEY   = (OpenAI key, hoặc Groq key...)   # để trống -> ai_reply trả None (bot dùng câu mặc định)
    LLM_BASE_URL  = https://api.openai.com/v1         # Groq: https://api.groq.com/openai/v1
    LLM_MODEL     = gpt-4o-mini                        # Groq: llama-3.3-70b-versatile
"""
import os, pathlib
try:
    import requests
except ImportError:
    requests = None

BASE      = pathlib.Path(__file__).parent
LLM_KEY   = os.environ.get("LLM_API_KEY", "")
LLM_URL   = os.environ.get("LLM_BASE_URL", "https://api.openai.com/v1").rstrip("/")
LLM_MODEL = os.environ.get("LLM_MODEL", "gpt-4o-mini")
MAXH      = 10

def _load_brain():
    f = BASE / "advisor_brain.md"
    return f.read_text(encoding="utf-8") if f.exists() else \
        "Bạn là trợ lý tư vấn bán hàng thân thiện. Hướng khách gõ /start để xem menu và /mua_combo để mua."

BRAIN   = _load_brain()
HISTORY = {}   # chat_id -> [{role, content}, ...]

def _remember(chat_id, role, content):
    h = HISTORY.setdefault(chat_id, [])
    h.append({"role": role, "content": content})
    del h[:-MAXH]

def ai_reply(chat_id, user_text):
    """Trả lời tư vấn bằng AI. Trả None nếu chưa cấu hình AI hoặc lỗi -> caller tự fallback."""
    if not LLM_KEY or requests is None or not (user_text or "").strip():
        return None
    _remember(chat_id, "user", user_text)
    msgs = [{"role": "system", "content": BRAIN}] + HISTORY.get(chat_id, [])
    try:
        r = requests.post(
            f"{LLM_URL}/chat/completions",
            headers={"Authorization": f"Bearer {LLM_KEY}", "Content-Type": "application/json"},
            json={"model": LLM_MODEL, "messages": msgs, "temperature": 0.5, "max_tokens": 500},
            timeout=30,
        )
        reply = r.json()["choices"][0]["message"]["content"].strip()
        _remember(chat_id, "assistant", reply)
        return reply or None
    except Exception as e:
        print("ai_advisor error:", e)
        return None

def reset(chat_id):
    HISTORY.pop(chat_id, None)

if __name__ == "__main__":
    # selftest: không cần mạng. Kiểm tra brain load + fallback khi không có key.
    assert isinstance(BRAIN, str) and len(BRAIN) > 20, "brain phải load được"
    saved = LLM_KEY
    globals()["LLM_KEY"] = ""          # ép không có key
    assert ai_reply(1, "tư vấn giúp em") is None, "không key -> phải trả None (fallback)"
    globals()["LLM_KEY"] = saved
    print("ai_advisor selftest PASS ✓ (brain", len(BRAIN), "ký tự )")
