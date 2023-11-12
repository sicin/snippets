const daysElFirst = document.getElementById("days-first");
const daysElSecond = document.getElementById("days-second");
const hoursElFirst = document.getElementById("hours-first");
const hoursElSecond = document.getElementById("hours-second");
const minutesElFirst = document.getElementById("minutes-first");
const minutesElSecond = document.getElementById("minutes-second");
const secondsElFirst = document.getElementById("seconds-first");
const secondsElSecond = document.getElementById("seconds-second");

const hoursParent = hoursElFirst.parentNode.parentNode.parentNode;
const minutesParent = minutesElFirst.parentNode.parentNode.parentNode;
const secondsParent = secondsElFirst.parentNode.parentNode.parentNode;

const end = "November 29, 2023 12:00:00";
let days;
let hours;
let minutes;
let seconds;

let currentOrangedPart = "days";

function makeOrange() {
  if (days === 0) {
    currentOrangedPart = "hours";
    hoursParent.classList.add("timer-elapsed-color");
    if (hours === 0) {
      currentOrangedPart = "minutes";
      minutesParent.classList.add("timer-elapsed-color");
      if (minutes === 0) {
        currentOrangedPart = "seconds";
        secondsParent.classList.add("timer-elapsed-color");
      }
    }
  }
}

function countdown() {
  const endDate = new Date(end);
  const currentDate = new Date();

  const totalSeconds = (endDate - currentDate) / 1000;

  days = Math.floor(totalSeconds / 3600 / 24);
  hours = Math.floor(totalSeconds / 3600) % 24;
  minutes = Math.floor(totalSeconds / 60) % 60;
  seconds = Math.floor(totalSeconds) % 60;
  if (days < 0) {
    days = 0;
    hours = 0;
    minutes = 0;
    seconds = 0;
  }

  const formattedDays = formatTime(days);
  const formattedHours = formatTime(hours);
  const formattedMinutes = formatTime(minutes);
  const formattedSeconds = formatTime(seconds);

  daysElFirst.innerHTML = formattedDays.firstDigit;
  daysElSecond.innerHTML = formattedDays.secondDigit;
  hoursElFirst.innerHTML = formattedHours.firstDigit;
  hoursElSecond.innerHTML = formattedHours.secondDigit;
  minutesElFirst.innerHTML = formattedMinutes.firstDigit;
  minutesElSecond.innerHTML = formattedMinutes.secondDigit;
  secondsElFirst.innerHTML = formattedSeconds.firstDigit;
  secondsElSecond.innerHTML = formattedSeconds.secondDigit;

  switch (currentOrangedPart) {
    case "days":
      if (days == 0) {
        currentOrangedPart = "hours";
        makeOrange();
      }
      break;
    case "hours":
      if (hours == 0) {
        currentOrangedPart = "minutes";
        makeOrange();
      }
      break;
    case "minutes":
      if (minutes == 0) {
        currentOrangedPart = "seconds";
        makeOrange();
      }
      break;
    case "seconds":
      makeOrange();
      break;
  }
}

function formatTime(time) {
  secondDigit = time % 10;
  firstDigit = (time - secondDigit) / 10;
  return {
    firstDigit,
    secondDigit,
  };
}

countdown();

setInterval(countdown, 1000);
