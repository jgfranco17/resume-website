window.addEventListener('DOMContentLoaded', event => {
    let d;
    let time;
    let date;
    let hours;
    let minutes;
    let seconds;
    const clock = document.getElementById("clock");
    setInterval(() => {
        d = new Date();

        if (d.getHours().toString().length < 2) {
            hours = "0" + d.getHours().toString();
        }
        else {
            hours = d.getHours().toString();
        }

        if (d.getMinutes().toString().length < 2) {
            minutes = "0" + d.getMinutes().toString();
        }
        else {
            minutes = d.getMinutes().toString();
        }

        if (d.getSeconds().toString().length < 2) {
            seconds = "0" + d.getSeconds().toString();
        }
        else {
            seconds = d.getSeconds().toString();
        }

        time = hours + ":" + minutes + ":" + seconds;
        date = d.toLocaleDateString();
        clock.innerHTML = time + ", " + date;
    }, 1000);
});