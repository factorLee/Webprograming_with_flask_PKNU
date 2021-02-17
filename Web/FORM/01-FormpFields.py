from flask import Flask, render_template, session, redirect, url_for
# session 은 사용자에 대한 정보를 접속하는 동안 계속 유지하겠다.
# redirect 는 다른 페이지로 연결해주는 것.
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateField, 
                    RadioField, SelectField, TextField, 
                    TextAreaField, SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

class InfoForm(FlaskForm):
    dept = StringField('소속학과', validators=[DataRequired()])
    sugang = BooleanField('웹프로그래밍 수강여부', validators=[DataRequired()])
    special = RadioField('전공', choices=[('산업공학', '산업공학'),('기술서비스', '기술서비스')])
    interest = SelectField('흥미분야', choices=[('프로그래밍', '프로그래밍'), ('통계', '통계'), ('기술경영', '기술경영')])
    feedback = TextAreaField()
    submit = SubmitField('제출')

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = InfoForm() # FlaskForm이 실행
    if form.validate_on_submit(): # 폼에 값들이 다 제대로 들어갔다면
        session['dept'] = form.dept.data
        session['sugang'] = form.sugang.data
        session['special'] = form.special.data
        session['interest'] = form.interest.data
        session['feedback'] = form.feedback.data
        return redirect(url_for('thankyou'))

    return render_template('01-home.html', form = form)

@app.route('/thankyou')
def thankyou():
    return render_template('01-thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)


