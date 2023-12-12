from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def adding():
    a = int(request.args['a'])
    b = int(request.args['b'])
    answer = add(a, b)
    return str(answer)

@app.route('/sub')
def subtracting():
    a = int(request.args['a'])
    b = int(request.args['b'])
    answer = sub(a, b)
    return str(answer)

@app.route('/mult')
def multiplying():
    a = int(request.args['a'])
    b = int(request.args['b'])
    answer = mult(a, b)
    return str(answer)

@app.route('/div')
def dividing():
    a = int(request.args['a'])
    b = int(request.args['b'])
    answer = int(div(a, b))
    return str(answer)

operations = {'add': add, 'sub': sub, 'mult': mult, 'div': div}
@app.route('/math/<operator>')
def calculate(operator):
    a = int(request.args['a'])
    b = int(request.args['b'])
    answer = int(operations[operator](a, b))
    return str(answer)
