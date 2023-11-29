import pygame

def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

input_start = "input_start.mp3"
input_complete = "input_complete.mp3"

def play(type):
    if type == 'start':
        play_mp3(input_start)
    elif type == 'complete':
        play_mp3(input_complete)

    # MP3 파일이 실행될 동안 다른 작업을 보류
    while pygame.mixer.music.get_busy():
        pass
