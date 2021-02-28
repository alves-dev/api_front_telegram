from telebot import TeleBot
from typing import Union
import logging
import os
from config import settings
settings.get('VERSION')

bot = TeleBot(token=os.getenv('TOKEN_TELEGRAM', default=None))
MY_CHAT_ID = os.getenv('MY_CHAT_ID')


def send_message(message: Union[str, dict]) -> bool:
    try:
        bot.send_message(MY_CHAT_ID, str(message))
        logging.info(f'Message send: {str(message)}')
        return True
    except Exception as error:
        logging.error(error)
        return False


def send_photo(photo) -> bool:
    try:
        data = open(photo, 'rb')
        bot.send_photo(MY_CHAT_ID, data)
        logging.info(f'photo send: {photo}')
        return True
    except Exception as error:
        logging.error(error)
        return False


def send_archive(archive) -> bool:
    try:
        data = open(archive, 'rb')
        bot.send_document(MY_CHAT_ID, data)
        logging.info(f'Archive send: {archive}')
        return True
    except Exception as error:
        logging.error(error)
        return False
