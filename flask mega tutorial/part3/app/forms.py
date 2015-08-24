
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Length

class LoginForm(Form):
	# StringField mit validator DataRequired ausgestattet
	#DataRequired prueft, ob das Textfeld leer ist
	#kann in HTML eingebettet werden
	#zusaetzlich wird Laenge auch ueberprueft zwischen 2 und 5
    openid = StringField('openid', validators=[DataRequired(message="Bitte gib eine OpenID ein!"),Length(min=2,max=5, message="Stringlaenge muss zwischen 2 und 5 sein!")])

    #Checkbox
    #kann in HTML eingebettet werden
    remember_me = BooleanField('remember_me', default=False)