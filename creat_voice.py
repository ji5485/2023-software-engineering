from gtts import gTTS

voices = {
    'input_x': "X 좌표를 입력해주세요.",
    'input_y': "Y 좌표를 입력해주세요.",
    'input_status': "해당 지점의 상태를 입력해주세요.",
    'input_complete': "완료되었습니다."
}

for name, text in voices.items():
    tts = gTTS(text=text, lang='ko')
    tts.save(f'{name}.mp3')
