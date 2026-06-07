from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)

from datetime import datetime
import random

from models.user_model import User
from extensions import db

from services.email_service import (
    send_otp_email
)

auth = Blueprint(
    "auth",
    __name__
)


# ======================
# REGISTER
# ======================

@auth.route(
    "/register",
    methods=["GET", "POST"]
)
def register():

    if request.method == "POST":

        nama = request.form.get(
            "nama"
        )

        tanggal_lahir = (
            request.form.get(
                "tanggal_lahir"
            )
        )

        jenis_kelamin = (
            request.form.get(
                "jenis_kelamin"
            )
        )

        riwayat_penyakit = (
            request.form.get(
                "riwayat_penyakit"
            )
        )

        email = request.form.get(
            "email"
        )

        password = request.form.get(
            "password"
        )

        # cek email sudah ada
        existing_user = (
            User.query.filter_by(
                email=email
            ).first()
        )

        if existing_user:

            flash(
                "Email sudah digunakan",
                "danger"
            )

            return redirect(
                url_for(
                    "auth.register"
                )
            )

        # hitung umur otomatis
        birth_date = (
            datetime.strptime(
                tanggal_lahir,
                "%Y-%m-%d"
            )
        )

        today = datetime.today()

        umur = (
            today.year
            - birth_date.year
            - (
                (
                    today.month,
                    today.day
                )
                <
                (
                    birth_date.month,
                    birth_date.day
                )
            )
        )

        # generate OTP
        otp = str(
            random.randint(
                100000,
                999999
            )
        )

        # buat user baru
        user = User(
            nama=nama,
            tanggal_lahir=
            birth_date,
            umur=umur,
            riwayat_penyakit=
            riwayat_penyakit,
            jenis_kelamin=
            jenis_kelamin,
            email=email,
            otp_code=otp,
            is_verified=False
        )

        user.set_password(
            password
        )

        db.session.add(
            user
        )

        db.session.commit()

        # kirim OTP
        send_otp_email(
            email,
            otp
        )

        flash(
            "Kode OTP berhasil dikirim ke email",
            "info"
        )

        session[
            "verify_email"
        ] = email

        return redirect(
            url_for(
                "auth.verify"
            )
        )

    return render_template(
        "auth/register.html"
    )


# ======================
# VERIFY OTP
# ======================

@auth.route(
    "/verify",
    methods=["GET", "POST"]
)
def verify():

    if request.method == "POST":

        otp_input = (
            request.form.get(
                "otp"
            )
        )

        email = session.get(
            "verify_email"
        )

        user = (
            User.query.filter_by(
                email=email
            ).first()
        )

        if (
            user
            and
            user.otp_code
            == otp_input
        ):

            user.is_verified = (
                True
            )

            user.otp_code = (
                None
            )

            db.session.commit()

            flash(
                "Akun berhasil dibuat",
                "success"
            )

            return redirect(
                url_for(
                    "auth.login"
                )
            )

        flash(
            "Kode OTP salah",
            "danger"
        )

        return redirect(
            url_for(
                "auth.verify"
            )
        )

    return render_template(
        "auth/verify_otp.html"
    )


# ======================
# LOGIN
# ======================

@auth.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    if request.method == "POST":

        email = request.form.get(
            "email"
        )

        password = (
            request.form.get(
                "password"
            )
        )

        user = (
            User.query.filter_by(
                email=email
            ).first()
        )

        # email tidak ditemukan
        if not user:

            flash(
                "Email tidak ditemukan",
                "danger"
            )

            return redirect(
                url_for(
                    "auth.login"
                )
            )

        # belum verifikasi
        if (
            not user
            .is_verified
        ):

            flash(
                "Akun belum diverifikasi",
                "warning"
            )

            return redirect(
                url_for(
                    "auth.login"
                )
            )

        # password salah
        if not user.check_password(
            password
        ):

            flash(
                "Password salah",
                "danger"
            )

            return redirect(
                url_for(
                    "auth.login"
                )
            )

        # login sukses
        session[
            "user_id"
        ] = user.id

        session[
            "nama"
        ] = user.nama

        session[
            "email"
        ] = user.email

        flash(
            "Login berhasil",
            "success"
        )

        return redirect(
            url_for(
                "diagnosa.dashboard"
            )
        )

    return render_template(
        "auth/login.html"
    )


# ======================
# LOGOUT
# ======================

@auth.route(
    "/logout"
)
def logout():

    session.clear()

    flash(
        "Berhasil logout",
        "success"
    )

    return redirect(
        url_for(
            "auth.login"
        )
    )
    
# ==========================
# FORGOT PASSWORD
# ==========================

@auth.route(
    "/forgot-password",
    methods=["GET", "POST"]
)
def forgot_password():

    if request.method == "POST":

        email = request.form.get(
            "email"
        )

        user = User.query.filter_by(
            email=email
        ).first()

        if not user:

            flash(
                "Email tidak ditemukan",
                "danger"
            )

            return redirect(
                url_for(
                    "auth.forgot_password"
                )
            )

        otp = str(
            random.randint(
                100000,
                999999
            )
        )

        user.otp_code = otp

        db.session.commit()

        send_otp_email(
            email,
            otp
        )

        session[
            "reset_email"
        ] = email

        flash(
            "Kode OTP berhasil dikirim",
            "info"
        )

        return redirect(
            url_for(
                "auth.verify_reset"
            )
        )

    return render_template(
        "forgot_password.html"
    )


# ==========================
# VERIFY RESET OTP
# ==========================

@auth.route(
    "/verify-reset",
    methods=["GET", "POST"]
)
def verify_reset():

    if request.method == "POST":

        otp_input = request.form.get(
            "otp"
        )

        email = session.get(
            "reset_email"
        )

        user = User.query.filter_by(
            email=email
        ).first()

        if not user:

            flash(
                "User tidak ditemukan",
                "danger"
            )

            return redirect(
                url_for(
                    "auth.login"
                )
            )

        if user.otp_code == otp_input:

            flash(
                "OTP berhasil diverifikasi",
                "success"
            )

            return redirect(
                url_for(
                    "auth.reset_password"
                )
            )

        flash(
            "OTP salah",
            "danger"
        )

    return render_template(
        "verify_reset_otp.html"
    )


# ==========================
# RESET PASSWORD
# ==========================

@auth.route(
    "/reset-password",
    methods=["GET", "POST"]
)
def reset_password():

    if request.method == "POST":

        password = request.form.get(
            "password"
        )

        confirm_password = request.form.get(
            "confirm_password"
        )

        if password != confirm_password:

            flash(
                "Password tidak sama",
                "danger"
            )

            return redirect(
                url_for(
                    "auth.reset_password"
                )
            )

        email = session.get(
            "reset_email"
        )

        user = User.query.filter_by(
            email=email
        ).first()

        user.set_password(
            password
        )

        user.otp_code = None

        db.session.commit()

        session.pop(
            "reset_email",
            None
        )

        flash(
            "Password berhasil diubah",
            "success"
        )

        return redirect(
            url_for(
                "auth.login"
            )
        )

    return render_template(
        "reset_password.html"
    )