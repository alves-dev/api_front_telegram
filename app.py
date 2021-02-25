from config import settings
from flask import Flask
from api_front.routes_operation import bp_operation
from api_front.routes_send_api import bp_send
import threading
import main
from datetime import datetime


STARTED = datetime.now()


app = Flask('api_front_telegram')

app.register_blueprint(bp_operation)
app.register_blueprint(bp_send)


if __name__ == '__main__':
    app.run(port=settings.get('PORT_FLASK'))


tr = threading.Thread(name='Thread-tasks', target=main.teste)
tr.start()
