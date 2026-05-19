from flask import (
    Blueprint,
    render_template,
    request
)

from flask_login import (
    login_required,
    current_user
)

from data.gejala import GEJALA
from rules.forward_chaining import forward_chaining
from models.diagnosis_model import DiagnosisHistory
from extensions import db


diagnosa = Blueprint(
    'diagnosa',
    __name__
)


@diagnosa.route(
    '/diagnosa',
    methods=['GET', 'POST']
)
@login_required
def diagnosa_page():

    hasil = None

    if request.method == 'POST':

        selected_gejala = request.form.getlist(
            'gejala'
        )

        hasil = forward_chaining(
            selected_gejala
        )

        if hasil:

            nama_gejala = []

            for kode in selected_gejala:
                nama_gejala.append(
                    GEJALA[kode]
                )

            riwayat = DiagnosisHistory(
                user_id=current_user.id,

                disease_name=
                hasil["nama"],

                symptoms=
                ", ".join(
                    nama_gejala
                ),

                description=
                hasil["deskripsi"],

                similarity=
                hasil["persentase"]
            )

            db.session.add(
                riwayat
            )

            db.session.commit()

    return render_template(
        'diagnosa.html',
        gejala=GEJALA,
        hasil=hasil
    )