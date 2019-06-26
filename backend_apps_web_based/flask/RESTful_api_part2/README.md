## INTRO : RESTful API V2
  - Simplest API work with Database (sqlite)
  - No authentication methods 

## INTRO : RESTful API 
|  HTTP method | Action | Example |
| --- | -------- | ---- | 
|Get| Obtain information about a resource | http://0.0.0.0:5000/product/api/v1.0/products <br>(retrieve product list) | 
|Post| Create a new resource | http://0.0.0.0:5000/product/api/v1.0/products <br> (create a new order, from data provided with the request)| 
|Put| Update a resource | http://0.0.0.0:5000/product/api/v1.0/products/2 <br> (update product with id = 2, from data provided with the request) | 
|Delete| Delete a resource | http://0.0.0.0:5000/product/api/v1.0/products/2 <br> (delete prodcut with id = 2 ) | 

## Quick start 
``` bash
# fork the project 
# open 1 terminal run below commands 
$ cd~ && git clone https://github.com/yennanliu/web_development.git
$ cd~ && cd web_development/backend_apps_web_based/flask/RESTful_api_part2
$ pip install -r requirements.txt &&  python create_db.py && python app.py 

# when the flask server run at local successfully, 
# open the other terminal run the folloeing commands 
```
```bash 
# GET 
$ curl -i http://0.0.0.0:5000/product/api/v1.0/products

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 277
Server: Werkzeug/0.15.4 Python/3.6.4
Date: Wed, 19 Jun 2019 09:50:14 GMT

{
  "product": [
    {
      "description": "this is an apple pie", 
      "id": 1, 
      "sold": false, 
      "title": "apple pie"
    }, 
    {
      "description": "a yammy chicken burger", 
      "done": true, 
      "id": 2, 
      "title": "chicken burger"
    }
  ]
}

```
```bash 
# GET with parameter
$ curl -i http://0.0.0.0:5000/product/api/v1.0/products/2 
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 132
Server: Werkzeug/0.15.4 Python/3.6.4
Date: Wed, 19 Jun 2019 10:08:28 GMT

{
  "product": {
    "description": "a yammy chicken burger", 
    "done": true, 
    "id": 2, 
    "title": "chicken burger"
  }
}


```

```bash
# POST method 
$ curl -i -H "Content-Type: application/json" -X POST -d '{"title":"juice"}' http://0.0.0.0:5000/product/api/v1.0/products
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 378
Server: Werkzeug/0.15.4 Python/3.6.4
Date: Wed, 19 Jun 2019 10:27:38 GMT

{
  "product": [
    {
      "description": "this is an apple pie", 
      "id": 1, 
      "sold": false, 
      "title": "apple pie"
    }, 
    {
      "description": "a yammy chicken burger", 
      "done": true, 
      "id": 2, 
      "title": "chicken burger"
    }, 
    {
      "description": "", 
      "id": 3, 
      "sold": false, 
      "title": "juice"
    }
  ]
}

```

```bash
# UPDATE method 
# (update the "sold" status of product which with id =2 )
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"title": "THIS IS CAKE","description":"cake tasted good"}' http://0.0.0.0:5000/product/api/v1.0/products/2

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 133
Server: Werkzeug/0.15.4 Python/3.6.4
Date: Thu, 20 Jun 2019 08:36:44 GMT

{
  "product": {
    "description": "a yammy chicken burger", 
    "id": 2, 
    "sold": false, 
    "title": "chicken burger"
  }
}

``` 

```bash
# DELETE method 
# (delete product with id = 1 )
$ curl -i -H "Content-Type: application/json" -X DELETE  http://0.0.0.0:5000/product/api/v1.0/products/1
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 21
Server: Werkzeug/0.15.4 Python/3.6.4
Date: Thu, 20 Jun 2019 08:42:02 GMT

{
  "result": true
}

# (delete product with id = 2)
$ curl -i -H "Content-Type: application/json" -X DELETE  http://0.0.0.0:5000/product/api/v1.0/products/2
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 21
Server: Werkzeug/0.15.4 Python/3.6.4
Date: Thu, 20 Jun 2019 08:42:22 GMT

{
  "result": true
}

# show rest of the products 
$ curl -i http://0.0.0.0:5000/product/api/v1.0/products
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 20
Server: Werkzeug/0.15.4 Python/3.6.4
Date: Thu, 20 Jun 2019 08:42:37 GMT

{
  "product": []
}

``` 

## Ref 
- Flask RESTful API via SQLite 
	- https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-2-724ebf04d12
	- https://medium.com/pyladies-taiwan/%E5%A6%82%E4%BD%95%E5%9C%A8-flask-%E4%BD%BF%E7%94%A8-sqlite-%E8%B3%87%E6%96%99%E5%BA%AB-c26f300f1d87
- SQLite basics
	- https://www.tutorialspoint.com/flask/flask_sqlite.htm