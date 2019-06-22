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

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
