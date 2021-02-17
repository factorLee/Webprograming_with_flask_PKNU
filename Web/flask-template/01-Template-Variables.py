from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Go to /puppy/name</h1>'

@app.route('/puppy/<name>')
def puppy_name(name):
    #html 파일에 변수를 전달한다.
    #html 파일 내에서 name 이라고 하는 변수에
    #위에서 입력한 name의 값을 전달
    return render_template('01-Template-Variables.html', name = name)

@app.route('/advpuppy/<name>')
def adv_puppy_name(name):
    #list('abc')  => ['a','b','c']
    letters = list(name) # 한글자 한글자가 리스트로 바뀜(파이썬 문법)
    pup_dict = {'pup_name': name} #딕셔너리에 pup_name 키캆에 우리가 입력한 name을 밸류로 대응
    return render_template('01-Template-Variables.html', name=name, mylist = letters, mydict = pup_dict)

if __name__ == '__main__':
    app.run()
