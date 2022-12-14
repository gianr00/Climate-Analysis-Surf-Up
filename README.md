# Climate Analysis - Surf’s Up

Author: Rosie Gianan, gianr00@gmail.com

Build with: Python, SQLAlchemy ORM queries, Pandas, Matplotlib, Flasks API, Python, csv files, sqlite, Jupyter notebook

## Objective:
1.  Perform the climate analysis, data exploration and design of climate app using the data from climate database. 
2.  Find out if there’s a meaningful difference between the temperatures in, for example, June and December.
3.  Conduct an analysis using the historical data in the dataset, to find out what the temperature has previously been for a timeframe. 

## Solution:
1.    Climate analysis and data exploration
-   Precipitation analysis  - design the query to analyze the precipitation data using the date and prcp for the previous 12 months of precipitation data. Save the result in Pandas DataFrame and plot the result in a bar chart.

Precipitation analysis chart:

<img src="images/precipitation_analysis.png" width="400"> 

-   Station Analysis - design the query to calculate the lowest, highest, and average temperatures for the most active stations and for last 12 months of data. Using the most active station, design a query to retrieve the last 12 months of tobs (temperature observation data). Plot the result in a histogram chart.

Station analysis chart:

<img src="images/station_analysis.png" width="400">

2.    Climate app  – Design a Flask API to display the climate data using the following route:

<img src="images/app_all_routes.png" width="600"> 

-    Precipitation route - Returns the jsonified precipitation data for the last year in the database with the date as the key and the value as the precipitation
<img src="images/app_route_precipitation.png" width="600"> 

-    Stations route - Returns jsonified data of all of the stations in the database
<img src="images/app_route_stations.png" width="600">

-    Tobs route  - Returns the jsonified data for the most active station for the last year of data
<img src="images/app_route_tobs.png" width="600">

-    Dynamic route using the start date - Route accepts start date  as a parameter from the URL. Returns the min, max, and average temperatures calculated from the given start date to the end of the dataset
<img src="images/app_route_beg_date.png" width="600">

-    Dynamic route using  the start and end date - Route accepts the start and end dates as parameters from the URL. Returns the min, max, and average temperatures calculated from the given start date to the given end date
 <img src="images/app_route_beg_end_date.png" width="600">

3.  Perform an analysis to find out if there’s a meaningful difference between the temperatures in, for example, June and December. Using t-test to determine whether the difference in means, if any, is statistically significant. 

<img src="images/t-test_analysis.png" width="900"> 

4.  Conduct an analysis using the previous year data in the dataset, to find out what the temperature has previously been for a timeframe. Find the average temperature and daily temperature. Plot the results.

Average Temperature: 

<img src="images/average_temperature.png" width="200"> 

Daily Temperature:

<img src="images/daily_temperature.png" width="400"> 



