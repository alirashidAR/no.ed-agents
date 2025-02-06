from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent.agent import create_roadmap  # Assuming this is the correct import
from tools.recommend import get_recommended_roles
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GOOGLE_GEN_AI")

app = FastAPI()

# Apply CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class RoadmapRequest(BaseModel):
    resume: str
    role: str

class RecommendRolesRequest(BaseModel):
    tags: str

@app.get("/")
async def root():
    return {"message": "Welcome to the Roadmap Generator!"}

@app.post("/roadmap")
async def generate_roadmap(request: RoadmapRequest):
    roadmap = await create_roadmap(request.resume, request.role)  # Await the async function here
    return roadmap

@app.post("/recommend_roles")
async def generate_roles(request: RecommendRolesRequest):
    roles = get_recommended_roles(GEMINI_API_KEY, request.tags)
    return roles

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
