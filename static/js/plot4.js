// Money_of_the_Future project
// Auhor: Inna Baloyan
// Project Stock data: AAPL("Apple"), MSFT("Microsoft"), Intel("INTC"), IBM("IBM")   
// Plot Volume data for all 4 securities

//////////////////////////////////////////////////////////////////

// Utilize Chart.js library for building Grouped Bar Chart for Stock Quarters

var IBM_Q = [];
var MSTFY_Q = [];
var Apple_Q = [];
var Intel_Q = [];

// Get stock quarter data by using json in app routes     

var url3 = `http://127.0.0.1:5000/IBMY`
console.log( "URL3", url3)
d3.json(url3).then(function(data3) {
    IBM_Q = data3.Qs
    console.log( "IBM_Q", IBM_Q)


var url1 = `http://127.0.0.1:5000/MSFTY`
console.log( "URL1", url1)
d3.json(url1).then(function(data1) {
    MSTFY_Q = data1.Qs
    console.log( "MSTFY_Q", MSTFY_Q)


var url2 = `http://127.0.0.1:5000/applY`
console.log( "URL2", url2)
d3.json(url2).then(function(data2) {
    Apple_Q = data2.Qs
    console.log( "Apple_Q", Apple_Q)


var url4 = `http://127.0.0.1:5000/IntelY`
console.log( "URL4", url4)
d3.json(url4).then(function(data4) {
    Intel_Q = data4.Qs
    console.log( "Intel_Q", Intel_Q)


console.log( "IBM_Q later ", IBM_Q)
console.log( "MSTFY_Q later", MSTFY_Q)
console.log( "Apple_Q later", Apple_Q)
console.log( "Intel_Q later", Intel_Q)

    new Chart(document.getElementById("bar-chart-grouped"), {
        type: 'bar',
        data: {
          labels: ["1st Quarter", "2nd Quarter", "3rd Quarter", "4th Quarter"],
          datasets: [
            {
              label: "IBM",
              backgroundColor: "green", 
              data: IBM_Q
            }, {
              label: "Apple",
              backgroundColor: "red", 
              data: Apple_Q
            },
            {
                label: "Microsoft",
                backgroundColor: "#17BECF", 
                data: MSTFY_Q
            },
            {
                label: "Intel",
                backgroundColor: "gold", 
                data: Intel_Q
            }
          ]
        },
        options: {
          title: {
            display: true,
            text: "Microsoft, Apple, Intel, IBM Percent Changes over Quarter of Security Life Span"
          }
        }
    });

}); //URL3

}); //URL1

}); //URL2

}); //URL4