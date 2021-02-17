from flask import Flask, render_template
from flask_wtf import FlaskForm # flask 와 wtforms 를 연결해줌
from wtforms import StringField, SubmitField # 플라스크에서 사용할 수 있게 입력 받는 부분들만 함수로 뺀것.

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm): # flask_wtf 의 FlaskForm 함수의 여러 기능을 사용하겠다. => 상속 받은거임.
    dept = StringField('학과이름을 입력하세요: ')
    submit = SubmitField('제출')
    

@app.route('/', methods=['GET', 'POST'])
def index():
    dept = False
    form = InfoForm() # form 객체 생성 
    #만약에 사용자 입력하는 칸이 제대로 들어갔다면..
    if form.validate_on_submit(): # 내가 구현한 클래스(혹은 함수)에 사용자가 제대로 입력 됬는지 구별하는 것.(FlaskForm에서 상속받은 함수)
        # 사용자가 입력한 데이터를 dept 변수에 저장. form 객체에 저장된 dept 데이터를 저장함
        dept = form.dept.data
        # 사용자가 입력한 데이터를 초기화
        form.dept.data = ''
    
    return render_template('00-home.html', form = form, dept = dept)



if __name__ == '__main__':
    app.run(debug=True)
