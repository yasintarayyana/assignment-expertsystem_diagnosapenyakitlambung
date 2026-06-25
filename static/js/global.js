document.addEventListener("DOMContentLoaded", () => {

    // =========================
    // PAGE LOAD EFFECT
    // =========================
    document.body.style.opacity = "1";


    // =========================
    // SMOOTH LINK TRANSITION
    // =========================
    document.querySelectorAll("a[href]").forEach(link => {

        link.addEventListener("click", (e) => {

            const url = link.getAttribute("href");

            // ignore external link, anchor, mailto, dll
            if (!url || !url.startsWith("/")) return;

            e.preventDefault();

            document.body.classList.add("page-leave");

            setTimeout(() => {
                window.location.href = url;
            }, 200);

        });

    });


    // =========================
    // FLASH MESSAGE AUTO HIDE
    // =========================
    const flashContainer = document.querySelector(".flash-container");

    if (flashContainer) {

        setTimeout(() => {

            flashContainer.style.opacity = "0";
            flashContainer.style.transform = "translateY(-10px)";
            flashContainer.style.transition = "0.3s ease";

            setTimeout(() => {
                flashContainer.remove();
            }, 300);

        }, 3000); // 3 detik

    }

});