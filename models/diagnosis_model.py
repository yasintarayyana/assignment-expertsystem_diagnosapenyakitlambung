from extensions import db


class DiagnosisHistory(db.Model):
    __tablename__ = 'diagnosis_history'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        nullable=False
    )

    disease_name = db.Column(
        db.String(100),
        nullable=False
    )

    symptoms = db.Column(
        db.Text,
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=False
    )

    similarity = db.Column(
        db.Float,
        nullable=False,
        default=0
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )