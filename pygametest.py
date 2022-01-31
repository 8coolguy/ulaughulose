import pygame
import pygame.camera
import sys
from pygame import Color


pygame.init()
pygame.camera.init()
X =800
Y=600
webCam =pygame.camera.Camera(pygame.camera.list_cameras()[0],(X,Y))

screen=pygame.display.set_mode((X,Y))
pygame.display.set_caption("Web Cam Stream")

print(type(screen))
webCam.start()

frame = webCam.get_image()
while True:
    screen.blit(frame,(X/2,Y/2))
    pygame.display.update()
    frame =webCam.get_image()
    pygame.draw.rect(screen,Color(255,255,0,255),(397,21,0,230))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()




