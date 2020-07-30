#########################################################################
#
#  This is a simply starting template for python codes written to do
#  scientific/engineering computing.  You can put comments about what 
#  the code does, how it is supposed to be used and references to notes
#  about its construction here.  Special instructions will be welcome.
#
#########################################################################
#
#  Import section
#
#########################################################################

import numpy as np
import scipy as sc
from scipy import integrate
from scipy import signal
import scipy.io as sio
import matplotlib
matplotlib.use('TkAgg')
import os
import time
import sys
import random
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import pyplot

#########################################################################
#
# My special functions go here
#
#########################################################################

def area(xpos, ypos, zpos, x, y):
    answer = 4.0 *np.pi*((float(xpos) - x)**2+ (float(ypos)-y)**2 +(float(ypos)-y)**2+ (float(ypos))**2)
    return answer

def diffraction(xpos, ypos, zpos, x, y, z, t):
    refractive_angle = float(zpos)/np.sqrt((x-float(xpos))**2+(y-float(ypos))**2)
    result = t / refractive_angle
    return result

#########################################################################
#
# My main goes here
#
#########################################################################

def main():
    length_x = float(input(" What is the length in the x direction in meters? "))
    length_y = float(input(" What is the length in the y direction in meters? "))
    nx = float(input(" What is the number of steps in x? "))
    ny = float(input(" What is the number of steps in y? "))
    print(length_x,length_y,nx,ny)
    totalsource = float(input("What is the total source in Ci? " ))
    xpos=float(input("x position of observer:   "))
    ypos=float(input("y position of observer:   "))
    zpos=float(input("z position of observer:  "))
    t=float(input("give thickness of concrete:  "))
    lmda=float(input("give lambda for concrete:   "))
    print("position of observer:  ",xpos,ypos,zpos)
    s = totalsource*10**(-6)
    dx = length_x/float(nx)
    dy = length_y/float(ny)
    flux = 0.0
    x = -length_x/2.0 + dx/2.0
    y = -length_y/2.0 + dy/2.0
    z = 0.0
    while(x < (length_x / 2.0)):
        y = - length_y/2.0 + dy/2.0
        while (y < (length_y/2.0)):
            flux = flux + totalsource/(nx*ny) * (s*3.7 * 10.0**(10) * 2.0\
            /area(xpos, ypos, zpos, x, y)) * np.exp(-lmda *diffraction(xpos, ypos, zpos, x, y, z, t))
            y = y + dy
        x = x + dy
    print(flux)
    print("All done")

#########################################################################

if __name__ == "__main__":
    main()
