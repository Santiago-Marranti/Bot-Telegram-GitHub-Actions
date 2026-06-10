# notify.py
import requests
import os

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    print("Mensaje enviado:", response.json())

if __name__ == "__main__":
    send_message("🌙 Son las 2am! Recordatorio automático.")