from flaskblog.models import User,Post
from flaskblog import app,db,bcrypt
from flask import render_template,url_for,flash,redirect
from flaskblog.forms import RegistrationForm,LoginForm

#pip3 install flask-bcrypt
#open the python3 terminal
#from flask_bcrypt import Bcrypt
#bcrypt=Bcrypt
#crypt.generate_password_hash('testing')
#crypt.generate_password_hash('testing').decode('utf-8')
#hashed_pw=crypt.generate_password_hash('testing').decode('utf-8')
#check password
#bcrypt.check_password_hash(hashed_pw,'password')
#it should be False
#bcrypt.check_password_hash(hashed_pw,'testing')
#it should be True

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
		hashed_password=bcrypt.generate_passowrd_hash(form.password.data).decode('utf-8')
		user=User(username=form.user.data,email=form.email.data,password=hashed_password)
		db.session.add(user)
		db.session.commint()
		flash('you had created the account!please engjoy!','success')
		return redirect(url_for('login'))
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