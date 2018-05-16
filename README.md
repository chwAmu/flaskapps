# flaskapps
this git is the notes that while watching the youtube video of Corey Schafer.
https://www.youtube.com/watch?v=QnDWIZuWYW0&index=1&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH

## basic
### main.py
a simple code with route the website in more than one path
 
### main3.py
a simple code that created the dummy data with list of dictionary,
and return the data, looping those by using jinja2 in html
and return the title name also
in templates directory, using {% if %}{% endif %} to return title
and using {% block content%}{% endblock %} to config the global area

## basic_with_boostrap
a simple code for using boostrap library, flask url_for libraray,
and how to arrange the files in flask.

## forms and input 
a code that create the user log-in or reg pages

flask_wtf to create the form
- StringField
- PasswordField
- SubmitField
- BooleanField

flask_wtf.validators to check the data
- DataRequired
- Length
- Email
- EqualTo
- min
- max

using build-in secrets modules to create the sercets key 
import secrets
secrets.token_hex(16)

using flash to flash a new message while user login/reg
using redirect to redirect the web-pages while user login/reg

## usingWithSQL
pip3 install sqlalchemy to install the using modules
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

## withUsingSQL_Modules
group all the stuff into packages
main.py-->run.py
create a flaskblog folder

## WithuserAuthentication
an example for user authentication
### flask-bcrypt library to hash the userpassword
pip3 install flask-bcrypt
then open the python3 terminal, test the function first

>>>from flask_bcrypt import Bcrypt
>>>bcrypt=Bcrypt
>>>crypt.generate_password_hash('testing')
>>>crypt.generate_password_hash('testing').decode('utf-8')
>>>hashed_pw=crypt.generate_password_hash('testing').decode('utf-8')
how to check password?
>>>bcrypt.check_password_hash(hashed_pw,'password')
>>>False
bcrypt.check_password_hash(hashed_pw,'testing')
>>>True

### using the flask-login modules to control the login/logout function
pip3 install flask-login
from flask_login import LoginManager
from flask_login import login_user,current_user,logout_user,login_required

-login_user to login
-current_user to get the current user name
-logout_user to logout
-login_required to protect the route can only aceess after login

### using flask request modules to get the parameters
from flask import request
before login if the guys try to access the account routes
http://localhost:5000/login?next=%2Faccount
we can just take the parameters 'next'
next_page=request.args.get('next')

not only just need to login and also assing the route of login
login_manager.login_view='login'
login is the function name of route

login_manager.login_message_category='info'
you can styling the message.

current_user.is_authenticated 
to check the user is logined or not

### create your ouwn validation error
form weforms.validators import ValidationError
	def validate_username(self,username):
		user=User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('that username is taken.')
to raise the error if the user is existed while create a new account.



