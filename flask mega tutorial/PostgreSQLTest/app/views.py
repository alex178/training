from app import app
from app.LoginForm import LoginForm
from flask import render_template, redirect


@app.route("/index")
def index():
    return render_template("base.html", title="in base")


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print str(form.validate_on_submit())
        return redirect('/index')
    return render_template("login.html", title="einloggen", form=form)
