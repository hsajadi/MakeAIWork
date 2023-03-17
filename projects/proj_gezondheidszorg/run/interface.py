#!/usr/bin/env python

from pathlib import Path
import logging
import numpy as np
import pandas as pd
import pickle
import statsmodels as sm
import statsmodels.formula.api as smf

# Global configuration
logging.basicConfig(level=logging.DEBUG)
regModel = '../models/knn.pkl'

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
            else:
                print("Enter a value between %s and %s" %(min(acceptableRange), max(acceptableRange)))

        i += 1

    return None

def inputPatientData():
    logging.debug("Start dialog")
    
    length = int(inputDigit("Length : ", range(90, 220)))
    logging.debug(f"length : {length}")

    weigth = int(inputDigit("Weigth : ", range(40, 140)))
    logging.debug(f"weigth : {weigth}")
    
    # Return tuple
    return (length, weigth)

def predictLifespan(bmi):
    # Default return value
    prediction = None
    
    logging.info(f"Load regression model {Path(regModel).name}")
    with open(regModel, 'rb') as f:
        regressor = pickle.load(f)

    logging.debug("Predict lifespan with Regressor and BMI")
    X = np.array(bmi)
    prediction = int(regressor.predict(X.reshape(-1, 1))[0])

    return prediction     

(length, weigth) = inputPatientData()

logging.info("Determine BMI")
# BMI = (Weight in Kilograms / (Height in Meters x Height in Meters))
bmi = weigth / pow(length/100, 2) if (length > 0) else None    

if not bmi is None:
    predLifespan = predictLifespan(bmi)

if not predictLifespan is None:
    print(f"Estimated lifespan : {predLifespan}")    
    
