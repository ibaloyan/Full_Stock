Full-Stock
     
Building JavaScript plots [Plotly, Chart] based on life span stock data from Quandl API for Apple, IBM, Microsoft and Intel.  
Technologies => JavaScript, Plotly, Chart.js, CSS, Heroku deployment https://full-stock-ib.herokuapp.com
     
     Hypothesis:Securities become more stable the longer they remain public in the stock market.
     Process:We gathered data of 4 successful technology stocks (IBM, Apple, Microsoft and Intel) that have been in the market for at least 30 years from "Quandl," which is a marketplace for financial, economic and alternative data.
     After that, we cleaned, and munged the data to come up with the "Stocks Percent Change MoM over the Securities Life Span","Stocks Volume Change MoM over the Security's Life Span","Stocks Closing Prices MoM over the Security's Life Span", and "Stocks Percent Change over each quater of the Securitiy's Life Span"; these values were used to plot charts.

     For all 4 Charts, you can choose to look at each stock separately, or at 2 or more at the same time. The legend on the right is clickable. 
     If you choose to eliminate any stock, for example Apple, just click on the Aple on the right side of the chart, and Apple plot will disappear. When you hover with a mouse over the data points of each chart, it displays the label, the tooltip, with the monthly data for each active stock.