
from flask import Flask, render_template, request, redirect, g, session, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import or_


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tilotichxgywbm:eacaf88ac2b3576f3ea9cddd3ba1152be0aa278124db8c54a11f127ab1c4fd9c@ec2-107-22-245-82.compute-1.amazonaws.com:5432/dea6i97p3prkub'
db = SQLAlchemy(app)

class Users(db.Model):
    userid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    

    def init(self, username, email, password):
        self.username = username
        self.password = password
        self.email = email





