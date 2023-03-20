#!/usr/bin/env sh

# Imports
import pandas as pd
import logging
import requests
import sqlite3

logging.basic   Config(lavel="DEBUG")

# Global variables
dbName = "rest_server/medisch_centrum_randstad/db.sqlite3"
tableName = "rest_api_netlify"
url = "http://localhost:8080/medish_centrum_randstad/api/netlify?page=1"
csvFile = "rest_server/medisch_centrum_randstad/data/data.csv"


def extractFromDB():
    logging.info("Create DB connection")
    dbConnection = sqlite3.connect(dbName)

    dfFromDB = pd.read_sql_query(f"SELECT * FROM {tableName}", dbConnection)
    logging.debug(dfFromDB)
    pd.set_option('display.max_columns', 10)

    dbConnection.close()
