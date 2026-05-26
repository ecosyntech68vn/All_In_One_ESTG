#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Sales Assistant Bot (Telegram) — Cỗ Máy Nội Dung
- Tư vấn & bán hàng thông minh bằng LLM (tự hướng dẫn khách).
- Trả lời FAQ, xử lý lăn tăn, dẫn khách qua phễu tới mua.
- Bắt lead, hướng dẫn thanh toán VietQR, báo chủ shop, chuyển tư vấn viên.
- FALLBACK MENU khi không có/khi mất AI (offline-safe).
Chạy:  python bot.py            (chạy bot thật, cần .env)
       python bot.py --selftest (kiểm tra logic, không cần token/mạng)
"""
import os, sys, json, time, pathlib
try:
    import requests
except ImportError:
    requests = None

BASE = pathlib.Path(__file__).parent

# ---------- Cấu hình ----------
def load_env():
    env = {}
    f = BASE / ".env"
    if f.exists():
        for line in f.read_text(encoding="utf-8").splitlines():
            s = line.strip()
            if not s or s.startswith("#") or "=" not in s:
                continue
            k, v = s.split("=", 1)
            env[k.strip()] = v.strip().strip('"').strip("'")
    for k in ("TELEGRAM_BOT_TOKEN", "LLM_API_KEY", "LLM_BASE_URL", "LLM_MODEL",
              "OWNER_CHAT_ID", "BANK_NAME", "BANK_ACCOUNT", "BANK_HOLDER",
              "PRICE", "PRODUCT_NAME", "LANDING_URL", "LEAD_MAGNET_URL"):
        if os.environ.get(k):
            env[k] = os.environ[k]
    return env

CFG       = load_env()
TOKEN     = CFG.get("TELEGRAM_BOT_TOKEN", "")
API       = f"https://api.telegram.org/bot{TOKEN}"
LLM_KEY   = CFG.get("LLM_API_KEY", "")
LLM_URL   = CFG.get("LLM_BASE_URL", "https://api.openai.com/v1").rstrip("/")
LLM_MODEL = CFG.get("LLM_MODEL", "gpt-4o-mini")
OWNER     = CFG.get("OWNER_CHAT_ID", "")
PRODUCT   = CFG.get("PRODUCT_NAME", "Cỗ Máy Nội Dung")
PRICE     = CFG.get("PRICE", "990.000đ")
LANDING   = CFG.get("LANDING_URL", "(chưa cấu hình link landing)")
LEADMAG   = CFG.get("LEAD_MAGNET_URL", "(chưa cấu hình link quà tặng)")

# ---------- Bộ não (brain) — chỉnh trong assistant_config.md ----------
def load_brain():
    f = BASE / "assistant_config.md"
    base = f.read_text(encoding="utf-8") if f.exists() else "Bạn là trợ lý bán hàng thân thiện, tư vấn không ép."
    facts = (
        f"\n\n## DỮ LIỆU ĐỘNG (ưu tiên dùng số liệu này)\n"
        f"- Sản phẩm: {PRODUCT}\n- Giá: {PRICE}\n- Trang bán (landing): {LANDING}\n"
        f"- Quà miễn phí (lead magnet): {LEADMAG}\n"
        f"- Thanh toán: {CFG.get('BANK_NAME','')} | STK {CFG.get('BANK_ACCOUNT','')} | {CFG.get('BANK_HOLDER','')}\n"
    )
    return base + facts

BRAIN   = load_brain()
HISTORY = {}     # chat_id -> [{role, content}, ...]
STATE   = {}     # chat_id -> {"mode": "lead"/"buy", "step": "...", "data": {...}}
MAXH    = 12

MENU = [("📦 Sản phẩm là gì?", "intro"), ("💰 Bảng giá & ưu đãi", "price"),
        ("❓ Câu hỏi thường gặp", "faq"), ("🎁 Nhận quà miễn phí", "lead"),
        ("🛒 Mua ngay", "buy"), ("🙋 Gặp tư vấn viên", "human")]

# ---------- Telegram API ----------
def tg(method, **params):
    try:
        return requests.post(f"{API}/{method}", json=params, timeout=65).json()
    except Exception as e:
        print("tg error:", e); return {}

def send(chat_id, text, with_menu=False):
    kb = {"inline_keyboard": [[{"text": t, "callback_data": d}] for t, d in MENU]} if with_menu else None
    return tg("sendMessage", chat_id=chat_id, text=text, parse_mode="HTML",
              reply_markup=kb, disable_web_page_preview=True)

def notify_owner(text):
    if OWNER:
        send(OWNER, "🔔 " + text)

# ---------- LLM (OpenAI-compatible) ----------
def llm(chat_id, user_text):
    if not LLM_KEY or requests is None:
        return None
    msgs = [{"role": "system", "content": BRAIN}] + HISTORY.get(chat_id, []) + [{"role": "user", "content": user_text}]
    try:
        r = requests.post(f"{LLM_URL}/chat/completions",
                          headers={"Authorization": f"Bearer {LLM_KEY}", "Content-Type": "application/json"},
                          json={"model": LLM_MODEL, "messages": msgs, "temperature": 0.5, "max_tokens": 500},
                          timeout=60)
        return r.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("llm error:", e); return None

def remember(chat_id, role, content):
    h = HISTORY.setdefault(chat_id, [])
    h.append({"role": role, "content": content})
    del h[:-MAXH]

# ---------- Nội dung tĩnh (đáng tin, không cần AI) ----------
def text_intro():
    return (f"<b>{PRODUCT}</b> là hệ thống nội dung tự động cho coach / người bán khóa học, dịch vụ.\n\n"
            "Bạn biến 1 ý tưởng thành 5 bài đăng đa nền tảng, lên lịch theo giờ vàng VN, "
            "và tự động kéo học viên/khách về Zalo/Messenger — chỉ ~5 giờ/tuần.\n\n"
            "👉 Không phải khóa lý thuyết, mà là bộ công cụ chạy sẵn (bê về dùng ngay).")

def text_price():
    return (f"💰 <b>Giá mở bán: {PRICE}</b> (giá thường 1.490.000đ)\n"
            "Tự thuê rời sẽ tốn 12–25 triệu + 3–6 tháng.\n\n"
            "🛡️ Bảo đảm theo kết quả: hoàn 100% trong 14 ngày nếu áp dụng đủ mà không ra batch nội dung đầu tiên.\n"
            "🎁 Ưu đãi: 50 khách đầu tặng 3 tháng Câu lạc bộ.\n\n"
            f"Xem chi tiết: {LANDING}")

def text_faq():
    return ("❓ <b>Hay gặp:</b>\n\n"
            "• <b>Không rành công nghệ dùng được không?</b> Được — prompt copy-paste, AI trợ lý, video cầm tay.\n"
            "• <b>Có phải khóa học không?</b> Không — là hệ thống chạy sẵn.\n"
            "• <b>Hợp với ai?</b> Coach, người bán khóa học, dịch vụ, tư vấn online.\n"
            "• <b>Mất bao lâu?</b> Cài ~1 ngày, sau đó ~5 giờ/tuần.\n"
            "• <b>Không hiệu quả?</b> Hoàn tiền 14 ngày.")

# ---------- Xử lý ----------
def start_capture(chat_id, mode):
    STATE[chat_id] = {"mode": mode, "step": "name", "data": {}}
    msg = "Tuyệt vời ạ! 🎁 Cho em xin <b>tên</b> của anh/chị nhé?" if mode == "lead" \
          else "Cảm ơn anh/chị đã quan tâm! 🛒 Cho em xin <b>tên</b> để em hỗ trợ đặt mua nhé?"
    send(chat_id, msg)

def payment_text(name):
    return (f"Cảm ơn <b>{name}</b> ạ! 🛒 Thông tin thanh toán <b>{PRODUCT}</b> — <b>{PRICE}</b>:\n\n"
            f"🏦 Ngân hàng: {CFG.get('BANK_NAME','[THAY ngân hàng]')}\n"
            f"💳 Số TK: {CFG.get('BANK_ACCOUNT','[THAY số TK]')}\n"
            f"👤 Chủ TK: {CFG.get('BANK_HOLDER','[THAY tên]')}\n"
            f"📝 Nội dung CK: COMAY {name}\n\n"
            "Chuyển xong anh/chị nhắn 'đã CK' giúp em, em gửi sản phẩm + hướng dẫn ngay ạ! 🙌")

def process_capture(chat_id, text):
    st = STATE[chat_id]
    if st["step"] == "name":
        st["data"]["name"] = text.strip()
        st["step"] = "phone"
        send(chat_id, "Dạ, cho em xin thêm <b>số điện thoại/Zalo</b> để tiện liên hệ ạ?")
        return
    if st["step"] == "phone":
        st["data"]["phone"] = text.strip()
        d = st["data"]; mode = st["mode"]
        rec = {"time": time.strftime("%Y-%m-%d %H:%M"), "mode": mode,
               "name": d.get("name"), "phone": d.get("phone"), "chat_id": chat_id}
        try:
            with open(BASE / "leads.jsonl", "a", encoding="utf-8") as fh:
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
        except Exception as e:
            print("save lead error:", e)
        if mode == "lead":
            send(chat_id, f"Quà của anh/chị đây ạ 🎁: {LEADMAG}\n\nCó gì cần tư vấn cứ nhắn em nhé!", with_menu=True)
            notify_owner(f"LEAD MỚI: {d.get('name')} | {d.get('phone')}")
        else:
            send(chat_id, payment_text(d.get("name", "anh/chị")))
            notify_owner(f"ĐƠN MỚI (chờ CK): {d.get('name')} | {d.get('phone')}")
        STATE.pop(chat_id, None)

def handle_callback(chat_id, data, cbid, user):
    tg("answerCallbackQuery", callback_query_id=cbid)
    if data == "intro":   send(chat_id, text_intro(), with_menu=True)
    elif data == "price": send(chat_id, text_price(), with_menu=True)
    elif data == "faq":   send(chat_id, text_faq(), with_menu=True)
    elif data == "lead":  start_capture(chat_id, "lead")
    elif data == "buy":   start_capture(chat_id, "buy")
    elif data == "human":
        send(chat_id, "Em đã chuyển thông tin cho tư vấn viên, anh/chị chờ chút sẽ được hỗ trợ trực tiếp ạ 🙋")
        notify_owner(f"KHÁCH CẦN TƯ VẤN VIÊN — chat_id {chat_id} ({user})")

def handle_text(chat_id, text, user):
    if chat_id in STATE:
        process_capture(chat_id, text)
        return
    low = text.lower()
    if text.startswith("/start"):
        send(chat_id, f"Xin chào 👋 Em là trợ lý của <b>{PRODUCT}</b>. Em giúp anh/chị tìm hiểu và đặt mua nhé!\n"
                      "Anh/chị chọn nhanh bên dưới, hoặc cứ nhắn câu hỏi tự nhiên ạ 😊", with_menu=True)
        return
    if any(w in low for w in ("mua", "đặt", "order", "thanh toán", "chuyển khoản")):
        start_capture(chat_id, "buy"); return
    if any(w in low for w in ("tư vấn viên", "gặp người", "nhân viên", "gặp ai")):
        send(chat_id, "Em chuyển cho tư vấn viên hỗ trợ anh/chị ngay ạ 🙋")
        notify_owner(f"KHÁCH CẦN TƯ VẤN VIÊN — chat_id {chat_id} ({user})"); return
    remember(chat_id, "user", text)
    reply = llm(chat_id, text)
    if reply:
        remember(chat_id, "assistant", reply)
        send(chat_id, reply)
    else:
        send(chat_id, "Em sẵn sàng hỗ trợ ạ! Anh/chị chọn nhanh một mục bên dưới nhé 👇", with_menu=True)

def handle_update(u):
    if "callback_query" in u:
        cq = u["callback_query"]
        handle_callback(cq["message"]["chat"]["id"], cq.get("data", ""),
                        cq["id"], cq["from"].get("username") or cq["from"].get("first_name"))
    elif "message" in u and "text" in u["message"]:
        m = u["message"]
        handle_text(m["chat"]["id"], m["text"], m["from"].get("username") or m["from"].get("first_name"))

# ---------- Vòng lặp chính ----------
def run():
    if not TOKEN:
        print("THIẾU TELEGRAM_BOT_TOKEN trong .env — xem README.md"); sys.exit(1)
    if requests is None:
        print("Cần cài: pip install requests"); sys.exit(1)
    print(f"Bot đang chạy. AI: {'BẬT' if LLM_KEY else 'TẮT (chạy menu fallback)'}")
    offset = None
    while True:
        try:
            r = requests.get(f"{API}/getUpdates", params={"timeout": 50, "offset": offset}, timeout=60).json()
            for u in r.get("result", []):
                offset = u["update_id"] + 1
                handle_update(u)
        except KeyboardInterrupt:
            print("Dừng bot."); break
        except Exception as e:
            print("loop error:", e); time.sleep(3)

# ---------- Self-test (không cần token/mạng) ----------
def selftest():
    global send, notify_owner, llm
    out = []
    send = lambda cid, text, with_menu=False: out.append(("send", text[:60], with_menu))
    notify_owner = lambda text: out.append(("owner", text))
    llm = lambda cid, t: None
    assert PRICE in text_price()
    handle_text(1, "/start", "tester");                      assert out[-1][2] is True
    handle_text(1, "cho mình hỏi sản phẩm này", "tester");   assert out[-1][2] is True
    handle_callback(1, "buy", "cb1", "tester")
    handle_text(1, "Nguyen Van A", "tester")
    handle_text(1, "0901234567", "tester")
    assert any(o[0] == "owner" and "ĐƠN MỚI" in o[1] for o in out), "phải báo chủ shop"
    assert 1 not in STATE, "state phải clear"
    print("Self-test PASS ✓ —", len(out), "actions")

if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
    else:
        run()
