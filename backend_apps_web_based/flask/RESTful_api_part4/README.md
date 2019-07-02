## INTRO : RESTful API V4
  - RESTful API work with DB migration and test 

## INTRO : RESTful API 
|  HTTP method | Action | Example |
| --- | -------- | ---- | 
|Get| Obtain information about a resource | http://0.0.0.0:5000/product/api/v1.0/products <br>(retrieve product list) | 
|Post| Create a new resource | http://0.0.0.0:5000/product/api/v1.0/products <br> (create a new order, from data provided with the request)| 
|Put| Update a resource | http://0.0.0.0:5000/product/api/v1.0/products/2 <br> (update product with id = 2, from data provided with the request) | 
|Delete| Delete a resource | http://0.0.0.0:5000/product/api/v1.0/products/2 <br> (delete prodcut with id = 2 ) | 

## Quick start 
```bash
# step 1) init db 
python config.py db init

# step 2) db migrate 
python config.py db migrate

# step 3) db upgrade 
python config.py db upgrade


```
## Ref 
- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
- https://github.com/twtrubiks/Flask-Migrate-Tutorial
