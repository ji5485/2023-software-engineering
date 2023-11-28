import record_voice
import google_speech_to_text

def transcription():
    google_speech_to_text.transcribe_audio()

    print(google_speech_to_text.information)

def get_information_result():
    record_voice.record()

    transcription()

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
