# -*- coding: utf-8 -*-
"""SQLite: đơn hàng + link giao + log GD không khớp + license (Farm OS)."""
import sqlite3, time, pathlib

DB = pathlib.Path(__file__).parent / "bot.db"

def _c():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init():
    with _c() as c:
        c.execute("""CREATE TABLE IF NOT EXISTS orders(
            txn TEXT PRIMARY KEY, chat_id TEXT, sku TEXT, amount INTEGER,
            status TEXT, created TEXT, channel TEXT)""")
        c.execute("""CREATE TABLE IF NOT EXISTS links(sku TEXT PRIMARY KEY, url TEXT)""")
        c.execute("""CREATE TABLE IF NOT EXISTS unmatched(
            id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT, amount INTEGER, created TEXT)""")
        c.execute("""CREATE TABLE IF NOT EXISTS licenses(
            key TEXT PRIMARY KEY, txn TEXT, sku TEXT, chat_id TEXT, lic_type TEXT,
            issued TEXT, expires_day INTEGER, status TEXT, reminded INTEGER DEFAULT 0)""")

# ---------- orders ----------
def create_order(txn, chat_id, sku, amount, channel="telegram"):
    with _c() as c:
        c.execute("INSERT OR REPLACE INTO orders VALUES(?,?,?,?,?,?,?)",
                  (txn, str(chat_id), sku, amount, "pending", time.strftime("%Y-%m-%d %H:%M"), channel))

def get_order(txn):
    with _c() as c:
        r = c.execute("SELECT * FROM orders WHERE txn=?", (txn,)).fetchone()
        return dict(r) if r else None

def mark_paid(txn):
    with _c() as c:
        c.execute("UPDATE orders SET status='paid' WHERE txn=?", (txn,))

def orders_by_chat(chat_id):
    with _c() as c:
        return [dict(r) for r in c.execute(
            "SELECT * FROM orders WHERE chat_id=? ORDER BY rowid DESC LIMIT 10", (str(chat_id),)).fetchall()]

# ---------- links (giao bằng link) ----------
def set_link(sku, url):
    with _c() as c:
        c.execute("INSERT OR REPLACE INTO links VALUES(?,?)", (sku, url))

def get_link(sku):
    with _c() as c:
        r = c.execute("SELECT url FROM links WHERE sku=?", (sku,)).fetchone()
        return r["url"] if r else None

# ---------- unmatched ----------
def log_unmatched(content, amount):
    with _c() as c:
        c.execute("INSERT INTO unmatched(content,amount,created) VALUES(?,?,?)",
                  (content, amount, time.strftime("%Y-%m-%d %H:%M")))

def list_unmatched(n=10):
    with _c() as c:
        return [dict(r) for r in c.execute(
            "SELECT * FROM unmatched ORDER BY id DESC LIMIT ?", (n,)).fetchall()]

# ---------- licenses (Farm OS: license / subscription) ----------
def add_license(key, txn, sku, chat_id, lic_type, expires_day):
    with _c() as c:
        c.execute("INSERT OR REPLACE INTO licenses VALUES(?,?,?,?,?,?,?,?,?)",
                  (key, txn, sku, str(chat_id), lic_type, time.strftime("%Y-%m-%d %H:%M"),
                   int(expires_day or 0), "active", 0))

def license_by_txn(txn):
    with _c() as c:
        r = c.execute("SELECT * FROM licenses WHERE txn=?", (txn,)).fetchone()
        return dict(r) if r else None

def licenses_by_chat(chat_id):
    with _c() as c:
        return [dict(r) for r in c.execute(
            "SELECT * FROM licenses WHERE chat_id=? ORDER BY rowid DESC LIMIT 20", (str(chat_id),)).fetchall()]

def revoke(key):
    with _c() as c:
        cur = c.execute("UPDATE licenses SET status='revoked' WHERE key=?", (key.strip().upper(),))
        return cur.rowcount

def expiring(today_day, within_days):
    """Subscription đang active, còn hạn, sẽ hết trong [hôm nay .. hôm nay+within], chưa nhắc."""
    lo, hi = int(today_day), int(today_day) + int(within_days)
    with _c() as c:
        return [dict(r) for r in c.execute(
            "SELECT * FROM licenses WHERE lic_type='subscription' AND status='active' "
            "AND expires_day>0 AND expires_day>=? AND expires_day<=? AND reminded=0", (lo, hi)).fetchall()]

def mark_reminded(key):
    with _c() as c:
        c.execute("UPDATE licenses SET reminded=1 WHERE key=?", (key,))

# ---------- stats ----------
def stats():
    with _c() as c:
        r = c.execute("SELECT COUNT(*) n, COALESCE(SUM(amount),0) rev FROM orders WHERE status='paid'").fetchone()
        lic = c.execute("SELECT COUNT(*) n FROM licenses WHERE status='active'").fetchone()
        return {"orders": r["n"], "revenue": r["rev"], "licenses": lic["n"]}
