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

# test via pytest 
$ pytest

# ============================= test session starts ==============================
# platform darwin -- Python 3.6.4, pytest-3.3.1, py-1.5.2, pluggy-0.6.0
# rootdir: /Users/jerryliu/web_development/backend_apps_web_based/flask/RESTful_api_part3, inifile:
# collected 1 item                                                               

# test.py .                                                            [100%]

# =========================== 1 passed in 0.57 seconds ===========================

# test via pytest 
$ python  test.py 

# /Users/jerryliu/anaconda3/envs/yen_dev/lib/python3.6/site-packages/flask_sqlalchemy/__init__.py:814: UserWarning: Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. Defaulting SQLALCHEMY_DATABASE_URI to "sqlite:///:memory:".
#   'Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. '
# /Users/jerryliu/anaconda3/envs/yen_dev/lib/python3.6/site-packages/flask_sqlalchemy/__init__.py:835: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
#   'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
# <Response [200]>
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.014s

# OK

# coverage report
$ coverage report -m test.py

# Name          Stmts   Miss  Cover   Missing
# -------------------------------------------
# test.py      31      0   100%

```
## Ref 
- python test 
- Unit test 
	- https://www.patricksoftwareblog.com/unit-testing-a-flask-application/
	- https://stackoverflow.com/questions/31716604/how-to-setup-testing-script-in-flask-with-sqlite