from flask import Flask #flask 모듈안에 Flask 함수를 사용하겠다.
app = Flask(__name__) #Flask 함수를 불러와서, 이 프로그램에서 app이라는 변수로 사용하겠다.

@app.route('/')# 웹페이지의 주소를 생성 "홈주소" (데코레이터)
def index(): #홈주소 '/' 안에서 웹페이지의 내용을 반환한다.
    return "<h1>Hello Puppy!</h1>"

if __name__ == '__main__':
    app.run()