from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from . import login_manager


class User(UserMixin):
    username = ''
    password_hash = ''
    email = ''

    @property
    def password(self):
        raise AttributeError('password is not a readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
