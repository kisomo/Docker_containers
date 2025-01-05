
'''
docker image build -t lof /Users/tmuth/MODELS/Docker_containers/three_models/LOF
docker run --name lof_container -p 80:80 -v ${pwd}:/src/code lof
'''
import pandas as pd 
import numpy as np 
#from pydantic_models import QueryInput, QueryResponse
import joblib
from fastapi import FastAPI

from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
class QueryInput(BaseModel):
    x1: int
    x2: int
    x3: int
    x4:int
    x5:int
    x6:int

#print("Welcome")
model = joblib.load("src/LOF_model.joblib")

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to LOF endpoint"}

#@app.post("/predict/", response_model=QueryResponse)
@app.post("/predict/")
def predict(data: QueryInput):
    #features = np.array(data['features']).reshape(1, -1)
    features = np.array([data.x1, data.x2, data.x3, data.x4, data.x5, data.x6]).reshape(1,-1)
    prediction = model.predict(features)
    #class_name = iris.target_names[prediction][0]
    #return {"class": class_name}
    return f"LOF output is {int(prediction)}"




