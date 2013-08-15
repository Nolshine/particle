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
from math import sqrt
#need square roots.

import pygame
from pygame.locals import *
#imported core engine parts

from vec2d import vec2d
#need vectors.

from particle import Particle
#the stock with which I work.

#Display functions:
def processDisplay():
    global screen
    global particles
    screen.fill((0,0,0))
    for particle in particles:
        pos = particle.pos
        pygame.draw.circle(screen, (255,255,255), (int(round(pos[0])),
                                                   int(round(pos[1]))), int(particle.mass/2))
        
    pygame.display.update()

    
#Display data:
scr_size = (500,500)

############################

#Engine functions:
def update():
    """A function that advances the simulation one frame."""
    processEvents()
    processParticles()
    processDisplay()

def processEvents():
    for event in pygame.event.get():
        if event.type == QUIT or(event.type == KEYDOWN
                                 and event.key == K_ESCAPE):
            pygame.quit()
            quit()

def processParticles():
    global particles
    global grav_constant
    for particle in particles:
        for other in particles:
            if other is particle:
                continue
            else:
                if particle.pos == other.pos:
                    particle.pos = ((particle.pos[0]+1), (particle.pos[1]+1))
                dx = other.pos[0]-particle.pos[0]
##                print dx
                dy = other.pos[1]-particle.pos[1]
##                print dy
                M = particle.mass
##                print M
                m = other.mass
##                print m
                grav_dir = vec2d(dx, dy).normalized()
##                print grav_dir
                D = sqrt((dx*dx)+(dy*dy))
                if D == 0:
                    D = 0.001
##                print D
                F = grav_constant*M*m/D*D
##                print F
                particle.addVec(grav_dir*F)
    for particle in particles:
        particle.updatePos()
                
        
            

def populate():
    particles = []
    for i in range(20):
        particles.append(Particle())
    return particles
    

#Engine data:
particles = populate()
grav_constant = 0.00001

#############################
pygame.init()

screen = pygame.display.set_mode(scr_size, DOUBLEBUF)
screen.fill((0,0,0))

clock  = pygame.time.Clock()

while True:
    time_passed = clock.tick()
    update()


