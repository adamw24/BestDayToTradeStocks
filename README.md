# BestTimeToTradeStocks
Can be used to naively determine which day is the best to buy and which day is the best to sell certain stocks.
It averages the closing price for each weekday and finds the percent gain with respect to Monday.
There are two was of obtaining the data: downloading a CSV file from Yahoo Finance or using pandas.get_data_yahoo().
Downloading the data is inefficient and requires the user to do it manually when they want a different time interval or stock.
Using the pandas function has slow execution time but is much more streamlined and does not require the user to manually download the data.
