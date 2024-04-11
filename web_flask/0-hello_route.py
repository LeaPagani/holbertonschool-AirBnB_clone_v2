#!/usr/bin/python3
"""
Start a Flask web application.
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This function handles the root route of the Flask application.
    It returns a string 'Hello HBNB!' when the route is accessed.
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)