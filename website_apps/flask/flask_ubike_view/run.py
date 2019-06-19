from flask import Flask, render_template, redirect, url_for, request
import csv
from controller import  ubike

app = Flask(__name__)



@app.route('/')
def test():
    stop_list = ubike()
    #print (stop_list)
    return render_template('basic.html',stop_list=stop_list) 





if __name__ == '__main__':
   app.run(debug = True)
