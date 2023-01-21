import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((800, 600))
menu = pygame_menu.Menu('=+=+=+=+=+=+=+=Pong=+=+=+=+=+=+=+=', 800, 600,
                        theme=pygame_menu.themes.THEME_ORANGE)

from Game import main

menu.add.button('Play', main)
menu.add.button('Player One: "W" "S"')
menu.add.button('Player Two: "Up" "Down"')
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)