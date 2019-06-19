import sqlite3 as sql
import pandas as pd , numpy as np 
from flask import Flask, redirect, url_for, request,render_template,request,\
                  session,escape ,session


app = Flask(__name__)
app.secret_key = 'any random string'



conn = sql.connect('database.db')
print ("Opened database successfully");



@app.route('/test1')
def test01():
   user = { 'nickname': 'Miguel' }
   return render_template('index.html', user=user)
   return render_template('base.html')
   return " heello world !!! "



@app.route('/')
def test():
   return "Enter new data<br><a href = '/enternew'></b>" + \
      "click here to enter</b></a> <br>Check the record<br><a href = '/list'></b>" + \
      "click here to check</b></a>"


@app.route('/enternew')
def new_student():
   return render_template('student.html')



@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         pin = request.form['pin']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()



@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall(); 
   return render_template("list.html",rows = rows)




@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template('result.html',result = result)





if __name__ == '__main__':
   app.run(debug = True)
