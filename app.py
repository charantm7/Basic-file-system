from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Hey i am charan"

@app.route('/login/<int:score>')
def login_func(score):
    return "Hey here is the login page"+ str(score)

@app.route('/home/<int:page>')
def home_page(page):
    return "Hey here is the home page "+ str(page)

if __name__=='__main__':
    app.run(debug=True)