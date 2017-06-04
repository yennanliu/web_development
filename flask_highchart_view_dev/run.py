import sqlite3 as sql
import pandas as pd , numpy as np 
from flask import Flask, redirect, url_for, request,render_template,request,\
                  session,escape ,session,flash
from flask_sqlalchemy import SQLAlchemy
from controllers import  get_fred_gep, stock


app = Flask(__name__)




@app.route('/')
def hello():
   return ('hello world')



@app.route('/try4')
def  fun_4():
   return render_template('try4.html')  


@app.route('/try5')
def  fun_5():
   return render_template('try5.html')  


@app.route('/try2')
def fun_2():
   
   data_stock_ = stock()
   print (data_stock_)
   return render_template('try2.html', data_stock_ = data_stock_ ) 

@app.route('/try3')
def fun_3():
   
   data_ = get_fred_gep()
   print (data_)
   return render_template('try3.html', data_ = data_ ) 




if __name__ == '__main__':
   app.run(debug = True)
