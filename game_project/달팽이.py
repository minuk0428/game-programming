import pygame
import random as r

SCREEN_WIDTH = 1000
SCREEN_HEIGHT  = 950

pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snail Racing Game")

clock = pygame.time.Clock()

player_blue = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/game_project/파란달팽이.png")
player_blue = pygame.transform.scale(player_blue, (100, 100))
player_blue2 = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/game_project/파란달팽이.png")
player_blue2 = pygame.transform.scale(player_blue, (70, 70))

player_pink = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/game_project/분홍달팽이.png")
player_pink = pygame.transform.scale(player_pink, (100, 100))
player_pink2 = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/game_project/분홍달팽이.png")
player_pink2 = pygame.transform.scale(player_pink, (70, 70))

player_red = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/game_project/빨간달팽이.png")
player_red = pygame.transform.scale(player_red, (100, 100))
player_red2 = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/game_project/빨간달팽이.png")
player_red2 = pygame.transform.scale(player_red, (70, 70))

player_green = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/game_project/초록달팽이.png")
player_green = pygame.transform.scale(player_green, (100, 100))
player_green2 = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/game_project/초록달팽이.png")
player_green2 = pygame.transform.scale(player_green, (70, 70))

player_yellow = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/game_project/노란달팽이.png")
player_yellow = pygame.transform.scale(player_yellow, (100, 100))
player_yellow2 = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/game_project/노란달팽이.png")
player_yellow2 = pygame.transform.scale(player_yellow, (70, 70))

background = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/game_project/배경.jpg")
background = pygame.transform.scale(background,(1000,800))
road = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/game_project/길.png")
road = pygame.transform.scale(road,(1000,500))

player_Rect_blue = player_blue.get_rect()
player_Rect_blue2 = player_blue2.get_rect()

player_Rect_pink = player_pink.get_rect()
player_Rect_pink2 = player_pink2.get_rect()

player_Rect_yellow = player_yellow.get_rect()
player_Rect_yellow2 = player_yellow2.get_rect()

player_Rect_green = player_green.get_rect()
player_Rect_green2 = player_green2.get_rect()

player_Rect_red = player_red.get_rect()
player_Rect_red2 = player_red2.get_rect()

player_Rect_pink.centerx = round(100)
player_Rect_pink.centery = round(70)
player_Rect_red.centerx = round(100)
player_Rect_red.centery = round(230)
player_Rect_yellow.centerx = round(100)
player_Rect_yellow.centery = round(390)
player_Rect_blue.centerx = round(100)
player_Rect_blue.centery = round(550)
player_Rect_green.centerx = round(100)
player_Rect_green.centery = round(710)

player_Rect_blue2.centerx = 80
player_Rect_blue2.centery = 880
player_Rect_pink2.centerx = 160
player_Rect_pink2.centery = 880
player_Rect_red2.centerx = 240
player_Rect_red2.centery = 880
player_Rect_green2.centerx = 320
player_Rect_green2.centery = 880
player_Rect_yellow2.centerx = 400
player_Rect_yellow2.centery = 880

dx = 0
dy = 0

def r_move():
    dx = r.randint(-1,7)
    # print(dx)
    return dx
sysfont = pygame.font.SysFont(None, 36)
rank=0
ranks={}
playing = True
win = 0
my = 0
move = 0
player_blue3 = False
player_red3 = False
player_yellow3 = False
player_green3 = False
player_pink3 = False

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()
        if not player_blue3 and not player_red3 and not player_yellow3 and not player_green3 and not player_pink3:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print(event.pos[0], event.pos[1])
                for player in (player_Rect_blue2,player_Rect_pink2,player_Rect_red2,player_Rect_yellow2,player_Rect_green2):
                    if player.collidepoint(event.pos):
                        print("okokok")
                        if player == player_Rect_blue2 :
                            player_blue3 = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/game_project/파란달팽이.png")
                            player_blue3 = pygame.transform.scale(player_blue, (70, 70))
                        elif player == player_Rect_red2 :
                            player_red3 = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/game_project/빨간달팽이.png")
                            player_red3 = pygame.transform.scale(player_red, (70, 70))
                        elif player == player_Rect_yellow2 :
                            player_red3 = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/game_project/노란달팽이.png")
                            player_red3 = pygame.transform.scale(player_yellow, (70, 70))
                        elif player == player_Rect_green2 :
                            player_red3 = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/game_project/초록달팽이.png")
                            player_red3 = pygame.transform.scale(player_green, (70, 70))
                        elif player == player_Rect_pink2 :
                            player_red3 = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/game_project/분홍달팽이.png")
                            player_red3 = pygame.transform.scale(player_pink, (70, 70))
                        move = 1

    SCREEN.blit(background,(0,0))
    SCREEN.blit(road,(0,300))
    SCREEN.blit(road,(0,140))
    SCREEN.blit(road,(0,-20))
    SCREEN.blit(road,(0,-180))
    SCREEN.blit(road,(0,-340))

    if move == 1:
        if 'blue' not in ranks:
            if player_Rect_blue.x <= 830:
                player_Rect_blue.x += r_move()
            else:
                ranks['blue']=rank+1
                rank+=1

        if 'green' not in ranks:
            if player_Rect_green.x <= 830:
                player_Rect_green.x += r_move()
            else:
                ranks['green']=rank+1
                rank+=1

        if 'pink' not in ranks:
            if player_Rect_pink.x <= 830:
                player_Rect_pink.x += r_move()
            else:
                ranks['pink']=rank+1
                rank+=1
        
        if 'yellow' not in ranks:
            if player_Rect_yellow.x <= 830:
                player_Rect_yellow.x += r_move()
                # print("노란달팽이 승")
            else:
                ranks['yellow']=rank+1
                rank+=1
        if 'red' not in ranks:
            if player_Rect_red.x <= 830:
                player_Rect_red.x += r_move()
                # print("빨간달팽이 승")
            else:
                ranks['red']=rank+1
                rank+=1




    score_image = sysfont.render("which one is fast?",True, ('yellow'))
    my_pick = sysfont.render("MY PICK",True, ('yellow'))
    st_1 = sysfont.render("1.st ",True, ('yellow'))
    SCREEN.blit(player_blue, player_Rect_blue)
    SCREEN.blit(player_yellow, player_Rect_yellow)
    SCREEN.blit(player_pink, player_Rect_pink)
    SCREEN.blit(player_green, player_Rect_green)
    SCREEN.blit(player_red, player_Rect_red)

    SCREEN.blit(player_blue2, player_Rect_blue2)
    SCREEN.blit(player_pink2, player_Rect_pink2)
    SCREEN.blit(player_red2, player_Rect_red2)
    SCREEN.blit(player_green2, player_Rect_green2)
    SCREEN.blit(player_yellow2, player_Rect_yellow2)

    if player_blue3 :
        SCREEN.blit(player_blue3, (550,840,80,80))
        my = 4
    elif player_red3 :
        my = 2
        SCREEN.blit(player_red3, (550,840,80,80))
    elif player_yellow3 :
        my = 5
        SCREEN.blit(player_yellow3, (550,840,80,80))
    elif player_green3 :
        my = 1
        SCREEN.blit(player_green3, (550,840,80,80))
    elif player_pink3 :
        my = 3
        SCREEN.blit(player_pink3, (550,840,80,80))


        
    for key,value in ranks.items():
        print(f'{key}달팽이 는 {value}등입니다.')
        
        if value == 1:              
            if key == 'green':
                SCREEN.blit(player_green2, (700,840,80,80))
                win = 1
            elif key == 'red':
                SCREEN.blit(player_red2, (700,840,80,80))
                win = 2
            elif key == 'pink':
                SCREEN.blit(player_pink2, (700,840,80,80))
                win = 3
            elif key == 'blue':
                SCREEN.blit(player_blue2, (700,840,80,80))
                win = 4
            elif key == 'yellow':
                SCREEN.blit(player_yellow2, (700,840,80,80))
                win = 5
            if my == win:
                winlose = sysfont.render("WIN",True, ('yellow'))
                SCREEN.blit(winlose, (850, 860))
            else:   
                winlose = sysfont.render("LOSE",True, ('yellow'))
                SCREEN.blit(winlose, (850, 860))
    
    win_lose = sysfont.render("WIN OR LOSE",True, ('yellow'))
    SCREEN.blit(win_lose, (820, 810))
    SCREEN.blit(score_image, (150, 810))
    SCREEN.blit(my_pick, (550, 810))
    SCREEN.blit(st_1, (700, 810))
    pygame.display.flip()

    clock.tick(30)