$.getScript("ajax/test.js", function () {
  alert("Load was performed.");
});

$(document).ready(function () {
  setTimeout(function () {
    $("body").removeClass("cut");
    $("#pulsar").addClass("hide");
    $("#preloader").addClass("moveUp");
  }, 1000);
});
