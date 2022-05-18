#!/usr/bin/python3
'''
First program using Flask framework
'''
from email.policy import default
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    '''Print a message from Flask'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''Print a message from Flask'''
    return 'HBNB'


@app.route('/c/<text>')
def c_is(text):
    '''Print a message from Flask'''
    return 'C ' + text.replace("_", " ")


@app.route('/python', defaults={'text': 'is_cool'})
@app.route('/python/<text>')
def python_is_cool(text):
    '''Print a message from Flask'''
    return 'Python ' + text.replace("_", " ")


if __name__ == "__main__":
    app.run(debug=True)
