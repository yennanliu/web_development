import pymysql
from pymysql import * 
from sqlalchemy import create_engine
import datetime as dt   
import time
import pandas as pd, numpy as np
import pprint
import matplotlib.pyplot as plt
import seaborn as sns
import json 

def insert_data_df_local_mysql():
	try:
		# db = dbname, table = offer 
		engine = create_engine('mysql+pymysql://root@localhost/local_dev')
		df=pd.read_csv('/Users/yennanliu/Desktop/movie_metadata.csv')
		df.to_sql('movie_metadata', engine, if_exists = 'append')
		print ('insert df OK')
	except:
		print ('insert df failed')
        

def sqlalchemy_connect():
	try:
		engine = create_engine('mysql+pymysql://root@localhost/local_dev')
		print ('connect success')
		query="SELECT * FROM movie_metadata limit 10"
		df = pd.read_sql_query(query, engine)
		df.head()
		return df 
	except:
		print ('MySQL connect failed')
        
def grab_data(query):
	try:
		engine = create_engine('mysql+pymysql://root@localhost/local_dev')
		print ('connect success')
		print (query)
		df = pd.read_sql_query(query, engine)
		#print (df.head())
		return df 
	except:
		print ('MySQL connect failed')






def test_data():
	df = grab_data("select * from movie_metadata ")
	df=df.fillna(0)
	d={}
	xx = df[['budget','imdb_score']].head().reset_index()
	d[0] = [[x, y] for x, y in json.loads(df[['budget','imdb_score']].head().to_json(orient='values'))]
	d[1] = [[x, y] for x, y in json.loads(df[['budget','duration']].head().to_json(orient='values'))]
	return d


def test_data2():
	query = """
	select movie_title, 
	count(*) as count
	from movie_metadata 
	group by movie_title order by count(*) desc 
"""
	df = grab_data(query)
	df=df.fillna(0)
	d={}
	d[0] = [[x, y] for x, y in json.loads(df[['movie_title','count']].head(10).to_json(orient='values'))]
	return d


def year_data():
	df = grab_data("select * from movie_metadata ")
	df_ =df.groupby('title_year').agg({'num_critic_for_reviews':np.sum, 'num_user_for_reviews': np.sum}).reset_index()
	df=pd.DataFrame(df.groupby('title_year').count()['index'].reset_index())
	df.columns = ['title_year','count']
	df.title_year = df.title_year.astype(np.int64)
	df_final = df_.merge(df)
	df_final.set_index('title_year')
	d={}
	d[0] = [[x, y] for x, y in json.loads(df_final[['title_year','count']].to_json(orient='values'))]
	d[1] = [[x, y] for x, y in json.loads(df_final[['title_year','num_critic_for_reviews']].to_json(orient='values'))]
	d[2] = [[x, y] for x, y in json.loads(df_final[['title_year','num_user_for_reviews']].to_json(orient='values'))]
	
	return d


def get_all():
	df = grab_data("select * from movie_metadata ")
	df=df.fillna(0)
	
	return df


def movie_data():
	df = grab_data("select * from movie_metadata ")
	df= df[['movie_title','budget']].sort('budget').fillna(0)
	d={}
	d = [[x, y] for x, y in json.loads(df[['movie_title','budget']].to_json(orient='values'))]
	return d


def heat_map():
	df = grab_data("select * from movie_metadata ")
	df['diff_gross'] = df['gross'] - df['budget']
	df_copy = df.copy().dropna()
	director_budge = df_copy.groupby(df_copy['director_name'])['diff_gross'].sum()
	direcotr_budge_indx = director_budge.sort_values(ascending=False)[:20].index
	director_budge = df_copy.groupby(df_copy['director_name'])['diff_gross'].sum()
	direcotr_budge_indx = director_budge.sort_values(ascending=False)[:20].index
	director_budge_pivot = pd.pivot_table(data = df_copy[df_copy['director_name'].isin(direcotr_budge_indx)],
                                      index=['title_year'],
                                      columns=['director_name'],
                                      values=['diff_gross'],
                                      aggfunc='sum')

	director_budge_pivot_final = director_budge_pivot.reset_index()['diff_gross']
	x_categories = list(director_budge_pivot_final.columns)
	y_categories = list(director_budge_pivot_final.index.values) 
	d={}
	d = [[x, y] for x, y in json.loads(director_budge_pivot_final[['Andrew Adamson','Chris Columbus']].to_json(orient='values'))]
	return d, x_categories, y_categories








