from knowledge_base.rules import RULES
from data.gejala import GEJALA


# =========================
# CF COMBINATION FUNCTION
# =========================
def combine_cf(cf1, cf2):
    return cf1 + cf2 * (1 - cf1)


# =========================
# MAIN INFERENCE ENGINE
# =========================
def forward_chaining(selected_gejala, selected_onset, selected_riwayat):
    hasil = None
    highest_cf = 0

    matched_rules = []
    reasoning = []

    W_GEJALA = 0.6
    W_ONSET = 0.2
    W_RIWAYAT = 0.2
    
    for penyakit, data in RULES.items():
        gejala_rule = data["gejala"]

        cf_combine = 0
        first = True
        gejala_cocok = []

        # ======================
        # 1. GEJALA
        # ======================
        for kode, cf_user in selected_gejala.items():

            cf_pakar = gejala_rule.get(kode, 0)
            cf_gejala = cf_user * cf_pakar

            gejala_cocok.append({
                "kode": kode,
                "nama": GEJALA.get(kode, kode),
                "cf_pakar": round(cf_pakar, 2),
                "cf_user": round(cf_user, 2),
                "hasil_cf": round(cf_gejala, 2)
            })

            if cf_gejala > 0:
              if first:
                cf_combine = cf_gejala
                first = False
              else:
                cf_combine = combine_cf(cf_combine, cf_gejala)

        # ======================
        # 2. ONSET
        # ======================
        cf_onset = data["onset"].get(selected_onset, 0)

        # ======================
        # 3. RIWAYAT
        # ======================
        cf_riwayat = data["riwayat"].get(selected_riwayat, 0)
        
        # ======================
        # FINAL SCORE
        # ======================
        cf_final = (
            cf_combine * W_GEJALA +
            cf_onset * W_ONSET +
            cf_riwayat * W_RIWAYAT
        )

        persen = round(cf_final * 100, 1)

        matched_rules.append({
            "penyakit": penyakit,
            "persen": persen
        })

        reasoning.append({
            "penyakit": penyakit,
            "persentase": persen,
            "gejala": gejala_cocok,
            "cf_onset": cf_onset,
            "cf_riwayat": cf_riwayat
        })

        if cf_final > highest_cf:
            highest_cf = cf_final

            hasil = {
                "nama": penyakit,
                "persentase": persen,
                "deskripsi": data["deskripsi"],
                "solusi": data["solusi"],
                "obat": data["obat"],
                "pantangan": data["pantangan"],
                "selected_gejala": [GEJALA[g] for g in selected_gejala]
            }

    matched_rules.sort(key=lambda x: x["persen"], reverse=True)

    if not hasil:
        hasil = {
            "nama": "Tidak Diketahui",
            "persentase": 0,
            "deskripsi": "Gejala belum cukup untuk menentukan diagnosis.",
            "solusi": [],
            "obat": [],
            "pantangan": []
        }

    hasil["matched_rules"] = matched_rules
    hasil["reasoning"] = reasoning

    return hasil