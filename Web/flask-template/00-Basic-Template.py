from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') #127.0.0.1:5000 주소값
def index():
    #HTML 파일을 다음과 같이 연결
    return render_template('00-Basic-Template.html')

if __name__ == '__main__':
    app.run()
