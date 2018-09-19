// Money_of_the_Future project
// Auhor: Inna Baloyan

var stock = "MSFT";

function buildPlot(stock) {

  // Get stock data by using json in app routes     
  var url = `http://127.0.0.1:5000/MSFTY`

  console.log( "URL", url)

  d3.json(url).then(function(data) {

    // Grab values from the response json object to build the plots
    // var name = data.dataset.name;
    // var stock = data.dataset.dataset_code;
    // var startDate = data.dataset.start_date;
    // var endDate = data.dataset.end_date;
    // var dates = unpack(data.dataset.data, 0);
    // var closingPrices = unpack(data.dataset.data, 1);

    var name = "MICROSOFT";
    
    var startDate = "1986-03-31";
    var endDate = "2018-08-31";
    var dates = data.Dates;
    var PercentChanges = data.Change;

    console.log( "Data", data)

    var trace1 = {
      type: "scatter",
      mode: "lines",
      name: name,
      x: dates,
      y: PercentChanges,
      line: {
        color: "#17BECF"
      }
    };

    var data = [trace1];

    var layout = {
      title: "Microsoft, Apple, Intel, IBM Stock Fluctuation over Security Life Span",
      xaxis: {
        range: [startDate, endDate],
        type: "date"
      },
      yaxis: {
        autorange: true,
        type: "linear"
        // type: "bar"
      }
    };

    // Build the plot based on user entered Stock option 
    
    // Project Stock data: AAPL("Apple"),MSFT("Microsoft"),AMZN-("Amazon"), GOOGL("Google")   
    // The Stock indicator could be hardcoded in each of 4 js files, for exp, build_AAPL_plot.js,
    // inserted into index.html for the page ( route ) and all 4 market data based plots 
    // could be build. The routes could be for the years: from 2010 to 2018. On the page 
    // the comparison to Bitcoin data will be clear seen for the particular year. 
    // In this case the date range would be passed as a function parameter from main app.py script 
    // or by some other means.
    Plotly.newPlot("plot", data, layout);

  });
}

// // Add event listener for submit button
// d3.select("#submit").on("click", handleSubmit);

  // Build the plot with the new stock
  buildPlot("MSFT");
