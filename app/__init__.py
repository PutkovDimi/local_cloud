from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_mail import Mail
from flask import Blueprint
from flask_login import LoginManager

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object('config')
    app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'mail address'  # to
    app.config['MAIL_PASSWORD'] = 'password'  # from's password
    app.config['STORAGE_MAIL_SUBJECT_PREFIX'] = '[Storage]'
    app.config['STORAGE_MAIL_SENDER'] = 'Storage Admin <putkovdimi@gmail.com>'  # from

    auth = Blueprint('auth', __name__)
    app.register_blueprint(auth, url_prefix='/auth')

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    app.register_blueprint(auth)
    return app, auth
