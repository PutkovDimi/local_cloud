import os

SECRET_KEY = 'hard to guess string'
class Config:
    SECRET_KEY = 'hard to guess string'
    STORAGE_MAIL_SUBJECT_PREFIX = '[Storage]'
    STORAGE_MAIL_SENDER = 'Storage Admin <putkovdimi@gmail.com>'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'username'  # this field and field below are required for correct sending messages to email
    MAIL_PASSWORD = 'password'


class TestingConfig(Config):
    TESTING = True
    # place for db


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}