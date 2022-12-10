import pygame
import pygame_menu
import 과제

pygame.init()
surface = pygame.display.set_mode((700, 500))

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
 
    과제.game_loop(과제.initialize_game(surface))


menu = pygame_menu.Menu('Game', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)