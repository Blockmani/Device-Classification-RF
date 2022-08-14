'''
    The model used here is RANDOM FOREST(RF) with forest size
    being 100 (subjected to change). RF is accompanied by 
    Majority Voting to pick out the best classification for the
    given test data.
'''

# basic imports
import pandas as pd
import numpy as np

# sklearn-specific imports
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

# read csv
dataset = pd.read_csv('../dataset/device_specs.csv')

# label encode 
le=LabelEncoder()

le_columns = ['BRAND', 'DEVICE_OUTPUT_TYPE', 'DEVICE_MAJORITY_COMPOSITION', 'SENSOR_TYPE']

for i in le_columns:
  dataset[i]=le.fit_transform(dataset[i])

# identify the target variable
X = dataset.drop(columns=['SENSOR_TYPE'])
y = dataset['SENSOR_TYPE']

# Split dataset into training set and test set (30% of data will be used for testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Create a RF Classifier with 100 trees in the forest
clf=RandomForestClassifier(n_estimators=100)

clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)

# Model Accuracy
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))