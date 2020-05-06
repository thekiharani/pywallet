from datetime import datetime
from wallet import db

# models
class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	email = db.Column(db.String(100), unique=True, nullable=False)
	phone = db.Column(db.String(20), unique=True)
	balance = db.Column(db.Integer, nullable=False, default=500)
	password = db.Column(db.String(60), nullable=False)

	txns_out = db.relationship('Transaction', backref='sender', lazy=True, foreign_keys='transactions.sender_id')
	txns_in = db.relationship('Transaction', backref='receiver', lazy=True, foreign_keys='transactions.receiver_id')

	def __repr__(self):
		return f'User({self.name}, {self.email}, {self.phone})'

class Transaction(db.Model):
	__tablename__ = 'transactions'
	id = db.Column(db.Integer, primary_key=True)
	txn_id = db.Column(db.String(25), nullable=False)
	sender_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='cascade'), nullable=False)
	receiver_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='cascade'), nullable=False)
	amount = db.Column(db.Integer, nullable=False)
	direction = db.Column(db.String(20), nullable=False)
	timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __repr__(self):
		return f'Transaction({self.sender.name}, {self.receiver.name})'