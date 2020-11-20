# SQL Alchemy Challenge

## Background

In this repository, I use SQLAlchemy and Python to help plan a fictional trip to Honolulu, Hawaii. For this fictional trip, I wanted to do some climate analysis on the area first before traveling there.

## Step 1 - Climate Analysis and Exploration

All of the following analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* Before I began, I needed to choose a start date and end date for my trip. Since August is my birthday month, I thought why not take a couple weeks of vacation then? So my range was August 8th to August 22nd.

* Use SQLAlchemy `create_engine` to connect to your sqlite database.

* Use SQLAlchemy `automap_base()` to reflect your tables into classes and save a reference to those classes called `Station` and `Measurement`.
