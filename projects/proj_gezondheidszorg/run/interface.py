#!/usr/bin/env python

import logging
import pandas as pd
import pickle
import statsmodels as sm
import statsmodels.formula.api as smf
import sqlite3

# Global configuration
logging.basicConfig(level=logging.DEBUG)
regModel = '../models/model_pkl'

logging.info("Load model")
with open(regModel, 'rb') as f:
    regressor = pickle.load(f)


def predict(inputData):

    # Predict lifespan with regressor and inputData
    prediction = regressor(inputData)
    return prediction


def inputDigit(message, acceptableRange):
    inputStr = str()
    withinRange = False
    numberOfTries = 3
    inputNum = None
    i = 0

    while not (inputStr.isdigit() and withinRange) and i < numberOfTries:
        inputStr = input(message)
        logging.debug(inputStr)

        if inputStr.isdigit():
            inputNum = float(inputStr)

            if inputNum in acceptableRange:
                return inputNum

        i += 1

    return None


acceptableRange = range(18, 118)
age = int(inputDigit("Age [18 - 118]: ", acceptableRange))
logging.debug(f"age : {age}")
