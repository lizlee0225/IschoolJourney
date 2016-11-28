from app import myapp, models
from flask import render_template, Flask, redirect, url_for, session, request, jsonify, flash
from flask_oauthlib.client import OAuth
from .forms import LoginForm, SignUpForm


app = Flask(__name__)
app.config.from_object('config')
oauth = OAuth()

linkedin = oauth.remote_app(
	'linkedIn',
	consumer_key='86faisvke7rqht',
	consumer_secret='vfywuq3lwEUUqzU2',
	request_token_params={
		'scope': 'r_basicprofile',
		'state': 'RandomString',
	},
	base_url='https://api.linkedin.com/v1/',
	request_token_url=None,
	access_token_method='POST',
	access_token_url='https://www.linkedin.com/uas/oauth2/accessToken',
	authorize_url='https://www.linkedin.com/uas/oauth2/authorization',
)

@myapp.route('/')
@myapp.route('/index')
def index():
	if 'linkedin_token' in session:
		print("in session")
		me = linkedin.get('people/~')
		print(jsonify(me.data))
		return jsonify(me.data)
	return redirect(url_for('login'))


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

# @myapp.route('/')
# @myapp.route('/index')
# def index():
#     print("YAY")
#     return redirect(url_for('/login'))

# @app.route('/')
# @myapp.route('/index')
# def index():
#     print("YAY")
#     if 'linkedin_token' in session:
#         print("in session")
#         me = linkedin.get('people/~')
#         print(jsonify(me.data))
#         return jsonify(me.data)
#     return redirect(url_for('/login'))


# @app.route('/login')
# def login():
#     return linkedin.authorize(callback=url_for('authorized', _external=True))


# @app.route('/logout')
# def logout():
#     session.pop('linkedin_token', None)
#     return redirect(url_for('/index'))


# @app.route('/login/authorized')
# def authorized():
#     resp = linkedin.authorized_response()
#     if resp is None:
#         return 'Access denied: reason=%s error=%s' % (
#             request.args['error_reason'],
#             request.args['error_description']
#         )
#     session['linkedin_token'] = (resp['access_token'], '')
#     me = linkedin.get('people/~')
#     return jsonify(me.data)


# @linkedin.tokengetter
# def get_linkedin_oauth_token():
#     return session.get('linkedin_token')


# def change_linkedin_query(uri, headers, body):
#     auth = headers.pop('Authorization')
#     headers['x-li-format'] = 'json'
#     if auth:
#         auth = auth.replace('Bearer', '').strip()
#         if '?' in uri:
#             uri += '&oauth2_access_token=' + auth
#         else:
#             uri += '?oauth2_access_token=' + auth
#     return uri, headers, body

# linkedin.pre_request = change_linkedin_query


# if __name__ == '__main__':
#     app.run()