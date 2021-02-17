import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#현재 작업폴더에 대한 정보
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# 데이터베이스 설정
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 데이터베이스를 연결
db = SQLAlchemy(app)



# 데이터베이스 스키마 생성
class Puppy(db.Model):
    #만들 테이블의 이름
    __tablename__ = 'puppies'
    #열추가
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    toys = db.relationship('Toy', backref = 'puppy', lazy='dynamic') # one to one
    owner = db.relationship('Owner', backref = 'puppy', uselist=False) # one to many
   
    # 생성자 만들때 이름 나이 받음
    def __init__(self, name):
        self.name = name

    # 객체 생성시 출력될 메세지
    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} and owner is {self.owner.name}"
        else:
            return f"Puppy name is {self.name} and has no owner assigned yet"
    
    def report_toys(self):
        print("Here are my toys!")
        for toy in self.toys:
            print(toy.item_name)


class Toy(db.Model):
    __tablename__='toys'

    id = db.Column(db.Integer, primary_key = True)
    item_name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, item_name, puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id

class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key = 'True')
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id