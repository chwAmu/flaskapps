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
>pip3 install flask-login
>from flask_login import LoginManager
>from flask_login import login_user,current_user,logout_user,login_required

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


## 07_createTheProfiles
the code to create the user profiles, upload pictures and resize it into a small sizes.

### account.html - add user code
- enctype="multipart/form-data" seeems like it is very import for uploading the files?
- add the form-group of username,email,and picture upload.
- add the current user information by using:
-- current_user.username
-- current_user.email
-- imge class src='image_file' , it is passed form route.py

### form.py - add new form for the account update
from flask_wtf.file import FileField,FileAllowed
let the user can upload the files

#### from flask_login import current_user
add the current_user information to verify the current_user

#### class UpdateAccountForm 
it is the class for the form of accout update
validators that we used is FileAllowed(['jpg','png']) to limit which type of files can be upload.
the customeize validators is changed if the username is not equal the current_user name.

### route .py

#### def save_picture(form_pictrue) is added
- step1, generate a random hex code
- step2, get the file name by using os.path.splitext(form_picuture.filename)
- step3, set the file name variables to random_hex_code.ext that you get in step1,2
- step4, set the path by using os.path.join(app.root_path,path)
- step5, resize the pictures to 125x125 because the large pics will slow down the web and waste the space.
- Step6, from PIL import Image - it seems like this modules can not worked in my mac,pip3 install pillow==5.0.0 to install pre version
- Step7, open the picture file that we passed inside the function and resize it.
- Step8, return the filename

#### def account() is changed
current_user.image_file=picture_fn to set the picture name to DB aslo.

if the user reload the web,
request.method =='GET': to get the request type

## 08_create_update_delete_Post

### forms.py
- add PostForm,TextAreaField to let the user the enter their post.

### home.html
- delete all the dummy post.
- display the dataformat to use strftime('%Y-%m-%d').
- in the post title,href="{{url_for('post',post_id=post.id)}}" pass the id to route.py

### post.html
- this is the web page that for create the update/delete/view the own page.
- src="{{ url_for('static',filename='profile_pics/'+post.author.image_file)}}" to load the user image file
- if current user is equal to post user, then show the page
- show the update and delete button
- if delete button is pressed, use the bootstrap modal to make a confirm button.

### route.py

#### def post(post_id):
- a function to return the post of the current id
- if the user focely some link is not existed, /post/1234, return a 404

#### def update_post(post_id):
- if post is not in here, return 404
- if the user tried to edit some post that not created to him/her, return 403
- and also if the submit button pressed, update the db and flash
- and also if the method is 'get', just return the post content.

#### def delete_post(post_id):
- if the user tried to delete some post that not created to him/her, return 403



