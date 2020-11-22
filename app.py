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

    # Converts the above results to a dictionary
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
    station_list = list(np.ravel(results))

    return jsonify(station_list)