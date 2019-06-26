## INTRO : RESTful API V3
  - RESTful API work with test and Database (sqlite)

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
$ cd~ && cd web_development/backend_apps_web_based/flask/RESTful_api_part3
$ pip install -r requirements.txt &&  python create_db.py && python app.py 

# when the flask server run at local successfully, 
# open the other terminal run the folloeing commands 
```
```bash
$ cd~ && cd web_development/backend_apps_web_based/flask/RESTful_api_part3
$ pytest 
```
## Ref 
- python test 
- Unit test 