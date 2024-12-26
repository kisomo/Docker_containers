from fastapi import fastAPI  
import uvicorn 

app = fastAPI() 

@app.get("/")
def greetings():
   return "Mambo poa"
