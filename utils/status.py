from config import settings
import logging


def get_status() -> dict:
    from app import STARTED
    status = {'status': 'Running', 'started': STARTED, 'version': settings.get('VERSION'),
              'application': 'api_front_telegram'}
    logging.info(f'Get status: {status}')
    return status
