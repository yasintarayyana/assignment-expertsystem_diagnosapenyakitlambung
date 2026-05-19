from flask import (
    Flask,
    redirect,
    url_for
)

from config import Config
from extensions import (
    db,
    login_manager
)


def create_app():

    app = Flask(__name__)

    app.config.from_object(
        Config
    )

    db.init_app(app)

    login_manager.init_app(app)

    login_manager.login_view = (
        'auth.login'
    )

    from models.user_model import User
    from models.diagnosis_model import DiagnosisHistory

    @login_manager.user_loader
    def load_user(user_id):

        return User.query.get(
            int(user_id)
        )

    from routes.auth_routes import auth
    from routes.dashboard_routes import dashboard
    from routes.diagnosa_routes import diagnosa

    app.register_blueprint(auth)
    app.register_blueprint(dashboard)
    app.register_blueprint(diagnosa)

    # HOME REDIRECT
    @app.route('/')
    def home():

        return redirect(
            url_for(
                'auth.login'
            )
        )

    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)