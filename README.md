# SQL Alchemy Challenge

## Background

In this repository, I use SQLAlchemy and Python to help plan a fictional trip to Honolulu, Hawaii. For this fictional trip, I wanted to do some climate analysis on the area first before traveling there.

## Step 1 - Climate Analysis and Exploration

All of the following analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* Before I began, I needed to choose a start date and end date for my trip. Since August is my birthday month, I thought why not take a couple weeks of vacation then? So my range was August 8th to August 22nd.

* First I used SQLAlchemy `create_engine` to connect to my sqlite database.

* Next I used SQLAlchemy `automap_base()` to reflect my tables into classes and saved a reference to those classes using variables called `Measurement` and `Station`.

### Precipitation Analysis

* Designed a query to retrieve the last 12 months of precipitation data.

* Selected only the `date` and `prcp` values to use for this query.

* Loaded the query results into a Pandas DataFrame and set the index to the date column.

* Sorted the DataFrame values by `date`.

* Plotted the results using the DataFrame `plot` method.

* Last used Pandas to print the summary statistics for the precipitation data.

### Station Analysis 

* Designed a query to calculate the total number of stations.

* Designed a query to find the most active stations.

    * Listed the stations and their observation counts in descending order.

    * Used functions `func.min`, `func.max`, `func.avg` and `func.count` in the query to help with this process.

* Designed a query to retrieve the last 12 months of temperature observation data (TOBS).

    * Filtered by the station with the highest number of observations.

    * Plotted the results as a histogram with `bins=12`


## Step 2 - Climate App
For this part I designed a Flask API based on the queries from Step 1 and I'll use Flask to create my routes.

### Routes

* `/`

    * Home page.

    * Lists all routes that are available.

* `/api/v1.0/precipitation`

    * Converts the query results to a dictionary using `date` as the key and `prcp` as the value.

    * Returns the JSON representation of my dictionary.

* `/api/v1.0/stations`

    * Returns a JSON list of stations from the dataset.

* `/api/v1.0/tobs`

    * Queries the dates and temperature observations of the most active station for the last year of data.

    * Returns a JSON list of temperature observations (TOBS) for the previous year.

* `api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

    * Returns a JSON list of the minimum temperature, average temperature and max temperature for a given start or start-end range.

    * When given the start only, calculates `TMIN`, `TAVG` and `TMAX` for all dates greater than and equal to the start date.

    * When given the start and the end date, calculate thes `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.