import os

class Config:

    SECRET_KEY = (
        "sistem-pakar-lambung"
    )

    SQLALCHEMY_DATABASE_URI = (
        'sqlite:///user.db'
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False


    # EMAIL CONFIG

    MAIL_SERVER = (
        'smtp.gmail.com'
    )

    MAIL_PORT = 587

    MAIL_USE_TLS = True

    MAIL_USERNAME = (
        'projectsistempakarlambung@gmail.com'
    )

    MAIL_PASSWORD = (
        'xttrgwygkqgwhgfq'
    )

    MAIL_DEFAULT_SENDER = (
        'projectsistempakarlambung@gmail.com'
    )