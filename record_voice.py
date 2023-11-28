import threading

import pyaudio
import wave
import os
import play_voice

CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_DIRECTORY = r'assistant'
os.makedirs(WAVE_OUTPUT_DIRECTORY, exist_ok=True)


def record(type):
    WAVE_OUTPUT_FILENAME = os.path.join(WAVE_OUTPUT_DIRECTORY, f'output_{type}.wav')

    p = pyaudio.PyAudio()

    thread = threading.Thread(target=play_voice.play, args=(type,))

    thread.start()
    thread.join()

    frames = []
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    play_voice.play('complete')

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()