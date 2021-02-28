import time
from api_telegram import bot_telegram
from utils import get_status
from config import settings


def send_info():
    while True:
        time.sleep(settings.get('TIME_SEND_INFO', default=18000))
        bot_telegram.send_message(get_status())
