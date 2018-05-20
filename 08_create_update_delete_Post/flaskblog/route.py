from flaskblog.models import User,Post
from flaskblog import app,db,bcrypt
from flask import render_template,url_for,flash,redirect,request,abort
from flaskblog.forms import RegistrationForm,LoginForm,UpdateAccountForm,PostForm
from flask_login import login_user,current_user,logout_user,login_required
import secrets
import os
from PIL import Image

@app.route("/")
@app.route("/home")
def home():
	# 
	posts=Post.query.all()
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


def save_picture(form_pictrue):
	#rename first
	random_hex=secrets.token_hex(8)
	#get the extention 
	_,f_ext=os.path.splitext(form_pictrue.filename)
	picture_fn = random_hex+f_ext 
	picture_path=os.path.join(app.root_path,'static/profile_pics',picture_fn)
	
	# 
	output_size=(125,125)
	i=Image.open(form_pictrue)
	i.thumbnail(output_size)

	i.save(picture_path)
	return picture_fn

@app.route("/account",methods=['GET','POST'])
@login_required
def account():
	form=UpdateAccountForm()
	if form.validate_on_submit():
		if form.picture.data:
			picture_fn=save_picture(form.picture.data)
		current_user.username=form.username.data
		current_user.email=form.email.data
		current_user.image_file=picture_fn
		db.session.commit()
		flash('your account has been updated !','success')
		return redirect(url_for('account'))
	elif request.method =='GET':
		form.username.data=current_user.username
		form.email.data=current_user.email
	image_file = url_for('static',filename='profile_pics/'+current_user.image_file)
	return render_template('account.html',title='account',image_file=image_file,form=form)

@app.route('/post/new',methods=['GET','POST'])
@login_required
def new_post():
	form=PostForm()
	if form.validate_on_submit():
		post=Post(title=form.title.data,content=form.content.data,author=current_user)
		db.session.add(post)
		db.session.commit()
		flash('your post has been created','success')
		return redirect(url_for('home'))
	return render_template('create_post.html',title='create post',form=form,legend='Update Post')

# 
@app.route('/post/<int:post_id>')
def post(post_id):
	# 
	post=Post.query.get_or_404(post_id)
	return render_template('post.html',title=post.title,post=post)

@app.route('/post/<int:post_id>/update',methods=['GET','POST'])
@login_required
def update_post(post_id):
	post=Post.query.get_or_404(post_id)
	if post.author != current_user:
		# 
		abort(403)
	form=PostForm()
	if form.validate_on_submit():
		post.title=form.title.data
		post.content=form.content.data
		db.session.commit()
		flash('your post is updated','success')
		return redirect(url_for('post',post_id=post.id))
	elif request.method == 'GET':		
		form.title.data=post.title
		form.content.data=post.content

	return render_template('create_post.html',title='Update post',form=form,legend='Update Post')


@app.route('/post/<int:post_id>/delete',methods=['POST'])
@login_required
def delete_post(post_id):
	post=Post.query.get_or_404(post_id)
	if post.author != current_user:
		# 
		abort(403)

	db.session.delete(post)
	db.session.commit()
	flash('your post is deleted','success')
	return redirect(url_for('home'))






























