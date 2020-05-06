from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
	name = StringField('Official Name', validators=[DataRequired(), Length(min=2)])
	email = StringField('Email Address', validators=[DataRequired(), Email()])
	phone = StringField('Phone Number', validators=[DataRequired(), Length(10)])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

	submit=SubmitField('Sign Up')

class LoginForm(FlaskForm):
	phone = StringField('Phone Number', validators=[DataRequired(), Length(10)])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')

	submit=SubmitField('Login')

class ForgotPasswordForm(FlaskForm):
	phone = StringField('Phone Number', validators=[DataRequired(), Length(10)])

	submit=SubmitField('Request Reset')

class ResetPasswordForm(FlaskForm):
	password = PasswordField('New Password', validators=[DataRequired(), EqualTo('confirm_password')])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])

	submit=SubmitField('Reset')