

# OP 
from flask import Flask, render_template, session, redirect, url_for, flash,request
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy
import pandas as pd
import os

# UDF 
from controller import *


# config 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

try:
	db_url = os.environ['db_url']
	print ('db_url : ' , db_url)
except:
	print ('no db_url offer')



# flask app 


@app.route('/')
def hello():
    #return "hello world" 
    return render_template('base.html')


# ---------- access request tool  ----------
@app.route('/access_request/', methods=['GET', 'POST'])
def access_request_main():
    data = pd.DataFrame({'index': [], 'name': [], 'url':[]})
    return render_template('report.html',data=data)


@app.route('/access_request/<member_id>', methods=['GET', 'POST'])
def access_request(member_id):
    #data = get_toy_data(q_)
    data = get_DB_data(member_id, db_url)
    print (data)
    return render_template('report.html',data=data)




# ---------- report tool  ----------
@app.route('/tool_report/', methods=['GET', 'POST'])
def report_main():
    data = pd.DataFrame({'index': [], 'name': [], 'url':[]})
    return render_template('report.html',data=data)


@app.route('/tool_report/<q_>', methods=['GET', 'POST'])
def report(q_):
    #data = get_toy_data(q_)
    data = get_DB_data(q_, db_url)
    print (data)
    return render_template('report.html',data=data)











# run flask server 
if __name__ == '__main__':
   app.run(debug = True)










