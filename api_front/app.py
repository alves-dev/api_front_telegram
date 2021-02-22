from flask import Flask, request, jsonify
from config import settings
from api_telegram import bot_telegram
import logging
import main

app = Flask('api_front_telegram')


@app.route('/message', methods=['POST'])
def message():
    logging.info('Message received')
    body = request.get_json()
    logging.info(f'body: {body}')
    print(body)
    bot_telegram.send(body)
    return jsonify(body), 201


@app.route('/', methods=['GET'])
def raiz():
    return 'rodando', 200

"""
fila = ['igor', 'daiara', 'jade']


@app.route('/home', methods=['GET'])
def home():
    return jsonify(fila), 200


@app.route('/home/<int:index>', methods=['GET'])
def home_index(index):
    return fila[index], 200


@app.route('/fila', methods=['POST'])
def home_post():
    body = request.get_json()
    print(type(body))
    print(body)
    fila.append(body['fila'][0])
    return jsonify(body), 201
"""


def start():
    app.run(port=settings.get('PORT_FLASK'))


#main.config_log()
#main.teste()
