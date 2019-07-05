import sys, os, json, requests
import pytest, unittest
from flask_sqlalchemy import SQLAlchemy
# main flask app 
from app import app 
from db import db 
from model import ProductData

#db = SQLAlchemy(app)

def TestHelloworld():
    response = requests.get('http://0.0.0.0:5000/')
    assert response.status_code == 200

def TestApi():
    response = requests.get('http://0.0.0.0:5000/product/api/v1.0/products')
    print (response)
    assert response.status_code == 200
 
class TestDB(unittest.TestCase):
# setup and tear down  
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'database.db'
        self.app = app.test_client()
        #db.drop_all()
        db.create_all()
        self.assertEqual(app.debug, False)
    # executed after each test
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    # tests api 
    def test_api(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    # test DB model 
    def test_model(self):
        # add prod 1 
        product1 = ProductData("cafe latte", "coffee + milk", "False") 
        db.session.add(product1)
        # add prod 2 
        product2 = ProductData("pizza", "dev love", "True") 
        db.session.add(product2)
        # add prod 3 
        product3 = ProductData("cake", "this is apple cake", "True") 
        db.session.add(product3)
        db.session.commit()
        assert len(ProductData.query.all()) == 3 
 

if __name__ == "__main__":
    TestHelloworld()
    TestApi()
    unittest.main()