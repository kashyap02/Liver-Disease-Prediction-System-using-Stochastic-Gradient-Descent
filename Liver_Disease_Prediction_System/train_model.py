# -*- coding: utf-8 -*-
"""
Original file is located at
    https://colab.research.google.com/drive/1TzCHYQAjEqnllohe8oPGpDaddM7O_9iv
"""

# importing libraries

import numpy as np
import pandas as pd
from sklearn.linear_model import SGDClassifier
import pickle

# Read the data

datasetLink = 'https://trello-attachments.s3.amazonaws.com/5d1c3b054d63637c0960f05f/5d1c3b6e42bbc51272bd69af/bf12b99b99042ffdc3f39434a4584778/indian_liver_patient_prepared_prepared.csv'

data = pd.read_csv(datasetLink)

data.head()

# Either data has some missing values or not?
# print(data.isnull().sum())
# data free from empty values
data = data.fillna(np.mean(data['Albumin_and_Globulin_Ratio']))
print(data.isnull().sum())

# Defining independent and dependent variables
independent_variables = data.columns
#print(independent_variables)
independent_variables = independent_variables.delete(-1)
print(independent_variables)

dependent_variables = 'Dataset'
print(dependent_variables)

# separting contents of independent and dependent variables 
X = data[independent_variables]
Y = data[dependent_variables]
# print(X)
# print(Y)

# Create a SGD Classifier Model
clf = SGDClassifier()
clf

# Train the model
clf.fit(X,Y)

# Save the model to the disk
filename = 'finalized_model.sav'
pickle.dump(clf, open(filename, 'wb'))
