import datetime as dt
from datetime import datetime
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import inspect
from flask import Flask, jsonify

# reflect existing database and view all classes 
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

# save references to each table 
measurement = Base.classes.measurement
Station = Base.classes.station
app = Flask(__name__)


# Home page
# List all routes that are available

@app.route("/")
def home():
    # print all routes available on home page
    return (
        f"Home Page <br/>"
        f"All routes that are available <br/>"
        f"------------------------------------- <br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/start <br/>"
        f"/api/v1.0/start/end <br/>" 
        )



# Convert the query results to a dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.

@app.route("/api/v1.0/precipitation/")
def precipitation():
    # open session link from Python to the database 
    session = Session(engine)

    # find 12 months before last date in data 
    last_date_query = session.query(measurement.date).order_by(measurement.date.desc()).first()
    last_date = last_date_query[0]
    last_date_dt = dt.datetime.strptime(last_date, '%Y-%m-%d')
    date_1yr_ago = last_date_dt - dt.timedelta(days=365)
    
    # query data for date and precipitation for greater than 12 months from the last date
    sel = [measurement.date, measurement.prcp]
    year_rainfall = session.query(*sel).filter(measurement.date >= date_1yr_ago).order_by(measurement.date).all()

    # close the session
    session.close()

    # make a dictionary of results with date as the key
    results = {date: prcp for date, prcp in year_rainfall}

    return jsonify(results)



# Return a JSON list of stations from the dataset.

@app.route("/api/v1.0/stations/")
def station():
    # open session link from Python to the database
    session = Session(engine)
    
    # query data for all stations and the names
    stations_query = session.query(Station.station, Station.name).all() 

    # close the session
    session.close() 

    # make a dictionary for displaying results
    results =  {station: name for station, name in stations_query}

    return jsonify(results)



#Query the dates and temperature observations of the most active station for the last year of data.
#Return a JSON list of temperature observations (TOBS) for the previous year.

@app.route("/api/v1.0/tobs/")
def tobs():
    # open session link from Python to the database
    session = Session(engine)

    # query data for most active station 
    sel = [measurement.station, func.count(measurement.prcp)]
    most_active_query = session.query(*sel).group_by(measurement.station).order_by(func.count(measurement.prcp).desc()).all()

    # save the most active station in query to variable
    most_active_station = most_active_query[0][0]
    
    # query date and temp. observation for the most active station
    sel = [measurement.station, measurement.date, measurement.tobs]
    tobs_query = session.query(*sel).filter(measurement.station == most_active_station).all()

    # unpack results into list
    results = list(np.ravel(tobs_query))

    # close the session
    session.close() 

    return jsonify(tobs_query)



# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.

@app.route("/api/v1.0/<start>")
def start(start):
    # open session link from Python to the database
    session = Session(engine)   

    # query data for the min, max and average temp. from the input start date to last date in data
    sel = [func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)]
    summary_query = session.query(*sel).filter(measurement.date >= start).all()

    # unpack results into list
    result = list(np.ravel(summary_query))

    # close the session
    session.close()

    return jsonify(result)



# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

@app.route("/api/v1.0/<start>/<end>")
def startend(start, end):
    # open session link from Python to the database
    session = Session(engine)

    # query data for temp. min, max and average between input start and end date
    sel = [func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)]
    summary_query = session.query(*sel).filter(measurement.date >= start).filter(measurement.date <= end).all()

    # unpoack results into list
    result = list(np.ravel(summary_query))

    # close the session
    session.close()

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)