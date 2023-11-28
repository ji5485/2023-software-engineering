import io
from google.cloud import speech
from parse import *

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

patterns = [
    "x 좌표 {x} y 좌표 {y} {status}",
    "X 좌표 {x} y 좌표 {y} {status}",
    "x 좌표 {x} Y 좌표 {y} {status}",
    "X 좌표 {x} Y 좌표 {y} {status}",
]
def transcribe_audio():
    print('start')
    file_path = f'./assistant/output_xystatus.wav'
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

    if response.results:
        print(f"Google API 호출 성공: {len(response.results)} 개의 결과가 반환되었습니다.")
    else:
        print("Google API 호출 실패: 결과가 없습니다.")
    # 문장에 대한 파싱 결과를 추출
    for result in response.results:
        for pattern in patterns:
            parsed_result = parse(pattern, result.alternatives[0].transcript)
            if parsed_result:
                print(f"파싱된 결과: {parsed_result.named}")
                break
        # 파싱 성공하면 해당 정보를 저장하고 completed를 True로 설정
        if parsed_result:
            for key in information.keys():
                if key in parsed_result.named.keys():
                    information[key]['result'] = parsed_result.named[key]
                    check_result_validation()
        else:
            print(file_path, 'Parsing failed for:', result.alternatives[0].transcript)



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