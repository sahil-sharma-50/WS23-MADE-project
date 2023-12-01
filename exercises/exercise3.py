#  Task: Write data into a SQLite database called “cars.sqlite”, in the table “cars”
#  Author: Sahil Sharma
#  Date: December 01, 2023

# Importing necessary libraries:
import pandas as pd
from sqlalchemy import create_engine, String, Integer

url = "https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv"

data = pd.read_csv(url, sep=";", skiprows=7, skipfooter=4, encoding="ISO-8859-1", engine='python')
data = data.iloc[:, [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]]

# Rename columns names
data = data.rename(
    columns={
        data.columns[0]: "date",
        data.columns[1]: "CIN",
        data.columns[2]: "name",
        data.columns[3]: "petrol",
        data.columns[4]: "diesel",
        data.columns[5]: "gas",
        data.columns[6]: "electro",
        data.columns[7]: "hybrid",
        data.columns[8]: "plugInHybrid",
        data.columns[9]: "others",
    }
)

column_DataTypes = {
    "date": String,
    "CIN": String,
    "name": String,
    "petrol": Integer,
    "diesel": Integer,
    "gas": Integer,
    "electro": Integer,
    "hybrid": Integer,
    "plugInHybrid": Integer,
    "others": Integer,
}


# Connection to the Database:
engine = create_engine("sqlite:///cars.sqlite")

# Store the data in airports table:
data.to_sql("cars", engine, index=False, dtype=column_DataTypes, if_exists="replace")

# Connection close
engine.dispose()
