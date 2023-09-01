import pygame , random

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 710

screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Snake Xenzia")

#fps
FPS = 15
clock = pygame.time.Clock()
#values
SNAKE_SIZE = 20
head_x = WINDOW_WIDTH//2
head_y = WINDOW_HEIGHT//2

snake_dx = 0
snake_dy = 0

score = 0
#colors
GREEN = (0,255,0)
DRGREEN = (10,50,10)
RED = (255,0,0)
DRRED = (150,0,0)
WHITE = (255,255,255) 
#fonts
font = pygame.font.SysFont("gabriola",48)

#txt
title_txt = font.render("Snake",True,GREEN,DRRED)
title_rect = title_txt.get_rect(center = (WINDOW_WIDTH//2,30))

score_txt = font.render("Score: " + str(score),True,GREEN,DRRED)
score_rect = score_txt.get_rect(topleft = (10,50))

game_over_txt = font.render("Game Over",True,RED,DRGREEN)
game_over_rect = game_over_txt.get_rect(center = (WINDOW_WIDTH//2,WINDOW_HEIGHT//2))
continue_txt = font.render("Press any key to play again",True,RED,DRGREEN)
continue_rect = continue_txt.get_rect(center = (WINDOW_WIDTH//2,WINDOW_HEIGHT//2+60))
#music

pck_snd = pygame.mixer.Sound("pick_up_sound.wav")

#img
#(topx,topy,wdth,ht)
apple_coord = (500,500,SNAKE_SIZE,SNAKE_SIZE)
head_coord = (head_x,head_y,SNAKE_SIZE,SNAKE_SIZE)
body_coords = []

apple_rect = pygame.draw.rect(screen,RED,apple_coord)
head_rect = pygame.draw.rect(screen,GREEN,head_coord)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
                snake_dx = -1*SNAKE_SIZE
                snake_dy = 0
            if (event.key == pygame.K_RIGHT) or (event.key ==  pygame.K_d):
                snake_dx = SNAKE_SIZE
                snake_dy = 0
            if (event.key == pygame.K_UP) or (event.key == pygame.K_w):
                snake_dx = 0
                snake_dy = -1*SNAKE_SIZE
            if (event.key == pygame.K_DOWN )or (event.key == pygame.K_s):
                snake_dx = 0
                snake_dy = SNAKE_SIZE

    #add head to 1st indedx of body
    body_coords.insert(0,head_coord)
    body_coords.pop()
    #updating pos of snakes head
    head_x += snake_dx
    head_y += snake_dy
    head_coord = (head_x,head_y,SNAKE_SIZE,SNAKE_SIZE)

    #game_over
    if head_rect.left<0 or head_rect.right>WINDOW_WIDTH or head_rect.top<110 or head_rect.bottom>WINDOW_HEIGHT or head_coord in body_coords:
        screen.fill(WHITE)
        pygame.draw.line(screen,(0,0,0),(0,110),(WINDOW_WIDTH,110),3)
        screen.blit(title_txt,title_rect)
        screen.blit(score_txt,score_rect)
        screen.blit(game_over_txt,game_over_rect)
        screen.blit(continue_txt,continue_rect)
        pygame.display.update()
        is_paused = True
        while is_paused:
            for ev in pygame.event.get():
                if ev.type == pygame.KEYDOWN:
                    is_paused = False
                    head_x = WINDOW_WIDTH//2
                    head_y = WINDOW_HEIGHT//2
                    apple_coord = (500,500,SNAKE_SIZE,SNAKE_SIZE)
                    head_coord = (head_x,head_y,SNAKE_SIZE,SNAKE_SIZE)
                    body_coords = []
                    snake_dx = 0
                    snake_dy = 0
                    score = 0
                if ev.type == pygame.QUIT:
                    running = False
                    is_paused = False
    

    #collision
    if head_rect.colliderect(apple_rect): 
        pck_snd.play()
        score += 1
        apple_x = random.randint(0,WINDOW_WIDTH-SNAKE_SIZE)
        apple_y = random.randint(110,WINDOW_HEIGHT)
        apple_coord = (apple_x,apple_y,SNAKE_SIZE,SNAKE_SIZE)
        body_coords.append(head_coord)
    score_txt = font.render("Score: "+str(score),True,GREEN,DRRED)

    screen.fill(WHITE)
    pygame.draw.line(screen,(0,0,0),(0,110),(WINDOW_WIDTH,110),3)
    screen.blit(title_txt,title_rect)
    screen.blit(score_txt,score_rect)
    
    #body pending
    for body in body_coords:
        pygame.draw.rect(screen,DRGREEN,body)
    head_rect = pygame.draw.rect(screen,GREEN,head_coord)
    apple_rect = pygame.draw.rect(screen,RED,apple_coord)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()