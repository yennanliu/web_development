from flask import Flask, render_template, redirect, url_for, request
import csv
from controller import taxi

app = Flask(__name__)



@app.route('/')
def test():
    stop_list = taxi()
    print (stop_list)
    return render_template('basic.html',stop_list=stop_list) 



@app.route('/test1')
def test1():
   
    return render_template('test1.html') 




@app.route('/test2')
def test2():
    stop_list = taxi()
    print ('==========')
    return render_template('test2.html',stop_list=stop_list) 




if __name__ == '__main__':
   app.run(debug = True)
