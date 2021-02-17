import os
from forms import AddForm, DelForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Puppy(db.Model):

    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref = 'puppy', uselist=False) # one to many

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Puppy name: {self.name}"

class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key = 'True')
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

db.create_all()

#반갑습니다 플라스크입니다^^
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_pup():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    else:
        return render_template('add.html', form=form)

@app.route('/list')
def list_pup():
    #Grad a list of puppies from database.
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)

@app.route('/delete', methods=['GET','POST'])
def del_pup():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()
        
        return redirect(url_for('list_pup'))

    else:
        return render_template('delete.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
    