"""
PARTICLE PHYSICS ENGINE

file ID: particle.py

Purpose: describe a particle and its operations

Contains in-file:
    Particle class code:
        data members:
            (public):
            *Current position in float from centre
            *Old position in float from centre
            *Vector (which is also vecocity) in float
        methods:
            (private):
            *Birth, or init code
            (public):
            *Get position
            *Set position
            *Get vector
            *Set vector
            *Get old position
            *Update old position

Imports:
    Any libraries needed for object code.
"""
from random import randrange
#imported component for random generation

print "test"

class Particle:
    def __init__(self, (posx, posy)):
        print "yay"
        #position in two parts
        self.posx = posx
        self.posy = posy
        #old position in two parts
        self.old_posx = posx
        self.old_posy = posy
        #vector in two parts
        self.vecx = randrange(-5,6)
        self.vecy = randrange(-5,6)

    def get_pos(self):
        return (self.posx, self.posy)

    def get_vec(self):
        return (self.vecx, self.vecy)

    def set_pos(self, (x, y)):
        self.posx = x
        self.posy = y

    def set_vec(self, (x, y)):
        self.vecx = x
        self.vecy = y

    def get_old(self):
        return (self.old_posx, self.old_posy)

    def set_old(self):
        self.old_posx = self.posx
        self.old_posy = self.posy
        
