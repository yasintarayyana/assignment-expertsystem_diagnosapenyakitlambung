from flask import (
    Blueprint,
    render_template,
    request,
    session,
    redirect,
    url_for
)

from data.gejala import GEJALA

from rules.forward_chaining import (
    forward_chaining
)

from services.email_service import (
    send_result_email
)

diagnosa = Blueprint(
    'diagnosa',
    __name__
)


# ======================
# LANDING PAGE
# ======================

@diagnosa.route('/')
def landing():

    return render_template(
        'landing.html'
    )


# ======================
# QUIZ
# ======================

@diagnosa.route(
    '/quiz',
    methods=['GET', 'POST']
)
def quiz():

    if request.method == 'POST':

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
            'selected_gejala'
        ] = selected_gejala

        return redirect(
            url_for(
                'diagnosa.user_info'
            )
        )

    return render_template(
        'quiz.html',
        gejala=GEJALA
    )


# ======================
# USER INFO
# ======================

@diagnosa.route(
    '/user-info',
    methods=['GET', 'POST']
)
def user_info():

    if request.method == 'POST':

        nama = request.form.get(
            'nama'
        )

        email = request.form.get(
            'email'
        )

        session[
            'nama'
        ] = nama

        session[
            'email'
        ] = email

        return redirect(
            url_for(
                'diagnosa.loading'
            )
        )

    return render_template(
        'user_info.html'
    )


# ======================
# LOADING PAGE
# ======================

@diagnosa.route(
    '/loading'
)
def loading():

    return render_template(
        'loading.html'
    )


# ======================
# RESULT
# ======================

@diagnosa.route(
    '/result'
)
def result():

    selected_gejala = session.get(
        'selected_gejala',
        {}
    )

    nama = session.get(
        'nama'
    )

    email = session.get(
        'email'
    )

    hasil = (
        forward_chaining(
            selected_gejala
        )
    )

    if email:

        send_result_email(
            nama,
            email,
            hasil
        )

    return render_template(

        'result.html',

        hasil=hasil,

        nama=nama,

        email=email
    )