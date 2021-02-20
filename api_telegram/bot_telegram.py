import telebot
from config import settings
from typing import Union
import logging


bot = telebot.TeleBot(token=settings.get('TOKEN_TELEGRAM'))


def send(message: Union[str, dict]) -> None:
    bot.send_message(settings.get('MY_CHAT_ID'), str(message))
    logging.info(f'Message send: {str(message)}')

