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
        f"/api/v1.0/<start>/ add a start date there in YYYY-MM-DD format<br/>"
        f"/api/v1.0/<start>/<end>/ add both and a start and end date there in YYYY-MM-DD format"
    )