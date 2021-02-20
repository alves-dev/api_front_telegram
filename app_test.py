import os
from flask import Flask


app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return "<h1>Hello World!</h1>"


@app.route("/deploy", methods=['GET'])
def deploy():
    return "<h1>Testando deploy GitHub x Heroku </h1>"


def main():
    port = int(os.environ.get("PORT", 4321))
    app.run(port=port)


if __name__ == "__main__":
    main()
