"""
PARTICLE PHYSICS ENGINE

file ID: engine.py

Purpose: operate objects to run a simulation,
         displaying objects graphically(, and possibly interactively).

Contains in-file:
    ENGINE CODE:
    *Engine functions
    *Graphics interface
    *User interface, if any

Imports:
    *Engine object files
    *any other library needed for engine functions
"""

import pygame
from pygame.locals import *
#imported core engine parts


#Display functions:
def updateDisplay():
    global caption
    pygame.display.set_caption(caption)
    pygame.display.update()

#Display data:
scr_size = (400, 400) #HEIGHT, WIDTH
caption = "Initializing..."



#Engine functions:
def update():
    time_passed = clock.tick()
    global frames
    global caption
    frames += 1
    caption = "Frames: " + str(frames)
    processEvents()
    processParticles()
    updateDisplay()
    

def processEvents():
    for event in pygame.event.get():
        if event.type == QUIT:
            raise KeyboardInterrupt

def processParticles():
    pass

#Engine data:
frames = 0

##Let's display a screen first, doesn't have to blinker,
##i'll just count frames.
pygame.init()

screen = pygame.display.set_mode(scr_size, DOUBLEBUF)

clock  = pygame.time.Clock()

try:
    while True:
        update()
except(KeyboardInterrupt):
    print "yup"
    pygame.quit()
    raw_input("press enter to quit.")
    quit()


