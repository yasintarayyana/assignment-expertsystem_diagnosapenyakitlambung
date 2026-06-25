from extensions import db

from datetime import (
    datetime
)

import pytz


class DiagnosisHistory(
    db.Model
):

    __tablename__ = (
        "diagnosis_history"
    )

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "user.id"
        ),
        nullable=False
    )

    penyakit = db.Column(
        db.String(100),
        nullable=False
    )

    persentase = db.Column(
        db.Float,
        nullable=False
    )
    
    def now_wib():
        tz = pytz.timezone("Asia/Jakarta")
        return datetime.now(tz)

    created_at = db.Column(
        db.DateTime,
        default=now_wib
    )