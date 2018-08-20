

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


# flask app 


@app.route('/')
def hello():
    return "hello world" 


@app.route('/tool_report/', methods=['GET', 'POST'])
def keyword_main():
    data = pd.DataFrame({'index': [], 'name': [], 'url':[]})
    return render_template('report.html',data=data)


@app.route('/tool_report/<q_>', methods=['GET', 'POST'])
def keyword(q_):
    data = get_toy_data(q_)
    print (data)
    return render_template('report.html',data=data)





# run flask server 
if __name__ == '__main__':
   app.run(debug = True)
