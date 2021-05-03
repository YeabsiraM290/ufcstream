from flask import Flask, session, render_template
from form import *

app = Flask(__name__)
app.config['SECRET_KEY']='7ff61fae7049489'

# @app.before_request
# def before_request():
#     g.user = None

#     if 'userName' in session:
#         g.user = session['userName']

@app.route("/")
def index():
    userName="y"
    return render_template('index.html',user=userName)

@app.route("/login")
def login():
    return render_template('login.html',form=LoginForm())

@app.route("/signup")
def signup():
    return render_template('signup.html',form=SignupForm())
    