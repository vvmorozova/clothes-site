// var xValues = [2019, 2020, 2021, 2022];
//
// new Chart("myChart", {
//   type: "line",
//   data: {
//     labels: xValues,
//     datasets: [{
//       data: [3, 5, 10, 28],
//       borderColor: "red",
//       fill: false
//     },]
//   },
//   options: {
//     legend: {display: false}
//   }
// });
//
// // plot2
//
// var xValues1 = [2019, 2020, 2021, 2022];
//
// new Chart("myChart1", {
//   type: "line",
//   data: {
//     labels: xValues1,
//     datasets: [{
//       label: "Продавец",
//         data: [500,1000,10000,30000],
//       borderColor: "#d9b99b",
//       fill: false
//     },{
//       label: "СММ",
//       data: [1000,2000,17000,35000],
//       borderColor: "rgb(170, 170, 170)",
//       fill: false
//     },{
//       label: "Лектор",
//       data: [0, 0,17000,40000],
//       borderColor: "rgba(7,7,7,0.5)",
//       fill: false
//     },{
//         label: "Бухгалтер",
//         data: [800,2100,20000,50000],
//         borderColor: "#964B00",
//         fill: false
//       }]
//   },
//   options: {
//     legend: {display: true}
//   }
// });
//
// // график
//
// var xValues2 = [2019, 2020, 2021, 2022];
//
// new Chart("myChart2", {
//   type: "line",
//   data: {
//     labels: xValues2,
//     datasets: [{
//       label: "Покупатели",
//         data: [3,10,200,5000],
//       borderColor: "#d9b99b",
//       fill: false
//     },{
//       label: "Посетители сайта",
//       data: [30,50,1000,30000],
//       borderColor: "rgb(170, 170, 170)",
//       fill: false
//     }]
//   },
//   options: {
//     legend: {display: true}
//   }
// });
//
// // plot 3
// var xValues = ["Мода", "Экология", "Бизнес", "Искусство", "Другое"];
// var yValues = [15, 20, 7, 14, 3];
// var barColors = ["red", "rgb(170, 170, 170)","#d9b99b","rgb(170, 170, 170)","brown"];
//
// new Chart("myChart3", {
//   type: "bar",
//   data: {
//     labels: xValues,
//     datasets: [{
//       backgroundColor: barColors,
//       data: yValues
//     }]
//   },
//   options: {
//     legend: {display: false},
//     title: {
//       display: true,
//       text: "Темы проведенных у нас лекций"
//     }
//   }
// });
//
// var xValues = [2019, 2020, 2021, 2022];
//
// new Chart("myChart4", {
//   type: "line",
//   data: {
//     labels: xValues,
//     datasets: [{
//       data: [3, 20, 1050, 10000],
//       borderColor: "red",
//       fill: false
//     },]
//   },
//   options: {
//     legend: {display: false}
//   }
// });
//
// var xValues = ["<18", "18-24", "25-34", "35-45", ">45"];
// var yValues = [55, 49, 44, 24, 15];
// var barColors = [
//   "#b91d47",
//   "brown",
//   "rgba(7,7,7,0.5)",
//   "#e8c3b9",
//   "rgb(170, 170, 170)"
// ];
//
// new Chart("myChart5", {
//   type: "pie",
//   data: {
//     labels: xValues,
//     datasets: [{
//       backgroundColor: barColors,
//       data: yValues
//     }]
//   },
//   options: {
//     title: {
//       display: true,
//       text: "Возраст покупателей"
//     }
//   }
// });
//
// var xValues1 = ["янв", "фев","мар", "апр","май", "июн","июл", "авг","сен", "окт","ноя", "дек"];
//
// new Chart("myChart6", {
//   type: "line",
//   data: {
//     labels: xValues1,
//     datasets: [{
//       label: "Верхняя одежда",
//         data: [15, 10, 6, 2, 1, 2, 1, 1, 3, 6, 7, 10],
//       borderColor: "#d9b99b",
//       fill: false
//     },{
//       label: "Штаны",
//       data: [10, 15, 16, 19,  15, 16, 19, 16, 16, 15, 16, 19],
//       borderColor: "rgb(170, 170, 170)",
//       fill: false
//     },{
//       label: "Обувь",
//       data: [ 19, 8, 17, 13, 16, 10, 15, 16, 19, 1, 2, 1],
//       borderColor: "rgba(7,7,7,0.5)",
//       fill: false
//     },{
//         label: "Худи",
//         data: [ 13, 16, 10, 15, 10, 15, 17, 13, 16, 10, 15, 8],
//         borderColor: "#964B00",
//         fill: false
//       },{
//         label: "Футболки",
//         data: [ 1, 2, 1, 10, 15, 16, 19, 20, 17, 13, 16, 10],
//         borderColor: "#b91d47",
//         fill: false
//       },{
//         label: "Аксессуары",
//         data: [14, 13, 16, 15, 13, 16, 15, 15, 16, 15, 15, 17],
//         borderColor: "#EE4B00",
//         fill: false
//       }]
//   },
//   options: {
//     legend: {display: true,
//         text: "Продажи в этом году"
//     }
//   }
// });
//
// var xValues = ["Верхняя одежда", "Штаны", "Обувь", "Худи", "Футболки", "Аксессуары"];
// var yValues = [55, 49, 44, 24, 15, 30];
// var barColors = [
//   "#b91d47",
//   "brown",
//   "rgba(7,7,7,0.5)",
//   "#e8c3b9",
//   "rgb(170, 170, 170)",
//   "black"
// ];
//
// new Chart("myChart7", {
//   type: "pie",
//   data: {
//     labels: xValues,
//     datasets: [{
//       backgroundColor: barColors,
//       data: yValues
//     }]
//   },
//   options: {
//     title: {
//       display: true,
//       text: "Что у нас покупают?"
//     }
//   }
// });
//
//
// var xValues = ["5*", "4*", "3*", "2*", "1*"];
// var yValues = [1055, 49, 15, 3, 1];
// var barColors = [
//   "#b91d47",
//   "brown",
//   "rgba(7,7,7,0.5)",
//   "#e8c3b9",
//   "rgb(170, 170, 170)",
// ];
//
// new Chart("myChart8", {
//   type: "doughnut",
//   data: {
//     labels: xValues,
//     datasets: [{
//       backgroundColor: barColors,
//       data: yValues
//     }]
//   },
//   options: {
//     title: {
//       display: true,
//       text: "Наши оценки на яндекс картах"
//     }
//   }
// });
//
// // plot 3
// var xValues = ["Россия", "Казахстан", "Беларусь", "Другое"];
// var yValues = [1500, 700, 560, 14];
// var barColors = ["rgb(170, 170, 170)","#d9b99b","rgba(7,7,7,0.5)","brown"];
//
// new Chart("myChart9", {
//   type: "bar",
//   data: {
//     labels: xValues,
//     datasets: [{
//       backgroundColor: barColors,
//       data: yValues
//     }]
//   },
//   options: {
//     legend: {display: false},
//     title: {
//       display: true,
//       text: "Заказы в другие страны"
//     }
//   }
// });

new Chart(document.getElementById("pie-chart"), {
    type: 'pie',
    data: {
      labels: ["Africa", "Asia", "Europe", "Latin America", "North America"],
      datasets: [{
        label: "Population (millions)",
        backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
        data: [2478,5267,734,784,433]
      }]
    },
    options: {
      title: {
        display: true,
        text: 'Predicted world population (millions) in 2050'
      }
    }
});
new Chart(document.getElementById("line-chart"), {
  type: 'line',
  data: {
    labels: [1500,1600,1700,1750,1800,1850,1900,1950,1999,2050],
    datasets: [{
        data: [86,114,106,106,107,111,133,221,783,2478],
        label: "Africa",
        borderColor: "#3e95cd",
        fill: false
      }, {
        data: [282,350,411,502,635,809,947,1402,3700,5267],
        label: "Asia",
        borderColor: "#8e5ea2",
        fill: false
      }, {
        data: [168,170,178,190,203,276,408,547,675,734],
        label: "Europe",
        borderColor: "#3cba9f",
        fill: false
      }, {
        data: [40,20,10,16,24,38,74,167,508,784],
        label: "Latin America",
        borderColor: "#e8c3b9",
        fill: false
      }, {
        data: [6,3,2,2,7,26,82,172,312,433],
        label: "North America",
        borderColor: "#c45850",
        fill: false
      }
    ]
  },
  options: {
    title: {
      display: true,
      text: 'World population per region (in millions)'
    }
  }
});