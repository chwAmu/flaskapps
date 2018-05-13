from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

#create a secrets key
#import secrets
#secrets.token_hex(16)
app.config['SECRET_KEY']='b32ed2c46bcdc53f1b330dee8f7c8cf2'

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

if __name__ == '__main__':
    app.run(debug=True)
