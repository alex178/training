from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# wird global bereitgestellt, sobald das package app geladen wird
application = Flask(__name__)

# config.py wird hier gelesen und genutzt
application.config.from_object('config')

db = SQLAlchemy(application)

from app import views, models
