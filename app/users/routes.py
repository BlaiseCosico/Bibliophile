from flask import render_template, request, Blueprint, flash, redirect, url_for
from app.users.forms import RegistrationForm

users = Blueprint('users', __name__)

@users.route("/login")
def login():
    return render_template('login.html')    

@users.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)  