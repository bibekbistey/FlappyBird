import pygame
import sys
from pygame.locals import *
pygame.init()

screen=pygame.display.set_mode((350,622))
pygame.display.set_caption("Flappy bird")

bg_img=pygame.image.load("bg.png")

ground_img=pygame.image.load("ground.png")
bird_img=pygame.image.load("bird1.png")
bird_rect=bird_img.get_rect(center=(67,622//2))

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bg_img,(0,0))
    screen.blit(ground_img,(0,550))
    pygame.display.update()




