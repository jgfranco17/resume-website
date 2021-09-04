window.addEventListener('DOMContentLoaded', event => {
    if (window.location.pathname == '/profile') {
        console.log('Profile!')
    }
    else if (window.location.pathname == '/home') {
        const d = new Date();
        let clock = document.getElementById("clock");
        let month;
        switch (d.getMonth() + 1) {
            case 1:
                month = "January";
                break;
            case 2:
                month = "February";
                break;
            case 3:
                month = "March";
                break;
            case 4:
                month = "April";
                break;
            case 5:
                month = "May";
                break;
            case 6:
                month = "June";
                break;
            case 7:
                month = "July";
                break;
            case 8:
                month = "August";
                break;
            case 9:
                month = "September";
                break;
            case 10:
                month = "February";
                break;
            case 11:
                month = "February";
                break;
            case 12:
                month = "December";
                break;
            default:
                d.getMonth()
        }
        clock.innerHTML = d.getDate() + " " + month + " " + d.getFullYear();
    }
    else if (window.location.pathname == '/create-post') {
        const switch_button = document.getElementById("no-due");
        const day = document.getElementById("day-select");
        const month = document.getElementById("month-select");
        const year = document.getElementById("year-select");

        switch_button.onclick = function () {
            if (switch_button.checked === true){
                day.disabled = true;
                month.disabled = true;
                year.disabled = true;
                console.log('on');
            }
            else{
                day.disabled = false;
                month.disabled = false;
                year.disabled = false;
                console.log('off');
            }
        }
    }
    else if (window.location.pathname == '/pomodoro') {
        let interval;
        const time = document.getElementById('timer');
        const buttonStart = document.getElementById('start-button');
        const buttonReset = document.getElementById('reset-button');

        function resetClock() {
            let minutes = "25";
            let seconds = "00";
            time.innerHTML = minutes + ':' + seconds;
            time.classList.remove('text-success');
            time.classList.add('text-warning');
        }

        function countdown() {
            clearInterval(interval);
            interval = setInterval(function () {
                let timer = time.innerHTML;
                timer = timer.split(':');
                let minutes = timer[0];
                let seconds = timer[1];
                seconds -= 1;
                if (minutes < 0) return;
                else if (seconds < 0 && minutes != 0) {
                    minutes -= 1;
                    seconds = 59;
                } else if (seconds < 10 && length.seconds != 2) seconds = '0' + seconds;

                time.innerHTML = minutes + ':' + seconds;

                if (minutes == 0 && seconds == 0) clearInterval(interval);
            }, 1000);
        }

        buttonStart.onclick = function () {
            resetClock()
            time.classList.remove('text-warning');
            time.classList.add('text-success');
            countdown();
            buttonStart.disabled = true;
            buttonStart.classList.remove('btn-outline-success')
            buttonStart.classList.add('btn-outline-secondary')
        }

        buttonReset.onclick = function () {
            buttonStart.disabled = false;
            resetClock()
            clearInterval(interval);
            buttonStart.classList.add('btn-outline-success')
            buttonStart.classList.remove('btn-outline-secondary')
        }
    }
});

window.addEventListener('DOMContentLoaded', event => {
    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }
});

function charcountupdate(str) {
    let maxcount = 150;
    let lng = str.length;
    const charcount = document.getElementById("charcount");
	charcount.innerHTML = (maxcount-lng) + ' out of ' + maxcount + ' characters';
	if (lng >= (maxcount-100) && lng < (maxcount-50)){
	    charcount.classList.add('text-warning');
	    charcount.classList.remove('text-danger');
    }
	else if (lng >= (maxcount-50) && lng < maxcount){
	    charcount.classList.remove('text-warning');
	    charcount.classList.add('text-danger');
    }
	else if (lng == maxcount){
	    charcount.classList.remove('text-warning');
	    charcount.classList.add('text-danger');
	    charcount.innerHTML = 'MAX CHARACTER COUNT REACHED!';
    }
	else{
        charcount.classList.remove('text-warning');
        charcount.classList.remove('text-danger');
    }
}




