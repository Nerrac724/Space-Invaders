import pygame
import random

#Basic Display, title and icon
pygame.init()
pygame.display.set_caption("Heroes of the Storm")
screen = pygame.display.set_mode((1280,720))
icon = pygame.image.load("startup.png")
pygame.display.set_icon(icon)

#Background
background = pygame.image.load("background.jpg")

#Player Model
playerIMG = pygame.image.load("spaceship.png")
playerX = 600
playerY = 620
playerX_change = 0
playerY_change = 0
def player(x, y):
    screen.blit(playerIMG,(x, y))

#Enemy Model
enemyIMG = pygame.image.load("alien.png")
enemyX = random.randint(0,1216)
enemyY = random.randint(0,100)
enemyX_change = 0.3
enemyY_change = 40
def enemy(x, y):
    screen.blit(enemyIMG,(x, y))

#All running states for the game
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -0.7
            if event.key == pygame.K_d:
                playerX_change = 0.7
            if event.key == pygame.K_s:
                playerY_change = 0.7
            if event.key == pygame.K_w:
                playerY_change = -0.7
            if event.key == pygame.K_a and event.key == pygame.K_w:
                playerY_change = -0.7
                playerX_change = -0.7
            if event.key == pygame.K_d and event.key == pygame.K_w:
                playerY_change = -0.7
                playerX_change = 0.7
            if event.key == pygame.K_a and event.key == pygame.K_s:
                playerY_change = 0.7
                playerX_change = -0.7
            if event.key == pygame.K_d and event.key == pygame.K_s:
                playerY_change = 0.7
                playerX_change = 0.7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_s or event.key == pygame.K_w:
                playerY_change=0
                playerX_change=0
    
    #Player Movement
    playerX += playerX_change
    playerY += playerY_change
    if playerX <=0:
        playerX =0
    elif playerX>=1216:
        playerX = 1216
    if playerY <=0:
        playerY =0
    elif playerY>=656:
        playerY = 656

    #Enemy Movement
    enemyX += enemyX_change
    if enemyX <=0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX>=1216:
        enemyX_change = -0.3
        enemyY += enemyY_change

    #Upadting information everytime
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()