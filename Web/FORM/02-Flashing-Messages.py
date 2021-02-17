from flask import Flask, render_template, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

class SimpleForm(FlaskForm):
    submit = SubmitField('클릭하세용.')

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = SimpleForm()
    if form.validate_on_submit():
        flash('버튼을 클릭하셨습니다.') # 메세지를 알려주는 것
        return redirect(url_for('index'))
    return render_template('02-home.html', form = form)


if __name__ == '__main__':
    app.run(debug=True)