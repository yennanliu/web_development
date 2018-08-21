# python 3 


import psycopg2
from sqlalchemy import create_engine
from pytz import timezone
import datetime
import os
import pandas as pd


def get_toy_data(input):
	#print (' input : ', input)
	#print (' data : ', 123)
	data = pd.DataFrame({'name':[100,120,150] ,'url':[100,120,300] })
	print ('data : ' , data )
	return data 


def get_DB_data(sql, db_url):
    try:
        engine = create_engine(db_url)
        print (sql)
        df = pd.read_sql(sql=sql, con= engine)
        print (df.head())
        return df 
        print("extract data ok")
    except Exception as e:
        print (e)
        print ('fail to get data from db')







