import pandas as pd , numpy as np 
from flask import Flask, redirect, url_for, request,render_template,request,\
                  session,escape ,session




app = Flask(__name__)


@app.route('/')
def test1():
   return render_template('index.html')


@app.route('/dev1')
def dev1():
   return render_template('dev1.html')




if __name__ == '__main__':
   app.run(debug = True)
