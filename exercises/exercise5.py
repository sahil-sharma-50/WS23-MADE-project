#  Task: Data Pipelnie for GTFS data
#  Author: Sahil Sharma
#  Date: January 09, 2023

import zipfile, urllib.request, sqlalchemy 
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float

# Download and extract data
urllib.request.urlretrieve("https://gtfs.rhoenenergie-bus.de/GTFS.zip", "GTFS.zip")
with zipfile.ZipFile("GTFS.zip", 'r') as zip_ref:
    zip_ref.extract("stops.txt")

# Load and filter data
df = pd.read_csv("stops.txt", usecols=["stop_id", "stop_name", "stop_lat", "stop_lon", "zone_id"])
df = df[df["zone_id"] == 2001]
df = df[df["stop_lat"].between(-90, 90) & df["stop_lon"].between(-90, 90)]

# Define datatypes
df = df.astype({
    'stop_id': 'int',
    'stop_name': 'str',
    'stop_lat': 'float',
    'stop_lon': 'float',
    'zone_id': 'int'
})

# Save to database
engine = sqlalchemy.create_engine('sqlite:///gtfs.sqlite')
df.to_sql('stops', con=engine, if_exists='replace', index=False)