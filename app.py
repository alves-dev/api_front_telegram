from config import settings
from utils import config_log
from datetime import datetime
from flask import Flask, redirect
from api_front.routes_operation import bp_operation
from api_front.routes_send_api import bp_send
import threading
from utils import send_info
import logging
from api_telegram import bot_telegram
import os


config_log()
logging.info('Log configured')

print(f'Start the api front telegram: {settings.VERSION}')

app = Flask('api_front_telegram')

bot_telegram.send_message(f'Start the api front telegram: {settings.VERSION}, environment: '
                          f'{os.getenv("ENV_FOR_DYNACONF")}')

STARTED = datetime.now()


@app.route("/")
def redirect_status():
    return redirect('/operation/status')


app.register_blueprint(bp_operation)
app.register_blueprint(bp_send)

tr = threading.Thread(name='Thread-tasks', target=send_info)
tr.start()

if __name__ == '__main__':
    app.run(port=settings.get('PORT_FLASK'))
