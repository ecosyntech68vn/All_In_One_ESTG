# -*- coding: utf-8 -*-
"""
zalo.py — Kết nối Zalo OA, DÙNG CHUNG bộ não AI với Telegram (ai_advisor).
Là một Flask Blueprint cắm vào app.py đã có:

    from zalo import zalo_bp
    app.register_blueprint(zalo_bp)

Khách nhắn Zalo OA -> Zalo gửi event về /zalo-webhook -> AI tư vấn -> gửi trả qua Zalo OA API.
Phần thanh toán/giao hàng tự động vẫn nằm ở luồng Telegram + Sepay (xem INTEGRATION.md mục Zalo).

Env cần thêm:
    ZALO_OA_ACCESS_TOKEN = (access token của OA — xem INTEGRATION.md; token hết hạn ~25h, cần refresh)
    ZALO_APP_SECRET      = (tùy chọn) để xác thực chữ ký webhook
    ZALO_STRICT          = "1" để bắt buộc đúng chữ ký (mặc định "0" = nhận hết, chỉ cảnh báo)
"""
import os, json, hashlib
try:
    import requests
except ImportError:
    requests = None
from flask import Blueprint, request, jsonify

from ai_advisor import ai_reply  # dùng chung brain

ZALO_TOKEN  = os.environ.get("ZALO_OA_ACCESS_TOKEN", "")
ZALO_SECRET = os.environ.get("ZALO_APP_SECRET", "")
ZALO_STRICT = os.environ.get("ZALO_STRICT", "0") == "1"
ZALO_SEND_URL = "https://openapi.zalo.me/v3.0/oa/message"

zalo_bp = Blueprint("zalo", __name__)

def zalo_send(user_id, text):
    """Gửi tin văn bản tới user qua Zalo OA."""
    if not ZALO_TOKEN or requests is None:
        print("zalo_send: thiếu ZALO_OA_ACCESS_TOKEN"); return
    try:
        requests.post(
            ZALO_SEND_URL,
            headers={"access_token": ZALO_TOKEN, "Content-Type": "application/json"},
            json={"recipient": {"user_id": user_id}, "message": {"text": text[:2000]}},
            timeout=20,
        )
    except Exception as e:
        print("zalo_send error:", e)

def _verify(req):
    """Xác thực chữ ký Zalo (best-effort). Trả True nếu hợp lệ hoặc không bật strict."""
    if not ZALO_SECRET:
        return True
    sig = req.headers.get("X-ZEvent-Signature", "")
    body = req.get_data(as_text=True) or ""
    ts = ""
    try:
        ts = (req.get_json(silent=True) or {}).get("timestamp", "")
    except Exception:
        pass
    app_id = os.environ.get("ZALO_APP_ID", "")
    mac = "mac=" + hashlib.sha256((app_id + body + str(ts) + ZALO_SECRET).encode()).hexdigest()
    ok = (sig == mac)
    if not ok:
        print("zalo: chữ ký không khớp", "-> CHẶN" if ZALO_STRICT else "-> vẫn nhận (lenient)")
    return ok or (not ZALO_STRICT)

@zalo_bp.route("/zalo-webhook", methods=["GET"])
def zalo_verify():
    # Zalo có thể gọi GET để kiểm tra endpoint sống.
    return jsonify({"status": "ok", "service": "Zalo OA + AI Thực Chiến"}), 200

@zalo_bp.route("/zalo-webhook", methods=["POST"])
def zalo_webhook():
    if not _verify(request):
        return jsonify({"ok": True}), 200
    data = request.get_json(silent=True) or {}
    event = data.get("event_name", "")
    sender = (data.get("sender") or {}).get("id")
    # Chỉ xử lý khi khách gửi text
    if event in ("user_send_text", "user_submit_info") and sender:
        text = ((data.get("message") or {}).get("text") or "").strip()
        if text:
            reply = ai_reply("zalo_" + str(sender), text)
            if not reply:
                reply = ("Dạ em là trợ lý AI Thực Chiến 👋 Anh/chị quan tâm gói nào ạ? "
                         "Combo Full / Claude / OpenCode — em tư vấn nhanh nhé!")
            zalo_send(sender, reply)
    return jsonify({"ok": True}), 200

if __name__ == "__main__":
    # selftest cú pháp + logic verify lenient (không cần mạng/flask app context).
    import types
    fake = types.SimpleNamespace(
        headers={}, get_data=lambda as_text=True: "{}", get_json=lambda silent=True: {})
    assert _verify(fake) is True, "không secret -> phải pass"
    print("zalo selftest PASS ✓")
