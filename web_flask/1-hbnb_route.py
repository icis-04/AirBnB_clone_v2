#!/usr/bin/python3
"""
    Script that routes url to functions in flask
"""
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """ renders "Hello HBNB" """
    return "Hello HBNB!"
@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """ renders "HBNB" """
    return "HBNB"

if __name__ == '__main__':
    app.run(host="0.0.0.0")
