#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:08:51 2020

@author: pyaephyohein
"""
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


class agent:
    def __init__(self,health,x,y,right,left,up,down,rightneighbor,leftneighbor,upneighbor,downneighbor,time_infected,iquar):
        self.health = health
        self.x = x
        self.y = y
        self.right = right
        self.left = left
        self.up = up
        self.down = down
        self.time_infected = time_infected
        self.iquar = iquar
        self.rightneighbor = np.aarray([rightneighbor,y])
        self.leftneighbor = np.aarray([leftneighbor,y])
        self.upneighbor = np.aarray([upneighbor,y])
        self.downneighbor = np.aarray([downneighbor,y])
        

def move(myagent, i , xsize, ysize):
    if (myagent[i].iquar != 1):
        moveran = np.random.randint(0,3)
        x = myagent[i].x
        y = myagent[i].y
        
        if (moveran == 0):
            xnew = x - 1
            ynew = y
        elif (moveran == 1):
            xnew = x+1
            ynew = y
        elif (moveran == 2):
            xnew = x
            ynew = y-1
        elif (moveran == 3):
            xnew = x
            ynew = y+1
    else:
        xnew = x
        ynew = y
    
    if(xnew > xsize):
        xnew = 0
    if(xnew < xsize):
        xnew = xsize
    if(ynew > ysize):
        ynew = 0
    if(ynew < ysize):
        ynew = ysize
        
    return myagent
#
 # This function finds what agents are occupying the nearest neighbor locations
 # for each agent passed to it.  By knowing the agents that are nearby, we can 
 # allow for interactions between nearest neighbors.
 #   

def findoccupation(myagent):
	
    nagent = len(myagent)
    for i in range(0, nagent):
        x = myagent[i].x
        y = myagent[i].y
        xleft = myagent[i].left
        xright = myagent[i].right
        yup = myagent[i].up
        ydown = myagent[i].down
        myagent[i].rightneighbor = -1
        myagent[i].leftneighbor = -1
        myagent[i].upneighbor = -1
        myagent[i].downneighbor = -1
	   
    
        for j in range(0,nagent) and j != i:
            xtest = myagent[j].x
            ytest = myagent[j].y
	   
            if (xtest == xright and ytest ==y):
                myagent[i].rightneighbor = j
	       
            if (xtest == xleft and ytest == y):
     	        myagent[i].leftneighbor = j
	   
            if (xtest == x and ytest == yup ):
                myagent[i].upneighbor = j
	  
            if (xtest == x and ytest == ydown):
                myagent[i].downneighbor  = j
		   
    return myagent	   
	   
		

#########################################################################
#
# My main goes here
#
#########################################################################

def main():

#
# Setup
#	
	
    print("This is a virus simulation")
    nagent = int(input("How many agents are there (<10000)? "))
    pgetsick = float(input("What is the probability of getting sick from a nearest neighbor? (p<= 1.0)  "))
    pdeath = float(input("What is the probability of death while sick (per time step)  "))
    trecover = float(input("How many timesteps to recover? "))
	
    xsize = int(input("How large is the x-space? (<=10000) " ))
    ysize = int(input("How large is the yspace? (<=10000) " ))
    ntime = int(input("How many time steps for this simulation? "))
    spaceset = int(input("Do you want agents randomly distributed in x,y space or clustered in groups (0: random, n: clustered with n clusters: "))
    ninitsick = int(input("How many are sick at t = 0? "))
	
    myagent=[]
    xarray = np.array([])
    yarray = np.array([])
    xn = np.array([])
    yn = np.array([])
    harray = np.array([])
    nsick = 0
	
    for i in range(0,nagent):
        xraninit = round(np.random.randint(0,xsize))
        yraninit = round(np.random.randint(0,ysize))
# (self,health,x,y,right,left,up,down, rightneighbor, leftneighbor, upneighbor, downneighbor, time_infected,iquar)		
        if (nsick < ninitsick):
            myagent.append(agent("red",xraninit,yraninit,0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
            nsick = nsick+1
        else:
            myagent.append(agent("green",xraninit,yraninit, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
            
        myagent = findneighbors(myagent,xsize,ysize)    
            

        xarray = np.append(xarray,[myagent[i].x])
        yarray = np.append(yarray,[myagent[i].y])
        harray = np.append(harray,[myagent[i].health])
        
        xn = np.append(xn,[myagent[i].right])
        yn = np.append(yn,[myagent[i].y])
        
        xn = np.append(xn,[myagent[i].left])
        yn = np.append(yn,[myagent[i].y])
        
        xn = np.append(xn,[myagent[i].x])
        yn = np.append(yn,[myagent[i].up])
        xn = np.append(xn,[myagent[i].x])
        yn = np.append(yn,[myagent[i].down])
        
           
     
    plt.scatter(xarray,yarray,c=harray,s=5.0)
    plt.scatter(xn,yn,c="black",s=5.0)
    plt.xlabel("X axis ")
    plt.ylabel("Y axis")
    plt.show()


    
#
#  Now we need to find the nearest neighbor positions and find the occupations.
#

    for i in range(0,nagent):
        myagent = findneighbors(myagent,xsize,ysize)
    
#
#
#  Now that we know what the nearest neighbor positions are for each, we can find out if the spot is
#  occupied by another agent.


#
# Time loop
# 		
#    for it in range(0,ntime):
#        for ia in range(0, nagent):
#            myagent = move(myagent, ia, xsize, ysize)
	        
	    
	
	
	
    print("All done")

#########################################################################

if __name__ == "__main__":
    main()

