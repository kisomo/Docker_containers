
from fastapi import fastAPI      
import uvicorn  
from motor.motor_asyncio import AsyncIOMotorClient

app = fastAP()

@app.get("/")
async def greetings():
    return "Chao"

