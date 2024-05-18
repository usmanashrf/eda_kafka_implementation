
from contextlib import asynccontextmanager
from time import sleep 
from json import dumps
from fastapi import FastAPI



@asynccontextmanager
async def lifespan(app: FastAPI):
    print("event_consumer started")
    yield
    
app = FastAPI(lifespan = lifespan, title="Event Consumer",
            #   servers=[
            #       {
            #           "url": "http://127.0.0.1:8000",
            #           "description": "Development server"
            #         },
            #   ]
              )

@app.get("/")
def root():
    return {"message": "Hello from consumer!"}