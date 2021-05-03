from flask_wtf import FlaskForm
from sqlalchemy.sql.expression import text
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import *

class SignupForm(FlaskForm):
   email = StringField('Email:', validators=[
        DataRequired()
    ])

   username = StringField('Username:', validators=[
        DataRequired()
    ])

   password = PasswordField('Password:', validators=[
        DataRequired(),
        EqualTo('confirm', 
                           message='Passwords must match')
    ])

   confirm = PasswordField('confirm password:', validators=[
        DataRequired()
    ])

   signup = SubmitField('Register')

class LoginForm(FlaskForm):

    username = StringField('Username:', validators=[
        DataRequired()
    ])

    password = PasswordField('Password:', validators=[
        DataRequired()
    ])


    login = SubmitField('Login')

class CommentForm(FlaskForm):
    
    text_area = TextAreaField(' ', validators=[
        DataRequired()
    ])
    submit = SubmitField('Submit')
