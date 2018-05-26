from flask_wtf import FlaskForm
from wtforms import SubmitField

class saveLayoutForm(FlaskForm):
	submit=SubmitField('Save the Layout')