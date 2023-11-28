from openai import OpenAI
import json
import record_voice

client = OpenAI(api_key="")
information = {
    'x': None,
    'y': None,
    'status': None
}
def create_hazard_spot(x, y):
  # Hazard Spot 생성 로직
  information['x'] = x
  information['y'] = y
  information['status'] = "hazard"
  print(information)

def create_color_blob_spot(x, y):
  # Color Blob 생성 로직
  information['x'] = x
  information['y'] = y
  information['status'] = "color blob"
  print(information)

registered_functions = {
  "create_hazard_spot": create_hazard_spot,
  "create_color_blob_spot": create_color_blob_spot
}

functions = [
    {
        "name": "create_hazard_spot",
        "description": "x, y 좌표를 전달하면 위험 지점을 생성한다.",
        "parameters": {
            "type": "object",
            "properties": {
                "x": { "type": "number", "description": "x 좌표를 입력받는다." },
                "y": { "type": "number", "description": "y 좌표를 입력받는다." },
            },
            "required": ["x", "y"],
        }
    },
    {
        "name": "create_color_blob_spot",
        "description": "x, y 좌표를 전달하면 중요 지점을 생성한다.",
        "parameters": {
            "type": "object",
            "properties": {
                "x": { "type": "number", "description": "x 좌표를 입력받는다." },
                "y": { "type": "number", "description": "y 좌표를 입력받는다." },
            },
            "required": ["x", "y"],
        }
    }
]

record_voice.record()
audio_file = open("./assistant/output_xystatus.wav", "rb")

transcript = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{ "role": "user", "content": transcript.text }],
    functions=functions,
    function_call="auto"
)

if response.choices[0].message.function_call:
  name = response.choices[0].message.function_call.name
  args = json.loads(response.choices[0].message.function_call.arguments)

  registered_functions[name](args.get("x"), args.get("y"))
else:
  # 실패 처리 로직
  print("Failure")