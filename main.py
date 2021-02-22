from config import settings
import threading
import logging
import logging.handlers
from pathlib import Path
from api_telegram import bot_telegram
import time


print(f'Start the api front telegram: {settings.VERSION}')


def config_log():
    LOG_DIRECTORY = settings.get('LOG_DIRECTORY', default='logs/')
    LOG_FILENAME = settings.get('LOG_FILENAME')
    if not Path(LOG_DIRECTORY).exists():
        Path(LOG_DIRECTORY).mkdir(parents=True)

    handler = logging.handlers.RotatingFileHandler(f'{LOG_DIRECTORY}{LOG_FILENAME}',
                                                   maxBytes=settings.get('LOG_MAX_BYTES'),
                                                   backupCount=settings.get('LOG_BACKUP_COUNT'))

    formatter = logging.Formatter(settings.get('LOG_FORMAT'), datefmt=settings.get('LOG_DATE_FORMAT'))
    handler.setFormatter(formatter)
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().addHandler(handler)


#config_log()

logging.info(f'Start the api front telegram: {settings.VERSION}')

#tr = threading.Thread(name='Thread-tasks', target=start)
#tr.start()

logging.info('Threads started')


def teste():
    while True:
        time.sleep(5)
        bot_telegram.send('teste essa bosta aqui')
