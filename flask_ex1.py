from flask import Flask, request
from math import exp
import os

app = Flask(__name__)


@app.route('/')
def say_hello():
    return 'Hello!' + request.args.get('name')


@app.route('/exp')
def exp_number():
    return 'The exponent is:'+ str(exp(float(request.args.get('num1'))))


port = int(os.environ.get('PORT'))
app.run(host='0.0.0.0', port=port)

