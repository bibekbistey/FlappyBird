import pygame
import sys
from pygame.locals import *
import random

def obstacles():
    pipex=random.randint(250,550)
    top_pipe=pipe_img.get_rect(midtop=(660,pipex))
    bottom_pipe = pipe_img.get_rect(midbottom=(660, pipex-200))
    return top_pipe,bottom_pipe
def collision():
    global game_over,score_time
    for pipe in pipes:
        if pipe.bottom>636:
            #flipped_pipe=pygame.transform.flip(pipe_img,False,True)
            #screen.blit(flipped_pipe,pipe)
            screen.blit(pipe_img,pipe)
        else:
            #screen.blit(pipe_img,pipe)
            flip_pipe=pygame.transform.flip(pipe_img,False,True)
            screen.blit(flip_pipe,pipe)

        #screen.blit(pipe_img,pipe)
        pipe.centerx-=pipe_speed
        if bird_rect.colliderect(pipe):
            game_over=True
            score_time=True
            hit_sound.play()
pygame.init()

SCORE_FONT = pygame.font.Font('freesansbold.ttf', 32)

def score_display():
    display = SCORE_FONT.render(str (score), True, (255,255,255))
    score_rect=display.get_rect(center=(350,66))
    screen.blit(display,score_rect)
def score_update():
    global score, score_time, high_score
    if pipes:
        for pipe in pipes:
            if 65 < pipe.centerx < 69 and score_time:
                score += 1
                score_sound.play()

                score_time = False

            if pipe.left <= 0:
                score_time = True

    #if score > high_score:
        #high_score = score



clock = pygame.time.Clock()
fps = 40

width=664
height=636
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Flappy Bird')


#define game variables
moving_ground = 0
ground_speed = 4
gravity=0.60
bird_movement=0
pipe_height=[350,400,533,490]
pipe_speed=4

#load images
bg = pygame.image.load("bg.png")
ground_img = pygame.image.load("ground.png")
bird_img=pygame.image.load("bird1.png")
bird_rect=bird_img.get_rect(center=(67,622/2))
pipe_img=pygame.image.load("pipe.png")
pipes=[]
create_pipes=pygame.USEREVENT+1
pygame.time.set_timer(create_pipes,1800)
#game over
game_over=False
game_over_image=pygame.image.load("restart.png")
game_over_rect=game_over_image.get_rect(center=(width//2,height//2))
# score
score=0
high_score=0
score_time=True
score_sound = pygame.mixer.Sound("score.wav")
#flap_sound = pygame.mixer.Sound("sounds/wing.wav")
fall_sound = pygame.mixer.Sound("Fall.wav")
hit_sound = pygame.mixer.Sound("Hit_sound.wav")


run = True
while run:

    clock.tick(fps)

    #draw background
    screen.blit(bg, (0,0))
    #Adding bird
    screen.blit(bird_img,bird_rect)
    #Adding obstacles
    #screen.blit(pipe_img,(300,100))

    #draw and move the ground
    screen.blit(ground_img, (moving_ground, 568))
    moving_ground -= ground_speed
    if abs(moving_ground) > 35:
        moving_ground = 0
        # moving bird




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==pygame.K_SPACE and not game_over  :
                bird_movement=0
                bird_movement=-7
            if event.key == pygame.K_SPACE and game_over :
                bird_rect=bird_img.get_rect(center=(67,622/2))
                bird_movement=0
                pipes=[]
                game_over=False
                score=0
                score_time=True

        if event.type==create_pipes:
            pipes.extend(obstacles())
    if not game_over:

        bird_movement += gravity

        bird_rect.centery += bird_movement

        #rotated_bird = pygame.transform.rotozoom(bird_image, bird_movement * -6, 1)

        if bird_rect.top <= 5:
            game_over = True
            fall_sound.play()


        if bird_rect.bottom >= 550:
            game_over = True




        collision()
        score_display()
        score_update()

    elif game_over:
        screen.blit(game_over_image, game_over_rect)


    #bird_movement += gravity
    #bird_rect.centery += bird_movement



    #collision()
        #obstacles()
    pygame.display.update()

pygame.quit()
