# -*- coding: utf-8 -*-
from flask import render_template
from app import application

#Ausgabe unter "/" oder "/index"
@application.route('/')
@application.route('/index')
def index():
	user = {'nickname': 'Flask-programmer'}
	posts = [  
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Germany!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'Flask micro framework!' 
        },
        { 
            'author': {'nickname': 'Karl'}, 
            'body': 'Hello Osnabrueck!' 
        }
    ]
	return render_template('index.html',title='Start',user=user,posts=posts)
