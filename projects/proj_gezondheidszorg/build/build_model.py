#!/usr/bin/env python

import logging
import numpy as np
import pandas as pd
import pickle
import statsmodels.api as sm
import sqlite3

# Global configuration
logging.basicConfig(level=logging.DEBUG)

dbName = "../rest_server/medisch_centrum_randstad/db.sqlite3"
tableName = "rest_api_netlify"

logging.info("Load transformed data from database into dataframe")
dbConnection = sqlite3.connect(dbName)
dfFromDB = pd.read_sql_query(f"SELECT * FROM {tableName}", dbConnection)

logging.info("Build Regression Model")

Y = dfFromDB['lifespan']
logging.debug(f"Y : {Y}")

X = dfFromDB['length']
logging.debug(f"X : {X}")

# model = sm.OLS(y, X).fit()
duncan_prestige = sm.datasets.get_rdataset("Duncan", "carData")
Y = duncan_prestige.data['income']
X = duncan_prestige.data['education']
X = sm.add_constant(X)
model = sm.OLS(Y, X)

# pickle.dump(self.model, open(exportFile,'wb'))
    