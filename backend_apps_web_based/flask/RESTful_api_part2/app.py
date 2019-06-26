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

# PUT method 
@app.route('/product/api/v1.0/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
	with sqlite3.connect("database.db") as con:
		cur = con.cursor()
		cur.execute("SELECT * FROM products where id = {};".format(product_id))
		result = cur.fetchall() 
		if len(result) == 0:
			abort(404)
		if not request.json:
			abort(400)
		if 'title' in request.json and type(request.json['title']) != str:
			abort(400)
		if 'description' in request.json and type(request.json['description']) is not str:
			abort(400)
		if 'sold' in request.json and type(request.json['sold']) is not bool:
			abort(400)
		cur.execute("UPDATE products SET  title = '{}', description = '{}' where id = {} ".format(request.json['title'],request.json['description'], product_id))
		con.commit() 
	return jsonify({'product': result[0]}) 

# DELETE method 
@app.route('/product/api/v1.0/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
	with sqlite3.connect("database.db") as con:
		cur = con.cursor()
		cur.execute("DELETE FROM products WHERE ID = {};".format(product_id))
		con.commit()
		print ('Delete data OK')
	return jsonify({'result': True})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
