from flask import Flask
from flask import request

from functions.func1 import *
from functions.func2 import *
from functions.funcalc import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/my_awesome_function', methods=['POST'])
def func1_my_awesome_function():
    x = my_awesome_function()
    return x

@app.route('/func2', methods=['POST'])
def func2_func2():
    x = func2()
    return x

@app.route('/funnything', methods=['POST'])
def funcalc_funnything():
    yourname = request.args.get('yourname','N/A')
    yourage = request.args.get('yourage','N/A')
    x = funnything(yourname, yourage)
    return x

@app.route('/somejoke', methods=['POST'])
def funcalc_somejoke():
    yourlocation = request.args.get('yourlocation','N/A')
    x = somejoke(yourlocation)
    return x


# @app.route('/postme', methods=['POST'])
# def postme():
#     myarg = request.args.get('person','N/A')
#     x = somejoke(myarg)
#     return x