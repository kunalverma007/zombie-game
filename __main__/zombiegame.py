import pygame
from pygame.locals import *
import random

pygame.init()

width = 800
height = 500

red = 255,0,0

bg_img = pygame.image.load('images/background.png')
zombie_1 = pygame.image.load('images/zombie_1.png')
zombie_2 = pygame.image.load('images/zombie_2.png')
zombie_3 = pygame.image.load('images/zombie_3.png')
zombie_4 = pygame.image.load('images/zombie_4.png')

zombie_images = [zombie_1, zombie_2, zombie_3, zombie_4]

player_gun = pygame.image.load('images/gun_1.png')
gun_pointer = pygame.image.load('images/aim_pointer.png')

gun_shot = pygame.mixer.Sound('sounds/gunShot.wav')

bg_music = pygame.mixer.Sound('sounds/ve_music.wav')
bg_music.play(-1)

screen = pygame.display.set_mode((width,height))

def score(counter):
    font = pygame.font.SysFont(None, 40)
    text = font.render("Score : "+str(counter), True, red)
    screen.blit(text,(20,20))

def timer(time):
    font = pygame.font.SysFont(None, 40)
    text = font.render("Time Left : "+str(time), True, red)
    screen.blit(text,(width-200,20))

def homeScreen():
    font = pygame.font.SysFont(None,50)
    text = font.render("Press SPACE to start game",True, red)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()

        screen.blit(bg_img, (0,0))
        screen.blit(text,(200,100))

        pygame.display.update()

def main():
    zombie = random.choice(zombie_images)
    zombie_x = random.randint(0, width - 250)
    zombie_y = random.randint(0, height - 250)
    player_x = 0
    counter = 0
    pygame.time.set_timer(USEREVENT, 1000)
    seconds = 30
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == USEREVENT:
                seconds -= 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                gun_shot.play()
                if zombie_rect.colliderect(aim_rect):
                    zombie = random.choice(zombie_images)
                    zombie_x = random.randint(0, width - 250)
                    zombie_y = random.randint(0, height - 250)
                    print("Collision Detection")
                    counter += 1

        if seconds == 0:
            break

        pos_x,pos_y = pygame.mouse.get_pos()

        screen.blit(bg_img,(0,0))
        screen.blit(zombie, (zombie_x, zombie_y))
        screen.blit(player_gun, (pos_x, height-300))
        screen.blit(gun_pointer, (pos_x - 50,pos_y - 50))

        zombie_rect = pygame.Rect(zombie_x, zombie_y, zombie.get_width(), zombie.get_height())
        aim_rect = pygame.Rect(pos_x - 50,pos_y - 50,gun_pointer.get_width(), gun_pointer.get_height())

        score(counter)
        timer(seconds)

        pygame.display.update()

# homeScreen()
main()