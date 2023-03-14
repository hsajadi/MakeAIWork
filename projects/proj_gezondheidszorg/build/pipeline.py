#!/usr/bin/env python

# Imports
import logging
import pandas as pd
import sqlite3

# Hardening
from pathlib import Path

# Global configuration
logging.basicConfig(level=logging.DEBUG)
dbName = "../rest_server/medisch_centrum_randstad/db.sqlite3"
tableName = "rest_api_netlify"

# Collecting the data
logging.info("Load transformed data from database into dataframe")

logging.info(f"Connect to {Path(dbName).name}")
dbConnection = sqlite3.connect(dbName)
dfFromDB = pd.read_sql_query(f"SELECT * FROM {tableName}", dbConnection)
logging.debug(dfFromDB.head())

# Cleaning
logging.info("Preprocessing : remove rows with missing values")
dfCleanFromDB = dfFromDB.dropna()
logging.debug(dfCleanFromDB.head())

# Transform
dfSelection = dfCleanFromDB[['length', 'mass', 'lifespan']]
length = dfSelection['length']
mass = dfSelection['mass']
logging.debug(dfSelection.head())

# BMI = (Weight in Kilograms / (Height in Meters x Height in Meters))
noemer = pow(length/100, 2)
bmi = (mass / noemer) if (noemer > 0) else 0
logging.debug(f"BMI : {bmi}")

# Save df as new table
dfSelection.to_sql('bmi', con=dbConnection, if_exists='replace', index=False)

# close Connection
dbConnection.close()
