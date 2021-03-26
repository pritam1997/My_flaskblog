import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import
from flask_login import LoginManager
from flask_mail import Mail
#
from flaskblog.config import Config

# this is put in to create_config function
# app = Flask(__name__)
# app.config.from_object(Config)


# app.config['SECRET_KEY'] = '27c1ef3f888be823ac7ac19bc9c3b41a'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# from here below 4 line remove the app and from Mail() also
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
                            # login method from routes module
login_manager.login_message_category = 'info'
                                        # bootstrap class
# app.config['MAIL_SERVER'] = 'smtp.ethereal.email'                                     
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USER_TLS'] = True
# app.config['MAIL_USERNAME'] = os.environ.get('magdalen87@ethereal.email')
# app.config['MAIL_PASSWORD'] = os.environ.get('wp4pxvjTXjAJVVPg9Q')

mail = Mail()

# from flaskblog import routes



# creation of application inside this function
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)    
    app.register_blueprint(errors)    
    

    return app

