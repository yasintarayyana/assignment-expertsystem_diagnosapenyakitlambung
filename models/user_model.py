from extensions import db
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

class User(db.Model):

    __tablename__ = "user"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nama = db.Column(
        db.String(150),
        nullable=False
    )

    tanggal_lahir = db.Column(
        db.Date,
        nullable=False
    )

    umur = db.Column(
        db.Integer,
        nullable=False
    )

    riwayat_penyakit = db.Column(
        db.Text,
        nullable=True
    )

    jenis_kelamin = db.Column(
        db.String(20),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    is_verified = db.Column(
        db.Boolean,
        default=False
    )

    otp_code = db.Column(
        db.String(6),
        nullable=True
    )
    
    # RELATIONSHIP
    histories = db.relationship(
        "DiagnosisHistory",
        backref="user",
        lazy=True,
        cascade=
        "all, delete-orphan"
    )

    def set_password(
        self,
        password
    ):
        self.password = generate_password_hash(
            password
        )

    def check_password(
        self,
        password
    ):
        return check_password_hash(
            self.password,
            password
        )