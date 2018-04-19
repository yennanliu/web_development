# python 3 

# ref 
# https://stackoverflow.com/questions/20776205/point-in-polygon-with-geojson-in-python

import pandas as pd 
import json
from shapely.geometry import shape, Point



# ---------------------------------
# help function

def combine_lng_lat(lng,lat):
    return str([lng,lat])
    

def fetch_hz_name_(geojson,lat,lon):
    """
    --- argument  ---
    
    geojson : a json file with geojson form  (e.g. : test.geo.json)
    x       : a set of geo-coordinates [lng, lat]
    
    --- argument  ---
    """
    # open hz geojson file and retrun as dict (python json object)
    with open('ldn_hz.geo.json') as f:
        js = json.load(f)
    # get point lon & lat 
    point = Point(float(lat), float(lon))
    print (point)
    # loop over all hz in the dict
    for feature in js['features']:
        polygon = shape(feature['geometry'])
        if polygon.contains(point):
            print ('Found containing polygon:', feature['properties'])
            return str(feature['properties']['Name'])
        else:
            print ('none')
            pass
        
        

# ---------------------------------






if __name__ == '__main__':
	df = pd.read_csv('sample.csv')
	df=df.head(50)
	#df['lng_lat_']=df.apply(lambda row : pd.Series(combine_lng_lat(row['search_lng'],row['search_lat']))  ,axis=1)
	geojson='sample.geo.json'
	df['hz'] = df.apply(lambda row : pd.Series(fetch_hz_name_(geojson,row['search_lng'],row['search_lat']))  ,axis=1)
	print (df.head(30))








