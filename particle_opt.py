"""
PARTICLE PHYSICS ENGINE

file ID: particle.py

Purpose: describe a particle and its operations

Contains in-file:
    Particle class code:
        data members:
            (public):
            mass(float)
            position(float)
            old position(for display)(float)
            direction(vec2d)
        methods:
            (private):
            *Birth, or init code
            (public):
            update position
            update old position to current position
            add vec2d to direction

Imports:
    Any libraries needed for object code.


Notes:
    A particle needs to know where it is,
    where it's going, and how to update itself.
    A particle should also have mass.
    When a particle updates itself,
    it should react to all other particles.
    During update the particle should pull
    itself towards all the others, using
    its own mass in the process.
"""
from random import randrange

import pygame
from pygame.locals import *

from vec2d import vec2d
#need vectors!

class Particle:
    
    __slots__ = ['pos', 'old_pos', 'mass', 'direction', 'dead', 'rect', 'color'] 
    def __init__(self, pos = None):
        if pos == None:
            self.pos = vec2d((randrange(100,401)*1.00),(randrange(100,401)*1.00))
        else:
            self.pos = pos
        self.mass = float(randrange(5,15))
        self.color = (self.mass/100.0)*255.0
        self.direction = vec2d(0,0)
        self.dead = False
        self.rect = pygame.Rect(self.pos.x, self.pos.y, int(self.mass/3), int(self.mass/3))
    def updatePos(self):
        self.pos = (self.pos[0]+self.direction.x,
                    self.pos[1]+self.direction.y)
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    def updateOld(self):
        self.old_pos = self.pos

    def addVec(self, vec):
        self.direction += vec
        
        
