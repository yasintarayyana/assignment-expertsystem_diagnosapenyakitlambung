from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle


def generate_result_pdf(
    nama,
    email,
    jenis_kelamin,
    tanggal_lahir,
    usia,
    onset,
    riwayat,
    hasil,
    file_path
):

    doc = SimpleDocTemplate(file_path, pagesize=A4)
    usable_width = A4[0] - doc.leftMargin - doc.rightMargin

    styles = getSampleStyleSheet()
    
    center_style = ParagraphStyle(
    "CenterStyle",
    parent=styles["BodyText"],
    alignment=TA_CENTER
    )

    content = []

    # ======================
    # HEADER
    # ======================
    
    content.append(
        Paragraph(
            "HASIL DIAGNOSA PENYAKIT LAMBUNG",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 40))

    data_diri = [
        Paragraph("<b>DATA DIRI</b>", styles["Heading3"]),
        Paragraph(f"Nama : {nama}", styles["Normal"]),
        Paragraph(f"Email : {email}", styles["Normal"]),
        Paragraph(f"Jenis Kelamin : {jenis_kelamin}", styles["Normal"]),
        Paragraph(f"Tanggal Lahir : {tanggal_lahir}", styles["Normal"]),
        Paragraph(f"Usia : {usia}", styles["Normal"]),
    ]

    riwayat_keluhan = [
        Paragraph("<b>RIWAYAT KELUHAN</b>", styles["Heading3"]),
        Paragraph(f"Lama Keluhan : {onset}", styles["Normal"]),
        Paragraph(f"Riwayat Sebelumnya : {riwayat}", styles["Normal"]),
    ]

    table_info = Table(
        [[data_diri, riwayat_keluhan]],
        colWidths=[
            usable_width / 2,
            usable_width / 2
        ]
    )

    table_info.setStyle(
        TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'TOP')
        ])
    )

    content.append(table_info)

    content.append(
        Paragraph(
            f"<b>Diagnosis:</b> {hasil['nama']}",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"Tingkat Keyakinan: {hasil['persentase']}%",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            hasil["deskripsi"],
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 20))

    # ======================
    # SOLUSI
    # ======================

    solusi_text = [
        Paragraph("<b>SARAN PENANGANAN AWAL</b>", styles["Heading3"])
    ]

    for item in hasil["solusi"]:
        solusi_text.append(
            Paragraph(f"• {item}", styles["Normal"])
        )

    pantangan_text = [
        Paragraph("<b>PANTANGAN</b>", styles["Heading3"])
    ]

    for item in hasil["pantangan"]:
        pantangan_text.append(
            Paragraph(f"• {item}", styles["Normal"])
        )

    table_saran = Table(
        [[solusi_text, pantangan_text]],
        colWidths=[
            usable_width / 2,
            usable_width / 2
        ]
    )

    table_saran.setStyle(
        TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'TOP')
        ])
    )

    content.append(table_saran)

    # ======================
    # OBAT
    # ======================

    content.append(
        Paragraph(
            "Rekomendasi Obat",
            styles["Heading2"]
        )
    )

    ada_resep = False

    for obat in hasil["obat"]:

        if "*" in obat:
            ada_resep = True

        content.append(
            Paragraph(
                f"• {obat}",
                styles["Normal"]
            )
        )

    if ada_resep:

        content.append(
            Paragraph(
                "<b>Catatan:</b> Obat dengan tanda (*) memerlukan resep dan konsultasi dokter sebelum digunakan.",
                styles["Normal"]
            )
        )


    # ======================
    # KEMUNGKINAN LAIN
    # ======================

    content.append(
        Paragraph(
            "Kemungkinan Penyakit Lain",
            styles["Heading2"]
        )
    )

    for item in hasil["matched_rules"]:

        content.append(
            Paragraph(
                f"{item['penyakit']} - {item['persen']}%",
                styles["Normal"]
            )
        )
    
    content.append(Spacer(1, 35))

    content.append(
        Paragraph(
            "<i>Hasil merupakan hasil analisis sistem pakar dan tidak menggantikan diagnosis maupun konsultasi langsung dengan dokter.</i>",
            center_style
        )
    )

    doc.build(content)