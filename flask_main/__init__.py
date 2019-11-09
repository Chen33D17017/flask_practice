from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_main.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
#pass the function name in routes.py into login_view
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info' 
#.config['MAIL_SERVER'] = 'smtp.gmail.com'

mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    #extension parts
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flask_main.users.routes import users
    from flask_main.posts.routes import posts
    from flask_main.main.routes import main
    from flask_main.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app

