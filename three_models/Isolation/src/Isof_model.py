import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest
'''
from sklearn.svm import OneClassSVM
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
#Model and performance
from sklearn.metrics import classification_report
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn import metrics
from sklearn.preprocessing import StandardScaler, LabelEncoder
from imblearn.over_sampling import SMOTE
'''
X = pd.read_csv("src/X_df.csv") 
y = pd.read_csv("src/y_df.csv")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# initialize and fit the model
clf_IF = IsolationForest(contamination=0.1)
clf_IF.fit(X_train)
# predict the anomalies in the data
#y_pred_train_IF = clf_IF.predict(X_train)
##y_pred_test_IF = clf_IF.predict(X_test)
#print(y_pred_train_IF)
#print(y_pred_test_IF)

joblib.dump(clf_IF, 'IF_model.joblib')

'''
# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target
# Train a random forest classifier
model = RandomForestClassifier()
model.fit(X, y)
# Save the trained model
joblib.dump(model, 'model.joblib')
print(np.unique(y))
'''
#x = [10,5,1,7,8,3]
#prediction = SVM_model.predict(np.array(x).reshape(1,-1))
#print(f"prediction = {int(prediction)}")

