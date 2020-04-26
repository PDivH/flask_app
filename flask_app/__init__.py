# pylint: disable=import-outside-toplevel
from os.path import abspath, dirname, join as joinpath
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
#from flask_app.config import Config

# Database
db = SQLAlchemy()
# bcrypt for hashing and verifying passwords
# bcrypt = Bcrypt()
# Login manager
login_manager = LoginManager()
login_manager.login_view = "user.login"
login_manager.login_message_category = "info"
# Mail
mail = Mail()


def create_app():
    app = Flask(__name__)
    # Set the app configuration
    if app.config["ENV"] == "production":
        app.config.from_object("config.ProductionConfig")
    else:
        app.config.from_object("config.DevelopmentConfig")
    # Set the extensions configurations
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    # Register blueprints
    from flask_app.users.routes import users
    from flask_app.posts.routes import posts
    from flask_app.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    return app
