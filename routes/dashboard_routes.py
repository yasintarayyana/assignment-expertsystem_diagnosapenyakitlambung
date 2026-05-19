from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_required,
    current_user
)

from models.diagnosis_model import DiagnosisHistory
from models.user_model import User
from extensions import db

dashboard = Blueprint(
    'dashboard',
    __name__
)


# ======================
# DASHBOARD
# ======================
@dashboard.route('/dashboard')
@login_required
def dashboard_page():

    total_diagnosa = DiagnosisHistory.query.filter_by(
        user_id=current_user.id
    ).count()

    latest = DiagnosisHistory.query.filter_by(
        user_id=current_user.id
    ).order_by(
        DiagnosisHistory.created_at.desc()
    ).first()

    # ======================
    # LOGIC KONDISI
    # ======================

    kondisi = "Belum Dicek"
    pesan_kondisi = "Lakukan diagnosa"

    if latest:

        persen = latest.similarity

        if persen < 50:
            kondisi = "Baik"
            pesan_kondisi = (
                "Risiko rendah"
            )

        elif persen < 75:
            kondisi = (
                "Perlu Perhatian"
            )
            pesan_kondisi = (
                "Jaga pola makan"
            )

        else:
            kondisi = "Waspada"
            pesan_kondisi = (
                "Segera konsultasi"
            )
        
    return render_template(
        'dashboard.html',
        user=current_user,
        total_diagnosa=total_diagnosa,
        latest=latest,
        kondisi=kondisi,
        pesan_kondisi=pesan_kondisi
    )


# ======================
# RIWAYAT DIAGNOSA
# ======================
@dashboard.route('/riwayat')
@login_required
def riwayat():

    riwayat_data = DiagnosisHistory.query.filter_by(
        user_id=current_user.id
    ).order_by(
        DiagnosisHistory.created_at.desc()
    ).all()

    return render_template(
        'riwayat.html',
        riwayat=riwayat_data
    )


# ======================
# DETAIL RIWAYAT
# ======================
@dashboard.route('/riwayat/<int:id>')
@login_required
def detail_riwayat(id):

    data = DiagnosisHistory.query.get_or_404(id)

    return render_template(
        'detail_riwayat.html',
        data=data
    )


# ======================
# PROFILE
# ======================
@dashboard.route(
    '/profile',
    methods=['GET', 'POST']
)
@login_required
def profile():

    if request.method == 'POST':

        username = request.form.get(
            'username'
        )

        email = request.form.get(
            'email'
        )

        current_user.username = username
        current_user.email = email

        db.session.commit()

        flash(
            'Profile berhasil diperbarui',
            'success'
        )

        return redirect(
            url_for(
                'dashboard.profile'
            )
        )

    return render_template(
        'profile.html'
    )