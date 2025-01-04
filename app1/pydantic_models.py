

'''
Pydantic is a data validation library that uses Python type annotations to define data schemas. 
In our FastAPI application, we use Pydantic models to define the structure of our request and response data. 
Let's break down the models defined in
'''

from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime

class QueryInput(BaseModel):
    petal_length: int
    petal_width: int
    sepal_width: int
    sepal_length:int

class QueryResponse(BaseModel):
    class_score: int
    class_name: str



