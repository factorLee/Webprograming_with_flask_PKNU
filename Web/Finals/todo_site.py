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

#class Date(db.Model):
#
#    __tablename__ = 'dates'
#    id = db.Column(db.Integer, primary_key=True)
#    date = db.Column(db.Text, unique=True)
#    todo = db.relationship('Todo', backref = 'todo', uselist=False) # one to many
#    def __init__(self, date):
#        self.date = date
#    def __repr__(self):
#        return f"번호: {self.id} Date: {self.date}"

class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key = 'True')
    name = db.Column(db.Text)
    duedate = db.Column(db.Integer)
    ect = db.Column(db.Text)
#    dates_id = db.Column(db.Integer, db.ForeignKey('dates.id'))

    def __init__(self, name, duedate, ect):
        self.name = name
        self.duedate = duedate
        self.ect = ect
    def __repr__(self):
        return f"{self.id}번: Task: {self.name}, Due-date: {self.duedate}, 기타 부가설명: {self.ect}"
db.create_all()

# flask
#@app.route('/', methods=['GET', 'POST'])
#def home_todo():
#    form = AddForm()
#
#    if form.validate_on_submit():
#        date = form.date.data
#        new_date = Date(date)
#
#        db.session.add(new_date)
#        db.session.commit()
#
#        return redirect(url_for('add_todo'))
#    else:
#        return render_template('home.html', form=form)
        

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

#@app.route('/list')
#def list_todo():
#    #Grad a list of data from database.
##    dates = Date.query.all()
#    todos = Todo.query.all()
#    now = datetime.today()
#    nowDate = now.strftime('%Y-%m-%d')
#    return render_template('list.html',  todos=todos, nowDate=nowDate)

#@app.route('/modify02')
#def modify01_todo():
#    form = Modi01Form()
#
#
#    if form.validate_on_submit():
#        
#        modiId = form.modiId.data
#        mi = Todo.query.get(modiId)
#        todos_modi = Todo.query.get(mi)
#        
#
#
#        return render_template('modify02.html',todos_modi=todos_modi,form=form)
#    else:
#        return render_template('modify01.html',form=form)
#
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
    