from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.health_manager

def insert_all():
    db.date.drop()
    doc = [
    {'year_month': 202001, 'date': []},
    {'year_month': 202002, 'date': []},
    {'year_month': 202003, 'date': []},
    {'year_month': 202004, 'date': []},
    {'year_month': 202005, 'date': []},
    {'year_month': 202006, 'date': []},
    {'year_month': 202007, 'date': []},
    {'year_month': 202008, 'date': []},
    {'year_month': 202009, 'date': []},
    {'year_month': 202010, 'date': []},
    {'year_month': 202011, 'date': []},
    {'year_month': 202012, 'date': []},
    {'year_month': 202101, 'date': []},
    {'year_month': 202102, 'date': []},
    {'year_month': 202103, 'date': []},
    {'year_month': 202104, 'date': []},
    {'year_month': 202105, 'date': []},
    {'year_month': 202106, 'date': []},
    {'year_month': 202107, 'date': []},
    {'year_month': 202108, 'date': []},
    {'year_month': 202109, 'date': []},
    {'year_month': 202110, 'date': []},
    {'year_month': 202111, 'date': []},
    {'year_month': 202112, 'date': []},
    {'year_month': 202201, 'date': []},
    {'year_month': 202202, 'date': []},
    {'year_month': 202203, 'date': []},
    {'year_month': 202204, 'date': []},
    {'year_month': 202205, 'date': []},
    {'year_month': 202206, 'date': []},
    {'year_month': 202207, 'date': []},
    {'year_month': 202208, 'date': []},
    {'year_month': 202209, 'date': []},
    {'year_month': 202210, 'date': []},
    {'year_month': 202211, 'date': []},
    {'year_month': 202212, 'date': []}
    ]

    for i in doc:
        db.date.insert_one(i)

insert_all()
