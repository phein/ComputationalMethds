#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 09:40:58 2020

@author: pyaephyohein
"""
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

# variables

b = 1.0 # friction constant
m = 100.0 # mass of an object
g = 9.8 # gravity in m/s 


def fx(h,t,x,vx):
    fxresult = - (b/m)*vx
    return fxresult

def fz(h,t,x,vz):
    fzresult = -g - (b/m)*vz
    return fzresult

def k1x(h,tpass,xpass,vxpass):
    k1xresult = h*fx(h,tpass,xpass,vxpass)
    return k1xresult

def k2x(h,tpass,xpass,vxpass):
    k2xresult = h*fx(h,tpass,xpass,vxpass)
    return k2xresult

def k3x(h,tpass,xpass,vxpass):
    k3xresult = h*fx(h,tpass,xpass,vxpass)
    return k3xresult

def k4x(h,tpass,xpass,vxpass):
    k4xresult = h*fx(h,tpass,xpass,vxpass)
    return k4xresult

def k1z(h,tpass,zpass, vzpass):
    k1zresult = h*fz(h,tpass,zpass,vzpass)
    return k1zresult

def k2z(h,tpass,zpass, vzpass):
    k2zresult = h*fz(h,tpass,zpass,vzpass)
    return k2zresult

def k3z(h,tpass,zpass, vzpass):
    k3zresult = h*fz(h,tpass,zpass,vzpass)
    return k3zresult

def k4z(h,tpass,zpass, vzpass):
    k4zresult = h*fz(h,tpass,zpass,vzpass)
    return k4zresult

#########################################################################
def main():
    t = 0
    t = float(input("Enter initial time "))
    tmax = float(input("Enter maximum time "))
    h = float(input("Enter step size "))
    N =(tmax - t)/ h
    tarray=[]
    tarray.append(t)
    x = 0
    xarray = []
    xarray.append(0.0)
    z = 0
    zarray = []
    zarray.append(0.0)
    vx = 0
    vz = 0
    vxpass =[]
    vzpass = []
    vxpass.append(0.0)
    vzpass.append(0.0)
    
    for i in range(0,int(N)):
        k1xpass = k1x(h,t,x,vx)
        k2xpass = k2x(h,t+h/2, x+h/2*vx+h/8*k1xpass, vx+k1xpass/2)
        k3xpass = k3x(h,t+h/2, x+h/2*vx+h/8*k1xpass, vx+k2xpass/2)
        k4xpass = k4x(h,t+h, x+ h*vx + h/2*k3xpass, vx+ k3xpass)
        xnext =  xarray[i] + h*(vx + (1.0/6.0)*(k1xpass+k2xpass+k3xpass+k4xpass))
        xarray.append(xnext)
        vxnext = vxpass[i] + (1.0/6.0)*(k1xpass + 2 * k2xpass + 2 * k3xpass + k4xpass)
        vxpass.append(vxnext)
        
        k1zpass = k1z(h,t,z,vz)
        k2zpass = k2z(h,t+h/2, z+h/2*vx+h/8*k1zpass, vz+k1zpass/2)
        k3zpass = k3z(h,t+h/2, z+h/2*vx+h/8*k1zpass, vz+k2zpass/2)
        k4zpass = k4z(h,t+h, z+ z*vz + h/2*k3zpass, vx+ k3zpass)
        znext =  zarray[i] + h*(vz + (1.0/6.0)*(k1zpass+k2zpass+k3zpass+k4zpass))
        zarray.append(znext)
        vznext = vzpass[i] + (1.0/6.0)*(k1zpass + 2 * k2zpass + 2 * k3zpass + k4zpass)
        vzpass.append(vznext)
        
        t = t+h
        tarray.append(t)
        
    print(xarray)
    print(vxpass)
    print(zarray)
    print(vzpass)
    print(t)
    print("All done")
    
#########################################################################

if __name__ == "__main__":
    main()
