document.addEventListener("DOMContentLoaded", () => {

    /* ==================
       DARK MODE
    ================== */

    const themeBtn = document.getElementById('themeToggle');

    if (themeBtn) {
        themeBtn.addEventListener('click', () => {

            document.body.classList.toggle('dark-mode');

            themeBtn.innerHTML =
                document.body.classList.contains('dark-mode')
                    ? '☀️'
                    : '🌙';
        });
    }


    /* ==================
       LANGUAGE TOGGLE
    ================== */

    const langBtn = document.getElementById('langToggle');

    let bahasa = 'id';

    if (langBtn) {
        langBtn.addEventListener('click', () => {

            bahasa = (bahasa === 'id') ? 'en' : 'id';

            langBtn.innerHTML =
                (bahasa === 'id')
                    ? '🇮🇩 ID'
                    : '🇺🇸 EN';
        });
    }

});