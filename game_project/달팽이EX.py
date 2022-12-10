import pygame

 

# 스크린 전체 크기 지정

SCREEN_WIDTH = 1000
SCREEN_HEIGHT  = 900

 

# pygame 초기화

pygame.init()

 

# 스크린 객체 저장
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("pygame test")

 

# FPS를 위한 Clock 생성
clock = pygame.time.Clock()

 

# 이미지 로딩 및 크기 변경

player_blue = pygame.image.load("C:/2022python/gamepython(2)/game_project/파란달팽이.png")
player_blue = pygame.transform.scale(player_blue, (100, 100))
background = pygame.image.load("C:/2022python/gamepython(2)/game_project/배경.jpg")
background = pygame.transform.scale(background,(1000,800))
road = pygame.image.load("C:/2022python/gamepython(2)/game_project/길.png")
road = pygame.transform.scale(road,(1000,500))

 

# 이미지의 Rect 정보를 저장

player_Rect = player_blue.get_rect()

 

# 이미지가 가운데 올 수 있도록 좌표값 수정

# python 3.8 이상에서 integer가 필요한 곳에 float가 들어가면 DeprecationWarning이 나옴.

# 따라서 round() 처리를 해준다.

player_Rect.centerx = round(SCREEN_WIDTH / 22)

player_Rect.centery = round(SCREEN_HEIGHT / 1.265)

 

dx = 0

dy = 0

 

playing = True
while playing:

    # 이벤트 처리
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()

 
    # 스크린 배경색 칠하기

    SCREEN.blit(background,(0,0))
    SCREEN.blit(road,(0,300))
    SCREEN.blit(road,(0,150))
    SCREEN.blit(road,(0,0))
    SCREEN.blit(road,(0,-150))
    SCREEN.blit(road,(0,-300))


    # 스크린의 원하는 좌표에 이미지 복사하기, 좌표값은 Rect를 이용

    SCREEN.blit(player_blue, player_Rect)

 

    # 작업한 스크린의 내용을 갱신하기

    pygame.display.flip()

 

    # 1초에 60번의 빈도로 순환하기

    clock.tick(60)