import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.neighbors import LocalOutlierFactor
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

lof_novelty = LocalOutlierFactor(n_neighbors=20, novelty=True)
lof_novelty.fit(X_train)
joblib.dump(lof_novelty, 'src/LOF_model.joblib')

#SVM_model = OneClassSVM(nu=0.001, kernel="rbf", gamma=0.001)
#SVM_model.fit(X_train)
#joblib.dump(SVM_model, 'SVM_model.joblib')

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

