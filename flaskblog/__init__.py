from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)	#initializer for flask application. Tells the machine 
						#where to look for the Flask Application Code
app.config['SECRET_KEY'] = 'db1bacd0b582a7e7427d98054e3d3517'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from flaskblog import routes