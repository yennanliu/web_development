refer from  :  http://www.tutorialspoint.com/flask/flask_sqlite.htm

step 1 : create the Sqlite DB
```
>>>import sqlite3 
>>>conn = sqlite3.connect('database.db')
>>>print "Opened database successfully";

>>>conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
>>>print "Table created successfully";
>>>conn.close()
```

step 2 : run 

```
$cd flask_test_1
$python run.py
```
