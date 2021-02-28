from api_telegram import bot_telegram
from config import settings
import logging
import logging.handlers
from pathlib import Path


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


def send_log() -> bool:
    try:
        file_log = f'{str(Path.cwd())}/{settings.get("LOG_DIRECTORY")}{settings.get("LOG_FILENAME")}'
        logging.info(f'Send log: {file_log}')
        bot_telegram.send_archive(file_log)
        return True
    except Exception as error:
        logging.error(error)
        return False


def read_log() -> str:
    try:
        file_log = f'{str(Path.cwd())}/{settings.get("LOG_DIRECTORY")}{settings.get("LOG_FILENAME")}'
        logging.info(f'Read log: {file_log}')
        with open(file_log, 'r') as log:
            log_text = log.read()
        return log_text
    except Exception as error:
        logging.error(error)
        return 'Error reading log!'
