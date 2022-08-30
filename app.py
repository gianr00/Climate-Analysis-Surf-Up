import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"--------------------<br/>"
        f"Available Routes:<br/>"
        f"--------------------<br/>"
        f"Precipitation for the last 12 months                           :   /api/v1.0/precipitation<br/>"
        f"List of all the stations                                       :   /api/v1.0/stations<br/>"
        f"Temperatures for the most active station for the last 12 months:   /api/v1.0/tobs<br/>"
        f"Temperature statatistics for start date                        :   /api/v1.0/yyyy-mm-dd<br/>"
        f"Temperature statatistics for start date to end date            :   /api/v1.0/beg_yyyy-mm-dd/end_yyyy-mm-dd"
    )      

#====================================================================================
# Returns the jsonified precipitation data for the last year in the database
# Returns json with the date as the key and the value as the precipitation
#====================================================================================
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    #--------------------------------------------------------------------
    # Retrieve the recent and latest date
    #--------------------------------------------------------------------
    query_result_recent_date  = session.query(Measurement.date).\
                                     order_by(Measurement.date.desc()).limit(1)
                           
    # Extract the content of SQLAlchemy row object
    for row in query_result_recent_date :
        
        # Convert date str to date format
        recent_date = dt.datetime.strptime(row[0], '%Y-%m-%d')  

    # Calculate the date one year from the last date in data set.
    date_last_12_months = dt.datetime( recent_date.year -1 \
                                     , recent_date.month \
                                     , recent_date.day)

    # Extract the yyyy-mm-dd from the date time and save as string
    date_prev_year = dt.datetime.strftime(date_last_12_months, '%Y-%m-%d')

    """Return a list of all precipitation"""
    #--------------------------------------------------------------------
    # Retrieve the precipitation data for the last year in the database
    #--------------------------------------------------------------------
    sel     = [Measurement.date, Measurement.prcp]
    
    results = session.query(*sel).filter(Measurement.date >= date_prev_year).all()
    session.close()

    # Save result into list of dictionary
    precipitation = []
  
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict[date ] = prcp
        precipitation.append(prcp_dict)
    
    print (f"count precipitation: {len( precipitation )}") 
    # Returns json with the date as the key and the value as the precipitation
    return jsonify(precipitation)

#====================================================================================
# Returns jsonified data of all of the stations in the database
#====================================================================================
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of all stations from the dataset."""
    # Retrive the data of all of the stations in the database
    sel     = [Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation]
    results = session.query(*sel).all()

    session.close()

    # Save result into list of dictionary
    all_stations = []
    for station, name, latitude, longitude, elevation in results:
        stations_dict = {}
        stations_dict["Station"]   = station
        stations_dict["Name"]      = name
        stations_dict["Latitude"]  = latitude
        stations_dict["Longitude"] = longitude
        stations_dict["Elevation"] = elevation
        all_stations.append(stations_dict)
    
    print (f"count stations: {len( all_stations )}")    
    # Returns jsonified data of all of the stations in the database
    return jsonify(all_stations)


#====================================================================================
# Returns jsonified data for the most active station for the last year of data
#====================================================================================
@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    #--------------------------------------------------------------------
    # Retrieve the recent and latest date
    #--------------------------------------------------------------------
    query_result_recent_date  = session.query(Measurement.date).\
                                     order_by(Measurement.date.desc()).limit(1)
                           
    # Extract the content of SQLAlchemy row object
    for row in query_result_recent_date :
        
        # Convert date str to date format
        recent_date = dt.datetime.strptime(row[0], '%Y-%m-%d')   
   
    # Calculate the date one year from the last date in data set.
    date_last_12_months = dt.datetime( recent_date.year -1 \
                                     , recent_date.month \
                                     , recent_date.day)

    # Extract the yyyy-mm-dd from the date time and save as string
    date_prev_year = dt.datetime.strftime(date_last_12_months, '%Y-%m-%d')

    #--------------------------------------------------------------------
    # Get the most active station
    #--------------------------------------------------------------------
    sel             = [Measurement.station, \
            func.count(Measurement.station)]    
    
    active_stations = session.query(*sel).\
                          group_by(Measurement.station).\
                          order_by(func.count(Measurement.station).desc()).first()
 
    most_active_station = active_stations [0]
    print (f"type(most_active_station) {type(most_active_station )} {most_active_station}")
   
    """Return a list of all precipitation"""
    #--------------------------------------------------------------------
    # Retrieve the precipitation for last 12 months for the most active station
    #--------------------------------------------------------------------
    sel     = [Measurement.date, Measurement.tobs]
   
    results = session.query(*sel).\
                     filter(Measurement.date    >= date_prev_year).\
                     filter(Measurement.station == most_active_station ).all() 

    session.close()

    # Save result into list of dictionary
    temperature = []
    for date, tobs in results:
        tobs_dict = {}
        tobs_dict["Date"]        = date 
        tobs_dict["Temperature"] = tobs
        temperature.append(tobs_dict)
        
    print (f"count tobs: {len( temperature )}")    
    # Returns jsonified data for the most active station for the last year of data   
    return jsonify(temperature)

#====================================================================================
# Return a JSON list of the minimum temperature, the average temperature, and the 
# maximum temperature for all dates greater than or equal to the start date.
#====================================================================================
@app.route("/api/v1.0/<start>")
def temperature_start(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start."""
    # Retrieve the list of the minimum temperature, the average temperature, and the 
    # maximum temperature for all dates greater than or equal to the start date.        
    sel = [ func.min(Measurement.tobs) \
          , func.avg(Measurement.tobs) \
          , func.max(Measurement.tobs) \
          ] 
    
    results = session.query(*sel).\
                     filter(Measurement.date >= start ).all()

    session.close()

    # Save result into list of dictionary
    all_temperature_start = []

    for min, avg, max in results:
        temperature_dict = {}
        temperature_dict["Minimum"]  = min
        temperature_dict["Average"]  = avg
        temperature_dict["Maximum"]  = max
        all_temperature_start.append(temperature_dict)
        
    return jsonify(all_temperature_start)

#====================================================================================
# Return a JSON list of the minimum temperature, the average temperature, and the 
# maximum temperature for dates from the start date through the end date (inclusive)
#====================================================================================
@app.route("/api/v1.0/<start>/<end>")
def temperature_start_end(start, end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start."""

    # Retrieve the list of the minimum temperature, the average temperature, and the 
    # maximum temperature for dates from the start date through the end date (inclusive)    
    sel = [ func.min(Measurement.tobs) \
          , func.avg(Measurement.tobs) \
          , func.max(Measurement.tobs) \
          ] 
                     
    results = session.query(*sel).\
                     filter(Measurement.date >= start ).\
                     filter(Measurement.date <= end ).all()

    session.close()

    # Save result into list of dictionary
    all_temperature_start_end = []
    
    for min, avg, max in results:
        temperature_dict= {}
        temperature_dict["Minimum"] = min
        temperature_dict["Average"] = avg
        temperature_dict["Maximum"] = max
        all_temperature_start_end.append(temperature_dict)
        
    return jsonify(all_temperature_start_end)

if __name__ == '__main__':
    app.run(debug=True)
    
#====================================================================================