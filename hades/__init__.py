from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///adverts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '90ef207dd27760040e6d30bf'

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager=LoginManager(app)

from hades import routes
