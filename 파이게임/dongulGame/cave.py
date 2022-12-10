""" cave - Copyright 2016 Kenichiro Tanaka  """
from curses import KEY_DOWN, KEY_UP
import sys
from random import randint
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE

import random as r

pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((800, 600)) # 게임이 진행될 화면
FPSCLOCK = pygame.time.Clock()  #프레임 레이트(속도) 조절용 타이머

def main():
    """ 메인 루틴 """
    color = ["Red","White","Green","Blue","Yellow"]
    color_random = r.choice(color)
    color_random2 = ""
    last_score = 0
    walls = 60
    ship_y = 500
    ship_x = 250
    velocity = 0
    score = 0
    slope = randint(3, 30)  #동굴의 기울기
    sysfont = pygame.font.SysFont(None, 36)
    ship_image = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/파이게임/dongulGame/도전과제 리소스/shipv.png")
    bang_image = pygame.image.load("/Users/imin-ug/Python/게임프로그래밍/파이게임/dongulGame/bang.png")
    holes = []  # 맵의 직사각형을 저장하는 배열
    for ypos in range(walls):
        holes.append(Rect(10, ypos * 10, 800, 10))
    game_over = False

    while True:
        color_random2 = color_random 
        is_space_down = False
        is_up_arrow = False
        is_down_arrow = False
        is_right_arrow = False
        is_left_arrow = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    is_space_down = True
                elif event.key == pygame.K_DOWN:
                    is_down_arrow = True
                elif event.key == pygame.K_UP:
                    is_up_arrow = True
                elif event.key == pygame.K_LEFT:
                    is_left_arrow = True
                elif event.key == pygame.K_RIGHT:
                    is_right_arrow = True


        # 내 캐릭터를 이동
        if not game_over:
            score += 10
            #velocity += -3 if is_space_down else 3
            #ship_y += velocity
            if is_down_arrow:
                ship_y += 6
            elif is_up_arrow:
                ship_y += -6
            elif is_right_arrow:
                ship_x += 6
            elif is_left_arrow:
                ship_x += -6
            # 동굴을 스크롤
            edge = holes[0].copy()
            test = edge.move(slope, 0)
            if test.left <= 0 or test.right >= 800:
                slope = randint(3, 30) * (-1 if slope > 0 else 1)
                edge.inflate_ip(-20, 0)
            edge.move_ip(slope, -10)
            holes.insert(0,edge)
            del holes[-1]
            holes = [y.move(0, 10) for y in holes]  # 이부분 동글스크롤 예정

            # 충돌?
            '''
            if holes[0].top > ship_y or \
                holes[0].bottom < ship_y + 80:
                last_score = str(score)
                f = open("/Users/imin-ug/Python/게임프로그래밍/파이게임/dongulGame/score_cave.txt",'w')
                f.write(last_score)
                game_over = True
                f.close()
               '''
            if holes[-1].left > ship_x or \
                holes[-1].right < ship_x + 60:
                last_score = str(score)
                    
                # f = open('/Users/imin-ug/Python/게임프로그래밍/파이게임/dongulGame/score_cave.txt', 'r')
                # a = int(f.readlines())
                
                # if last_score < a:
                #      f.write(str(a))
                
                    
                    
                
                f = open("/Users/imin-ug/Python/게임프로그래밍/파이게임/dongulGame/score_cave.txt",'w')
                f.write(last_score)
                print(ship_x, holes[-1])
                game_over = True
                f.close()

        # 그리기
        

        if score % 1000 == 0 :
            while color_random == color_random2:
                color_random = r.choice(color)
                SURFACE.fill((color_random))  #배경 색깔 
        else:
            SURFACE.fill((color_random))  #배경 색깔 
            
        for hole in holes:
            pygame.draw.rect(SURFACE, (0, 0, 0), hole)
        #SURFACE.blit(ship_image, (0, ship_y))
        SURFACE.blit(ship_image, (ship_x, ship_y))
        score_image = sysfont.render("score is {}".format(score),
                                     True, (0, 0, 225))
        SURFACE.blit(score_image, (600, 20))

        if game_over:
            #SURFACE.blit(bang_image, (0, ship_y-40))
            SURFACE.blit(bang_image, (ship_x-40, ship_y-40))

        pygame.display.update()
        FPSCLOCK.tick(15)

if __name__ == '__main__':
    main()
