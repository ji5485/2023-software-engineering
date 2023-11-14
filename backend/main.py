from fastapi import FastAPI

app = FastAPI()

@app.post("/")
def create_map():
  return "Create Map"

@app.get("/")
def request_robot_movement():
  return "Request Robot Movement"

@app.get("/voice")
def handle_voice_command():
  return "Handle Voice Command"