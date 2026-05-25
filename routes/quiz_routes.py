from flask import render_template


def render_quiz_result(hasil, nama):
    return render_template(
        "result.html",
        hasil=hasil,
        nama=nama
    )