import pygame
import string
from common.support import import_folder,BASEDIR
from map.decoration import Sky

class InputScreen:
    def __init__(self,surface):
        self.pressing=True
        self.str_list=[]

        self.display_surface = surface

        self.font = pygame.font.Font(BASEDIR+'imgs/ui/ARCADEPI.TTF',30)

        self.sky = Sky(8,'overworld') # 장식용 구름
    
        self.frame_index = 0
        self.animation_speed = 0.15
        
        flipped_imgs = [pygame.transform.flip(image,True,False) for image in import_folder(BASEDIR+'imgs/character/idle')]
        self.animations = import_folder(BASEDIR+'imgs/character/idle')+\
                          import_folder(BASEDIR+'imgs/character/jump')+\
                          import_folder(BASEDIR+'imgs/character/fall')+\
                          flipped_imgs
        self.image = self.animations[self.frame_index]
        self.img_rect = self.image.get_rect(topleft=(550,200))
    
    def input(self):
        keys = pygame.key.get_pressed()
        if not self.pressing: # 키보드를 꾹누르고 있을때 글자가 계속 생기지않게 방지 (한글자씩 입력받을 수 있게)
            for character in (string.ascii_lowercase + string.digits): # a~z , 0~9 를 입력받을때
                if eval(f"keys[pygame.K_{character}]"):
                    self.str_list.append(character.upper())
                    self.pressing = True
            if keys[pygame.K_SPACE]:
                if self.str_list:
                    self.str_list.append(" ")
                    self.pressing = True
            elif keys[pygame.K_BACKSPACE]:
                if self.str_list:
                    self.str_list.pop()
                self.pressing = True
            elif keys[pygame.K_RETURN]:
                if self.str_list:
                    return True
            if len(self.str_list)>10: # 글자수 제한
                self.str_list.pop()
        elif not keys.__contains__(True): # 뭔가 눌려있지 않을땐
            self.pressing = False
    
    def animate(self):
        # 보여줄 이미지 계산
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animations):
            self.frame_index = 0

        # 보여줄 이미지
        self.image = self.animations[int(self.frame_index)]
        self.display_surface.blit(self.image,self.img_rect)
    
    def show_text(self):
        text_input_surf = self.font.render('Please enter you nickname:',True,'#33323d')
        text_input_rect = text_input_surf.get_rect(bottomleft=(self.img_rect.left-180,self.img_rect.bottom+40))
        self.display_surface.blit(text_input_surf,text_input_rect)

        nickname = "".join(letter for letter in self.str_list)
        nickname_surf = self.font.render(f'{nickname}',True,'#33323d')
        self.nickname_rect = nickname_surf.get_rect(bottomleft=(text_input_rect.centerx-50,text_input_rect.centery+40))
        self.nickname_rect.x+=-10*len(self.str_list)
        self.display_surface.blit(nickname_surf,self.nickname_rect)

    def run(self):
        self.sky.draw(self.display_surface)
        self.animate()
        self.show_text()
        if self.input():
            return self.str_list