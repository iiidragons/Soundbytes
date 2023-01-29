let audio = null

let progress = document.getElementById("progress")
let progressBar = document.getElementById("progress-bar")
let currTime = document.getElementById("curr-time")
let length = document.getElementById("length")



function playAudio() {
    try {
        if (audio == null) {
            audio = document.getElementById("audioPlayer");
            setInterval(updateCurrentSecond, 1000)
            setTimeout(updateTotalDuration, 1000)
            setTimeout(initVolume, 1000)
        }
        if (audio.paused) {
            audio.play()
        } else {
            audio.pause()
        }
    } catch {
        console.log("An error occurred while playing the audio.")
    }
}

function rewind() {
    if (audio != null) {
        audio.currentTime -= 10
    }
    updateCurrentSecond()
}

function forward() {
    if (audio != null) {
        audio.currentTime += 10
    }
    updateCurrentSecond()
}

function updateCurrentSecond() {
    let elapsed = (audio.currentTime / audio.duration) * 100
    progress.setAttribute("aria-valuenow", elapsed)
    progressBar.style.width = elapsed + "%"
    let elapsedMin = Math.floor(audio.currentTime / 60)
    let elapsedSec = Math.floor(audio.currentTime % 60)
    if (elapsedSec < 10) {
        currTime.innerHTML = elapsedMin + ":0" + elapsedSec
    } else {
        currTime.innerHTML = elapsedMin + ":" + elapsedSec
    }
}

function updateTotalDuration() {
    total = audio.duration
    totalMin = Math.floor(total / 60)
    totalSec = Math.floor(total % 60)
    if (totalSec < 10) {
        length.innerHTML = totalMin + ":0" + totalSec
    } else {
        length.innerHTML = totalMin + ":" + totalSec
    }
}

// VOLUME CONTROL

let volumeButton = document.getElementById("volume-button")
let volumeBar = document.getElementById("volume-bar")
let volumeLevel = document.getElementById("volume-level")

// Sets the initial volume level
function initVolume() {
    volumeLevel.style.width = (audio.volume * 100) + "%"
}

// Add event listener to toggle the volume bar when the volume button is clicked
volumeButton.addEventListener("mouseover", function() {
    volumeBar.classList.toggle("active")
})

// Add event listener to hide the volume bar when it loses focus
document.addEventListener("mousedown", function(event) {
    if (!event.target.closest("#volume-control")) {
        volumeBar.classList.remove("active")
    }
})

// Add event listener to change the volume level when the user clicks on the volume bar
volumeBar.addEventListener("click", function(event) {
    try {
        let x = event.clientX - volumeBar.getBoundingClientRect().left
        let percent = x / volumeBar.clientWidth
        audio.volume = percent
        volumeLevel.style.width = (percent * 100) + "%"
    } catch {
        volumeBar.classList.remove("active")
        console.log("An error occurred while trying to use the volume control.")
    }
})

// Add event listener to change the volume level when the user drags the volume level
volumeLevel.addEventListener("mousedown", function(event) {
    try {
        let initialX = event.clientX
        let initialWidth = volumeLevel.clientWidth

        function move(event) {
            let x = event.clientX
            let diff = x - initialX
            let percent = (initialWidth + diff) / volumeBar.clientWidth
            if (percent >= 0 && percent <= 1) {
                audio.volume = percent
                volumeLevel.style.width = (percent * 100) + "%"
            }
        }

        document.addEventListener("mousemove", move)

        document.addEventListener("mouseup", function() {
            document.removeEventListener("mousemove", move)
        })
    } catch {
        volumeBar.classList.remove("active")
        console.log("An error occurred while trying to use the volume control.")
    }
})