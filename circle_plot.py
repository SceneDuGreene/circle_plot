# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 10:58:09 2022

@author: mike3
"""
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-1, 3), ylim=(-2, 1)) #set axes limits
ax.set_aspect('equal') #this will ensure that circle looks circular (as opposed to elliptical)

def circle(r,x_0,y_0,res): #r between 0->1
    theta = np.linspace(0, 2*np.pi,res) # theta goes from 0 to 2pi

    # the radius of the circle applied below
    # compute cartesian (rectangular)  x1 and x2 coords
    circlex1 = r*np.cos(theta) + x_0 #offset circle by desired IniPos, x_0
    circley1 = r*np.sin(theta) + y_0 #offset circle by desired IniPos, y_0
    return circlex1, circley1, x_0, y_0 #return values for later use

## Draw circles at specified resolution, initial position, and radius
#Specify resolution, initial position, and radius    
res = 100 # Resolution of shape. keep between 50->200
x_0 = 0.0 ; y_0 = -0.5 # initial x,y position
radius1 = 1; radius2 = 0.5 #radius of circles 1 & 2
x1, y1, x1_0, y1_0 = circle(radius1,x_0,y_0,res)  #r between 0->1
x2, y2, x2_0, y2_0 = circle(radius2,x_0,y_0,res) #r between 0->1
centroid1 = np.array([x1_0,y1_0]) #centroid of circle

#plot circles in orange and blue. include title and labels
plt.plot(x1,y1,'b',) #plot circle1 in blue
plt.plot(x2,y2,color='orange') #plot circle2 in orange
plt.plot(centroid1[0],centroid1[1],'ko') #plot centroid point in black
plt.title("Kinematic Fun, res=%d" % res)
#plt.title("Kinematic Fun")
plt.xlabel("time (s)"); plt.ylabel("Amplitude (m)")
