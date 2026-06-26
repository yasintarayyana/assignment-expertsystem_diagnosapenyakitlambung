from flask import (
    Blueprint,
    render_template,
    request,
    session,
    redirect,
    url_for,
    flash
)

from data.gejala import (
    GEJALA
)

from models.user_model import (
    User
)

from rules.forward_chaining import (
    forward_chaining
)

from services.email_service import (
    send_result_email
)

from extensions import db

from models.diagnosis_history_model import (
    DiagnosisHistory
)

import os

from flask import (
    send_file
)

from services.pdf_service import (
    generate_result_pdf
) 

diagnosa = Blueprint(
    "diagnosa",
    __name__
)


# ======================
# LANDING PAGE
# ======================

@diagnosa.route("/")
def landing():

    return render_template(
        "landing.html"
    )


# ======================
# GUIDELINES
# ======================

@diagnosa.route("/guidelines")
def guidelines():

    if not session.get(
        "user_id"
    ):

        return redirect(
            url_for(
                "auth.login"
            )
        )

    return render_template(
        "guidelines.html"
    )
    
    
# ======================
# FAQ
# ======================

@diagnosa.route("/faq")
def faq():

    return render_template(
        "faq.html"
    )
    

# ======================
# TEST PROFILE
# ======================

@diagnosa.route("/test-profile", methods=["GET", "POST"])
def test_profile():

    if not session.get("user_id"):
        return redirect(url_for("auth.login"))

    user = User.query.get(session["user_id"])

    if request.method == "POST":

        session["nama"] = request.form.get("nama")
        session["jenis_kelamin"] = request.form.get("jk")
        session["tanggal_lahir"] = request.form.get("tanggal_lahir")
        session["usia"] = request.form.get("usia")
        session["email"] = request.form.get("email")

        return redirect(url_for("diagnosa.onset"))

    return render_template(
        "test_profile.html",
        user=user
    )
    
    
# ======================
# ONSET
# ======================

@diagnosa.route(
    "/onset",
    methods=["GET", "POST"]
)
def onset():

    if not session.get("user_id"):
        return redirect(
            url_for("auth.login")
        )

    if request.method == "POST":

        session["onset"] = request.form.get("onset")
        session["riwayat"] = request.form.get("riwayat")
        session["jenis_riwayat"] = request.form.get("jenis_riwayat")

        return redirect(
            url_for("diagnosa.quiz")
        )

    return render_template(
        "onset.html"
    )
    
    
# ======================
# QUIZ
# ======================

@diagnosa.route(
    "/quiz",
    methods=["GET", "POST"]
)
def quiz():

    # cek login
    if not session.get(
        "user_id"
    ):

        flash(
            "Silakan login terlebih dahulu",
            "warning"
        )

        return redirect(
            url_for(
                "auth.login"
            )
        )

    if request.method == "POST":

        selected_gejala = {}

        for kode in (
            GEJALA.keys()
        ):

            nilai = request.form.get(
                kode
            )

            if nilai:

                cf_user = float(
                    nilai
                )

                if cf_user > 0:

                    selected_gejala[
                        kode
                    ] = cf_user

        session[
            "selected_gejala"
        ] = selected_gejala

        return redirect(
            url_for(
                "diagnosa.loading"
            )
        )

    return render_template(
        "quiz.html",
        gejala=GEJALA
    )


# ======================
# LOADING PAGE
# ======================

@diagnosa.route(
    "/loading"
)
def loading():

    if not session.get(
        "user_id"
    ):

        return redirect(
            url_for(
                "auth.login"
            )
        )

    return render_template(
        "loading.html"
    )


# ======================
# RESULT
# ======================

@diagnosa.route(
    "/result"
)
def result():

    if not session.get(
        "user_id"
    ):

        return redirect(
            url_for(
                "auth.login"
            )
        )

    selected_gejala = session.get(
        "selected_gejala",
        {}
    )

    user = User.query.get(
        session[
            "user_id"
        ]
    )
    
    selected_onset = session.get("onset")
    riwayat_status = session.get("riwayat")
    jenis_riwayat = session.get("jenis_riwayat")

    if riwayat_status == "Ya" and jenis_riwayat:
      selected_riwayat = jenis_riwayat
    else:
      selected_riwayat = "Tidak"

    hasil = forward_chaining(
        selected_gejala,
        selected_onset,
        selected_riwayat
    )
    
    # ambil penyakit tertinggi
    penyakit_utama = {
        "penyakit": hasil["nama"],
        "persentase": hasil["persentase"]
    }

    # simpan histori
    history = DiagnosisHistory(

        user_id=user.id,

        penyakit=
        penyakit_utama[
            "penyakit"
        ],

        persentase=
        penyakit_utama[
            "persentase"
        ]
    )

    db.session.add(
        history
    )

    db.session.commit()

    # kirim email hasil
    if user and user.email:
      try:
          send_result_email(
            hasil=hasil,
            nama=session.get("nama"),
            email=session.get("email"),
            jenis_kelamin=session.get("jenis_kelamin"),
            tanggal_lahir=session.get("tanggal_lahir"),
            usia=session.get("usia"),
            onset=selected_onset,
            riwayat=selected_riwayat
          )
      except Exception as e:
        print("EMAIL ERROR:", e)

    return render_template(
      "result.html",
      hasil=hasil,
      nama=session.get("nama"),
      email=session.get("email"),
      onset=selected_onset,
      riwayat=selected_riwayat
    )
    
# ======================
# HISTORY
# ======================

@diagnosa.route(
    "/history"
)
def history():

    if not session.get(
        "user_id"
    ):

        return redirect(
            url_for(
                "auth.login"
            )
        )

    histories = (
        DiagnosisHistory
        .query
        .filter_by(
            user_id=session[
                "user_id"
            ]
        )
        .order_by(
            DiagnosisHistory
            .created_at
            .desc()
        )
        .all()
    )

    return render_template(
        "history.html",
        histories=histories
    )

# ======================
# DASHBOARD
# ======================

@diagnosa.route(
    "/dashboard"
)
def dashboard():

    if not session.get(
        "user_id"
    ):

        return redirect(
            url_for(
                "auth.login"
            )
        )

    user = User.query.get(
        session[
            "user_id"
        ]
    )

    total_diagnosa = len(
        user.histories
    )

    last_history = None

    if user.histories:

        last_history = (
            DiagnosisHistory
            .query
            .filter_by(
                user_id=user.id
            )
            .order_by(
                DiagnosisHistory
                .created_at.desc()
            )
            .first()
        )

    return render_template(
        "dashboard.html",
        user=user,
        total_diagnosa=
        total_diagnosa,
        last_history=
        last_history
    )
    
# ======================
# DOWNLOAD PDF
# ======================

@diagnosa.route(
    "/download-pdf"
)
def download_pdf():

    if not session.get(
        "user_id"
    ):

        return redirect(
            url_for(
                "auth.login"
            )
        )

    user = User.query.get(
        session[
            "user_id"
        ]
    )

    selected_gejala = session.get(
        "selected_gejala",
        {}
    )
    
    selected_onset = session.get("onset")
    riwayat_status = session.get("riwayat")
    jenis_riwayat = session.get("jenis_riwayat")

    if riwayat_status == "Ya":
      selected_riwayat = jenis_riwayat
    else:
      selected_riwayat = "Tidak"

    hasil = forward_chaining(
        selected_gejala,
        selected_onset,
        selected_riwayat
    )
    
    os.makedirs(
      "temp",
      exist_ok=True
    )

    file_path = f"hasil_{session['user_id']}.pdf"
    
    generate_result_pdf(
        nama=session.get("nama"),
        email=session.get("email"),
        jenis_kelamin=session.get("jenis_kelamin"),
        tanggal_lahir=session.get("tanggal_lahir"),
        usia=session.get("usia"),
        onset=selected_onset,
        riwayat=selected_riwayat,
        hasil=hasil,
        file_path=file_path
    )

    return send_file(
        file_path,
        as_attachment=True
    )