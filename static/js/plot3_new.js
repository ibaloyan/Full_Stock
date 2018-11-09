// Full Stock project
// Author: Inna Baloyan
// Project Stock data: AAPL("Apple"), MSFT("Microsoft"), Intel("INTC"), IBM("IBM")   

//////////////////////////////////////////////////////////////////
var my_data1 = [];
var my_data2 = [];
var my_data3 = [];
var my_data4 = [];


// Get stock data by using json in app routes     
var url3 = `/IBMY`
console.log( "URL3", url3)
var url1 = `/MSFTY`
console.log( "URL1", url1)
var url2 = `/applY`
console.log( "URL2", url2) 
var url4 = `/IntelY`
console.log( "URL4", url4)


// Build the plot with the new stock - "IBM"
d3.json(url3).then(function(data3) {

    var name3 = "IBM"; // for the legend on the side of the graph
    var labels3 = data3.title;
    var startDate = "1962-01-31";
    var endDate = "2018-11-30";
    var dates3 = data3.Dates;
    // var dates3 = data3.DatesN;
    var close3 = data3.Close;
    console.log( "Data3", data3)

    var trace3 = {
      type: "scatter",
      mode: "lines",
      name: name3,
      x: dates3,
      y: close3,
      line: {
        color: "green",
        width: 3
      },
      font: {
        family: 'Arial',
        size: 16,
        color: 'black'
      },
      text: labels3
    };

    my_data3 = [trace3];
    console.log( "my_data3", my_data3)


    var layout = {
      showlegend: true,
      // height: 1200,
      // width: 1200,
      title: "Microsoft, Apple, Intel, IBM Stocks Closing Prices over Security Life Span",
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
        title: "ClosingPrices",
        autorange: true,
        type: "linear"
      }
    };
  
    // Create new Plot1 with IBM Data
    Plotly.newPlot("plot3", my_data3, layout);

    //////////////////////////////////////////////////////////////////


// Add MICROSOFT data to the Plot
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
    // var startDate = "1980-12-31";
    // var endDate = "2018-09-30";
    var dates1 = data1.Dates;
    // var dates1 = data1.DatesN;
    var close1 = data1.Close;
    console.log( "Data1", data1)

    var trace1 = {
      type: "scatter",
      mode: "lines",
      name: name1,
      x: dates1,
      y: close1,
      line: {
        color: "#17BECF", // bluish color
        width: 3
      },
      font: {
        family: 'Arial',
        size: 16,
        color: 'black'
      },
      text: labels1
    };

    my_data1 = [trace1];
    console.log( "my_data1", my_data1)

     
    // Update Plot1 with Microsoft Data
    Plotly.addTraces("plot3", my_data1);

//////////////////////////////////////////////////////////
// Add Apple Data to the Plot

d3.json(url2).then(function(data2) {

    var name2 = "Apple"; // for the legend on the side of the graph
    var labels2 = data2.title;
    // var startDate = "1980-12-31";
    // var endDate = "2018-09-30";
    var dates2 = data2.Dates;
    // var dates2 = data2.DatesN;
    var close2 = data2.Close;
    console.log( "Data2", data2)

    var trace2 = {
      type: "scatter", 
      mode: "lines",
      name: name2,
      x: dates2,
      y: close2,
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

    my_data2 = [trace2];
    console.log( "my_data2", my_data2)


    // Update Plot1 with Apple Data
    Plotly.addTraces("plot3", my_data2);

    // ///////////////////////////////////////////////////////
// Add Intel Data to the Plot

  d3.json(url4).then(function(data4) {

    var name4 = "Intel"; // for the legend on the side of the graph
    var labels4 = data4.title;
    // var startDate = "1980-12-31";
    // var endDate = "2018-09-30";
    var dates4 = data4.Dates;
    // var dates4 = data4.DatesN;
    var close4 = data4.Close;
    // for( var i = 0 ; i < PercentChanges4.length ; i++ ) {
    //   PercentChanges4[i] = PercentChanges4[i] + "%";
    //   console.log ( "PercentChanges4", PercentChanges4)
    // };
    console.log( "Data4", data4)

    var trace4 = {
      type: "scatter",
      mode: "lines",
      name: name4,
      x: dates4,
      y: close4,
      line: {
        color: "gold",
        width: 2
      },
      font: {
        family: 'Arial',
        size: 16,
        color: 'black'
      },
      text: labels4
    };

    my_data4 = [trace4];
    console.log( "my_data4", my_data4)

    // Update Plot1 with Intel Data
    Plotly.addTraces("plot3", my_data4);

  }); //URL4

  }); //URL2

  }); //URL1

  }); //URL3