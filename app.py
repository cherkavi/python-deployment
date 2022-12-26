## #webframework 
# uvicorn simple-fastapi:app --host 0.0.0.0 --port 8080

from datetime import datetime
from time import sleep
from fastapi import FastAPI
from pydantic import BaseModel
from multiprocessing import Process
import uvicorn

# Create a FastAPI app
fast_app = FastAPI()

# Define the input schema for the endpoint
class Input(BaseModel):
    x1: float
    x2: float
    x3: float
    x4: float

@fast_app.get("/time")
def get_time():
    return datetime.now()

@fast_app.post("/echo")
def echo(input: Input):
    return {input.x1, input.x2, input.x3, input.x4}

if __name__=='__main__':
    uvicorn.run(fast_app, host="::", port=8080, log_level="debug")
    
