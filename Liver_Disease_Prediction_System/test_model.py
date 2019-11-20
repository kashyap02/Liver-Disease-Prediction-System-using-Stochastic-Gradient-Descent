# importing libraries

import numpy as np
import pandas as pd
from sklearn.linear_model import SGDClassifier
import pickle



# Read the data for getting independent_variables

datasetLink = 'https://trello-attachments.s3.amazonaws.com/5d1c3b054d63637c0960f05f/5d1c3b6e42bbc51272bd69af/bf12b99b99042ffdc3f39434a4584778/indian_liver_patient_prepared_prepared.csv'

data = pd.read_csv(datasetLink)

#data.head()

# Either data has some missing values or not?

# print(data.isnull().sum())
# data free from empty values
data = data.fillna(np.mean(data['Albumin_and_Globulin_Ratio']))
#print(data.isnull().sum())

# Defining independent and dependent variables

independent_variables = data.columns
#print(independent_variables)
independent_variables = independent_variables.delete(-1)
#print(independent_variables)

dependent_variables = 'Dataset'
#print(dependent_variables)



##########################################


# Load the model from the disk
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# Taking input

data_info = {}
import sys
counter = 1
# com_line_str = sys.argv
for feature in independent_variables:
  temp = sys.argv[counter]
  data_info[feature] = temp
  counter = counter + 1
  
#print(data_info)

#aliasing the loaded_model into clf

clf = loaded_model

# Predict whether a person has liver disease or not
# create a test data frame from data_info

test_data = pd.DataFrame(data_info,index=[0],columns=independent_variables)
#print('test data = ' ,test_data)
disease_predict = clf.predict(test_data)
#print('-----Result--- = ',disease_predict)
if disease_predict[0] == 1 :
  print("Patient Needs to be Diagonised")
else :
  print("Patient is well but should take care of himself")
