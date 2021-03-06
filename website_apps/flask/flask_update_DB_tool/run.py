

# OP 
from flask import Flask, render_template, session, redirect, url_for, flash,request, Response,send_file
#from flask.ext.script import Manager
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required
import pandas as pd
import os
import subprocess
from subprocess import PIPE, run, Popen
import shlex

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
def home_():
	#return "hello world" 
	return render_template('home.html')




# ---------- access request tool  ----------
@app.route('/access_request/', methods=['GET', 'POST'])
def access_request_main():
	data = pd.DataFrame({'result': []})
	return render_template('access_request.html',data=data)


@app.route('/access_request/<member_id>', methods=['GET', 'POST'])
def access_request(member_id):
	print (' member_id : ', member_id )
	try:
		get_access_request_report(member_id, db_url)
		path = 'access_req_report_sample.xlsx'
		#flash('job run OK !')
		return send_file(path, as_attachment=True)
	except Exception as e:
		flash('job run FAILED ')
		return redirect(url_for('access_request_main'))
	#return redirect(url_for('access_request_main'))
	return render_template('access_request.html')




# ---------- deletion request tool  ----------
@app.route('/deletion_request/', methods=['GET', 'POST'])
def deletion_request_main():
	data = pd.DataFrame({'result': []})
	return render_template('deletion_request.html',data=data)


@app.route('/deletion_request/<member_id>', methods=['GET', 'POST'])
def deletion_request(member_id):
	print (' member_id : ', member_id )
	#subprocess.call(["bash deletion_request.sh ", member_id])
	try : 
		os.system("bash deletion_request.sh {}".format(member_id))
		#process = subprocess.call(shlex.split("bash deletion_request.sh {} ".format(member_id)))
		#py2output = subprocess.check_call(['deletion_request.sh {}'.format(member_id)], shell=True)
		#print ('py2output : ', py2output)
		return render_template('deletion_request.html')
	except Exception as e:
		flash('job run FAILED ')
		return redirect(url_for('deletion_request_main'))
	return render_template('deletion_request.html')





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





# ---------- dev   ----------

@app.route("/getPlotCSV")
def getPlotCSV():
    csv = '1,2,3\n4,5,6\n'
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=myplot.csv"})


@app.route('/dev/')
def dev_func():
	return render_template('404.html')



# ---------- run flask server  ----------
if __name__ == '__main__':
   app.run(host='0.0.0.0',port=5000, debug = True)










