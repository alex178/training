from flask import Flask

#wird global bereitgestellt, sobald das package app geladen wird
application = Flask(__name__)

#config.py wird hier gelesen und genutzt
application.config.from_object('config')


from app import views