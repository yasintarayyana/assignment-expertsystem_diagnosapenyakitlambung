from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

from models.user_model import User
from extensions import db


auth = Blueprint(
    'auth',
    __name__
)


# ======================
# REGISTER
# ======================
@auth.route('/register', methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:
        return redirect(
            url_for(
                'dashboard.dashboard_page'
            )
        )

    if request.method == 'POST':

        username = request.form.get(
            'username'
        )

        email = request.form.get(
            'email'
        )

        password = request.form.get(
            'password'
        )

        confirm_password = request.form.get(
            'confirm_password'
        )

        # validasi password
        if password != confirm_password:
            flash(
                'Password tidak sama!',
                'danger'
            )
            return redirect(
                url_for('auth.register')
            )

        # cek email
        existing_user = User.query.filter_by(
            email=email
        ).first()

        if existing_user:
            flash(
                'Email sudah digunakan!',
                'warning'
            )
            return redirect(
                url_for('auth.register')
            )

        # buat user baru
        new_user = User(
            username=username,
            email=email
        )

        new_user.set_password(
            password
        )

        db.session.add(
            new_user
        )

        db.session.commit()

        flash(
            'Registrasi berhasil!',
            'success'
        )

        return redirect(
            url_for('auth.login')
        )

    return render_template(
        'register.html'
    )


# ======================
# LOGIN
# ======================
@auth.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(
            url_for(
                'dashboard.dashboard_page'
            )
        )

    if request.method == 'POST':

        email = request.form.get(
            'email'
        )

        password = request.form.get(
            'password'
        )

        user = User.query.filter_by(
            email=email
        ).first()

        if user and user.check_password(
            password
        ):

            login_user(user)

            flash(
                'Login berhasil!',
                'success'
            )

            return redirect(
                url_for(
                    'dashboard.dashboard_page'
                )
            )

        flash(
            'Email atau password salah!',
            'danger'
        )

    return render_template(
        'login.html'
    )


# ======================
# LOGOUT
# ======================
@auth.route('/logout')
@login_required
def logout():

    logout_user()

    flash(
        'Logout berhasil',
        'info'
    )

    return redirect(
        url_for('auth.login')
    )