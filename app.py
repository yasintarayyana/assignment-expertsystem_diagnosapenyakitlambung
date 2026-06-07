from flask import Flask

from config import Config

from extensions import (
    db,
    mail
)

from routes.diagnosa_routes import (
    diagnosa
)

from routes.auth_routes import (
    auth
)

# ==========================
# IMPORT MODEL
# ==========================

from models.user_model import User
from models.diagnosis_history_model import (
    DiagnosisHistory
)


def create_app():

    app = Flask(__name__)

    app.config.from_object(
        Config
    )

    db.init_app(app)

    mail.init_app(app)

    app.register_blueprint(
        diagnosa
    )

    app.register_blueprint(
        auth
    )

    with app.app_context():

        db.create_all()

    return app


app = create_app()


if __name__ == "__main__":

    app.run(
        debug=True
    )