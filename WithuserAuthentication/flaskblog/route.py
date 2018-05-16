from flaskblog.models import User,Post
from flaskblog import app,db,bcrypt
from flask import render_template,url_for,flash,redirect,request
from flaskblog.forms import RegistrationForm,LoginForm
from flask_login import login_user,current_user,logout_user,login_required


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
	# if user is logged in
	if current_user.is_authenticated:
		return redirect(url_for('home'))

	form=RegistrationForm()
	# if sumbit is pressed in the Registration pages
	if form.validate_on_submit():
		# generate a hash password
		hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		# add to database
		user=User(username=form.username.data,email=form.email.data,password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('you had created the account!please engjoy!','success')
		return redirect(url_for('login'))
	return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():

	if current_user.is_authenticated:
		return redirect(url_for('home'))

	form=LoginForm()
	#if sumbit is pressed in the login page
	if form.validate_on_submit():
		user=User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password,form.password.data):
			login_user(user,form.remember.data)
			# http://localhost:5000/login?next=%2Faccount
			# if the guys click the page before login
			next_page=request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('login failed...','danger')
	return render_template('login.html',title='login',form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
	return render_template('account.html',title='account')





