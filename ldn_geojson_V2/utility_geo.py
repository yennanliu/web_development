# python 3 



import pandas as pd 
import json
from shapely.geometry import shape, Point



# ---------------------------------
# help function

def combine_lng_lat(lng,lat):
    #return 'ok'
    return str([lng,lat])
    

def fetch_hz_name(geojson,lng_lat):
    """
    --- argument  ---
    
    geojson : a json file with geojson form  (e.g. : test.geo.json)
    x       : a set of geo-coordinates [lng, lat]
    
    --- argument  ---
    """
    # open hz geojson file and retrun as dict (python json object)
    with open(geojson) as f:
        js = json.load(f)
    # get point lon & lat 
    point = Point(lng_lat[0], lng_lat[1])
    # loop over all hz in the dict
    for feature in js['features']:
        polygon = shape(feature['geometry'])
        if polygon.contains(point):
            print ('Found containing polygon:', feature['properties'])
        else:
            print ('none')

# ---------------------------------






if __name__ == '__main__':
	df = pd.read_csv('sample.csv')
	df['lng_lat_']=df.apply(lambda row : pd.Series(combine_lng_lat(row['search_lng'],row['search_lat']))  ,axis=1)
	df['hz'] = df.apply(lambda x : fetch_hz_name(geojson, lng_lat_))







