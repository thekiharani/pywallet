from flask import render_template, url_for, flash, redirect

from wallet import app
from wallet.models import User, Transaction
from wallet.forms import RegistrationForm, LoginForm, ForgotPasswordForm, ResetPasswordForm

@app.route("/")
def index():
	return render_template('index.html', title='Welcome')

@app.route("/wallet")
def wallet():
	return render_template('wallet.html', title='Wallet')

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash('Registration Successful! Login to Proceed.', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form = form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.phone.data == '0700112233' and form.password.data == '0700112233':
			flash('Success! You are Loggedin', 'success')
			return redirect(url_for('index'))
		flash('Authentication failed! Please check your credentials.', 'danger')
	return render_template('login.html', title='Login', form = form)

@app.route("/forgot_password", methods=['GET', 'POST'])
def forgot_password():
	form = ForgotPasswordForm()
	return render_template('forgot_password.html', title='Forgot Password', form = form)

@app.route("/reset_password", methods=['GET', 'POST'])
def reset_password():
	form = ResetPasswordForm()
	return render_template('reset_password.html', title='Reset Password', form = form)