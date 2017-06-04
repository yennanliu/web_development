# this is controllers, define all functions that this flask site needs



import quandl
import pandas as pd, numpy as np
import requests
from bs4 import BeautifulSoup
import lxml
import urllib, json
import urllib.request
from optparse import OptionParser
import sys


quandl.ApiConfig.api_key = "8xawN97zMz2wU2xEuUen"


def get_data():
	data_fred_gep = quandl.get("FRED/GDP")
	data = {}
	pd.DataFrame.to_json(data_fred_gep.reset_index())
	return json.loads(pd.DataFrame.to_json(data_fred_gep.reset_index()))



def get_fred_gep():
	data_fred_gep = quandl.get("FRED/GDP")
	data = {}
	data=[[x, y] for x, y in json.loads(pd.DataFrame(data_fred_gep.reset_index()).to_json(orient='values'))]
	return data

def stock():
	data_stock = quandl.get(["WIKI/IBM","WIKI/AAPL"])[['WIKI/IBM - Volume','WIKI/AAPL - Adj. Volume']]
	data_stock_ = {}
	data_stock_[0] =  [[x, y] for x, y in json.loads(pd.DataFrame(data_stock['WIKI/IBM - Volume'].reset_index()).to_json(orient='values'))]
	data_stock_[1] =  [[x, y] for x, y in json.loads(pd.DataFrame(data_stock['WIKI/AAPL - Adj. Volume'].reset_index()).to_json(orient='values'))]
	return data_stock_








