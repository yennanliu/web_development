from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)
Migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Product(db.Model):
	__tablename__ = 'products'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64), unique=False, primary_key=False)
	description = db.Column(db.String(128), unique=False, primary_key=False)
	sold = db.Column(db.String(64), unique=False, primary_key=False)

	def __init__(self, title, description, sold):
		self.title = title
		self.description = description
		self.sold = sold

if __name__ == '__main__':
	manager.run()