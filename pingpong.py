import pygame
import os
import random
window = pygame.display.set_mode((500,500))
x=random.randint(50,100)
y=random.randint(50,450)
lose=False

player1_x=0
player1_y=0

player2_x=490
player2_y=0

run=True
def change_window():
    if lose:
        window.blit(pygame.image.load(os.path.join("F:","10.jpg")),(-175,0))
        pygame.display.update()
    else:
        window.fill((0,0,0))
        pygame.draw.circle(window, (255, 0, 0), (x, y),10)
        pygame.draw.rect(window,(255,255,0),(player1_x,player1_y,10,60))
        pygame.draw.rect(window, (255, 255, 0), (player2_x, player2_y, 10, 60))
        pygame.display.update()

velocity=5

x_dir=1
y_dir=1


def collide(player,x,y):
    global y_dir,x_dir,lose
    if player==1:
        if x-10<=player1_x+10 and y>=player1_y and y<=player1_y+60:
            x_dir*=-1
            return True
    if player==2:
        if x+10>=player2_x and y>=player2_y and y<=player2_y+60:
            x_dir*=-1
            return True
    lose=True

while run:
    pygame.time.delay(50)
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            run=False
    x+=velocity*x_dir
    y+=velocity*y_dir
    keys=pygame.key.get_pressed()

    if keys[pygame.K_UP] and player2_y>0:
        player2_y-=5
    if keys[pygame.K_DOWN] and player2_y<440:
        player2_y+=5

    if keys[pygame.K_w] and player1_y>0:
        player1_y-=5
    if keys[pygame.K_s] and player1_y<440:
        player1_y+=5


    if x>=490-10 and x<=510:
       if collide(2,x,y):
           velocity+=1
    if x>510 or x<0:
        lose=True
    if x<20 and x>=0:
        if collide(1,x,y):
            velocity+=1
    if y>500:
        y=490
        y_dir=-1
    if y<0:
        y=10
        y_dir=1
    change_window()
