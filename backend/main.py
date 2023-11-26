from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
def create_map():
  return "Create Map"

@app.get("/")
def request_robot_movement():
  return "Request Robot Movement"

@app.post("/voice")
async def handle_voice_command(voice: UploadFile):
  print(voice)
  return "Handle Voice Command"