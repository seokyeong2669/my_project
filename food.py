from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.health_manager

def insert_all():
    db.food.drop()
    food = [
    {'menu': '백반', '칼로리': 624},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '요거트', '칼로리': 105},
    {'menu': '닭가슴살', '칼로리': 115},
    {'menu': '우유', '칼로리': 70},
    {'menu': '치즈', '칼로리': 403},
    {'menu': '바나나', '칼로리': 93},
    {'menu': '사과', '칼로리': 89},
    {'menu': '떡', '칼로리': 250},
    {'menu': '만두', '칼로리': 400},
    {'menu': '자장면', '칼로리': 423},
    {'menu': '짜장면', '칼로리': 423},
    {'menu': '짬뽕', '칼로리': 418},
    {'menu': '집밥', '칼로리': 624},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    {'menu': '샐러드', '칼로리': 148},
    ]

    for i in food:
        db.food.insert_one(i)

insert_all()