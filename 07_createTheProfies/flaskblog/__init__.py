
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY']='b32ed2c46bcdc53f1b330dee8f7c8cf2'

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
# the function name of route
login_manager.login_view='login'
# sytleing of the message
login_manager.login_message_category='info'




from flaskblog import route