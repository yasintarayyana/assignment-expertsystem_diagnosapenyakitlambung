from extensions import db

from datetime import (
    datetime
)


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

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )