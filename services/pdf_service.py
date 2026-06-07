from reportlab.platypus import (
    SimpleDocTemplate,
    Spacer,
    Paragraph
)

from reportlab.lib import colors

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.platypus import (
    Table,
    TableStyle
)

from datetime import (
    datetime
)


def generate_result_pdf(

    nama,
    email,
    hasil,
    output_path

):

    doc = SimpleDocTemplate(
        output_path
    )

    styles = (
        getSampleStyleSheet()
    )

    content = []

    title = Paragraph(
        "HASIL DIAGNOSA SISTEM PAKAR LAMBUNG",
        styles["Title"]
    )

    content.append(
        title
    )

    content.append(
        Spacer(
            1,
            20
        )
    )

    tanggal = datetime.now().strftime(
        "%d-%m-%Y %H:%M"
    )

    content.append(
        Paragraph(
            f"<b>Nama:</b> {nama}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Email:</b> {email}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Tanggal:</b> {tanggal}",
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(
            1,
            20
        )
    )

    content.append(
        Paragraph(
            "Hasil Diagnosa",
            styles["Heading2"]
        )
    )

    data = [
        [
            "Penyakit",
            "Persentase"
        ]
    ]

    for item in hasil:

        data.append(
            [
                item[
                    "penyakit"
                ],
                f'{item["persentase"]:.2f}%'
            ]
        )

    table = Table(
        data
    )

    table.setStyle(
        TableStyle([

            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.green
            ),

            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),

            (
                "GRID",
                (0, 0),
                (-1, -1),
                1,
                colors.black
            )
        ])
    )

    content.append(
        table
    )

    content.append(
        Spacer(
            1,
            20
        )
    )

    content.append(
        Paragraph(
            """
            <b>Disclaimer:</b>
            Hasil diagnosa ini hanya
            sebagai rekomendasi awal
            dan tidak menggantikan
            pemeriksaan dokter.
            """,
            styles["Italic"]
        )
    )

    doc.build(
        content
    )