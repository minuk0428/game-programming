""" mine_sweeper.py - Copyright 2016 Kenichiro Tanaka  """
import sys
from math import floor
from random import randint
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
import pygame_menu
count_P = "OPEN_COUNT:"
WIDTH = 20
HEIGHT = 15
SIZE = 50
NUM_OF_BOMBS = 40
EMPTY = 0
BOMB = 1
OPENED = 2
OPEN_COUNT = 0

c = 0
time_str = "Timer"
start_ticks = pygame.time.get_ticks() 
CHECKED = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

pygame.init()
SURFACE = pygame.display.set_mode([WIDTH*SIZE+ 300, HEIGHT*SIZE])
surface = pygame.display.set_mode((600,400))
FPSCLOCK = pygame.time.Clock()




def level(self, value):
    print("LEVEL CHOICE: ",value)
    
def start():
    print("GAME_START")

def num_of_bomb(field, x_pos, y_pos):
    """ 주위에 있는 폭탄 수를 반환한다 """
    count = 0
    for yoffset in range(-1, 2):
        for xoffset in range(-1, 2):
            xpos, ypos = (x_pos + xoffset, y_pos + yoffset)
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and \
                field[ypos][xpos] == BOMB:
                count += 1
    return count

def open_tile(field, x_pos, y_pos):
    """ 타일을 오픈 """
    global OPEN_COUNT
    if CHECKED[y_pos][x_pos]:  # 이미 확인된 타일
        return

    CHECKED[y_pos][x_pos] = True

    for yoffset in range(-1, 2):
        for xoffset in range(-1, 2):
            xpos, ypos = (x_pos + xoffset, y_pos + yoffset)
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and \
                field[ypos][xpos] == EMPTY:
                field[ypos][xpos] = OPENED
                OPEN_COUNT += 1
                count = num_of_bomb(field, xpos, ypos)
                if count == 0 and \
                    not (xpos == x_pos and ypos == y_pos):
                    open_tile(field, xpos, ypos)

def main():
    """ 메인 루틴 """
    global c
    while c == 0:
        t = pygame_menu.themes.THEME_BLUE;
        t.widget_font = pygame.font.SysFont("gulim",30)
        c = 1
    
    smallfont = pygame.font.SysFont(None, 36)
    largefont = pygame.font.SysFont(None, 72)
    message_clear = largefont.render("!!CLEARED!!",
                                     True, (0, 255, 225))
    message_over = largefont.render("GAME OVER!!",
                                    True, (0, 255, 225))
    message_rect = message_clear.get_rect()
    message_rect.center = (WIDTH*SIZE/2, HEIGHT*SIZE/2)
    game_over = False

    field = [[EMPTY for xpos in range(WIDTH)]
             for ypos in range(HEIGHT)]

    # 폭탄을 설치
    count = 0
    while count < NUM_OF_BOMBS:
        xpos, ypos = randint(0, WIDTH-1), randint(0, HEIGHT-1)
        if field[ypos][xpos] == EMPTY:
            field[ypos][xpos] = BOMB
            count += 1

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and \
                event.button == 1:
                xpos, ypos = floor(event.pos[0] / SIZE),\
                             floor(event.pos[1] / SIZE)
                if field[ypos][xpos] == BOMB:
                    game_over = True
                else:
                    open_tile(field, xpos, ypos)

        # 그리기
        
        menu = pygame_menu.Menu("Menu",400,300, theme = t)
        menu.add.selector("LEVEL ",[("EASY",1),("NOMAL",2),("HARD",3)],onchange=level)
        menu.add.button("GAME_EXIT", pygame_menu.events.EXIT)
        menu.mainloop(surface)
        
        SURFACE.fill((0, 0, 0))
        elapsed_time = (pygame.time.get_ticks() - start_ticks) // 1000
        time_print = smallfont.render( "{}".format(time_str), True, (255, 255, 0))
        SURFACE.blit(time_print,(1020,20))
        count_time = smallfont.render( "{}".format(elapsed_time), True, (255, 255, 0))
        SURFACE.blit(count_time,(1120,20))
        count_print = smallfont.render( "{}".format(count_P), True, (255, 255, 0))
        SURFACE.blit(count_print,(1020,100))
        count_image = smallfont.render( "{}".format(OPEN_COUNT), True, (255, 255, 0))
        SURFACE.blit(count_image,(1220,100))
        for ypos in range(HEIGHT):
            for xpos in range(WIDTH):
                tile = field[ypos][xpos]
                rect = (xpos*SIZE, ypos*SIZE, SIZE, SIZE)

                if tile == EMPTY or tile == BOMB:
                    pygame.draw.rect(SURFACE,
                                     (192, 192, 192), rect)
                    if game_over and tile == BOMB:
                        pygame.draw.ellipse(SURFACE,
                                            (225, 225, 0), rect)
                elif tile == OPENED:
                    count = num_of_bomb(field, xpos, ypos)
                    if count > 0:
                        num_image = smallfont.render(
                            "{}".format(count), True, (255, 255, 0))
                        SURFACE.blit(num_image,
                                     (xpos*SIZE+10, ypos*SIZE+10))

        # 선 그리기
        for index in range(0, WIDTH*SIZE, SIZE):
            pygame.draw.line(SURFACE, (96, 96, 96),
                             (index, 0), (index, HEIGHT*SIZE))
        for index in range(0, HEIGHT*SIZE, SIZE):
            pygame.draw.line(SURFACE, (96, 96, 96),
                             (0, index), (WIDTH*SIZE, index))

        # 메시지 나타내기
        if OPEN_COUNT == WIDTH*HEIGHT - NUM_OF_BOMBS:
            SURFACE.blit(message_clear, message_rect.topleft)
        elif game_over:
            SURFACE.blit(message_over, message_rect.topleft)

        pygame.display.update()
        FPSCLOCK.tick(15)

if __name__ == '__main__':
    main()
