#!/usr/bin/env python

# Imports
import logging
import pandas as pd
import sqlite3

# Hardening
from pathlib import Path

# Global configuration
logging.basicConfig(level=logging.INFO)
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
logging.debug(dfSelection.head())

bmiList = list()

# Maak tuples van naam en diameter
lenghtMassList = list(zip(dfSelection["length"], dfSelection["mass"]))

for (length, mass) in lenghtMassList:
    # BMI = (Weight in Kilograms / (Height in Meters x Height in Meters))

    # Voorkom delen door nul!
    bmi = mass / pow(length/100, 2) if (length > 0) else None

    bmiList.append(bmi)

dfWithBMI = dfSelection.copy()
nrOfCols = dfWithBMI.shape[1]
dfWithBMI.insert(loc=nrOfCols, column='bmi', value=bmiList)

# Save df as new table
dfWithBMI.to_sql('data_with_bmi', con=dbConnection,
                 if_exists='replace', index=False)

# close Connection
dbConnection.close()
