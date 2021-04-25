from config import settings
import logging
import os


def get_status() -> dict:
    from app import STARTED
    status = {'status': 'Running', 'started': STARTED, 'version': settings.get('VERSION'),
              'application': 'api_front_telegram', 'environment': os.getenv('ENV_FOR_DYNACONF')}
    logging.info(f'Get status: {status}')
    return status
