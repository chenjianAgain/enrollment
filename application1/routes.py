from application1 import application
from flask import render_template

@application.route("/")
@application.route("/index")
@application.route("/home")
@application.route("/joseph")
def index():
    return render_template("index.html", login=False)

@application.route("/denglu")
def login():
    return render_template("login.html", login=False)

@application.route("/kecheng")
def courses():
    return render_template("courses.html", login=False)

@application.route("/zhuce")
def register():
    return render_template("register.html", login=False)