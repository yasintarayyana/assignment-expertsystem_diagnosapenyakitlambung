document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("userForm");

    if (!form) return;

    form.addEventListener("submit", (e) => {

        // OPTIONAL: kalau mau intercept dulu
        // e.preventDefault();

        const btn = form.querySelector("button");

        // =========================
        // UX LOADING STATE
        // =========================

        btn.disabled = true;
        btn.innerHTML = "Memproses...";

        // kasih sedikit delay biar terasa smooth
        // (kalau backend cepat, user tidak kaget)
        setTimeout(() => {

            form.submit();

        }, 600);

    });

});