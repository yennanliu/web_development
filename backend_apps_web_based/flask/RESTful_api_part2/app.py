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
		con.close()
		print ('result :', result)
		return jsonify(result)

# GET method with parameter 
@app.route('/product/api/v1.0/products/<int:product_id>', methods=['GET'])
def get_product_with_parameter(product_id):
	with sqlite3.connect("database.db") as con:
		cur = con.cursor()
		cur.execute("SELECT * FROM products WHERE id = {};".format(product_id))
		result = cur.fetchall()
		con.close()
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
		con.close()
		print ('Insert data OK')
	return jsonify({'product': product}), 201 


# PUT method 
# dev 
@app.route('/product/api/v1.0/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
	with sqlite3.connect("database.db") as con:
		cur = con.cursor()
		cur.execute("SELECT * FROM products where id = {};".format(product_id))
		result = cur.fetchall() 
		con.close()
    product = [product for product in result if product['id'] == product_id]
    if len(product) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'sold' in request.json and type(request.json['sold']) is not bool:
        abort(400)
    with sqlite3.connect("database.db") as con:
    	cur.execute("UPDATE products SET title={},  description={}, sold={} WHERE id={};".format(request.json['title'], request.json['description'], request.json['sold'], product_id )) 
    	con.close()
    return jsonify({'product': product[0]}) 

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
