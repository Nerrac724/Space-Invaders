import pygame
import random
import math
from pygame import mixer

score=0

#Basic Display, title and icon
pygame.init()
pygame.display.set_caption("Heroes of the Storm")
screen = pygame.display.set_mode((1280,720))
icon = pygame.image.load("startup.png")
pygame.display.set_icon(icon)

#Background
background = pygame.image.load("background.jpg")
mixer.music.load('background.wav')
mixer.music.play(-1)

#Player Model
playerIMG = pygame.image.load("spaceship.png")
playerX = 600
playerY = 620
playerX_change = 0
playerY_change = 0
def player(x, y):
    screen.blit(playerIMG,(x, y))

#Enemy Model

enemyIMG = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 5
for i in range(num_of_enemies):
    enemyIMG.append(pygame.image.load("alien.png"))
    enemyX.append(random.randint(0,1216))
    enemyY.append(random.randint(0,100))
    enemyX_change.append(1.5)
    enemyY_change.append(60)
def enemy(x, y, i):
    screen.blit(enemyIMG[i],(x, y))

#Collision
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX,2)) +(math.pow(enemyY - bulletY,2)))
    if distance<35:
        return True


#Bullet Model
bulletIMG = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 620
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"
def fire_bullet(x,y):
    global bullet_state 
    bullet_state = "fire"
    screen.blit(bulletIMG,(x+16,y+10))

#Scoreboard
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
txt_X = 20
txt_Y = 20

def show_score(x, y):
    score  = font.render("Score: "+ str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))

#Game Over Text
Over_font = pygame.font.Font('freesansbold.ttf', 96)

def game_over_txt():
    over_text  = Over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (340, 620))


#All running states for the game
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    bulletY = playerY
                fire_bullet(bulletX, bulletY)
            if event.key == pygame.K_a:
                playerX_change = -2
            if event.key == pygame.K_d:
                playerX_change = 2
            if event.key == pygame.K_s:
                playerY_change = 2
            if event.key == pygame.K_w:
                playerY_change = -2
            if event.key == pygame.K_a and event.key == pygame.K_w:
                playerY_change = -2
                playerX_change = -2
            if event.key == pygame.K_d and event.key == pygame.K_w:
                playerY_change = -2
                playerX_change = 2
            if event.key == pygame.K_a and event.key == pygame.K_s:
                playerY_change = 2
                playerX_change = -2
            if event.key == pygame.K_d and event.key == pygame.K_s:
                playerY_change = 2
                playerX_change = 2
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

    #Bullet Movement
    if bulletY<=0:
        bullet_state = "ready"
        bulletY = 610

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    

    #Enemy Movement
    for i in range(num_of_enemies):

        if enemyY[i]>620:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_txt()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <=0:
            enemyX_change[i] = 1.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i]>=1216:
            enemyX_change[i] = -1.5
            enemyY[i] += enemyY_change[i]
        #Collision Mechanics
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            death_sound = mixer.Sound('explosion.wav')
            death_sound.play()
            bulletY = 620
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0,1216)
            enemyY[i] = random.randint(0,100)
        enemy(enemyX[i], enemyY[i], i)

    #Upadting information everytime
    player(playerX, playerY)
    show_score(txt_X, txt_Y)
    pygame.display.update()