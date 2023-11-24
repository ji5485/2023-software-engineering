import io
from google.cloud import speech

information = {
    'x': {
        'result': None,
        'completed': False,
    },
    'y': {
        'result': None,
        'completed': False,
    },
    'status': {
        'result': None,
        'completed': False,
    }
}
def transcribe_audio(file_key):
    print('start', file_key)
    file_path = f'./assistant/output_{file_key}.wav'
    credentials_path = "./apiKey/probable-analog-404312-9a16ee9633f7.json"  # 키 파일의 경로를 지정합니다.
    client = speech.SpeechClient.from_service_account_file(credentials_path)

    with io.open(file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,  # 파일의 샘플링 속도에 맞게 설정
        language_code="ko-KR"  # 음성 언어 코드 설정 (한국어는 "ko-KR")
    )

    response = client.recognize(config=config, audio=audio)
    # 결과 출력
    for result in response.results:
        print(file_path, 'transcript: {}'.format(result.alternatives[0].transcript))
        information[file_key]['result'] = result.alternatives[0].transcript
        print(file_key, information[file_key], information[file_key]['result'])

    check_result_validation()

def check_result_validation():
    KOREAN_TO_NUMBERS = {
        '영': 0, '일': 1, '이': 2, '삼': 3, '사': 4, '오': 5, '육': 6, '칠': 7, '팔': 8, '구': 9, '십': 10
    }
    if not information['x']['completed']:
        value = information['x']['result']
        if type(value) is str:
            value = value.strip()
            if value.isnumeric():
                information['x']['result'] = int(value)
                information['x']['completed'] = True
            elif value in KOREAN_TO_NUMBERS.keys():
                information['x']['result'] = KOREAN_TO_NUMBERS[value]
                information['x']['completed'] = True
        else:
            information['x']['result'] = None

    if not information['y']['completed']:
        value = information['y']['result']
        if type(value) is str:
            value = value.strip()
            if value.isnumeric():
                information['y']['result'] = int(value)
                information['y']['completed'] = True
            elif value in KOREAN_TO_NUMBERS.keys():
                information['y']['result'] = KOREAN_TO_NUMBERS[value]
                information['y']['completed'] = True
        else:
            information['y']['result'] = None

    if not information['status']['completed']:
        value = information['status']['result']
        if type(value) is str:
            if value in ['위험지역', '위험 지역']:
                information['status']['result'] = 'hazard'
                information['status']['completed'] = True
            elif value in ['중요지역', '중요 지역']:
                information['status']['result'] = 'color blob'
                information['status']['completed'] = True
            else:
                information['status']['result'] = None