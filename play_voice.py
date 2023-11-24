import pygame

def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

input_x = "input_x.mp3"
input_y = "input_y.mp3"
input_status = "input_status.mp3"
input_complete = "input_complete.mp3"

def play(type):
    if type == 'x':
        play_mp3(input_x)
    elif type == 'y':
        play_mp3(input_y)
    elif type == 'status':
        play_mp3(input_status)
    elif type == 'complete':
        play_mp3(input_complete)

    # MP3 파일이 실행될 동안 다른 작업을 보류
    while pygame.mixer.music.get_busy():
        pass
