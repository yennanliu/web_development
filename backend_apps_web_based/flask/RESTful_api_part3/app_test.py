import sys, os, json, requests
import pytest, unittest
from flask_sqlalchemy import SQLAlchemy
# main flask app 
from app import app 

db = SQLAlchemy(app)

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
        db.drop_all()
        db.create_all()
        self.assertEqual(app.debug, False)
    # executed after each test
    def tearDown(self):
        pass
 	# tests 
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    TestHelloworld()
    TestApi()
    unittest.main()