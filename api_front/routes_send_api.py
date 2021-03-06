from flask import jsonify, request
from api_telegram import bot_telegram
import logging
from .authentication import token_required
from flask import Blueprint
from config import settings

bp_send = Blueprint('send_api', __name__, url_prefix='/send')


@bp_send.route('/message', methods=['POST'])
@token_required
def message():
    logging.info('Message received')
    body = request.get_json()
    logging.info(f'body: {body}')
    print(body)
    if 'type' in body.keys() and body['type'] in settings.get('TYPE_MESSAGE_NOT_REDIRECT'):
        return jsonify({'return_send': False, 'parameters': body, 'caused': 'Not send: TYPE_MESSAGE_NOT_REDIRECT'}), 200
    return_send = bot_telegram.send_message(body)
    if not return_send:
        return_send = bot_telegram.send_message(body)
        if not return_send:
            return jsonify({'return_send': return_send, 'attempts': '2', 'parameters': body}), 500
    return jsonify({'return_send': return_send, 'parameters': body}), 201 if return_send else 500


@bp_send.route('/photo', methods=['POST'])
@token_required
def photo():
    return 'Not implemented!', 201
