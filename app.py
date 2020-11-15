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
    print(infoes)
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
    # print(breakfast_receive)

    breakfast = db.food.find_one({'menu': breakfast_receive}, {'_id': False})
    lunch = db.food.find_one({'menu': lunch_receive}, {'_id': False})
    dinner = db.food.find_one({'menu': dinner_receive}, {'_id': False})
    # print(breakfast)

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


@app.route('/date', methods=['POST'])
def date_show():
    date_receive = request.form['date_give']
    year_receive = request.form['year_give']
    month_receive = request.form['month_give']

    # year_month 형식으로 변경 : 2020년 11월 -> 202011
    year_month = int(year_receive) * 100 + int(month_receive)

    # now_count = now_count[0]['date']
    print(year_month, date_receive)

    if date_receive == '1000':
        db.date.update_one({'year_month': year_month}, {'$set': {'date': []}})
        return jsonify({'result': 'success', 'ans': 0})

    else:
        now_count = list(db.date.find({'year_month': year_month}, {'_id': False}))
            # 달력에 표시한 날짜리스트(date_list)에 타겟 날짜(date_receive) 가 없으면 리스트에 타겟날짜 추가
        if str(date_receive) in now_count[0]['date']:  ## 있으면 삭제
            now_count[0]['date'].remove(str(date_receive))
            # date_list.remove(date_receive)
            db.date.update_one({'year_month': year_month}, {'$set': {'date': now_count[0]['date']}})
            print('삭제', now_count[0]['date'])
            return jsonify({'result': 'success', 'ans': 0, "count": len(now_count[0]['date'])})
        else:
            now_count[0]['date'].append(date_receive)  ## 없으면 추가
            db.date.update_one({'year_month': year_month}, {'$set': {'date': now_count[0]['date']}})
            print('추가', now_count[0]['date'])
            return jsonify({'result': 'success', 'ans': 1, "count": len(now_count[0]['date'])})

## 해당 연,월에 해당하는 달성 횟수를 DB에서 불러옴 : len(date리스트)
@app.route('/achieve', methods=['POST'])
def get_date():
    year_receive = request.form['year_give']
    month_receive = request.form['month_give']
    year_month = int(year_receive) * 100 + int(month_receive)
    now_count = list(db.date.find({'year_month': year_month}, {'_id': False}))
    # print(len(now_count[0]['date']))
    achieve = len(now_count[0]['date'])
    return jsonify({'result': 'success', "achieve": achieve})


## 페이지 시작 또는 새로고침 시 달성체크한 날짜를 달력에 뿌려주기위한 API
## 현재 페이지의 연,월에 해당하는 date 리스트를 DB에서 불러옴
@app.route('/color', methods=['POST'])
def get_color():
    year_receive = request.form['year_give']
    month_receive = request.form['month_give']
    year_month = int(year_receive) * 100 + int(month_receive)

    now_count = list(db.date.find({'year_month': year_month}, {'_id': False}))

    color = now_count[0]['date']

    return jsonify({'result': 'success', "color": color})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
