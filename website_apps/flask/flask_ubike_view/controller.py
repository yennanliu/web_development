import csv
import requests
from bs4 import BeautifulSoup
import lxml
import urllib, json
import pandas as pd, numpy as np



def ubike():
	url = "http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=ddb80380-f1b3-4f8e-8016-7ed9cba571d5"
	response = requests.get(url)
	txt = response.text
	data = json.loads(txt)

	geo=[[] for k in range(3)]
	for item in range(len(data['result']['results'])):
		geo[0].append(data['result']['results'][item]['sna'])
		geo[1].append(data['result']['results'][item]['lat'])
		geo[2].append(data['result']['results'][item]['lng'])


	location = pd.DataFrame(geo).T
	location.columns = ['name','lat', 'lon']
	location=location.reset_index()
	data = {}
	data[0]=json.loads(pd.DataFrame.to_json(location['name']))
	data[1]=json.loads(pd.DataFrame.to_json(location['lat']))
	data[2]=json.loads(pd.DataFrame.to_json(location['lon']))
	print (location)
	return data 


