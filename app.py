from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():  # 함수명 수정 - 이름만 보고 접속되는 페이지를 확인할 수 있게!
    return render_template('index.html')


@app.route('/exercise')
def my_page():
    return render_template('exercise_check.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)