/**
 * Helper function to select stock data
 * Returns an array of values
 * @param {array} rows
 * @param {integer} index
 * index 0 - Date
 * index 1 - Open
 * index 2 - High
 * index 3 - Low
 * index 4 - Volume
 */
function unpack(rows, index) {
  return rows.map(function(row) {
    return row[index];
  });
}

// Submit Button handler
function handleSubmit() {
  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Select the input value from the form
  var stock = d3.select("#stockInput").node().value;
  console.log(stock);

  // clear the input value
  d3.select("#stockInput").node().value = "";

  // Build the plot with the new stock
  buildPlot(stock);
}

function buildPlot(stock) {
  var apiKey = "V2vzspYSYL8eenGuq8uF";

  // Get stock data chosen by user in the date range [ January 1,2010 - August 31,218]
  var url = `https://www.quandl.com/api/v3/datasets/WIKI/${stock}.json?start_date=2010-01-01&end_date=2018-08-31&api_key=${apiKey}`;

  d3.json(url).then(function(data) {

    // Grab values from the response json object to build the plots
    var name = data.dataset.name;
    var stock = data.dataset.dataset_code;
    var startDate = data.dataset.start_date;
    var endDate = data.dataset.end_date;
    var dates = unpack(data.dataset.data, 0);
    var closingPrices = unpack(data.dataset.data, 1);

    var trace1 = {
      type: "scatter",
      mode: "lines",
      name: name,
      x: dates,
      y: closingPrices,
      line: {
        color: "#17BECF"
      }
    };

    var data = [trace1];

    var layout = {
      title: `${stock} closing prices`,
      xaxis: {
        range: [startDate, endDate],
        type: "date"
      },
      yaxis: {
        autorange: true,
        type: "linear"
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

// Add event listener for submit button
d3.select("#submit").on("click", handleSubmit);
