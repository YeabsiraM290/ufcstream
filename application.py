import os, hashlib

from flask import Flask, session, render_template,request, redirect,url_for, g
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_socketio import SocketIO, send
from form import *

app = Flask(__name__)
app.config['SECRET_KEY']='7ff61fae7049489'
socketio = SocketIO(app, cors_allowed_origins='*')

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.before_request
def before_request():
    g.user = None

    if 'userName' in session:
        g.user = db.execute(f"SELECT * FROM users WHERE username = '{session['userName']}'").first().username

@app.route("/")
def index():
    if g.user is None:
    
        return redirect(url_for('login'))
    return render_template('index.html',user=g.user)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':

        session.pop('user_id', None)
        username = form.username.data
        password = hashlib.sha1(form.password.data.encode('utf-8')).hexdigest()

        user = db.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'").first()

        if user is None:

            return render_template("login.html",message="* Wrong password or username", form=form)

        if user:

            session['userName'] = user.username
            return redirect(url_for('index'))

    return render_template("login.html", form=form)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if request.method == "POST":

        username = form.username.data
        password = hashlib.sha1(form.password.data.encode('utf-8')).hexdigest()
        email = form.email.data

        if db.execute("SELECT * FROM users WHERE username = :username", {"username": username}).rowcount != 0:
            return render_template("signup.html",message="* Username "+username+ " is already in use",form=form)
        
        if db.execute("SELECT * FROM users WHERE email = :email", {"email": email}).rowcount != 0:
            return render_template("signup.html",message="* Email is already in use",form=form)

        db.execute(f"INSERT INTO users(username, email, password) VALUES ('{username}', '{email}', '{password}');")
        db.commit()

        session['userName'] = username

        return redirect(url_for('index'))


    return render_template("signup.html", form=form)

@app.route("/logout")
def logout():

    session.pop('userName', None)
    g.user = None

    return redirect(url_for('login'))


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    socketio.emit('my response', json)

if __name__ == '__main__':
    socketio.run(app, debug=True)