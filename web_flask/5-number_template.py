#!/usr/bin/python3
"""
    Script that routes url to functions in flask
"""
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """ renders "Hello HBNB" """
    return "Hello HBNB!"
@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """ renders "HBNB" """
    return "HBNB"

@app.route('/c/<text>',strict_slashes=False)
def c_display(text):
    """ renders C and whatever is inside text """
    txt = text.replace("_", " ")
    return "C {}".format(txt)

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_display(text="is_cool"):
    """ renders Python + whatever is inside text """
    txt = text.replace('_', ' ')
    return "Python {}".format(txt)

@app.route('/number/<int:n>', strict_slashes=False)
def integer(n):
    """ renders the number n and 'is a number' """
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def int_html(n):
    """ renders a html file only if n is an integer """
    if type(n) is int:
        return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
