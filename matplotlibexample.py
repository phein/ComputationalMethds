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
#matplotlib.use('TkAgg')
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

def myfunction(x):
    y = x**2
    return y

def myrandom():
    rand = np.random.rand()
    return rand
#########################################################################
#
# My main goes here
#
#########################################################################

def main():
    nrand = int(input("How many random numbers: "))
    x = np.array([])
    y = np.array([])
    for i in np.arange(0,11,0.1):
        x = np.append(x,[i])
        ycalc = myfunction(i)
        y = np.append(y,[ycalc])
    
    print(len(x),len(y))
    
    plt.scatter(x,y,s=1.0)
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.show()
    
    xarray = np.array([])
    yarray = np.array([])
    for j in range(0,nrand):
        xrand = myrandom()
        yrand = myrandom()
        xarray = np.append(xarray,[xrand])
        yarray = np.append(yarray,[yrand])
        
    plt.scatter(xarray,yarray,s=1.0)
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.show()
        
    print("All done")

#########################################################################

if __name__ == "__main__":
    main()
