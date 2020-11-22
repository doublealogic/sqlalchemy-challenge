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