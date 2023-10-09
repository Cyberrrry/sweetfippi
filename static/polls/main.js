
// Function to start the timer
function startTimer(duration, display) {
    var timer = duration;
    var minutes, seconds;

    var intervalId = setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (--timer < 0) {
            clearInterval(intervalId);
            display.textContent = "Expired";
        }
    }, 1000);
}

// Timer duration (in seconds)
var timerDuration = 60 * 10; // 10 minutes

// Start the timer
var display = document.getElementById("timer");
startTimer(timerDuration, display);