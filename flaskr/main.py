from flask import Flask
from flask import request

from functions.crates import *
from functions.func1 import *
from functions.func2 import *
from functions.funcalc import *
from functions.funcalc import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    msg = "Welcome to FuncFlasker"
    if request.method == 'POST':
        return msg
    else:
        return msg

@app.route('/get_rates', methods=['POST'])
def crates_get_rates():
    x = get_rates()
    return x
@app.route('/my_awesome_function', methods=['POST'])
def func1_my_awesome_function():
    x = my_awesome_function()
    return x
@app.route('/func2', methods=['POST'])
def func2_func2():
    x = func2()
    return x
@app.route('/two_params', methods=['POST'])
def funcalc_two_params():
    aname = request.args.get('aname','N/A')
    acolor = request.args.get('acolor','N/A')
    x = two_params(aname, acolor)
    return x
@app.route('/one_param', methods=['POST'])
def funcalc_one_param():
    alocation = request.args.get('alocation','N/A')
    x = one_param(alocation)
    return x
