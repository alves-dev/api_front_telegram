from flask import jsonify
from .authentication import token_required
from flask import Blueprint
from config import settings


bp_operation = Blueprint('operation', __name__, url_prefix='/operation')


@bp_operation.route('/token', methods=['GET'])
@token_required
def is_valid():
    return jsonify({'is_valid': True})


@bp_operation.route('/status', methods=['GET'])
@token_required
def status():
    from app import STARTED
    return jsonify({'status': 'Running',
                    'started': STARTED,
                    'version': settings.get('VERSION')}), 200


@bp_operation.route('/log', methods=['GET'])
@token_required
def log():
    from app import STARTED
    return jsonify({'status': 'Running',
                    'started': STARTED,
                    'version': settings.get('VERSION')}), 200
