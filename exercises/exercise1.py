# Task: Import a CSV file from a URL into a SQLite database
# Editor: Sahil Sharma
# Date: November 13, 2023

#Importing necessary libraries:
import pandas as pd
from sqlalchemy import create_engine, Integer, Float, Text

#URL of the CSV File:
url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"

#Read the CSV File:
data = pd.read_csv(url, sep=';')

# Define Datatypes:
column_DataTypes = {
    "column_1": Integer(),
    "column_2": Text(),
    "column_3": Text(),
    "column_4": Text(),
    "column_5": Text(),
    "column_6": Text(),
    "column_7": Float(),
    "column_8": Float(),
    "column_9": Integer(),
    "column_10": Float(),
    "column_11": Text(),
    "column_12": Text(),
    "geo_punkt": Text()
}

#Connection to the Database:
engine = create_engine("sqlite:///airports.sqlite")

# Store the data in airports table:
data.to_sql("airports", engine, index=False, dtype=column_DataTypes, if_exists="replace")

#Connection close
engine.dispose()
