# Climate Analysis - Surf’s Up

Author: Rosie Gianan, gianr00@gmail.com

Build With: Python, SQLAlchemy ORM queries, Pandas, Matplotlib, Flasks API, Python, and JSON.

## Goals:
1.    Perform the climate analysis, data exploration and design of climate app using the data from climate database. 
2.    Perform an analysis using t-test to determine whether the difference in means, if any, is statistically significant. 
3.    Conduct an analysis using the historical data in the dataset, to find out what the temperature has previously been for a timeframe. 

## Solutions:
1.    Climate analysis and data exploration
-    Precipitation analysis  - design the query to analyze the precipitation data using the date and prcp for the previous 12 months of precipitation data. Save the result in Pandas DataFrame and plot the result in a bar chart.
Precipitation analysis chart:
<img src="images/precipitation_analysis.png" width="700>"> 

-    Station Analysis - design the query to calculate the lowest, highest, and average temperatures for the most active stations and for last 12 months of data. Using the most active station, design a query to retrieve the last 12 months of tobs (temperature observation data). Plot the result in a histogram chart.
### Station analysis chart:
<img src="images/station_analysis.png" width="700>

