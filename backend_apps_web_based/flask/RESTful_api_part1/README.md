## Intro : RESTful API 
|  HTTP method | Action | Example |
| --- | -------- | ---- | 
|Get| Obtain information about a resource | http://0.0.0.0:5000/product/api/v1.0/products <br>(retrieve product list) | 
|Post| Create a new resource | http://0.0.0.0:5000/product/api/v1.0/products 
<br> (create a new order, from data provided with the request)| 
|Put| Update a resource | http://0.0.0.0:5000/product/api/v1.0/products/2 
<br> (update product with id = 2, from data provided with the request) | 
|Delete| Delete a resource | http://0.0.0.0:5000/product/api/v1.0/products/2 
<br> (delete prodcut with id = 2 ) | 

## Quick start 
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
$ curl -i -H "Content-Type: application/json" -X PUT -d '{"sold":false}' http://0.0.0.0:5000/product/api/v1.0/products/2

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
- https://blog.taiker.space/python-shi-yong-python-he-flask-she-ji-restful-api/
- https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask