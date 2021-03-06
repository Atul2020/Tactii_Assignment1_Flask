from flask_wtf import FlaskForm
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,Email,EqualTo


class RegistrationForm(FlaskForm):
	username = StringField('Username', validators = [DataRequired(),Length(min = 2, max = 20)])
	email = StringField('Email',validators = [DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired
	confirm_password = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')


 class loginForm(FlaskForm):
	email = StringField('Email',validators = [DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired
	submit = SubmitField('Login')
