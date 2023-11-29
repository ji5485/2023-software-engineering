from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from packages.AddOn import AddOn
from packages.Map import Map
from packages.Position import Position
from packages.Spot import Predefined, Hazard, ColorBlob
from api import Robot
from openai import OpenAI
import json
import record_voice

app = FastAPI()
add_on = None

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MapBody(BaseModel):
  map: str = Field(pattern="^\(\d \d\)$")
  start: str = Field(pattern="^\(\d \d\)$")
  predefined: str = Field(pattern="^\((\(\d \d\))*\)$")
  hazard: str = Field(pattern="^\((\(\d \d\))*\)$")
  colorBlob: str = Field(pattern="^\((\(\d \d\))*\)$")

@app.post("/")
def create_map(body: MapBody):
  # 좌표 파싱
  [width, height] = map(int, body.map[1:-1].split(" "))
  [start_x, start_y] = map(int, body.start[1:-1].split(" "))
  predefined = list(map(lambda coord: list(map(int, coord.split())), body.predefined[2:-2].split(")(")))
  hazard = list(map(lambda coord: list(map(int, coord.split())), body.hazard[2:-2].split(")(")))
  colorBlob = list(map(lambda coord: list(map(int, coord.split())), body.colorBlob[2:-2].split(")(")))

  # ADD ON 생성
  robot = Robot(Position(start_x, start_y))
  add_on = AddOn(Map(width, height), robot)

  for [x, y] in predefined:
    add_on.create_spot(Predefined(), Position(x, y))
  
  for [x, y] in hazard:
    add_on.create_spot(Hazard(), Position(x, y))

  for [x, y] in colorBlob:
    add_on.create_spot(ColorBlob(), Position(x, y))
  
  return {
    "map": { "width": width, "height": height },
    "robot": robot,
    "predefined": list(map(lambda coord: { "x": coord[0], "y": coord[1] }, predefined)),
    "hazard": list(map(lambda coord: { "x": coord[0], "y": coord[1] }, hazard)),
    "colorBlob": list(map(lambda coord: { "x": coord[0], "y": coord[1] }, colorBlob))
  }

@app.post("/robot")
def request_robot_movement():
  return "Request Robot Movement"

client = OpenAI(api_key="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")
information = {'x': None, 'y': None, 'status': None}

@app.post("/voice")
async def handle_voice_command(voice: UploadFile = File("./assistant/output_xystatus.wav")):
    with open(voice.file, "rb") as audio_file:
        audio = audio_file.read()
    
    transcript = client.audio.transcriptions.create(model="whisper-1", file=audio)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": transcript.text}],
        functions=functions,
        function_call="auto"
    )

    if response.choices[0].message.function_call:
        name = response.choices[0].message.function_call.name
        args = json.loads(response.choices[0].message.function_call.arguments)

        registered_functions[name](args.get("x"), args.get("y"))
    else:
        print("Failure")

    return JSONResponse(content={"transcript": transcript.text, "information": information})
