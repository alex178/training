from app import application

#Ausgabe unter "/" oder "/index"
@application.route('/')
@application.route('/index')
def index():
	return 'Hello World!'
