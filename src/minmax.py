#!/usr/bin/python

import random


class minmax:
    mmin=None
    mmax=None
    def __init__(self, mmin = -10, mmax = 10):
        minmax.mmin = mmin
        minmax.mmax = mmax
    
    def random(self):
        return random.randrange(self.mmin, self.mmax)
        
    def prinT(self):
        print "Minium {min}, maximum {max}".format(min=minmax.mmin, max=minmax.mmax)