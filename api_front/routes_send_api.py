from flask import jsonify, request
from api_telegram import bot_telegram
import logging
from .authentication import token_required
from flask import Blueprint


bp_send = Blueprint('send_api', __name__, url_prefix='/send')


@bp_send.route('/message', methods=['POST'])
@token_required
def message():
    logging.info('Message received')
    body = request.get_json()
    logging.info(f'body: {body}')
    print(body)
    return_send = bot_telegram.send(body)
    return jsonify({'return_send': return_send, 'parameters': body}), 201
