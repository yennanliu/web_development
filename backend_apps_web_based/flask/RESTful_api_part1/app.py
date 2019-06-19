from flask import Flask, jsonify, abort 

app = Flask(__name__)

# flask hello world 
@app.route('/')
def index():
    return "Hello, World!"

# define the sample API data (hardcode)
products = [
    {
        'id': 1,
        'title': u'apple pie',
        'description': u'this is an apple pie',
        'sold': False
    },
    {
        'id': 2,
        'title': u'chicken burger',
        'description': u'a yammy chicken burger',
        'done': True
    }
]

# GET method 
@app.route('/product/api/v1.0/products', methods=['GET'])
def get_product():
	return jsonify({'product': products})

# GET method with parameter 
@app.route('/product/api/v1.0/products/<int:product_id>', methods=['GET'])
def get_product_with_parameter(product_id):
	product = list(filter(lambda t : t['id'] ==  product_id, products))
	if len(product) == 0:
		# if can't find the product with input id 
		abort(404)
	return jsonify({'product': product[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
