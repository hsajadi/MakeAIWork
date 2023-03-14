#!/usr/bin/env python

import logging
import pandas as pd
import pickle
import statsmodels as sm
import statsmodels.formula.api as smf
import sqlite3

# Global configuration
logging.basicConfig(level=logging.DEBUG)

lengthStr = input("Enter your length : ")

if lengthStr.isdecimal():
    length = float(lengthStr)
    logging.debug(length)