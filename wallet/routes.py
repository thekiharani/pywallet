from random import random
from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required

from wallet import app, db, bcrypt, login_manager
from wallet.models import User, Transaction
from wallet.forms import RegistrationForm, LoginForm, ForgotPasswordForm, ResetPasswordForm, SendMoneyForm

@app.route("/")
def index():
	return render_template('index.html', title='Welcome')

@app.route("/wallet")
def wallet():
	return render_template('wallet.html', title='Wallet')

@app.route("/register", methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		# hash the password
		hash_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(name=form.name.data, email=form.email.data, phone=form.phone.data, password=hash_pwd)
		db.session.add(user)
		db.session.commit()

		flash('Success! Your account has been created. You have been awarded KSH 500 welcome credit. Login to start transacting.', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form = form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(phone=form.phone.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('index'))
		else:
			flash('Authentication failed! Please check your phone number and password.', 'danger')
	return render_template('login.html', title='Login', form = form)

@app.route("/send_money", methods=['GET', 'POST'])
@login_required
def send_money():
	form = SendMoneyForm()
	form.receiver.choices = [(user.id, f'{user.name} - {user.phone}')
                            for user in User.query.filter(User.id != current_user.id).order_by('name')]
	if form.validate_on_submit():
		txn_id = round(random()*10**10)
		txn = Transaction(txn_id=txn_id, sender_id=current_user.id, receiver_id=form.receiver.data, amount=form.amount.data)
		db.session.add(txn)
		db.session.commit()

		current_user.balance = current_user.balance - form.amount.data
		db.session.commit()

		receiver = User.query.filter_by(id=form.receiver.data).first()
		receiver.balance = receiver.balance + form.amount.data
		db.session.commit()

		flash(f'{txn_id} - Confirmed: KSH {form.amount.data} sent to {receiver.name}. Your new balance is KSH {current_user.balance}', 'success')
		return redirect(url_for('index'))

	return render_template('send_money.html', title='Send Money', form = form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route("/forgot_password", methods=['GET', 'POST'])
def forgot_password():
	form = ForgotPasswordForm()
	return render_template('forgot_password.html', title='Forgot Password', form = form)

@app.route("/reset_password", methods=['GET', 'POST'])
def reset_password():
	form = ResetPasswordForm()
	return render_template('reset_password.html', title='Reset Password', form = form)