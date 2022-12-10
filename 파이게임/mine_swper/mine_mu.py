import pygame, pygame_menu
pygame.init()
surface = pygame.display.set_mode((600,400))


def level(self, value):
    print("LEVEL CHOICE: ",value)
    
def start():
    print("GAME_START")
    
t = pygame_menu.themes.THEME_BLUE;
t.widget_font = pygame.font.SysFont("gulim",30)

menu = pygame_menu.Menu("Menu",400,300, theme = t)
menu.add.selector("LEVEL ",[("EASY",1),("NOMAL",2),("HARD",3)],onchange=level)
menu.add.button("GAME_EXIT", pygame_menu.events.EXIT)
menu.mainloop(surface)