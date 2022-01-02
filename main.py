import logging
logging.basicConfig(level=logging.DEBUG)

from flask import Flask

app = Flask(__name__)


@app.route('/startupProbe')
def startupProbe():
    return "startupProbe"

@app.route('/readinessProbe')
def readinessProbe():
    return "readinessProbe"

@app.route('/livenessProbe')
def livenessProbe():
    return "livenessProbe"


# @route('/hello/<name>')
# def index(name):
#     return template('<b>Hello {{name}}</b>!', name=name)

app.run(host='0.0.0.0', port=8080)
