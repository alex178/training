# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect
from app import application
from .forms import LoginForm

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


@application.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    #liefert true, wenn Daten korrekt sind
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form, providers=application.config['OPENID_PROVIDERS'])