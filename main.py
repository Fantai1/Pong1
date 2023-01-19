import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((800, 600))

def start_the_game():
    # NOAH'S CODE
    pass

menu = pygame_menu.Menu('=+=+=+=+=+=+=+=Pong=+=+=+=+=+=+=+=', 800, 600,
                       theme=pygame_menu.themes.THEME_DARK)

menu.add.button('Play',pygame_menu.events.PYGAME_WINDOWCLOSE, exec(open('Game.py').read()))
menu.add.button('Player One: "W" "S"')
menu.add.button('Player Two: "Up" "Down')
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)
