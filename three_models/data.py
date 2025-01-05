
''' 
generate the data to be used for the anomaly detection. 
Generate a dataset with 1000 samples, 2 features, and a 99% to 1% class imbalance
X contains the feature data, y contains the labels (0 for normal, 1 for anomaly)
'''
from sklearn.datasets import make_classification
import pandas as pd
import numpy as np

X, y = make_classification(n_samples=1000, n_features=5, n_informative=5, n_redundant=0,n_repeated=0, weights=[0.99, 0.01], random_state=42)
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
X_df = pd.DataFrame(X)
y_df = pd.DataFrame(y)
X_df.to_csv("X_df.csv")
y_df.to_csv("y_df.csv")
print("done")
