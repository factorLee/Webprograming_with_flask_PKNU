from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField

# 데이터를 받는 폼
class AddForm(FlaskForm):
    date = StringField('Today')
    todoName = StringField('작업 제목')
    duedate = StringField('Due date')
    feedback = TextAreaField()
    submit = SubmitField('Submit')

# 데이터 수정폼
class ModiForm(FlaskForm):
    modiId = IntegerField('수정할 데이터의 번호를 입력하세요.')
    todoName_modi = StringField('작업 제목')
    duedate_modi = StringField('Due date')
    feedback_modi = TextAreaField()
    submit = SubmitField('Submit')

# 데이터 삭제폼
class DelForm(FlaskForm):
    id = IntegerField('삭제할 데이터의 번호를 입력하세요.')
    submit = SubmitField('Submit')