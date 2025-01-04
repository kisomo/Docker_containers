'''
import numpy as np
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train a random forest classifier
model = RandomForestClassifier()
model.fit(X, y)

# Save the trained model
joblib.dump(model, 'model.joblib')

print(np.unique(y))

x = [10,5,1,7]
prediction = model.predict(np.array(x).reshape(1,-1))
print(f"prediction = {int(prediction)}")
'''