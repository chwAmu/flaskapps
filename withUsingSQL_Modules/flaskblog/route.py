from flaskblog.models import User,Post
from flaskblog import app
from flask import render_template,url_for,flash,redirect
from flaskblog.forms import RegistrationForm,LoginForm

#create a dummy data dictionary of list
posts=[
	{
		'author':'hiroshi',
		'title':'post1',
		'content':'mypost1',
		'data_posted':'2018-05-10'
	}
	,
	{
		'author':'amu',
		'title':'post2',
		'content':'mypost2',
		'data_posted':'2018-05-11'
	}
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')


@app.route("/register",methods=['GET','POST'])
def register():
	form=RegistrationForm()
	# if sumbit is pressed in the Registration pages
	if form.validate_on_submit():
		flash(f'Account Created for { form.username.data}!','success')
		return redirect(url_for('home'))
	return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
	form=LoginForm()
	#if sumbit is pressed in the login page
	if form.validate_on_submit():
		# just using a dummy data
		if form.email.data =='admin@login.com' and form.password.data=='password':
			# login ok
			flash('You have been logged in!','success')
			return redirect(url_for('home'))
		else:
			# login false
			flash('logged in failed...','danger')
	return render_template('login.html',title='login',form=form)