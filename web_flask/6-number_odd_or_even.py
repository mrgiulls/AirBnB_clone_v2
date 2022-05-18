#!/usr/bin/python3
'''
First program using Flask framework
'''
from email.policy import default
from flask import Flask, render_template


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


@app.route('/number/<int:n>')
def number(n):
    '''Print a message from Flask'''
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    '''Print a message from Flask'''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    '''Print a message from Flask'''
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(debug=True)
