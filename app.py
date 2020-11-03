from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.health_manager


@app.route('/')
def home():  # 함수명 수정 - 이름만 보고 접속되는 페이지를 확인할 수 있게!
    return render_template('index.html')


@app.route('/exercise')
def my_page01():
    return render_template('exercise_check.html')

@app.route('/food')
def my_page02():
    return render_template('food_manage.html')

@app.route('/together')
def my_page03():
    return render_template('together.html')


@app.route('/info', methods=['POST'])
## 클라이언트의 post요청으로부터 key 값들을 받아와 변수에 저장
def save_order():
    year_receive = request.form['year_give']
    month_receive = request.form['month_give']
    count_receive = request.form['count_give']

    doc = {
        'year': year_receive,
        'month': month_receive,
        'count': count_receive,
    }

    db.purpose.insert_one(doc)

    return jsonify(
        {'result': 'success', "msg": f'{year_receive}년 {month_receive}월 목표 운동횟수는 {count_receive}회 입니다.\n화이팅!!!'})

@app.route('/calender', methods=['GET'])
def view_orders():
## DB에서 데이터를 불러와 리스트형태로 orders 변수에 저장
    infoes = list(db.purpose.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'infoes': infoes})

@app.route('/calory', methods=['POST'])
## 클라이언트의 post요청으로부터 key 값들을 받아와 변수에 저장
def calory_info():
    name_receive = request.form['name_give']
    gender_receive = request.form['gender_give']
    height_receive = request.form['height_give']
    active_receive = request.form['active_give']

    doc = {
        'name': name_receive,
        'gender': gender_receive,
        'height': height_receive,
        'active': active_receive,
    }

    db.calory.insert_one(doc)

    return jsonify(
        {'result': 'success', "msg": '성공적으로 저장되었습니다!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
