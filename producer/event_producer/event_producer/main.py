from contextlib import asynccontextmanager
from time import sleep 
from json import dumps
from fastapi import FastAPI



@asynccontextmanager
async def lifespan(app: FastAPI):
    print("event_producer started")
    yield
    
app = FastAPI(lifespan = lifespan, title="Event producer"
            #   servers=[
            #       {
            #           "url": "http://127.0.0.1:8002",
            #           "description": "Development server"
            #         },
            #   ]
)

@app.get("/")
def root():
    return {"message": "Hello from producer"}



