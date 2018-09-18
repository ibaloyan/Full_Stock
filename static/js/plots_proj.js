// Money_of_the_Future project
// Auhor: Inna Baloyan

var stock = "MSFT";

function buildPlot(stock) {

  // Get stock data by using json in app routes     
  var url1 = `http://127.0.0.1:5000/MSFTY`

  console.log( "URL", url1)

  d3.json(url1).then(function(data1) {

    // Grab values from the response json object to build the plots
    // var name = data.dataset.name;
    // var stock = data.dataset.dataset_code;
    // var startDate = data.dataset.start_date;
    // var endDate = data.dataset.end_date;
    // var dates = unpack(data.dataset.data, 0);
    // var closingPrices = unpack(data.dataset.data, 1);

    var name = "MICROSOFT"; // for the legend on the side of the graph
    var labels = data1.title;
    var startDate = "1986-03-31";
    var endDate = "2018-08-31";
    var dates = data1.Dates;
    var PercentChanges = data1.Change;

    console.log( "Data", data1)

    var trace1 = {
      type: "scatter",
      mode: "lines",
      name: name,
      x: dates,
      y: PercentChanges,
      line: {
        color: "#17BECF",
        width: 2
      },
      font: {
        family: 'Arial',
        size: 16,
        color: 'black'
      },
      text: labels
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
  buildPlot("MSFT");
