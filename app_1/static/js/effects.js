$(document).ready(function () {
  $("#you").novacancy({
    reblinkProbability: 0.1,
    blinkMin: 0.2,
    blinkMax: 0.6,
    loopMin: 8,
    loopMax: 10,
    color: "#ffffff",
    glow: ["0 0 80px #ffffff", "0 0 30px #eb3232", "0 0 6px #ff006e"],
  });

  $("#flix").novacancy({
    blink: 1,
    off: 1,
    color: "Red",
    glow: ["0 0 80px Red", "0 0 30px FireBrick", "0 0 6px DarkRed"],
  });
});
