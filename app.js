// Select the submit button
var submit = d3.select("#submit");

submit.on("click", function() {

  // // Prevent the page from refreshing
    // d3.event.preventDefault();

  // Select the input element and get the raw HTML node
    var inputElement = d3.select("#video-list-input");

  // Get the value property of the input element
    var inputValue = inputElement.property("value");

    console.log(inputValue);
    console.log(people);


    var apiKey = "AIzaSyB82Fe14n8kBNsS1JGbawsh65TWr9L537U";

    /* global Plotly */
    var url =
      `http://gdata.youtube.com/feeds/api/standardfeeds/top_rated?v=2&alt=jsonc&api_key=${apiKey}`;



  
//   function buildPlot() {
//     d3.json(url).then(function(data) {
  
//       // Grab values from the data json object to build the plots
//       var name = data.dataset.name;
//       var stock = data.dataset.dataset_code;
//       var startDate = data.dataset.start_date;
//       var endDate = data.dataset.end_date;
//       var dates = unpack(data.dataset.data, 0);
//       var closingPrices = unpack(data.dataset.data, 1);
  
//       var trace1 = {
//         type: "scatter",
//         mode: "lines",
//         name: name,
//         x: dates,
//         y: closingPrices,
//         line: {
//           color: "#17BECF"
//         }
//       };
  
//       var data = [trace1];
  
//       var layout = {
//         title: `${stock} closing prices`,
//         xaxis: {
//           range: [startDate, endDate],
//           type: "date"
//         },
//         yaxis: {
//           autorange: true,
//           type: "linear"
//         }
//       };
  
//       Plotly.newPlot("plot", data, layout);
  
//     });
//   }
  
//   buildPlot();







// // Submit form with id function.
// function submit_by_id() {
//     var city = document.getElementById("city").value;
//     var radius = document.getElementById("radius").value;
//     }








// // Assign the data from `data.js` to a descriptive variable
// var people = data;

// // Select the submit button
// function submit_by_id() {
//     var city = document.getElementById("city").value;
//     var radius = document.getElementById("radius").value;

// submit.on("click", function() {

//   // Prevent the page from refreshing
//   d3.event.preventDefault();

//   // Select the input element and get the raw HTML node
//   var inputElement = d3.select("#patient-form-input");

//   // Get the value property of the input element
//   var inputValue = inputElement.property("value");

//   console.log(inputValue);
//   console.log(people);

// //   var filteredData = people.filter(person => person.bloodType === inputValue);

// //   console.log(filteredData);

//   // First, create an array with just the age values
//   var ages = filteredData.map(person => person.age);

//   // Next, use math.js to calculate the mean, median, mode, var, and std of the ages
//   var mean = math.mean(ages);
//   var median = math.median(ages);
//   var mode = math.mode(ages);
//   var variance = math.var(ages);
//   var standardDeviation = math.std(ages);

//   // Finally, add the summary stats to the `ul` tag
//   d3.select(".summary")
//     .append("li").text(`Mean: ${mean}`)
//     .append("li").text(`Median: ${median}`)
//     .append("li").text(`Mode: ${mode}`)
//     .append("li").text(`Variance: ${variance}`)
//     .append("li").text(`Standard Deviation: ${standardDeviation}`);
// });