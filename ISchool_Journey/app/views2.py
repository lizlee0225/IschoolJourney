'''
code adapted from 2016 FA INFO 290 TA project assignment
'''
from app import myapp, models
from flask import render_template, redirect, request, session, url_for, escape, flash
from .forms import LoginForm, SignUpForm

"""
View functions:
* Handle logic on the front-end
* Access the models file to use SQL functions
"""

# landing redirect
@myapp.route('/')
@myapp.route('/index')
def index():
	return redirect('/login')

# ------------ User Session Management ------------
# login
@myapp.route('/login', methods=['GET', 'POST'])
def login():
	user = ''
	error = None

	# if already logged in, redirect to the trips overview
	if 'user' in session:
		user = escape(session['user'])
		return redirect('/main')
	else: # login
		form = LoginForm()
		if form.validate_on_submit():
			error = None

			# user input
			email = form.email.data
			pwd = form.insecure_password.data

			# return user first name only if email, pwd match DB record
			user = models.validate_user(email, pwd)

			if user is not None:
				flash('Logging in')
				session['user'] = user
				session['email'] = email
				return redirect('/main')
			else:
				error = 'Invalid credentials'
	return render_template('login.html', error = error, form = form)

# # sign up
# @myapp.route('/signup', methods=['GET', 'POST'])
# def signup():
# 	user = ''
# 	error = None

# 	# if already logged in, redirect to the trips overview
# 	if 'user' in session:
# 		user = escape(session['user'])
# 		return redirect('/trips')
# 	else: # sign up
# 		form = SignUpForm()
# 		if form.validate_on_submit():
# 			error = None

# 			# user input
# 			email = form.email.data
# 			pwd = form.insecure_password.data
# 			fname = form.fname.data
# 			lname = form.lname.data

# 			# insert the user into the database if the email address is not already associated with an account
# 			if models.retrieve_user_id(email) is None:
# 				user = models.signup_user(email, fname, lname, pwd)
# 				return redirect('/login')
# 			else:
# 				error = 'An account with that email address already exits.'
# 	return render_template('signup.html', error = error, form = form)

# # logout
# @myapp.route('/logout')
# def logout():
# 	session.pop('user', None)
# 	flash('You were logged out')
# 	return redirect(url_for('login'))


# @myapp.route('/main')
# def main():
# 	if 'user' in session:
# 		user = escape(session['user'])
# 		return render_template('main.html', user = user)
# 	else: # login
# 		return redirect('/login')

# @myapp.route('/select')
# def select():
# 	if 'user' in session:
# 		user = escape(session['user'])
# 		return render_template('main2.html', user = user)
# 	else: # login
# 		return redirect('/login')
