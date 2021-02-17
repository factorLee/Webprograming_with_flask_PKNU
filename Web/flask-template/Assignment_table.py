from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return '/input number' # 입력을 요구하는 기본 주소
 
@app.route('/<num>')
def table(num):
    return render_template('Assignment_table.html', num=num)

if __name__ == '__main__':
    app.run() 