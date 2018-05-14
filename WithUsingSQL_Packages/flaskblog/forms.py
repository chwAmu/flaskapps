# a form class with using the flask_wtf modules
# pip3 install flask_wtf

from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo

#create a class to inherit from FlaskForm
class RegistrationForm(FlaskForm):
	#create the input stringfield and set some limit
	#1-no empty 2-the length
	#in the password field, make sure the password=confirm_password by using EqualTox
	username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
	email = StringField('Email',validators=[DataRequired(),Email()])
	password = PasswordField('Password',validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
	submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
	email = StringField('Email',validators=[DataRequired(),Email()])
	password = PasswordField('Password',validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')