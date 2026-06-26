from flask_mail import Message
from extensions import mail

def send_result_email(
    nama,
    email,
    hasil,
    jenis_kelamin,
    tanggal_lahir,
    usia,
    onset,
    riwayat
):

    subject = "Hasil Diagnosa Penyakit Lambung"

    body = f"""
Halo {nama},

Berikut hasil pemeriksaan pada Sistem Pakar Diagnosa Penyakit Lambung.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DATA DIRI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Nama               : {nama}
Jenis Kelamin      : {jenis_kelamin}
Tanggal Lahir      : {tanggal_lahir}
Usia               : {usia} tahun

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RIWAYAT KELUHAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Lama Keluhan Dirasakan : {onset}
Diagnosa Penyakit Lambung Sebelumnya : {riwayat}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HASIL DIAGNOSA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kemungkinan Penyakit : {hasil['nama']}
Tingkat Keyakinan : {hasil['persentase']}%
Deskripsi : {hasil['deskripsi']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PILIHAN GEJALA YANG MENANDAKAN {hasil['nama'].upper()}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    for item in hasil["reasoning"]:
        if item["penyakit"] == hasil["nama"]:

            for g in item["gejala"]:

                body += (
                    f"• {g['nama']} "
                    f"({round(g['hasil_cf'] * 100, 1)}%)\n"
                )

    body += """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
KEMUNGKINAN PENYAKIT LAIN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    for item in hasil["matched_rules"]:

        body += (
            f"• {item['penyakit']} : "
            f"{item['persen']}%\n"
        )

    body += """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SARAN PENANGANAN AWAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    for item in hasil["solusi"]:

        body += f"✓ {item}\n"

    body += """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REKOMENDASI OBAT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    for item in hasil["obat"]:

        body += f"✓ {item}\n"

    body += """
-------------------------------------------------------
CATATAN:
Obat dengan tanda (*) memerlukan resep dan hanya boleh 
digunakan sesuai anjuran dokter.
-------------------------------------------------------
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PANTANGAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    for item in hasil["pantangan"]:

        body += f"✗ {item}\n"

    body += """
    
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CATATAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Hasil ini merupakan prediksi awal menggunakan metode Forward Chaining dan Certainty Factor.
Hasil tidak dapat digunakan sebagai pengganti diagnosis medis profesional.
Jika keluhan berlanjut atau memburuk, segera konsultasikan dengan dokter.


Terima kasih,
SISTEM PAKAR LAMBUNG
"""

    msg = Message(
        subject=subject,
        recipients=[email],
        body=body,
        sender=(
            "SISTEM PAKAR LAMBUNG",
            "projectsistempakarlambung@gmail.com"
        )
    )

    try:
        mail.send(msg)
        print("Email berhasil dikirim.")
    except Exception as e:
        print(f"Gagal mengirim email: {e}")
    
# ==========================
# EMAIL OTP VERIFICATION
# ==========================

def send_otp_email(
    email,
    otp
):

    msg = Message(

        subject=
        "Kode Verifikasi Akun",

        recipients=[
            email
        ],

        body=f"""
Halo,

Berikut kode OTP verifikasi akun Anda:

━━━━━━━━━━━━━━━━━━

KODE OTP:
{otp}

━━━━━━━━━━━━━━━━━━

Jangan bagikan kode ini
kepada siapa pun.

Jika Anda tidak merasa
melakukan pendaftaran,
abaikan email ini.

Terima kasih,
SISTEM PAKAR LAMBUNG
""",

        sender=(

            "SISTEM PAKAR LAMBUNG",

            "projectsistempakarlambung@gmail.com"
        )
    )

    try:
        mail.send(msg)
        print("Email berhasil dikirim.")
    except Exception as e:
        print(f"Gagal mengirim email: {e}")