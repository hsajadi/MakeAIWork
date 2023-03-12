#!/usr/bin/env python

# Imports
import logging
import pandas as pd
import pickle
import sqlite3

# Hardening
from pathlib import Path
from sklearn.neighbors import KNeighborsRegressor

# Global configuration
logging.basicConfig(level=logging.DEBUG)
exportFile = "../models/knn.pkl"

dbName = "../rest_server/medisch_centrum_randstad/db.sqlite3"
tableName = "rest_api_netlify"

logging.info(f"Connect to {Path(dbName).name}")
dbConnection = sqlite3.connect(dbName)

logging.info("Load transformed data from database into dataframe")
dfFromDB = pd.read_sql_query(f"SELECT length, lifespan FROM {tableName}", dbConnection)

logging.info("Close DB Connection")
dbConnection.close()

logging.info("Preprocessing : remove rows with missing values")
dfCleanFromDB = dfFromDB.dropna()
logging.debug(dfCleanFromDB.head())

logging.info("Feature Selection")

y = dfCleanFromDB['lifespan'].values
logging.debug(f"Y : {type(y)}")

X = dfCleanFromDB['length'].values
logging.debug(f"X : {type(X)}")

logging.info("Build Regression Model")

regressor = KNeighborsRegressor(n_neighbors=4, metric='euclidean')
regressor.fit(X.reshape(-1, 1), y)

logging.debug(f"Check with single value {regressor.predict([[185]])}")

pickle.dump(regressor, open(exportFile,'wb'))
dbConnection.close()