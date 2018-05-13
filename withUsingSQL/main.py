from datetime import datetime 
from flask import Flask,render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

'''
manual to create db
cd to your directory
open python3 terminal 
from main import db
db.create_all() #to create the database that call site.debug
from main import User,Post
user_1=User(useranme='user',email='user@user.com',password='user')
db.session.add(user_1)
db.session.commit()
User.query.all()
User.query.first()
User.query.filter_by(username='?').all()
User.query.filter_by(username='?').first()
user1=User.query.filter_by(username='?').first()
user.id
user.password
user=User.query.get(2)#id
post_1=Post(title='Blog1',content='First blog',user_id=user.id)
post.author
delete data 
db.drop_all()
db.create_all()
'''


#create a secrets key
#import secrets
#secrets.token_hex(16)
app.config['SECRET_KEY']='b32ed2c46bcdc53f1b330dee8f7c8cf2'

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)

class User(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	username=db.Column(db.String(20), unique=True,nullable=False)
	email=db.Column(db.String(120), unique=True,nullable=False)
	image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
	password=db.Column(db.String(60),nullable=False)
	# link a post model and can ref by using author
	posts=db.relationship('Post',backref='author',lazy=True)

	def __repr__(self):
		return f"User('{self.username}','{self.email},'{self.image_file}')"

class Post(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	title=db.Column(db.String(100),nullable=False)
	date_posted=db.Column(db.DateTime,nullable=False, default=datetime.utcnow)
	content=db.Column(db.Text,nullable=False)
	user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

	def __repr__(self):
		return f"Post('{self.title}','{self.date_posted}'')"

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