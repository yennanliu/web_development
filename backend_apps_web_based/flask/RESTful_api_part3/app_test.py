import sys
import requests
import json
import pytest

def test_helloworld():
    response = requests.get('http://0.0.0.0:5000/')
    assert response.status_code == 200

def test_api():
    response = requests.get('http://0.0.0.0:5000/product/api/v1.0/products')
    print (response)
    assert response.status_code == 200

if __name__ == "__main__":
    test_helloworld()
    test_api()