from flask import Flask, jsonify, abort, make_response, request 
import sqlite3
import os

app = Flask(__name__)

# flask hello world 
@app.route('/')
def index():
	return "Hello, World!"

# handle error
@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

# GET method  (via DB)
@app.route('/product/api/v1.0/products', methods=['GET'])
def get_product():
	with sqlite3.connect("database.db") as con:
		cur = con.cursor()
		cur.execute("SELECT * FROM products;")
		result = cur.fetchall()
		print ('result :', result)
		return jsonify(result)

# GET method with parameter 
@app.route('/product/api/v1.0/products/<int:product_id>', methods=['GET'])
def get_product_with_parameter(product_id):
	with sqlite3.connect("database.db") as con:
		cur = con.cursor()
		cur.execute("SELECT * FROM products WHERE id = {};".format(product_id))
		result = cur.fetchall()
		print ('result :', result)
		if len(result) == 0:
			abort(404)
		return jsonify({'product':result})

# POST method 
@app.route('/product/api/v1.0/products', methods=['POST'])
def create_product():
	with sqlite3.connect("database.db") as con:
		cur = con.cursor()
		cur.execute("SELECT count(*) FROM products;")
		count = cur.fetchall()[0][0]
		product = {'id': count,
		'title': request.json['title'],
		'description': request.json.get('description', ""),
		'sold': False}
		cur.execute("INSERT INTO products (id, title, description, sold) VALUES (?,?,?,?)",  (count, request.json['title'], request.json.get('description', ""), 'false'))
		con.commit()
		print ('Insert data OK')
	return jsonify({'product': product}), 201 

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
