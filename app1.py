from flask import Flask,redirect,url_for,render_template,request
from os import sys

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/out/<int:score>')
def out(score):

    res = ''
    if score == 1:
        res = 'out'

    return render_template('result.html',result =res)

@app.route('/notout/<int:score>')
def notout(score):
    resa = ''
    if score == 0:
        resa = 'not out'
    return render_template('result.html',result =resa)

@app.route('/decision/<int:a>')


@app.route('/submit', methods = ['POST','GET'])
def submit():
    resu = ''
    resul=''
    if request.method == 'POST':
        resu = int(request.form['res'])
        
    if resu == 0:
        resul = 'notout'
    elif resu == 1:
        resul = 'out'
        
    
    return redirect(url_for(resul,score=resu))
            
if __name__ == '__main__':
    app.run(debug=True)