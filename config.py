import os

class Config:

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "sistem-pakar-lambung"
    )

    SQLALCHEMY_DATABASE_URI = "sqlite:///user.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.getenv(
        "MAIL_SERVER",
        "smtp.gmail.com"
    )

    MAIL_PORT = int(
        os.getenv(
            "MAIL_PORT",
            587
        )
    )

    MAIL_USE_TLS = (
        os.getenv(
            "MAIL_USE_TLS",
            "true"
        ).lower() == "true"
    )

    MAIL_USE_SSL = (
        os.getenv(
            "MAIL_USE_SSL",
            "false"
        ).lower() == "true"
    )

    MAIL_USERNAME = os.getenv(
        "MAIL_USERNAME",
        "projectsistempakarlambung@gmail.com"
    )

    MAIL_PASSWORD = os.getenv(
        "MAIL_PASSWORD",
        ""
    )

    MAIL_DEFAULT_SENDER = os.getenv(
        "MAIL_DEFAULT_SENDER",
        "projectsistempakarlambung@gmail.com"
    )
    
    MAIL_TIMEOUT = 10