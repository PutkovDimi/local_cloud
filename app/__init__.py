from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_mail import Mail
from flask import Blueprint
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
bootstrap = Bootstrap(app)
moment = Moment(app)
auth = Blueprint('auth', __name__)

mail = Mail(app)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.init_app(app)
