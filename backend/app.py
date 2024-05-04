from fastapi import FastAPI, HTTPException  # Importing FastAPI and HTTPException for handling HTTP errors.
from pydantic import BaseModel  # Import BaseModel from Pydantic to create data models.
from backend.main import startProgram

app = FastAPI()  # Create an instance of the FastAPI class. This instance is the core of your app.

class VideoRequest(BaseModel):  # Define a Pydantic model that will be used for data validation.
    topic: str  # Define a 'topic' field expected to be of type string.
    details: str  # Define a 'details' field expected to be of type string.


@app.post("/create_video/")  # Decorator to create a route that listens for POST requests at /create_video/
async def create_video(video_request: VideoRequest):  # Define an asynchronous route handler function.
    try:
        # Call the function from main.py with the provided topic and details
        results = startProgram(video_request.topic, video_request.details)
        return {"message": "Video creation process started", "results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/")  # Decorator to create a route that listens for GET requests at the root /
def read_root():  # Define a simple function to respond to root requests.
    return {"Hello": "World"}  # Returns a simple JSON response to indicate that the API is running.