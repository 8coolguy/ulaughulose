import pygame
import pygame.camera
import sys



pygame.init()
pygame.camera.init()
X =800
Y=600
webCam =pygame.camera.Camera(pygame.camera.list_cameras()[0],(X,Y))

screen=pygame.display.set_mode((X,Y))
pygame.display.set_caption("Web Cam Stream")

webCam.start()

frame = webCam.get_image()
while True:
    screen.blit(frame,(X/2,Y/2))
    pygame.display.update()
    frame =webCam.get_image()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()




