## Intro : RESTful API 
|  HTTP METHOD | ACTION | Example |
| --- | -------- | ---- | 
|Get| Obtain information about a resource |http://example.com/api/orders (retrieve order list) | 
|Post| Create a new resource | http://example.com/api/orders (create a new order, from data provided with the request)| 
|Put| Update a resource | http://example.com/api/orders/123 (update order #123, from data provided with the request) | 
|Delete| Delete a resource | http://example.com/api/orders/123 (delete order #123) | 

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
## Ref 
- https://blog.taiker.space/python-shi-yong-python-he-flask-she-ji-restful-api/
- https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask