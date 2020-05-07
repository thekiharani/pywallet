from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.fields import html5 as h5fields
from wtforms.widgets import html5 as h5widgets
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from wallet.models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
	name = StringField('Official Name', validators=[DataRequired(), Length(min=2)])
	email = StringField('Email Address', validators=[DataRequired(), Email()])
	phone = StringField('Phone Number', validators=[DataRequired(), Length(10)])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

	submit=SubmitField('Sign Up')

	# custom validation
	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('This email address is already taken! Please use a different one or login if the associated account belongs to you.')

	def validate_phone(self, phone):
		user = User.query.filter_by(phone=phone.data).first()
		if user:
			raise ValidationError('This phone number is already taken! Please use a different one or login if the associated account belongs to you.')


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

class SendMoneyForm(FlaskForm):
	receiver = SelectField('Select Receiver', validators=[
        DataRequired()], coerce=int)
	amount = h5fields.IntegerField('Amount to Send', widget=h5widgets.NumberInput(min=1, max=70000, step=1))

	submit=SubmitField('Send Money')

	# custom validation
	def validate_amount(self, amount):
		user = User.query.filter_by(email=current_user.email).first()
		if current_user.balance < amount.data:
			raise ValidationError(f'Sorry, but you have insufficient balance to complete this transaction. Your balance is {current_user.balance}. Please top-up and try again.')