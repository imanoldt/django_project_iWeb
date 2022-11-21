

const ctx_e = document.getElementById("myChart").getContext("2d");

new Chart(ctx_e, {
  type: "pie",
  data: {
    labels: ["LIKES", "DISLIKES"],
    datasets: [
      {
        label: "ESTADISTICA",
        data: [
          document.getElementById("likes").innerHTML,
          document.getElementById("dislikes").innerHTML,
        ],
        borderColor: "#1808a2",
        backgroundColor: "#d99e2b",
      },
    ],
  },
});
