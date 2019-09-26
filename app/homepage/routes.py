from flask import Blueprint
from flask import render_template, request, Blueprint

homepage = Blueprint('homepage', __name__)

@homepage.route("/")
@homepage.route("/home")
def home():
	return render_template('homepage.html')


