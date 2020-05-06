# system modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# Make use of variables in .env file within the app
from environs import Env
import os
env = Env()
env.read_env()

app = Flask(__name__)
# app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY") # reading from .env
app.config['SECRET_KEY'] = 'Fv3tgWAniOpjQpkyoxbHEEyQUrLsANz21LXVDr4G'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Wallet.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

from wallet import routes