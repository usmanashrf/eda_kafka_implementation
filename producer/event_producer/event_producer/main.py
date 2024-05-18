from contextlib import asynccontextmanager
from time import sleep 
from json import dumps
from fastapi import FastAPI
from sqlmodel import SQLModel
from typing import Optional
from aiokafka import AIOKafkaProducer


class RideRequest(SQLModel):
    id: Optional[int]
    client_name:str
    location :str
    destination :str
    fear : int



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
    return {"message": "Hello from class"}

@app.post("/create_request")
async def create_request():
    producer = AIOKafkaProducer(bootstrap_servers='broker:19092')
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        # Produce message
        await producer.send_and_wait("ride", b"book ride for me")
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()

    return {"this","is request","function"}

