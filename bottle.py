import logging
from bottle import route, run, template

logging.basicConfig(level=logging.DEBUG)

@route('/startupProbe')
def startupProbe():
    return "startupProbe"

@route('/readinessProbe')
def readinessProbe():
    return "readinessProbe"

@route('/livenessProbe')
def livenessProbe():
    return "livenessProbe"


# @route('/hello/<name>')
# def index(name):
#     return template('<b>Hello {{name}}</b>!', name=name)

run(host='0.0.0.0', port=8080)
