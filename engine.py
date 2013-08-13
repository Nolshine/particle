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
    *Engine object files, if any. I think use of the pos/vec dict
     means I don't have to make any new classes, for now.
    *any other library needed for engine functions
"""
from random import randrange
#imported component for random generation

import pygame
from pygame.locals import *
#imported core engine parts


#Display functions:
def drawParticle((posx, posy)):
    global center
    display_posx = (center[0]+posx)
    display_posy = (center[1]+posy)
    pygame.draw.circle(screen, (255,255,255), (display_posx, display_posy), 5)
    
    
def updateDisplay():
    global screen
    global particles
    global caption
    pygame.display.set_caption(caption)
    screen.fill((0,0,0))
    for particle in particles:
        drawParticle(particle)
    pygame.display.update()

#Display data:
scr_size = (400, 400) #HEIGHT, WIDTH
center = ((scr_size[0]/2), (scr_size[1]/2))
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
        elif event.type == KEY_DOWN and event.key == k_escape:
            raise KeyboardInterrupt

def processParticles():
    pass

def populate(n):
    particles = {}
    for i in range(n):
        posx = randrange(-100,101)
        posy = randrange(-100,101)
        vecx = randrange(-1,2)
        vecy = randrange(-1,2)
        particles[(posx, posy)] =  (vecx, vecy)
    return particles
    

#Engine data:
frames = 0
particles = populate(5)

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


