from flask import render_template, request, Blueprint
from app.models import User

homepage = Blueprint('homepage', __name__)

@homepage.route("/") 
@homepage.route("/home")
def home():
	user = User.query.first()
	return render_template('homepage.html', user=user)