from config import settings
import threading
import logging
import logging.handlers
from pathlib import Path
from api_telegram import bot_telegram
import time
from datetime import datetime


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


config_log()

logging.info(f'Start the api front telegram: {settings.VERSION}')

#tr = threading.Thread(name='Thread-tasks', target=start)
#tr.start()

logging.info('Threads started')


def teste():
    while True:
        time.sleep(30)
        #bot_telegram.send(datetime.now())
        """
        web: gunicorn "api_front.app:app"
        worker: gunicorn main.py

        gunicorn "api_front.app:api_front.app" -b localhost:5555
        gunicorn "main:main" -b localhost:5555

        gunicorn "main:main" --log-level debug --timeout 2000

        """
        logging.info('time')
        logging.info('time1')
        logging.info('time2')
        logging.info('time3')
        print('time')
