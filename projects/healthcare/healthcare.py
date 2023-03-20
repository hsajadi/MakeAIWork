#!/usr/bin/env python3
# Imports
import os
import csv

import logging
import pandas as pd
import numpy as np
import sqlite3
# import matplotlib.pyplot as plt

# Hardening
from pathlib import Path
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

import pickle
import statsmodels as sm
import statsmodels.formula.api as smf


# Imports for Interface
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from tkinter import filedialog


# Global configuration
logging.basicConfig(level=logging.INFO)
dbName = '/home/hossein/MakeAIWork/projects/old data project 1/healthcare/db.sqlite3'
tableName = 'rest_api_netlify'

# Collecting the data
logging.info('Load transformed data from database into dataframe')
logging.info(f'Connect to {Path(dbName).name}')
dbConnection = sqlite3.connect(dbName)
patient_DF = pd.read_sql_query(f'SELECT * FROM {tableName}', dbConnection)
logging.debug(patient_DF.head())

# Cleaning empty cells and removing its index
logging.info('Preprocessing : remove rows with missing values')
dfCleanFromDB = patient_DF.dropna()

# Replacing Wrong DataTypes and Replace NaN
dfCleanFromDB2 = dfCleanFromDB.apply(pd.to_numeric, errors='coerce')
dfCleanFromDB3 = dfCleanFromDB2[dfCleanFromDB.select_dtypes(include=[np.number]).ge(0).all(1)]

logging.debug(dfCleanFromDB3.head())
dfCleanFromDB3.to_csv('/home/hossein/MakeAIWork/projects/old data project 1/healthcare/data_cleaned.csv', header=True, index=False)


# Adding BMI
patient_DF = pd.read_csv('/home/hossein/MakeAIWork/projects/old data project 1/healthcare/data_cleaned.csv')
patient_DF['BMI'] = (patient_DF['mass']/patient_DF['length']**2)*10000

# Saving transformed DataFrame including BMI
patient_DF.to_csv('/home/hossein/MakeAIWork/projects/old data project 1/healthcare/medisch_centrum_randstad_BMI.csv', header=True, index=False)
# Storing DataFrame as Table inside .sql
patient_DF.to_sql('medisch_centrum_randstad_BMI', dbConnection, if_exists='replace', index=False)

# close Connection
dbConnection.close()


# Regression
patient_DF2 = pd.read_csv('/home/hossein/MakeAIWork/projects/old data project 1/healthcare/medisch_centrum_randstad_BMI.csv')
X = patient_DF2[['genetic', 'exercise', 'smoking', 'alcohol', 'sugar', 'BMI']]
y = patient_DF2['lifespan']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

regr = LinearRegression()
regr.fit(X_train, y_train)

# Data scatter of predicted values
y_pred = regr.predict(X_test)

sq = (mean_squared_error(y_test, y_pred))**0.5
mae = round((mean_absolute_error(y_test, y_pred)),2)

# Storing Regression Coefficients into Lists
regCoef = regr.coef_
regInter = regr.intercept_


# create an iterator object with write permission - model.pkl
with open('/home/hossein/MakeAIWork/projects/old data project 1/healthcare/model_pkl', 'wb') as files:
    pickle.dump(regr, files)
with open('/home/hossein/MakeAIWork/projects/old data project 1/healthcare/regModel', 'wb') as files:
    pickle.dump(regr, files)


# Global configuration
logging.basicConfig(level=logging.INFO)
regModel = 'models/regModel'


def predict(inputData):
    logging.info('Load model')
    
    with open(regModel , 'rb') as f:
        regressor = pickle.load(f)
    
    # Predict lifespan with regressor and inputData
    return predict

# def interface():
def inputDigit(message, acceptableRange):
    inputStr = str()
    withinRange = False
    numberOfTries = 3
    i = 0

    while not (inputStr.isdigit() and withinRange) and i < numberOfTries:
        inputStr = input(message)

        if inputStr.isdigit():
            inputNum = float(inputStr)

            if inputNum in acceptableRange:
                return inputNum

        i += 1

with open('/home/hossein/MakeAIWork/projects/old data project 1/healthcare/regModel' , 'rb') as f:
    lr = pickle.load(f)

# Recall Coefficients
regCoef = lr.coef_
regInter = lr.intercept_

# Defining MAX and MIN inputs (Range)
min_genetic = patient_DF.describe().transpose()['min']['genetic']
min_length = patient_DF.describe().transpose()['min']['length']
min_weigth = patient_DF.describe().transpose()['min']['mass']
min_exercise = patient_DF.describe().transpose()['min']['exercise']
min_smoking = patient_DF.describe().transpose()['min']['smoking']
min_alkohol = patient_DF.describe().transpose()['min']['alcohol']
min_sugar = patient_DF.describe().transpose()['min']['sugar']

max_genetic = patient_DF.describe().transpose()['max']['genetic']
max_length = patient_DF.describe().transpose()['max']['length']
max_weigth = patient_DF.describe().transpose()['max']['mass']
max_exercise = patient_DF.describe().transpose()['max']['exercise']
max_smoking = patient_DF.describe().transpose()['max']['smoking']
max_alcohol = patient_DF.describe().transpose()['max']['alcohol']
max_sugar = patient_DF.describe().transpose()['max']['sugar']

# Variables- for interface including Range
def show_error(error_message):
    messagebox.showerror('Input Error', f'Error: {error_message}')

def calculate(*args):
    try:
        g1 = float(genetic.get())
        if not min_genetic <= g1 <= max_genetic:
            show_error(f'Genetic have to be between {min_genetic} to {max_genetic} years')
            return
        len1 = float(length.get())
        if not min_length <= len1 <= max_length:
            show_error(f'Heigth have to be between {min_length} to {max_length} Cm')
            return
        mas1 = float(weigth.get())
        if not min_weigth <= mas1 <= max_weigth:
            show_error(f'Weigth have to be between {min_weigth} to {max_weigth} Kg')
            return
        ex1 = float(exercise.get())
        if not min_exercise <= ex1 <= max_exercise:
            show_error(f'Exercise have to be between {min_exercise} to {max_exercise} hours')
            return
        sm1 = float(smoking.get())
        if not min_smoking <= sm1 <= max_smoking:
            show_error(f'Cigarets have to be between {min_smoking} to {max_smoking}')
            return
        al1 = float(alcohol.get())
        if not min_alkohol <= al1 <= max_alcohol:
            show_error(f'Alcohol have to be between {min_alkohol} to {max_alcohol}')
            return
        su1 = float(sugar.get())
        if not min_sugar <= su1 <= max_sugar:
            show_error(f'Sugar have to be between {min_sugar} to {max_sugar}')
            return
        bm1 = (mas1)/((len1/100)**2)
        lifespan_advis.set(int((regCoef[0] * g1)+(regCoef[1] * ex1)+(regCoef[2] * sm1)+(regCoef[3] * al1)+(regCoef[4] * su1)+(regCoef[5] * bm1)+regInter))
        bmi1.set(int(bm1))
    except ValueError:
        pass


# Building interface
root = Tk()
root.title('Lifespan Prognosis')

# Font properties
s = ttk.Style()
font_1 = ('Ariel Nova', 35)
s.configure('.', font = font_1)

mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

genetic = StringVar()
genetic_entry = ttk.Entry(mainframe, width=10, font = font_1, textvariable=genetic)
genetic_entry.grid(column=2, row=1, sticky=(W, E))

length = StringVar()
length_entry = ttk.Entry(mainframe, width=10, font = font_1, textvariable=length)
length_entry.grid(column=2, row=2, sticky=(W, E))

weigth = StringVar()
weigth_entry = ttk.Entry(mainframe, width=10, font = font_1, textvariable=weigth)
weigth_entry.grid(column=2, row=3, sticky=(W, E))

exercise = StringVar()
exercise_entry = ttk.Entry(mainframe, width=10, font = font_1, textvariable=exercise)
exercise_entry.grid(column=2, row=4, sticky=(W, E))

smoking = StringVar()
smoking_entry = ttk.Entry(mainframe, width=10, font = font_1, textvariable=smoking)
smoking_entry.grid(column=2, row=5, sticky=(W, E))

alcohol = StringVar()
alcohol_entry = ttk.Entry(mainframe, width=10, font = font_1, textvariable=alcohol)
alcohol_entry.grid(column=2, row=6, sticky=(W, E))

sugar = StringVar()
sugar_entry = ttk.Entry(mainframe, width=10, font = font_1, textvariable=sugar)
sugar_entry.grid(column=2, row=7, sticky=(W, E))

bmi1 = StringVar()
ttk.Label(mainframe, textvariable=bmi1).grid(column=2, row=8, sticky=(W, E))

# Calculating Button (lower right)
lifespan_advis = StringVar()
ttk.Label(mainframe, textvariable=lifespan_advis).grid(column=2, row=9, sticky=(W, E))

# Creating method for adding picture
def on_click():
    global my_img
    top = Toplevel()
    top.title('Genetic')
    my_img = ImageTk.PhotoImage(Image.open('pics/miw.png'))
    Label(top, image=my_img).pack()

# Building interface Buttons
ttk.Button(mainframe, text='Info', command=on_click).grid(column=3, row=1, sticky=W)
ttk.Button(mainframe, text='Info', command=on_click).grid(column=3, row=2, sticky=W)
ttk.Button(mainframe, text='Info', command=on_click).grid(column=3, row=3, sticky=W)
ttk.Button(mainframe, text='Info', command=on_click).grid(column=3, row=4, sticky=W)
ttk.Button(mainframe, text='Info', command=on_click).grid(column=3, row=5, sticky=W)
ttk.Button(mainframe, text='Info', command=on_click).grid(column=3, row=6, sticky=W)
ttk.Button(mainframe, text='Info', command=on_click).grid(column=3, row=7, sticky=W)
ttk.Button(mainframe, text='Info', command=on_click).grid(column=3, row=8, sticky=W)
ttk.Button(mainframe, text='Calculate', command=calculate).grid(column=3, row=10, sticky=W)

# Information Labels for Input Data Buttons
ttk.Label(mainframe, text='Your genetic in years (64-102)').grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text='Your height in cm (154-214)').grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text='Your weight in kg (50-163.6)').grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text='Hours of exercise per week (0.1-5.5)').grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text='Cigarettes per day (0-22)').grid(column=1, row=5, sticky=W)
ttk.Label(mainframe, text='Glasses alcohol per day (0-6)').grid(column=1, row=6, sticky=W)
ttk.Label(mainframe, text='Cubes of sugar per day (0.7-13.8)').grid(column=1, row=7, sticky=W)
ttk.Label(mainframe, text='Your BMI is').grid(column=1, row=8, sticky=W)
ttk.Label(mainframe, text='Your lifespan prognosis').grid(column=1, row=9, sticky=W)
ttk.Label(mainframe, text='years').grid(column=3, row=9, sticky=W)

# Interface INPUT loop and OUTPUT
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=30, pady=15)

genetic_entry.focus()
length_entry.focus()
weigth_entry.focus()
exercise_entry.focus()
smoking_entry.focus()
alcohol_entry.focus()
sugar_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()