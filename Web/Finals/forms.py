from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField

class AddForm(FlaskForm):
    date = StringField('Today')
    todoName = StringField('작업 제목')
    duedate = StringField('Due date')
    feedback = TextAreaField()
    submit = SubmitField('Submit')



class ModiForm(FlaskForm):
    modiId = IntegerField('수정할 번호를 입력하세요.')
    todoName_modi = StringField('작업 제목')
    duedate_modi = StringField('Due date')
    feedback_modi = TextAreaField()
    submit = SubmitField('Submit')


class DelForm(FlaskForm):
    id = IntegerField('Id Number of Task to Remove')
    submit = SubmitField('Remove Todo')