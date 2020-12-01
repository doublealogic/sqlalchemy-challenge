# Setup and Dependencies
from flask import Flask, jsonify

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflects an existing database into a new model
Base = automap_base()

# Reflects the tables
Base.prepare(engine, reflect=True)

# Saves references to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask Setup
app = Flask(__name__)

# Flask Routes

@app.route("/")
def welcome():
    """Lists all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start>/ place YYYY-MM-DD format date in 'start' <br/>"
        f"/api/v1.0/<start>/<end>/ place YYYY-MM-DD format dates in both 'start' and 'end' "
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Returns list of all precipitation measurements recorded"""

    # Creates a session (link) from Python to the DB
    session = Session(engine)

    # Queries precipitation measurements recorded on each date from the data
    precip_results = session.query(Measurement.date, Measurement.prcp).all()

    # Closes the session
    session.close()

    # Converts the above results to a dictionary, then appended to a list
    precip_list = []
    for date, prcp in precip_results:
        precip_dict = {}
        precip_dict["date"] = date
        precip_dict["prcp"] = prcp
        precip_list.append(precip_dict)

    return jsonify(precip_list)

@app.route("/api/v1.0/stations")
def stations():
    """Returns list of all stations"""

    # Creates a session (link) from Python to the DB
    session = Session(engine)

    # Queries every station
    station_results = session.query(Station.name).all()

    # Closes the session
    session.close()

    # Creates a list of all the stations
    station_list = list(np.ravel(station_results))

    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    """Returns list of last 12 months of temperature observations from most active station"""

    # Creates a session (link) from Python to the DB
    session = Session(engine)

    # Queries last 12 months of precipitation data for most active station from Measurement Table
    tobs_results = session.query(Measurement.date, Measurement.tobs).\
                filter(Measurement.date <= '2017-08-23').\
                filter(Measurement.date >= '2016-08-23').\
                filter(Measurement.station == 'USC00519281')

    # Closes the session
    session.close()

    # Converts the above results to a dictionary, then appended to a list
    tobs_list = []
    for date, tobs in tobs_results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        tobs_list.append(tobs_dict)

    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
def start(start):
    """Returns list of all temperature observations from state date"""

    # Creates a session (link) from Python to the DB
    session = Session(engine)

    # Queries all Min Temperatures, Max Temperatures and Average Temperatures from the start date to the present
    start_results = session.query(Measurement.station,\
            func.min(Measurement.tobs),\
            func.max(Measurement.tobs),\
            func.avg(Measurement.tobs)).\
            filter(Measurement.date >= start).\
            group_by(Measurement.date).all()

    # Closes the session
    session.close()

    # Converts the above results to a dictionary, then appended to a list
    start_list = []
    for date, tmin, tmax, tavg in start_results:
        start_dict = {}
        start_dict["date"] = date
        start_dict["min"] = tmin
        start_dict["max"] = tmax
        start_dict["avg"] = tavg
        start_list.append(start_dict)

    return jsonify(start_list)

@app.route("/api/v1.0/<start>/<end>")
def start_n_end(start, end):
    """Returns list of all temperature observations between and including both the start and end dates"""

    # Creates a session (link) from Python to the DB
    session = Session(engine)

    # Queries all Min Temperatures, Max Temperatures and Average Temperatures from the start date to the present
    start_n_end_results = session.query(Measurement.station,\
            func.min(Measurement.tobs),\
            func.max(Measurement.tobs),\
            func.avg(Measurement.tobs)).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).\
            group_by(Measurement.date).all()

    # Closes the session
    session.close()

    # Converts the above results to a dictionary, then appended to a list
    start_n_end_list = []
    for date, tmin, tmax, tavg in start_n_end_results:
        start_n_end_dict = {}
        start_n_end_dict["date"] = date
        start_n_end_dict["min"] = tmin
        start_n_end_dict["max"] = tmax
        start_n_end_dict["avg"] = tavg
        start_n_end_list.append(start_n_end_dict)

    return jsonify(start_n_end_list)

    if name == 'main':
        app.run(debug=True)