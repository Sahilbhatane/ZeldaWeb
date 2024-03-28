const parallax_el = document.querySelectorAll(".parallax");
let xValue = 0, yValue = 0;

window.addEventListener("mousemove", (e) => {
    xValue = e.clientX - window.innerWidth / 2;
    yValue = e.clientY - window.innerHeight / 2;

    parallax_el.forEach((el) => {
        let speedx = parseFloat(el.dataset.speedx), speedy = parseFloat(el.dataset.speedy); // Parse speed values to float
        el.style.transform = `translateX(calc(0% + ${-xValue * speedx}px)) translateY(calc(0% + ${yValue * speedy}px))`; // Negate yValue for proper y-axis parallax effect
    });
});
