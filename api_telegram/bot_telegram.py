from telebot import TeleBot
from typing import Union
import logging
import os
import emoji
from config import settings

settings.get('VERSION')

bot = TeleBot(token=os.getenv('TOKEN_TELEGRAM', default=None))
MY_CHAT_ID = os.getenv('MY_CHAT_ID')


def send_message(message: Union[str, dict]) -> bool:
    try:
        bot.send_message(MY_CHAT_ID, __parse_message(message), parse_mode='HTML')
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


def __parse_message(message: dict) -> str:
    if isinstance(message, str):
        return f'<u>{message}</u>'
    if isinstance(message, dict):
        message_parse = ''
        for d in message:
            message_parse += f'<code>{d}</code>: <b>{message[d]}</b> \n'
            # https://pypi.org/project/emoji/

        message_parse = message_parse.replace('Error', str(emoji.emojize("Error :skull_and_crossbones:", language='pt',
                                                                         use_aliases=True)))
        message_parse = message_parse.replace('Info',
                                              str(emoji.emojize("Info :smile:", language='pt', use_aliases=True)))
        message_parse = message_parse.replace(' sucesso', str(emoji.emojize("sucesso :white_check_mark:", language='pt',
                                                                            use_aliases=True)))
        message_parse = message_parse.replace('insucesso', str(emoji.emojize("insucesso :x:", language='pt',
                                                                             use_aliases=True)))
        message_parse = message_parse.replace('Report', str(emoji.emojize("Report :page_facing_up:", language='pt',
                                                                          use_aliases=True)))
        return message_parse
    return message
