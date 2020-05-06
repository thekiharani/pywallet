from flask import Flask, render_template, url_for, flash, redirect

# Make use of variables in .env file within the app
from environs import Env
import os
env = Env()
env.read_env()
from forms import RegistrationForm, LoginForm, ForgotPasswordForm, ResetPasswordForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

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

if __name__ == '__main__':
	app.run(debug=True)