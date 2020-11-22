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

