import sqlite3 as sql
import pandas as pd , numpy as np 
from flask import Flask, redirect, url_for, request,render_template,request,\
                  session,escape ,session,flash

from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask_sqlalchemy import SQLAlchemy
from controller import  *
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField





app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(Form):
    query = StringField('please enter your query')




@app.route('/')
def hello():
   #return ('hello world')
   return render_template('base.html') 




@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/all_data')
# ref https://sarahleejane.github.io/learning/python/2015/08/09/simple-tables-in-webapps-using-flask-and-pandas-with-python.html
def all_():
   data = get_all()
   return render_template('view.html',tables=[data.to_html()],titles = ['Imdb 5000 movie data set']) 


@app.route('/year_data')
def get_year_data():
   data = year_data()
   print (data)
   return render_template('year_plot.html',data=data) 


@app.route('/movie_data')
def get_movie_data():
   data = year_data()
   print (data[0])
   return render_template('movie_plot.html',data=data) 



@app.route('/heat_map')
def heatmap():
   #data,x_categories,y_categories = heat_map()
   #print (data[0])
   return render_template('heat_map.html') 


@app.route('/notebook')

# adding the ipython's html inside a {% raw %} {% endraw %} block as in the documentation
# http://stackoverflow.com/questions/33662916/problems-with-flask-ipython-jinja2-integration
def get_notebook():
   return render_template('imdb_5000_movie_analysis.slides.html') 



@app.route('/sql/', methods=['GET', 'POST'])
#@app.route('/sql/query=<query>', methods=['GET', 'POST'])
def get_query_data_base():
   form =NameForm()

   return render_template('sql_view.html') 


@app.route('/sql/query=<query>', methods=['GET', 'POST'])
# ref http://flask.pocoo.org/docs/0.11/patterns/wtforms/
def get_query_data(query):
   form =NameForm()
   query2 = request.form.get('query')
   #print (request.form['query'])

   print (query2)
   print ('===========')
   print (query)
   data = grab_data(query)
   print (data)
   #return "Query ok !"
   return render_template('sql_view.html',tables=[data.to_html()],titles = ['Your query result']) 
   

   

@app.route('/try2')
def test2():
   data = test_data()
   print (data)
   return render_template('try2.html',data=data) 


@app.route('/try3')
def test3():
   data = test_data2()
   print (data)
   return render_template('try3.html',data=data) 


   



if __name__ == '__main__':
   app.run(debug = True)