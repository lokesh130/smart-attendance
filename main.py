import pygame
import time
import speech_recognition as sr
import os
import cv2
import sounddevice as sd
from scipy.io.wavfile import write
from scipy.io import wavfile
import numpy as np
import speaker as sp
display_width = 1366
display_height = 768

black = (0,0,0)
alpha = (0,88,255)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

pygame.init()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
mimg = pygame.image.load('img.jpg')


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',30)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()

def text_objects(text, font):
    textSurface = font.render(text, True, alpha)
    return textSurface, textSurface.get_rect()

def close():
    pygame.quit()
    quit()

def s2t():
    screen.blit(mimg,(0,0))

    pygame.mixer.music.load('recording-started.mp3')
    pygame.mixer.music.play(0)
    message_display("recording voice")

    time.sleep(2)
    fs = 16000
    seconds = 20
    data = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()

    y = (np.iinfo(np.int32).max * (data/np.abs(data).max())).astype(np.int32)
    write('test.wav', fs, y)

    screen.blit(mimg,(0,0))
    pygame.mixer.music.load('recorded-successfully.mp3')
    pygame.mixer.music.play(0)
    message_display("voice recorded successfully ")
    screen.blit(mimg,(0,0))

    time.sleep(3)
    str=sp.task_predict("test.wav", "model1.out")
    pygame.mixer.music.load('speaker-identified.mp3')
    pygame.mixer.music.play(0)

    img = pygame.image.load('pic\\'+str[1]+'.jpg')
    screen.blit(pygame.transform.scale(img, (200, 200)), (600, 150))
    message_display(str[0])

    pygame.mixer.music.load('welc\\i'+str[1]+'.mp3')
    pygame.mixer.music.play(0)

    time.sleep(10)



def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def main():
    stream = 'introv.mov'
    cap = cv2.VideoCapture(stream)
    ret, img = cap.read()
    img = cv2.transpose(img)

    surface = pygame.surface.Surface((img.shape[0], img.shape[1]))

    pygame.mixer.music.load('introa.mp3')
    pygame.mixer.music.play(0)

    done = False
    while not done:
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        ret, img = cap.read()
        if not ret:
            done = True
            break
        else:
            img = cv2.transpose(img)
            pygame.surfarray.blit_array(surface, img)
            screen.blit(surface, (0,0))

    pygame.mixer.music.load('a1.mp3')
    pygame.mixer.music.play(0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(mimg,(0,0))
        button("Speak!",450,650,100,50,green,bright_green,s2t)
        button("Quit",750,650,100,50,red,bright_red,close)
        pygame.display.update()


    pygame.quit()


if __name__ == '__main__':
    main()
