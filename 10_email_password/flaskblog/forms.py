# a form class with using the flask_wtf modules
# pip3 install flask_wtf

from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from flask_wtf.file import FileField,FileAllowed #
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flaskblog.models import User
from flask_login import current_user

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

	# custom your own validator for check the username and email is exist or not
	def validate_username(self,username):
		user=User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('that username is taken.')


	def validate_email(self,email):
		email=User.query.filter_by(email=email.data).first()
		if email:
			raise ValidationError('that email is taken.')

class LoginForm(FlaskForm):
	email = StringField('Email',validators=[DataRequired(),Email()])
	password = PasswordField('Password',validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
	username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
	email = StringField('Email',validators=[DataRequired(),Email()])
	# 
	picture = FileField('Update Profie picture',validators=[FileAllowed(['jpg','png'])])
	submit = SubmitField('Update')

	# custom your own validator for check the username and email is exist or not
	def validate_username(self,username):
		if username.data !=current_user.username:
			user=User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('that username is taken.')


	def validate_email(self,email):
		if email.data !=current_user.email:
			email=User.query.filter_by(email=email.data).first()
			if email:
				raise ValidationError('that email is taken.')

class PostForm(FlaskForm):
	title=StringField('Title',validators=[DataRequired()])
	content=TextAreaField('Content',validators=[DataRequired()])
	submit = SubmitField('Post')


class ResetRequestForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	submit = SubmitField('Reset your password')

	def validate_email(self,email):
		email=User.query.filter_by(email=email.data).first()
		if email is None :
			raise ValidationError('no accout with this email.')

class ResetPasswordForm(FlaskForm):
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Reset Password')