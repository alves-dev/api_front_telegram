from flask import jsonify, request
from functools import wraps
import os
import logging


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'token is missing', 'token': token}), 401
        try:
            token_app = os.getenv('TOKEN', default=None)
            if token_app is None:
                logging.error('Set TOKEN environment variable')
                print('Set TOKEN environment variable')
                raise ValueError('Set TOKEN environment variable')
            if not token == token_app:
                return jsonify({'message': 'token is invalid or expired', 'token': token}), 401
        except:
            return jsonify({'message': 'Internal Server Error'}), 500
        return f(*args, **kwargs)
    return decorated
