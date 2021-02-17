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
    age = db.Column(db.Integer)
    # 생성자 만들때 이름 나이 받음
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 객체 생성시 출력될 메세지
    def __repr__(self):
        return f"Puppy {self.name} is {self.age} years old."
        