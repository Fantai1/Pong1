import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((1000, 800))

def start_the_game():
    # NOAH'S CODE
    pass

menu = pygame_menu.Menu('=+=+=+=+=+=+=+=Pong=+=+=+=+=+=+=+=', 1000, 800,
                       theme=pygame_menu.themes.THEME_DARK)

menu.add.button('Play', exec('Game.py').read()))
menu.add.button('Player One: "W" "S"')
menu.add.button('Player Two: "Up" "Down')
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)
execfile()