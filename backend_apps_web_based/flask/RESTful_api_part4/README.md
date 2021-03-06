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
### DB init 

# step 1) init db 
$ python config.py db init

# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/flask_sqlalchemy/__init__.py:800: UserWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True to suppress this warning.
#   warnings.warn('SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True to suppress this warning.')
#   Creating directory /Users/yennanliu/web_development/backend_apps_web_based
#   /flask/RESTful_api_part4/migrations ... done
#   Creating directory /Users/yennanliu/web_development/backend_apps_web_based
#   /flask/RESTful_api_part4/migrations/versions ... done
#   Generating /Users/yennanliu/web_development/backend_apps_web_based/flask/R
#   ESTful_api_part4/migrations/script.py.mako ... done
#   Generating /Users/yennanliu/web_development/backend_apps_web_based/flask/R
#   ESTful_api_part4/migrations/env.py ... done
#   Generating /Users/yennanliu/web_development/backend_apps_web_based/flask/R
#   ESTful_api_part4/migrations/README ... done
#   Generating /Users/yennanliu/web_development/backend_apps_web_based/flask/R
#   ESTful_api_part4/migrations/alembic.ini ... done
#   Please edit configuration/connection/logging settings in '/Users/yennanliu
#   /web_development/backend_apps_web_based/flask/RESTful_api_part4/migrations
#   /alembic.ini' before proceeding.

# step 2) db migrate 
$ python config.py db migrate

# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/flask_sqlalchemy/__init__.py:800: UserWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True to suppress this warning.
#   warnings.warn('SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True to suppress this warning.')
# INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
# INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
# INFO  [alembic.autogenerate.compare] Detected added table 'products'
#   Generating /Users/yennanliu/web_development/backend_apps_web_based/flask/R
#   ESTful_api_part4/migrations/versions/89e52c547802_.py ... done

# step 3) db upgrade 
$ python config.py db upgrade

# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/flask_sqlalchemy/__init__.py:800: UserWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True to suppress this warning.
#   warnings.warn('SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True to suppress this warning.')
# INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
# INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
# INFO  [alembic.runtime.migration] Running upgrade  -> 89e52c547802, empty message

# step 4) insert data into db 
$ python db.py 

# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/flask_sqlalchemy/__init__.py:800: UserWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True to suppress this warning.
#   warnings.warn('SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True to suppress this warning.')
# insert data to DB ok
# insert data to DB ok
# insert data to DB ok

```
```bash
### code test
$ pytest test.py

# =============================== test session starts ================================
# platform darwin -- Python 3.5.4, pytest-5.0.1, py-1.8.0, pluggy-0.12.0
# rootdir: /Users/yennanliu/web_development/backend_apps_web_based/flask/RESTful_api_part4
# plugins: celery-4.2.1
# collected 2 items                                                                  

# test.py ..                                                                   [100%]

# ================================= warnings summary =================================
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/operations/base.py:94
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/operations/base.py:94
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/operations/base.py:94
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/operations/base.py:94
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/operations/base.py:94
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/operations/base.py:94
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/operations/base.py:94
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/operations/base.py:94
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/operations/base.py:94
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/operations/base.py:94
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/operations/base.py:94
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/operations/base.py:94
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/operations/base.py:94
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/operations/base.py:94
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/operations/base.py:94
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/operations/base.py:94
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/operations/base.py:94
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/operations/base.py:94
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/operations/base.py:94
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/operations/base.py:94
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/operations/base.py:94
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/operations/base.py:94
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/operations/base.py:94
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/operations/base.py:94
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/operations/base.py:94
#   /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/operations/base.py:94: DeprecationWarning: inspect.getargspec() is deprecated, use inspect.signature() instead
#     spec = inspect.getargspec(fn)

# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76
#   /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/alembic/util/langhelpers.py:76: DeprecationWarning: inspect.getargspec() is deprecated, use inspect.signature() instead
#     spec = inspect.getargspec(fn)

# /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/flask_sqlalchemy/__init__.py:800
#   /Users/yennanliu/anaconda3/envs/ds_dash/lib/python3.5/site-packages/flask_sqlalchemy/__init__.py:800: UserWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True to suppress this warning.
#     warnings.warn('SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True to suppress this warning.')

# -- Docs: https://docs.pytest.org/en/latest/warnings.html
# ====================== 2 passed, 69 warnings in 0.84 seconds =======================

```


## Ref 
- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
- https://github.com/twtrubiks/Flask-Migrate-Tutorial
- https://stackoverflow.com/questions/17791571/testing-flask-sql-alchemy
- https://spotofdata.com/flask-testing/

