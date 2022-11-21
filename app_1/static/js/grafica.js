Chart.defaults.color='#fff'
Chart.defaults.fontSize=40 /*NO LO ESTA COGIENDO */



const getColors = opacity => {
  const colors = ['#7448c2','#d99e2b']
  return colors.map(color => opacity ? `${color + opacity}` : color)
}

const ctx = document.getElementById('myChart').getContext("2d");   
new Chart(ctx, {
type: 'pie',
data: {
  labels: ['LIKES', 'DISLIKES'],
  datasets: [
      {
          label: 'ESTADISTICA',
          data: [document.getElementById("likes").innerHTML, document.getElementById("dislikes").innerHTML],
          borderColor: getColors(),
          backgroundColor:getColors(20),
        },  
  ]

},
options: {
  scales: {
      yAxes:[{
          ticks:{
              beginAtZero:true
              
          }
      }]
     
  },
  /*
  plugins:{
    legend:{position:'left'}
  }
  */

},
});
