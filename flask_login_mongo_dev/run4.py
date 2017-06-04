
from flask import Flask, render_template, session, redirect, url_for, flash,request,json
from flask.ext.bootstrap import Bootstrap
from flask import jsonify,flash
from flask import request
from flask_script import * 
from flask.ext.moment import Moment

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
import datetime




app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config['SECRET_KEY'] = 'hard to guess string'


class NameForm(Form):
	name = StringField('What is your name?', validators=[Required()])
	submit = SubmitField('Submit')
	



@app.route('/<name>')
def hello(name):
	if name =='jj':
		flash('Looks like you have came!')
	else:
    	flash('Looks like you have came!')
    return "hello world"
    #return render_template('form.html')


@app.route('/form', methods=['GET', 'POST'])
def index():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
	return render_template('form.html', form=form, name=name)





@app.route('/user/<name>')
def user(name):
    return render_template('user.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)





