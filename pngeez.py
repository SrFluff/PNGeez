import os
import sys
import pygame
from pygame.locals import *

pygame.init()
sys.argv.pop(0)

if os.name == "nt":
    icon = pygame.image.load("/Program Files/pngeez/icon.png")
title = "PNGeez"
pygame.display.set_icon(icon)

if len(sys.argv) == 0:
    if os.name == "nt":
        img = pygame.image.load("/Program Files/pngeez/nothing.png")
else:
    img = pygame.image.load(sys.argv[0])
    title = sys.argv[0]

screen = pygame.display.set_mode((img.get_width(),img.get_height()))
pygame.display.set_caption(title)
main = True
while main:
    for event in pygame.event.get():
        if event.type == QUIT:
            main = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            main = False
    screen.blit(img,(0,0))
    pygame.display.flip()
