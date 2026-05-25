from knowledge_base.rules import RULES
from data.gejala import GEJALA


def combine_cf(
        cf1,
        cf2):

    return (
        cf1 +
        cf2 *
        (1 - cf1)
    )


def forward_chaining(
        selected_gejala):

    hasil = None
    highest_cf = 0

    matched_rules = []
    reasoning = []

    for penyakit, data in RULES.items():

        gejala_rule = (
            data["gejala"]
        )

        gejala_cocok = []

        cf_combine = 0
        first = True

        # LOOP SEMUA GEJALA USER
        for kode, cf_user in (
            selected_gejala.items()
        ):

            # kalau gejala ada di rule
            if kode in (
                gejala_rule.keys()
            ):

                cf_pakar = (
                    gejala_rule[
                        kode
                    ]
                )

            # kalau tidak ada
            else:

                cf_pakar = 0

            cf_gejala = (
                cf_user *
                cf_pakar
            )

            gejala_cocok.append({

                "kode":
                kode,

                "nama":
                GEJALA[kode],

                "cf_pakar":
                round(
                    cf_pakar,
                    2
                ),

                "cf_user":
                round(
                    cf_user,
                    2
                ),

                "hasil_cf":
                round(
                    cf_gejala,
                    2
                )
            })

            # hanya combine jika > 0
            if cf_gejala > 0:

                if first:

                    cf_combine = (
                        cf_gejala
                    )

                    first = False

                else:

                    cf_combine = (
                        combine_cf(
                            cf_combine,
                            cf_gejala
                        )
                    )

        persen = round(
            cf_combine * 100,
            1
        )

        matched_rules.append({

            "penyakit":
            penyakit,

            "persen":
            persen
        })

        reasoning.append({

            "penyakit":
            penyakit,

            "persentase":
            persen,

            "gejala":
            gejala_cocok
        })

        if cf_combine > (
            highest_cf
        ):

            highest_cf = (
                cf_combine
            )

            hasil = {

                "nama":
                penyakit,

                "persentase":
                persen,

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
                "selected_gejala":
                [
                    GEJALA[g]
                    for g in selected_gejala
                ]
            }

    matched_rules = sorted(

        matched_rules,

        key=lambda x:
        x["persen"],

        reverse=True
    )

    if not hasil:

        hasil = {

            "nama":
            "Tidak Diketahui",

            "persentase":
            0,

            "deskripsi":
            "Gejala belum cukup.",

            "solusi":
            [],

            "pantangan":
            []
        }

    hasil[
        "matched_rules"
    ] = matched_rules

    hasil[
        "reasoning"
    ] = reasoning

    return hasil