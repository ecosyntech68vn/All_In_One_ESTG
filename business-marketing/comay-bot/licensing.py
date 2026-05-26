# -*- coding: utf-8 -*-
"""
Engine license key cho EcoSynTech - ky HMAC, verify duoc OFFLINE.

Key dang:  ECO-<PID>-<EXP>-<RAND>-<SIG>
  PID  : ma san pham (vd FOS = Farm OS license, FOSUB = Farm OS subscription)
  EXP  : so "ngay-unix" het han (0 = vinh vien), ma base32 5 ky tu
  RAND : 6 ky tu ngau nhien (dam bao duy nhat)
  SIG  : 8 ky tu HMAC-SHA256(secret, "PID-EXP-RAND") rut gon

Vi chu ky nam trong key, Farm OS co the NHUNG ham verify() nay de kiem tra
license ma KHONG can goi may chu - dung nguyen tac offline-safe.
Chi can dung chung LICENSE_SECRET voi bot phat hanh.

Dung:  python licensing.py --selftest
"""
import os, hmac, hashlib, secrets, time

ALPH = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"   # Crockford base32 (bo I,L,O,U)
_IDX = {c: i for i, c in enumerate(ALPH)}
SECRET = (os.environ.get("LICENSE_SECRET", "") or "DEV-INSECURE-CHANGE-ME").encode()

def today_day():
    return int(time.time() // 86400)

def _b32(n, width):
    s = ""; n = int(n)
    while n > 0:
        s = ALPH[n & 31] + s; n >>= 5
    return (s or "0").rjust(width, "0")

def _unb32(s):
    n = 0
    for c in s.upper():
        n = n * 32 + _IDX[c]
    return n

def _sig(body):
    mac = hmac.new(SECRET, body.encode(), hashlib.sha256).digest()
    return _b32(int.from_bytes(mac[:5], "big"), 8)

def gen(pid, days=0):
    """Sinh key. days=0 -> vinh vien. Tra (key, expires_day); expires_day=0 neu vinh vien."""
    pid = "".join(ch for ch in str(pid).upper() if ch.isalnum()) or "GEN"
    exp = 0 if not days else today_day() + int(days)
    expc = _b32(exp, 5)
    rand = "".join(secrets.choice(ALPH) for _ in range(6))
    body = f"{pid}-{expc}-{rand}"
    return f"ECO-{body}-{_sig(body)}", exp

def verify(key):
    """Verify offline. Tra dict: ok, reason, pid, expires_day, expired."""
    try:
        parts = str(key).strip().upper().split("-")
        if len(parts) != 5 or parts[0] != "ECO":
            return {"ok": False, "reason": "format", "pid": None, "expires_day": None, "expired": None}
        _, pid, expc, rand, sig = parts
        body = f"{pid}-{expc}-{rand}"
        if not hmac.compare_digest(sig, _sig(body)):
            return {"ok": False, "reason": "bad-signature", "pid": pid, "expires_day": None, "expired": None}
        exp = _unb32(expc)
        expired = (exp != 0 and today_day() > exp)
        return {"ok": (not expired), "reason": ("expired" if expired else "ok"),
                "pid": pid, "expires_day": exp, "expired": expired}
    except Exception as e:
        return {"ok": False, "reason": f"error:{e}", "pid": None, "expires_day": None, "expired": None}

def date_str(expires_day):
    if not expires_day:
        return "vinh vien"
    return time.strftime("%d/%m/%Y", time.gmtime(int(expires_day) * 86400))

if __name__ == "__main__":
    k1, e1 = gen("FOS", 0); r1 = verify(k1)
    assert r1["ok"] and r1["pid"] == "FOS" and r1["expires_day"] == 0, r1
    k2, e2 = gen("FOSUB", 365); r2 = verify(k2)
    assert r2["ok"] and r2["expires_day"] == today_day() + 365, r2
    bad = k1[:-1] + ("Z" if k1[-1] != "Z" else "Y")
    assert verify(bad)["ok"] is False, "key gia mao phai fail"
    pid, expc, rand = "FOSUB", _b32(today_day() - 1, 5), "AAAAAA"
    body = f"{pid}-{expc}-{rand}"; oldkey = f"ECO-{body}-{_sig(body)}"
    r3 = verify(oldkey)
    assert r3["ok"] is False and r3["reason"] == "expired", r3
    print("licensing selftest PASS - sample:", k1, "|", k2, "| exp:", date_str(e2))
