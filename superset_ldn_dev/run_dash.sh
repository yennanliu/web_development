#!/bin/sh


# 1) get visualization API key 

# plz get the mapbox API key  via https://www.mapbox.com
# add the mapbox API key to config.py or export it as env variable
# https://github.com/apache/incubator-superset/issues/952
export MAPBOX_API_KEY=<your_mapbox_api_key>


# 2) install/run the dash 

# run the dash locally 
# https://superset.incubator.apache.org/installation.html#making-your-own-build

# Install superset
pip install superset

# Create an admin user (you will be prompted to set username, first and last name before setting a password)
fabmanager create-admin --app superset

# plz notice the package dependence :  https://github.com/yennanliu/incubator-superset/blob/master/requirements.txt
# e.g. sqlalchemy-utils==0.32.21 
# Initialize the database
superset db upgrade

# Load some data to play with
superset load_examples

# Create default roles and permissions
superset init

# To start a development web server on port 8088, use -p to bind to another port
# then visit the dash on http://0.0.0.0:8088
superset runserver -d







