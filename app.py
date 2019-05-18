from boto3.docs import method
from flask import Flask, render_template, request, jsonify
from member.controller import MemberController
from ai_calc.controller import CalcController
from gd.controller import GradientDescentController
from iris.controller import IrisController
import re
from blood.model import BloodModel


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/login', methods=["POST"])
def login():
    print("로그인")
    userid = request.form['userid']
    password = request.form['password']
    print('로그인 들어온 아이디 {}, 비번{}'.format(userid, password))
    ctrl = MemberController()
    view = ctrl.login_check(userid, password)

    return render_template(view)

@app.route('/gradient_descent', methods=["GET","POST"])
def gradient_descent():
    ctrl = GradientDescentController()
    name = ctrl.service_mode()

    return render_template('gd.html', name = name)

@app.route('/move/<path>')
def move_ui_calc(path):
    return render_template("{}.html".format(path))

"""
@app.route('/move/<path>')
def move_ai_calc():
    return render_template("ai_calc.html")


@app.route('/move/<path>')
def move_blood():
    return render_template("blood.html")


@app.route('/move/<path>')
def home():
    return render_template("home.html")
"""

@app.route('/ui_calc')
def ui_calc():
    stmt = request.args.get('stmt', 'NONE')
    if stmt == 'NONE':
        print('넘어온 값이 없음')
    else :
        print('넘어온식 {}'.format(stmt))
        patt = '[0-9]+'
        op = re.sub(patt, '' , stmt)
        print('넘어온 연산자 {}'.format(op))
        nums = stmt.split(op)
        result = 0

        if op == '+':
            result = int(nums[0]) + int(nums[1])
        elif op == '-':
            result = int(nums[0]) - int(nums[1])
        elif op == '*':
            result = int(nums[0]) * int(nums[1])
        elif op == '/':
            result = int(nums[0]) / int(nums[1])

@app.route('/iris', methods=['POST'])
def iris():
    ctrl = IrisController()
    name = ctrl.service_model()

    return render_template('iris.html', result=name)



@app.route('/ai_calc')
def ai_calc():
    num1 = request.args.get('num1', 'NONE')
    num2 = request.args.get('num2', 'NONE')
    opcode = request.args.get('opcode', 'NONE')

    result = CalcController(num1, num2, opcode).calc()
    render_params = {}
    render_params['result'] = result
    return render_template('ai_calc.html', **render_params)
"""
    if num1 == 'NONE' or num2 == 'None' or opcode == 'None':
        print('값 오류')
    else:
        print('{} {} {}'.format(num1, opcode, num2))
        patt = '[0-9]+'
        result = 0

        if opcode == 'add':
            result = int(num1) + int(num2)
        elif opcode == 'sub':
            result = int(num1) - int(num2)
        elif opcode == 'mul':
            result = int(num1) * int(num2)
        elif opcode == 'div':
            result = int(num1) / int(num2)
    #return result
    return jsonify(result=result)
"""

@app.route('/blood')
def blood():
    weight = request.args.get('weight', 'NONE')
    age = request.args.get('age', 'NONE')

    print("무게 : {}".format(weight))
    print("나이 : {}".format(age))
    model = BloodModel('blood/data/data.txt')
    raw_data = model.create_raw_data()
    render_params = {}
    value=model.create_model(raw_data, weight, age)

    render_params = {}
    render_params['result'] = value
    return render_template('blood.html', **render_params)

if __name__ == '__main__':
    app.debug = True
    app.run()