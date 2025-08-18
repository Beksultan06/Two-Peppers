import json
import requests
from html import escape
from django.conf import settings

def _clean_chat_id(val):
    if val is None:
        return None
    val = str(val).strip().strip('"').strip("'")
    if val.startswith("@"):
        return val
    try:
        return int(val)
    except ValueError:
        return val 

def send_telegram_message(name: str, email: str, message: str):
    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = _clean_chat_id(settings.TELEGRAM_CHAT_ID)
    if not token or not chat_id:
        return False, "Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID", None

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    text = (
        "📩 <b>New contact form</b>\n"
        f"👤 <b>Name:</b> {escape(name)}\n"
        f"✉️ <b>Email:</b> {escape(email)}\n"
        f"📝 <b>Message:</b>\n{escape(message)}"
    )
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True,
    }

    try:
        r = requests.post(url, json=payload, timeout=10)
        data = r.json()
        if data.get("ok"):
            return True, None, data["result"].get("message_id")
        return False, json.dumps(data, ensure_ascii=False), None
    except requests.RequestException as e:
        return False, str(e), None
