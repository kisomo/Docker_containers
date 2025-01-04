import pandas as pd 
import numpy as np 
from pydantic_models import QueryInput, QueryResponse
import joblib
from fastapi import FastAPI

#print("Welcome")
#model = joblib.load("model.joblib")

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


app = FastAPI()

def class_name_predicted(x):
    if x == 0:
       res = "iris"
    elif x == 1:
       res = "sertosa"
    elif x == 2:
      res = "virginica"
    else:
        res = "NA"
    return res

@app.get("/")
def read_root():
    return {"message": "Welcome to the ML Model API"}

#@app.post("/predict/", response_model=QueryResponse)
@app.post("/predict/")
def predict(data: QueryInput):
    #features = np.array(data['features']).reshape(1, -1)
    features = np.array([data.petal_length, data.petal_width, data.sepal_width, data.sepal_width]).reshape(1,-1)
    prediction = model.predict(features)
    #class_name = iris.target_names[prediction][0]
    #return {"class": class_name}
    return class_name_predicted(int(prediction))








