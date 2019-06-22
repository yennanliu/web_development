from flask import Flask, jsonify, abort, make_response, request 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud_sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

# flask hello world 
@app.route('/')
def index():
	return "Hello, World!"

# handle error
@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

# define DB model 
class Products(db.Model):
	id  = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80), unique=False)
	description = db.Column(db.String(80), unique=False)
	sold = db.Column(db.String(80), unique=False)

	def __init__(self, id, title, description, sold):
		self.id = id 
		self.title = title
		self.description = description
		self.sold = sold

class ProductSchema(ma.Schema):
	class Meta:
		# fields to expose 
		fields = ('id', 'title', 'description', 'sold')

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# GET method  (via DB)
@app.route('/product/api/v1.0/products', methods=['GET'])
def get_product():
	all_products = Products.query_all()
	result = products_schema.dump(all_products)
	print ('result :', result)
	return jsonify(result.data)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
