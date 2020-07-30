#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 09:32:04 2020

@author: pyaephyohein
"""
import math
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

a = 1
b = 10 # limits of integration
N = 1000 # number of points


def func(x):
    return math.log(x)/x


#########################################################################
#
# My main goes here
#
#########################################################################

def main():
    in_area = 0.0
    length = 9
    width = 1/math.e
    xrand = random.uniform(a,b)
    yrand = random.uniform(0,1/math.e)

    for i in range(N):
        if yrand < func(xrand):
            in_area += 1
    
    area_box = length * width
    answer = (in_area / N) * area_box
        
    print(answer)


#########################################################################

if __name__ == "__main__":
    main()