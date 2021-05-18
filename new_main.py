from flask import Flask

from functions.func1 import *
from functions.func2 import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/func1')
def func1():
    x = func1()
    return x

@app.route('/func2')
def func2():
    x = func2()
    return x


# @app.route('/f2')
# def func2():
#     x = function2()
#     return x