from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Go to puppy/name </h1>'

@app.route('/puppy/<name>')
def puppy_name(name):
    return render_template('02-Template-Filters.html', name=name)

if __name__ == '__main__':
    app.run()
