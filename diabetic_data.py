# -*- coding: utf-8 -*-
"""Diabetic Data

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Cm6RHGtwhkT8D5rHf51JhJghQlOVEFeC
"""

!pip install --upgrade scikit-learn

!pip install scikit-learn==1.3.0

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

daibetes_dataset = pd.read_csv('/content/diabetes.csv')

daibetes_dataset.head()

daibetes_dataset.shape

daibetes_dataset.describe()

daibetes_dataset['Outcome'].value_counts()

daibetes_dataset.groupby('Outcome').mean()

from google.colab import drive
drive.mount('/content/drive')

X = daibetes_dataset.drop(columns='Outcome', axis=1)
Y = daibetes_dataset['Outcome']

print (X)

print(Y)

scaler=StandardScaler()

scaler.fit(X)

standardized_data = scaler.transform(X)

print(standardized_data)

X=standardized_data
Y=daibetes_dataset['Outcome']

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, stratify=Y, random_state=2)

print (X.shape, X_train.shape, X_test.shape)

from sklearn import svm # Import the svm module

classifier = svm.SVC(kernel='linear') # Now you can access the SVC class within the svm module

classifier.fit(X_train, Y_train)

X_train_prediction= classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy score of the training data : ', training_data_accuracy)

X_test_prediction= classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy score of the test data : ', test_data_accuracy)

input_data= (4,110,92,0,0,37.6,0.199,30)

input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

std_data = scaler.transform(input_data_reshaped)
print(std_data)

prediction = classifier.predict(std_data)
print(prediction)

if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')