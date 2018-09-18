// Money_of_the_Future project
// Auhor: Inna Baloyan
// Project Stock data: AAPL("Apple"), MSFT("Microsoft"), Intel("Intel"), IBM("IBM")   

var startDate = "1980-12-31";
var endDate = "2018-08-31";
var data12 = [];
// var dates = [];
// var layout = {};

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// build Microsoft stock plot
  // Get stock data by using json in app routes     
  var url1 = `http://127.0.0.1:5000/MSFTY`

  console.log( "URL1", url1)

  d3.json(url1).then(async function(data1) {

    // Grab values from the response json object to build the plots
    // var name = data.dataset.name;
    // var stock = data.dataset.dataset_code;
    // var startDate = data.dataset.start_date;
    // var endDate = data.dataset.end_date;
    // var dates = unpack(data.dataset.data, 0);
    // var closingPrices = unpack(data.dataset.data, 1);

    var name1 = "Microsoft"; // for the legend on the side of the graph
    var labels1 = data1.title;
    // var startDate = "1980-12-31";
    // var endDate = "2018-08-31";
    var dates1 = data1.Dates;
    var PercentChanges1 = data1.Change;

    console.log( "Data1", data1)
    await sleep(5000);

    var trace1 = {
      type: "scatter",
      mode: "lines",
      name: name1,
      x: dates1,
      y: PercentChanges1,
      line: {
        color: "#17BECF",
        width: 2
      },
      font: {
        family: 'Arial',
        size: 16,
        color: 'black'
      },
      text: labels1
    };

    data12[0] = trace1;
  });
//////////////////////////////////////////////////////////////
// build APPL stock plot

 // Get stock data by using json in app routes     
 var url2 = `http://127.0.0.1:5000/applY`

 console.log( "URL2", url2)

 d3.json(url2).then(async function(data2) {

   var name2 = "Apple"; // for the legend on the side of the graph
   var labels2 = data2.title;

   var dates2 = data2.Dates;
   var PercentChanges2 = data2.Change;

   console.log( "Data2", data2)
   await sleep(5000);

   var trace2 = {
     type: "scatter",
     mode: "lines",
     name: name2,
     x: dates2,
     y: PercentChanges2,
     line: {
       color: 'rgb(219,64,82)',
       width: 2
     },
     font: {
       family: 'Arial',
       size: 16,
       color: 'black'
     },
     text: labels2
   };

   data12[1] = trace2;

});

//////////////////////////////////////////////////////////////
var layout = {
      showlegend: true,
      // height: 600,
      // width: 900,
      title: "Microsoft, Apple, Intel, IBM Stocks Percent Change over Security Life Span",
      xaxis: {
        title: "Securities Life Span",
        font: {
          family: 'Arial',
          size: 16,
          color: 'black'
          },
        range: [startDate, endDate],
        type: "date"
      },
      yaxis: {
        title: "Percent Change",
        autorange: true,
        type: "linear"
      }
};

// data12 = [trace1, trace2];
console.log( "Data12", data12);
console.log( "Layout", layout);
  
// Project Stock data: AAPL("Apple"), MSFT("Microsoft"), Intel("Intel"), IBM("IBM") 
Plotly.newPlot("plot1", data12[0], layout);  
// Plotly.newPlot("plot1", data12, layout);
console.log( "the end " )