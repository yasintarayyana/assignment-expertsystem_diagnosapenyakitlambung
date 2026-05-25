from flask_mail import (
    Message
)

from extensions import (
    mail
)


def send_result_email(
        nama,
        email,
        hasil):

    subject = (
        "Hasil Diagnosa "
        "Penyakit Lambung"
    )

    body = f"""
Halo {nama},

Berikut hasil diagnosa penyakit lambung Anda.

━━━━━━━━━━━━━━━━━━

HASIL DIAGNOSA

Kemungkinan Penyakit:
{hasil['nama']}

Tingkat Keyakinan:
{hasil['persentase']}%

Deskripsi:
{hasil['deskripsi']}

━━━━━━━━━━━━━━━━━━

PANTANGAN

"""

    for item in hasil[
        'pantangan'
    ]:

        body += (
            f"✗ {item}\n"
        )

    body += (
        "\n━━━━━━━━━━━━━━━━━━\n"
        "\nREKOMENDASI\n\n"
    )

    for item in hasil[
        'solusi'
    ]:

        body += (
            f"✓ {item}\n"
        )

    body += f"""

━━━━━━━━━━━━━━━━━━

Catatan:
Hasil ini merupakan
prediksi awal menggunakan
metode Rule Based
dan Forward Chaining.

Silakan konsultasikan
ke dokter untuk
diagnosa medis resmi.

Terima kasih,
SISTEM PAKAR LAMBUNG
"""

    msg = Message(

        subject=subject,

        recipients=[
            email
        ],

        body=body,

        sender=(

            "SISTEM PAKAR LAMBUNG",

            "projectsistempakarlambung@gmail.com"
        )
    )

    mail.send(msg)