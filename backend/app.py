from fastapi import FastAPI, HTTPException  # Importing FastAPI and HTTPException for handling HTTP errors.
from pydantic import BaseModel  # Import BaseModel from Pydantic to create data models.
from fastapi.responses import FileResponse
from main import startProgram
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()  # Create an instance of the FastAPI class. This instance is the core of your app.


# Add CORS middleware to the application instance
app.add_middleware(
    CORSMiddleware,
    # List of URLs that are allowed to access this API.
    allow_origins=["http://localhost:3000"],  # Only allow requests from this origin
                                             # Change this to match the URL of your frontend application

    # Specifies whether to include the Access-Control-Allow-Credentials header in responses.
    # This is necessary when credentials are involved in requests (e.g., cookies, authorization headers).
    allow_credentials=True,

    # List of HTTP methods that are allowed for cross-origin requests.
    # You can specify individual methods ['GET', 'POST'] or use ['*'] for all.
    allow_methods=["*"],  # Allow all methods for simplicity, specify if needed for security

    # List of HTTP request headers that are allowed for cross-origin requests.
    # This should match the headers you use in your requests.
    allow_headers=["*"],  # Allow all headers for simplicity, specify if needed for security
)

class VideoRequest(BaseModel):  # Define a Pydantic model that will be used for data validation.
    topic: str  # Define a 'topic' field expected to be of type string.
    details: str  # Define a 'details' field expected to be of type string.


@app.post("/create_video/")  # Decorator to create a route that listens for POST requests at /create_video/
async def create_video(video_request: VideoRequest):  # Define an asynchronous route handler function.
    try:
        # Call the function from main.py with the provided topic and details
        results = startProgram(video_request.topic, video_request.details)
        # results = "STARTED"
        return {"message": "Video creation process started", "results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/get_video_creation_report/")
async def get_video_creation_report():
    file_path = "output/YouTube_Video_Creation_Report.txt"
    try:
        return FileResponse(file_path, media_type='text/plain', filename="YouTube_Video_Creation_Report.txt")
        # return ("REPORT HERE")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Report not found")
    