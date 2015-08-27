from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Length


class LoginForm(Form):
    openID = StringField("openID", validators=[DataRequired(message="openID-Feld ist leer!"),
                                               Length(min=2, max=5, message="zwischen 2 und 5 bitte!")])
    rememberMe = BooleanField("remember", default=None)
