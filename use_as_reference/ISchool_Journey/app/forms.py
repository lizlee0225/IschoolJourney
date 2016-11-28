'''
code adapted from 2016 FA INFO 290 TA project assignment
'''
from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, PasswordField, SelectField
from flask_wtf.html5 import EmailField
from wtforms import validators
import sqlite3 as sql

# existing user login form
class LoginForm(Form):
    email = EmailField('username / login email', [validators.required()])
    insecure_password = PasswordField('password', [validators.required()])

# user sign up form
class SignUpForm(Form):
	email = EmailField('username / login email', [validators.required()])
	insecure_password = PasswordField('password', [validators.required()])
	fname = StringField('fname', [validators.required()])
	lname = StringField('lname', [validators.required()])

class CareerForm(Form):
    careers_name = StringField('careers_name', [validators.required()])
    with sql.connect("app.db") as con:
        con.row_factory = sql.Row
        results = con.execute("SELECT * FROM careers").fetchall()
    career = SelectField(u'careers_name', choices = [ (str(item[1]), str(item[1])) for item in results])
