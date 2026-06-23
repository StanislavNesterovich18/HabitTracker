import requests

from config import settings


def send_telegram_message(chat_id, message):

    url = f"https://api.telegram.org/bot{settings.TG_BOT_TOKEN}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.get(url, params=params)
    return response.json()