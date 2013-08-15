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
from random import randrange
#some randomness.

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
    global paused
    """A function that advances the simulation one frame."""
    processEvents()
    if not paused:
        processParticles() 
    processDisplay()

def processEvents():
    global paused
    global particles
    for event in pygame.event.get():
        if event.type == QUIT or(event.type == KEYDOWN
                                 and event.key == K_ESCAPE):
            pygame.quit()
            quit()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            paused = not paused
        elif event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            pos = vec2d(float(pos[0]), float(pos[1]))
            particles.append(Particle(pos))

def processParticles():
    global particles
    global grav_constant
    for particle in particles:
        if particle.dead:
            particles.remove(particle)
            continue
        for other in particles:
            if other is particle:
                continue
            else:
                if particle.rect.collidepoint(other.pos):
                    if particle.mass > other.mass:
                        particle.mass += other.mass
                        other.dead = True
                    elif particle.mass == other.mass:
                        particle.direction = particle.direction*(-1)
                        other.direction = other.direction*(-1)
                    else:
                        other.mass += particle.mass
                        particle.dead = True
                        break
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

def populate(n):
    global bang_force
    #I support the big bang theory.
    particles = []
    for i in range(n):
        pos = vec2d((randrange(0,501)*1.00),(randrange(0,501)*1.00))
        dir_to_center = vec2d((pos.x-250), (pos.y-250)).normalized()
        bang_dir = dir_to_center * bang_force
        particle = Particle(pos)
        particle.addVec(bang_dir)
        particles.append(particle)
        particle = None
    return particles
    

#Engine data:
init_pop = 40
paused = True
bang_force = 0.5
particles = populate(init_pop)
grav_constant = 0.000008

#############################
pygame.init()

screen = pygame.display.set_mode(scr_size, DOUBLEBUF)
screen.fill((0,0,0))

clock  = pygame.time.Clock()

while True:
    time_passed = clock.tick()
    update()


