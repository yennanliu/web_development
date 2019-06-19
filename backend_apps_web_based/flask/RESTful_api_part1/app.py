from flask import Flask, jsonify 

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
