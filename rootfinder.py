#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 09:44:48 2020

@author: pyaephyohein
"""
import math
import numpy as np
import scipy as sc
from scipy import integrate
from scipy import signal
import scipy.io as sio
import matplotlib
matplotlib.use('TKAgg')
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
    y = 5*np.sin(x) - x
    return y

def myrandom():
    xrand = np.random.rand()
    return xrand

#########################################################################
#
# My main goes here
#
#########################################################################

def main():
    x = np.array([])
    y = np.array([])
    
    print("Finding roots via a number of techniques.")
    a = float(input("Lower edge of domain to search? "))
    b = float(input("Upper edge of domain to search? "))
    
    print("\nYou specified the domain: ", a,b)
    stepsize = 0.01*abs(b-a)

#
# Graphical Method
#    
    for xsample in np.arange(a,b,stepsize):
        x = np.append(x,[xsample])
        ycalc = myfunction(xsample)
        y = np.append(y,[ycalc])
        
    plt.scatter(x,y,s=1.0)
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.show()
#
# Dumb guess Method
#
    xold = a
    yold = myfunction(xold)
    ybest = yold
    xbest = a
    nguess = int(input("How many dumb guesses: "))
    for i in range(0,nguess):
        x = (b-a)*np.random.random() + a
        y = myfunction(x)
        if abs(y) < abs(ybest):
            xbest = x
            ybest = y
            print(i,xbest,ybest)
        
    print("After dumb guessing: " ,xbest, ybest)

#
# Bisection method
#
    xold = a
    yold = myfunction(xold)
    
    nbisection = int(input("How many bisection guesses: "))
    hstep = float(input("Initial Step: "))
    
    for i in range(0,nbisection):
        xnew = xold + hstep
        ynew = myfunction(xnew)

#
# Did y change sign?
        
        if(ynew - yold)/yold < 0:
            hstep = hstep + 2
            xnew = xold + hstep
        else:
            xnew = xold + hstep
    print("After bisection guessing: " ,xnew, ynew)


#########################################################################

if __name__ == "__main__":
    main()
            
    
