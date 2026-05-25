document.addEventListener("DOMContentLoaded", () => {

    const circle = document.querySelector(".percentage-circle");

    if (!circle) return;

    let target = parseInt(circle.innerText);

    let current = 0;

    circle.innerText = "0%";

    const interval = setInterval(() => {

        current++;

        circle.innerText = current + "%";

        if (current >= target) {
            clearInterval(interval);
        }

    }, 15);

});