import threading

import record_voice
import google_speech_to_text

def parallel_transcription(file_keys):
    threads = []

    for file_key in file_keys:
        thread = threading.Thread(target=google_speech_to_text.transcribe_audio, args=(file_key,))
        threads.append(thread)
        thread.start()

    # 모든 스레드의 종료를 기다림
    for thread in threads:
        thread.join()

    print(google_speech_to_text.information)

def get_information_result():
    file_keys = []
    for key, item in google_speech_to_text.information.items():
        if not item['completed']:
            record_voice.record(key)
            file_keys.append(key)

    parallel_transcription(file_keys)

def check_finish():
    for item in google_speech_to_text.information.values():
        if not item['completed']:
            return False
    return True

def command():
    while not check_finish():
        get_information_result()

    return {
        'x': google_speech_to_text.information['x']['result'],
        'y': google_speech_to_text.information['y']['result'],
        'status': google_speech_to_text.information['status']['result'],
    }

if __name__ == "__main__":
    while not check_finish():
        get_information_result()