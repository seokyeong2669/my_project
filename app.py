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
    # 주석 테스트
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


@app.route('/info', methods=['GET'])
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


@app.route('/calory', methods=['GET'])
def get_calory():
    infoes = list(db.calory.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'infoes': infoes})


@app.route('/food', methods=['POST'])
def get_menu():
    breakfast_receive = request.form['breakfast_give']
    lunch_receive = request.form['lunch_give']
    dinner_receive = request.form['dinner_give']
    print(breakfast_receive)
    # if breakfast_receive == '' or lunch_receive == '' or dinner_receive == "":
    #     msg = '메뉴를 입력해주세요!'
    #     return jsonify({'result': 'success', 'msg': msg})

    breakfast = db.food.find_one({'menu': breakfast_receive}, {'_id': False})
    lunch = db.food.find_one({'menu': lunch_receive}, {'_id': False})
    dinner = db.food.find_one({'menu': dinner_receive}, {'_id': False})
    print(breakfast)

    if breakfast is None:
        return jsonify({'result': 'success', "msg": 1})
    elif lunch is None:
        return jsonify({'result': 'success', "msg": 2})
    elif dinner is None:
        return jsonify({'result': 'success', "msg": 3})
    else:
        doc = {
                'break_cal': breakfast['칼로리'],
                'lunch_cal': lunch['칼로리'],
                'dinner_cal': dinner['칼로리']
            }
        return jsonify({'result': 'success', "menu": doc})

date_list =[]
@app.route('/date', methods=['POST'])
## 클라이언트의 post요청으로부터 key 값들을 받아와 변수에 저장


def date():
    date_receive = request.form['date_give']
    year_receive = request.form['year_give']
    month_receive = request.form['month_give']
    # print(year_receive)
    # print(month_receive)
    date_list.append(date_receive)
    doc = {
        'year': year_receive,
        'month': month_receive,
        'date': date_list
    }
    print(doc)
    db.date.insert_one(doc)
    db.date.find_one({'date': breakfast_receive}, {'_id': False})
    return jsonify(
        {'result': 'success', "msg": '성공적으로 저장되었습니다!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
