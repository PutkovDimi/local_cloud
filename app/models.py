from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.get_DB_object import find_user
from . import login_manager
import configparser
import os

class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id
        self.username = find_user(user_id=user_id)['login']
        self.password_hash = ''
        self.email = find_user(user_id=user_id)['email']

    @property
    def password(self):
        raise AttributeError('password is not a readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "%s/%s/%s" % (self.id, self.email, self.password)


@login_manager.user_loader
def load_user(user_id=None):
    with open(os.path.dirname(os.path.abspath(__file__))+'/id.txt', 'w') as con:
        con.write(str(user_id))
    if user_id:
        return User(str(user_id))
    # else:
    #    return User(user_id="5ad773cbfdef703d31f2bc30") # user_id by default
