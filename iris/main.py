from fastapi import FastAPI
import joblib
import numpy as np

#from model import iris 
from sklearn.datasets import load_iris as iris
app = FastAPI()

# Load the trained model
model = joblib.load('model.joblib')

@app.get("/")
def read_root():
    return {"message": "Welcome to the ML Model API"}

@app.post("/predict/")
def predict(data: dict):
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    class_name = iris.target_names[prediction][0]
    return {"class": class_name}


