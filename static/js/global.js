document.addEventListener("DOMContentLoaded", () => {

    // smooth page enter
    document.body.style.opacity = "1";

    // intercept semua link
    document.querySelectorAll("a[href]").forEach(link => {

        link.addEventListener("click", (e) => {

            const url = link.getAttribute("href");

            // ignore external / anchor
            if (!url.startsWith("/")) return;

            e.preventDefault();

            document.body.classList.add("page-leave");

            setTimeout(() => {
                window.location.href = url;
            }, 200);

        });

    });

});