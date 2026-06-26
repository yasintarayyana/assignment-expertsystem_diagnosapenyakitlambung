from flask import Flask, session

from config import Config
from extensions import db, mail

from routes.diagnosa_routes import diagnosa
from routes.auth_routes import auth

from models.user_model import User
from models.diagnosis_history_model import DiagnosisHistory


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    mail.init_app(app)
    
    print("MAIL_SERVER:", app.config["MAIL_SERVER"])
    print("MAIL_PORT:", app.config["MAIL_PORT"])
    print("MAIL_USE_TLS:", app.config["MAIL_USE_TLS"])
    print("MAIL_USE_SSL:", app.config["MAIL_USE_SSL"])
    print("MAIL_USERNAME:", app.config["MAIL_USERNAME"])
    print("MAIL_TIMEOUT:", app.config.get("MAIL_TIMEOUT"))

    app.register_blueprint(diagnosa)
    app.register_blueprint(auth)

    # ==========================
    # CONTEXT PROCESSOR (FIXED)
    # ==========================
    @app.context_processor
    def inject_user():
        user_id = session.get("user_id")

        user = User.query.get(user_id) if user_id else None

        return dict(user=user)

    with app.app_context():
        db.create_all()

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)