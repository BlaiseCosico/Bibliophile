from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(Config)
 
    db.init_app(app)

    from app.homepage.routes import homepage
    from app.users.routes import users

    app.register_blueprint(homepage)
    app.register_blueprint(users)

    return app
