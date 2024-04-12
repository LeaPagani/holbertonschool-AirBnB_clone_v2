#!/usr/bin/python3
"""Start a Flask app
"""

from flask import Flask
app = Flask(__name__)


app.route ('/')
def hello():
        return 'Hello HBNB!'


app.route ('/hbnb')
def hbnb():
        return 'HBNB'


app.route ('/c/<text>')
def text():
        return 'C' + text.replace('_', ' ')


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)