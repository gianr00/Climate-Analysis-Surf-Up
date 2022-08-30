Module 10 Challenge – SQLAlchemy: Surf’s Up

Objective:

This challenge will apply the skills learned in Module 10 –SQLAlchemy and Flask API. This challenge consists of two parts to perform climate analysis, data exploration and design of climate app using the data from climate database. This utilizes the skills in Python, SQLAlchemy ORM queries, Pandas, Matplotlib, Flasks API, Python, and JSON.

This also include 2 bonus challenges to more perform analysis using t-test to determine whether the difference in means, if any, is statistically significant. This also conduct an analysis using the historical data in the dataset, to find out what the temperature has previously been for a timeframe. 

Project Details:

Part 1: Climate Analysis and Exploration
1.    Precipitation Analysis 
-    Retrieve the date and prcp for the previous 12 months of precipitation data
-    Save the result in Pandas DataFrame and plot the result using the DataFrame `plot` method
2.    Station Analysis 
Design a query to calculate the lowest, highest, and average temperatures for the most active stations and for last 12 months of data

Part 2: Design Your Climate App – Design a Flask API to display the climate data:
1.    Precipitation route
-    Returns the jsonified precipitation data for the last year in the database
-    Returns the jsonified data with the date as the key and the value as the precipitation
2.    Stations route 
-    Returns jsonified data of all of the stations in the database
3.    Tobs route  
-    Returns the jsonified data for the most active station for the last year of data
4.    Dynamic route using the start date 
-    Route accepts start date  as a parameter from the URL 
-    Returns the min, max, and average temperatures calculated from the given start date to the end of the dataset
5.    Dynamic route using  the start and end date 
-    Route accepts the start and end dates as parameters from the URL
-    Returns the min, max, and average temperatures calculated from the given start date to the given end date

Bonus Challenge:
1.    Trip Temperature Analysis I 
    Uses an unpaired t-test to compare the means of the temperature in June and December.

2.    Trip Temperature Analysis II
-    Calculate  the min, max, and average temperatures for a date range 
-    Uses the calculated temperatures to generate a bar chart with an error bar.
-    Calculates the min, max, and average temperatures for each day of their trip and appends them to a list.
-    Creates a DataFrame from the list and generates a stacked line chart plotting the min, max, and average temps for each day of the trip 

Project Submission:
Save the files in GitHub repository called “sqlalchemy-challenge”.  Submit the shareable link of the GitHub repository in bootcamp spot site.
1.    The jupyter notebooks and `app.py` for the main scripts to run the analysis
2.    README file
