from flask import jsonify
from utils import get_status, send_log, read_log
from .authentication import token_required
from flask import Blueprint
import logging


bp_operation = Blueprint('operation', __name__, url_prefix='/operation')


@bp_operation.route('/token', methods=['GET'])
@token_required
def is_valid():
    logging.info('GET in operation/token')
    return jsonify({'is_valid': True})


@bp_operation.route('/status', methods=['GET'])
def status():
    logging.info('GET in operation/status')
    data = get_status()
    # todo: apenas para test do new relic
    from api_telegram import bot_telegram
    bot_telegram.send_message(data)
    return jsonify(data), 200


@bp_operation.route('/sendLogFile', methods=['GET'])
@token_required
def send_log_file():
    logging.info('GET in operation/log')
    return_read = send_log()
    return jsonify({'return_read': return_read}), 200


@bp_operation.route('/log', methods=['GET'])
@token_required
def log():
    logging.info('GET in operation/log')
    return_read = read_log()
    return jsonify({'Log': return_read}), 200
