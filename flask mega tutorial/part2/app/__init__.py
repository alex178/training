from flask import Flask

#wird global bereitgestellt, sobald das package app geladen wird
application = Flask(__name__)

from app import views