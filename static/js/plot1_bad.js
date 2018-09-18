// Money_of_the_Future project
// Auhor: Inna Baloyan
// Project Stock data: AAPL("Apple"), MSFT("Microsoft"), Intel("Intel"), IBM("IBM")   

// Build MICROSOFT Plot
var stock1 = "MSFT";

function buildPlot1(stock1) {

  // Get stock data by using json in app routes     
  var url1 = `http://127.0.0.1:5000/MSFTY`

  console.log( "URL1", url1)

  d3.json(url1).then(function(data1) {

    // Grab values from the response json object to build the plots
    // var name = data.dataset.name;
    // var stock = data.dataset.dataset_code;
    // var startDate = data.dataset.start_date;
    // var endDate = data.dataset.end_date;
    // var dates = unpack(data.dataset.data, 0);
    // var closingPrices = unpack(data.dataset.data, 1);

    var name1 = "Microsoft"; // for the legend on the side of the graph
    var labels1 = data1.title;
    var startDate = "1980-12-31";
    var endDate = "2018-08-31";
    var dates1 = data1.Dates;
    var PercentChanges1 = data1.Change;

    console.log( "Data1", data1)

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

    var data1 = [trace1];

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
  // };
     
    // Project Stock data: AAPL("Apple"),MSFT("Microsoft"),AMZN-("Amazon"), GOOGL("Google")   
       Plotly.newPlot("plot1", data1, layout);

  });
}

  // Build the plot with the new stock
  buildPlot1("MSFT");

///////////////////////////////////////////////////////
// Build Apple Plot

var stock2 = "AAPL";

function buildPlot2(stock2) {

  // Get stock data by using json in app routes     
  var url2 = `http://127.0.0.1:5000/applY`

  console.log( "URL2", url2)

  d3.json(url2).then(function(data2) {

    var name2 = "Apple"; // for the legend on the side of the graph
    var labels2 = data2.title;
    var startDate = "1980-12-31";
    var endDate = "2018-08-31";
    var dates2 = data2.Dates;
    var PercentChanges2 = data2.Change;

    console.log( "Data2", data2)

    var trace2 = {
      type: "scatter",
      mode: "lines",
      name: name2,
      x: dates2,
      y: PercentChanges2,
      line: {
        color: "red",
        width: 2
      },
      font: {
        family: 'Arial',
        size: 16,
        color: 'black'
      },
      text: labels2
    };

    var data2 = [trace2];

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
  // };
     
       Plotly.newPlot("plot1", data2, layout);

  });
}

  // Build the plot with the new stock
  buildPlot2("AAPL");

 
