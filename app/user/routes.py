from flask import render_template, request, Blueprint

user = Blueprint('User', __name__)

@user.route("/login")
def login():
    return render_template('login.html')