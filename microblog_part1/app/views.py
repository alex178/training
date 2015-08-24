# coding: utf8
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
	nameList = ["Lisa","Karl","Katja","Natalie","Stefan"]
	user = {'nickname': 'Alex'}
	return render_template('index.html',title='Home',user=user, this='this', iss='is', cool='cooool', nameList=nameList) #mehrere variablen können hier übergeben werden an das template
