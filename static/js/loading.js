document.addEventListener("DOMContentLoaded", () => {

    const fill = document.querySelector(".loading-fill");

    let progress = 0;

    const interval = setInterval(() => {

        // easing biar tidak linear kaku
        progress += Math.random() * 8;

        if (progress >= 100) progress = 100;

        if (fill) {
            fill.style.width = progress + "%";
        }

        if (progress === 100) {

            clearInterval(interval);

            setTimeout(() => {
                window.location.href = "/result";
            }, 400);

        }

    }, 60);

});