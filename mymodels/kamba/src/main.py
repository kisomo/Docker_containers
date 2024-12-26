from fastapi import fastAPI 
import uvicorn  
from motor.motor_asyncio import AsyncIOMotorClient

app = fastAPI()

@app.get("/")
async def greetings():
    return "Nikuseo"


