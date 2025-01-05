
from fastapi import FastAPI      
import uvicorn  
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

@app.get("/")
async def greetings():
    return "Chao"

