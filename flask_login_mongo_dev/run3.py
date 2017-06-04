#!/usr/bin/python
# -*- coding: utf-8 -*-

#ref  http://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection

#ref  https://flask-pymongo.readthedocs.io/en/latest/

from flask import Flask, render_template, session, redirect, url_for, flash,request,json
from flask.ext.bootstrap import Bootstrap
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient
import datetime as dt   
import time
import csv
import requests
import pandas as pd, numpy as np
from pymongo import InsertOne, DeleteOne, ReplaceOne
from datetime import datetime
from flask_script import * 

from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required



app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)


### 1 st mongo connection 
client = MongoClient('localhost', 27017)
db = client.restdb


### 2nd mongo connection 

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

mongo = PyMongo(app)

#mongo.db.restdb.insert_one({'username': 'david','password':'123'}).inserted_id





@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, current_time=datetime.utcnow())


@app.route('/user_/<name>')
def user_(name):
    return render_template('user_.html', name=name)


@app.route('/uploads/<path:filename>')
def get_upload(filename):
    return mongo.send_file(filename)


@app.route('/find')
def test():
    for k in mongo.db.restdb.find():
        print (k)
    if mongo.db.restdb.find({'username': "david"}):
        return ('we find david !!!')
    else:
        return ('not found')


@app.route('/write')
def test2():
    requests = [InsertOne({'y': 1}), DeleteOne({'x': 1}),ReplaceOne({'w': 1}, {'z': 1}, upsert=True)]
    db.restdb.bulk_write(requests)
    return ('done!')


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('success_login'))
    return render_template('login.html', error=error)


@app.route('/login', methods=['GET', 'POST'])
def login2():
    error = None
    if request.method == 'POST':
        name = db.user.find_one({"username" : "123"})['username']
        if request.form['username'] == name:
            print (name)
        
            return 'ok user found'
        else:
            print (name)
            print (name['username'])
            return 'user not found'
      
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        name = request.form['newuser']
        password = request.form['newpass']
        db.user.insert_one({'username': name,"password":password})
        #return 'ok new user added'
        return render_template('register.html')

    return render_template('register.html')

    




@app.route('/success_login')
def success_login():
    return render_template('welcome.html') 

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int('8080'), debug=True)


            