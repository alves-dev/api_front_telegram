from telebot import TeleBot
from typing import Union
import logging
import os


bot = TeleBot(token=os.getenv('TOKEN_TELEGRAM', default=None))
MY_CHAT_ID = os.getenv('MY_CHAT_ID')


def send(message: Union[str, dict]) -> bool:
    global bot, MY_CHAT_ID
    try:
        print(f'my MY_CHAT_ID: {MY_CHAT_ID}')
        bot.send_message(MY_CHAT_ID, str(message))
        logging.info(f'Message send: {str(message)}')
        return True
    except Exception as error:
        logging.error(error)
        return False
