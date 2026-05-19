from knowledge_base.rules import RULES


def forward_chaining(
        selected_gejala):

    hasil = None
    highest_match = 0
    matched_rules = []

    for penyakit, data in RULES.items():

        gejala_rule = (
            data["gejala"]
        )

        cocok = len(
            set(selected_gejala)
            &
            set(gejala_rule)
        )

        persen = (
            cocok /
            len(gejala_rule)
        ) * 100

        matched_rules.append({

            "penyakit":
            penyakit,

            "match":
            cocok,

            "persen":
            round(
                persen,
                1
            )
        })

        if persen > highest_match:

            highest_match = persen

            hasil = {

                "nama":
                penyakit,

                "persentase":
                round(
                    persen,
                    1
                ),

                "deskripsi":
                data[
                    "deskripsi"
                ],

                "solusi":
                data[
                    "solusi"
                ],

                "pantangan":
                data[
                    "pantangan"
                ],

                "rule":
                gejala_rule
            }

    # Tambahkan matched rules
    if hasil:

        hasil[
            "matched_rules"
        ] = matched_rules

    else:

        hasil = {

            "nama":
            "Tidak Diketahui",

            "persentase":
            0,

            "deskripsi":
            """
            Gejala belum cukup
            untuk menentukan
            kemungkinan penyakit.
            """,

            "solusi": [
                "Coba pilih gejala lain",
                "Konsultasi ke dokter"
            ],

            "pantangan": [],

            "rule": [],

            "matched_rules":
            matched_rules
        }

    return hasil