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
from math import sqrt
#needed for vector computations

import pygame
from pygame.locals import *
#imported core engine parts

from particle import Particle
#imported Particle object

#Display functions:
def updateDisplay():
    global screen
    displayParticles()
    pygame.display.update()

def displayParticles():
    global particles
    global center
    #First, blank all old positions
    for item in particles:
        #get data
        old = item.get_old()
        real_pos = ((center[0]+old[0]), (center[1]+old[1]))
        #blank the old
        rect = pygame.Rect(real_pos[0], real_pos[1], 4, 4)
        screen.fill((0,0,0), rect)
        item.set_old()
    #Now, draw them all anew
    for item in particles:
        #get data
        pos = item.get_pos()
        real_pos = (((center[0]+pos[0])+2), ((center[1]+pos[1])+2))
        #draw new
        pygame.draw.circle(screen, (255,255,255), real_pos, 2)

#Display data:
scr_size = (400, 400) #HEIGHT, WIDTH
center = ((scr_size[0]/2), (scr_size[1]/2))



#Engine functions:
def update():
    time_passed = clock.tick(50)
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
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            raise KeyboardInterrupt

def processParticles():
    global gravity_const
    for item in particles:
        #add gravity
        cur_pos = item.get_pos()
        cur_vec = item.get_vec()
        gravx = float(0-cur_pos[0])
        gravy = float(0-cur_pos[1])
        grav_len = sqrt((gravx*gravx)+(gravy*gravy))
        if grav_len == 0:
            grav_len = 1
        grav_vec = (((gravx/grav_len)*gravity_const), ((gravy/grav_len)*gravity_const))
        #^ normalized, and multiplied by grav constant
        new_vec = ((cur_vec[0]+grav_vec[0]), (cur_vec[1]+grav_vec[1]))
        item.set_vec(new_vec)
        
        #change position
        new_pos = (int(round(cur_pos[0]+(cur_vec[0])))), int(round(cur_pos[1]+(cur_vec[1])))
        item.set_pos(new_pos)
        

def populate(n):
    particles = []
    for i in range(n):
        posx = randrange(-100,101)
        posy = randrange(-100,101)
        particles.append(Particle((posx, posy)))
    return particles

#Engine data:
gravity_const = 0.3
frames = 0
particles = populate(1000)

##Let's display a screen first, doesn't have to blinker,
##i'll just count frames.
pygame.init()

screen = pygame.display.set_mode(scr_size, DOUBLEBUF)
screen.fill((0,0,0))

clock  = pygame.time.Clock()

try:
    while True:
        update()
except(KeyboardInterrupt):
    print "yup"
    pygame.quit()
    raw_input("press enter to quit.")
    quit()


