import os
from forms import AddForm, DelForm, ModiForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key = 'True')
    name = db.Column(db.Text)
    duedate = db.Column(db.Integer)
    ect = db.Column(db.Text)

    def __init__(self, name, duedate, ect):
        self.name = name
        self.duedate = duedate
        self.ect = ect
    def __repr__(self):
        return f"{self.id}번: Task: {self.name}, Due-date: {self.duedate}, 기타 부가설명: {self.ect}"

#Database 생성
db.create_all()

        
#index 및 add
@app.route('/', methods=['GET', 'POST'])
def add_todo():
    form = AddForm()

    if form.validate_on_submit():
        
        todoName = form.todoName.data
        duedate = form.duedate.data
        feedback = form.feedback.data
        todos = Todo.query.all()
        now = datetime.today()
        nowDate = now.strftime('%Y-%m-%d')
        
        new_todo = Todo(todoName, duedate, feedback)
        db.session.add(new_todo)
        db.session.commit()

        return render_template('add.html', form=form, todos=todos, nowDate=nowDate)
    else:
        return render_template('add.html', form=form)

#수정 함수
@app.route('/modify')
def modify_todo():
    form = ModiForm()
    
    if form.validate_on_submit():

        todoName_modi = form.todoName_modi.data
        duedate_modi = form.duedate_modi.data
        feedback_modi = form.feedback_modi.data

        modiId = form.modiId.data
        Todo.id(modiId).query.update({todoName_modi, duedate_modi, feedback_modi})
        #db.session.query(Todo).filter(int(Todo.id) == int(modiId)).update(todoName_modi, duedate_modi, feedback_modi)
        #modi_todo = Todo(todoName_modi, duedate_modi, feedback_modi)
        #db.session.update(todo_modi)
        db.session.commit()

        return redirect(url_for('add_todo'))
    else:
        return render_template('modify.html',form=form)

#삭제 함수
@app.route('/delete', methods=['GET','POST'])
def del_todo():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        todo_del = Todo.query.get(id)
        db.session.delete(todo_del)
        db.session.commit()
        
        return redirect(url_for('add_todo'))
    else:
        return render_template('delete.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
    