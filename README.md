# Plot a Circle
<p align="left"><img src="https://github.com/SceneDuGreene/circle_plot/blob/main/res%3D100.PNG" title="circle_plot"> </p>

Using the **CIRCLE** function and Matplotlib module to plot circles while specifying resolution.

# Overview
This PYTHON program is used to plot circles at a specified resolution, initial position (x_0,y_0), and radius. <br />
Let's break up the **CIRCLE** function into two parts : *Input* vs *Output*

***Input - 4 variables required:***
```Python
  def circle(r,x_0,y_0,res): #r between 0->1
```

>*Input1*) Radius, r: the straight line from the center of the circle to the circumference of the circle <br />
>*Input2*) Initial Position, x_0: Horizontal offset from origin  <br />
>*Input3*) Initial Position, y_0: Vertical offset from origin  <br />
>*Input4*) Resolution, res: # of points that make up circle. Keep between 50->200 for computation speed  <br />

***Output - 4 variables will be returned:***
```Python
return circle_x1, circle_y1, x_0, y_0 #return values for later use
```
>*Output1*) Circle x-coordinates, x1: plot with y1 to display circle in cartesian coordinates  <br />
>*Output2*) Circle y-coordinates, y1: plot with x1 to display circle in cartesian coordinates <br />
>*Output3*) Initial Position, x1_0: Horizontal offset from origin <br />
>*Output4*) Initial Position, y1_0: Vertical offset from origin <br />

 # Background on Equations Used
 > In theory a circle can be composed of infinite points. Fortunately, in order to plot a circle, we only need to use between 50->200 of these points. See "Comparing Resolution" below to play around with this. <br />
>> Any instantaneous point (x,y) on a circle (with a specified radius) can be found using the below equations (but me MUST specify θ). <br />
>> <p align="center"> <img src="https://github.com/SceneDuGreene/circle_plot/blob/main/Circle_PolarToRect.png" height=30% width=30%> </p>
>> <p align="center"> <img src= "https://latex.codecogs.com/svg.image?x&space;=&space;rcos(\theta)&space;" title="x-coords" /> & <img src="https://latex.codecogs.com/svg.image?y&space;=&space;rsin(\theta)&space;" title="y-coords"/> for <img src="https://latex.codecogs.com/svg.image?\theta\in\left&space;[&space;0,2\pi&space;&space;\right&space;]" title="theta belongs to 0 to 2pi"/> </p>  <br />
 >> In order to accumulate enough points, we have to cycle through θ (at regular intervals from 0 to 2π) and solve for and store all resulting (x,y) values
 
 The **CIRCLE** function in its entirety:
 ```Python
  def circle(r,x_0,y_0,res): #r between 0->1
    theta = np.linspace(0, 2*np.pi,res) # theta goes from 0 to 2pi

    # the radius of the circle applied below
    # compute cartesian (rectangular)  x1 and x2 coords
    circle_x1 = r*np.cos(theta) + x_0 #offset circle by desired IniPos, x_0
    circle_y1 = r*np.sin(theta) + y_0 #offset circle by desired IniPos, y_0
    return circle_x1, circle_y1, x_0, y_0 #return values for later use
```

## Getting Started
Start by figuring out the 4 pieces of information you will need to assign to each circle. <br />
We will make 2 concentric circles (circles that share the same origin):  <br />
The blue one with *radius* = 1 and the orange one with *radius* = 0.5 <br />
```Python
res = 100 # Resolution of shape. keep between 50->200
x_0 = 0 ; y_0 = -0.5 # initial x,y position
radius1 = 1; radius2 = 0.5 #radius of circles 1 & 2
```
We will then call the **CIRCLE** function for each circle, making sure to store all outputs for graphing purposes
```Python
x1, y1, x1_0, y1_0 = circle(radius1,x_0,y_0,res)  #r between 0->1
x2, y2, x2_0, y2_0 = circle(radius2,x_0,y_0,res) #r between 0->1
centroid1 = np.array([x1_0,y1_0]) #centroid of circle
```
Finally, we will plot the circles in their desired color making sure to include Titles and Axes labels
```Python
plt.plot(x1,y1,'b',) #plot circle1 in blue
plt.plot(x2,y2,color='orange') #plot circle2 in orange
plt.plot(centroid1[0],centroid1[1],'ko') #plot centroid point in black
plt.title("Kinematic Fun, res=%d" % res)
plt.xlabel("time (s)"); plt.ylabel("Amplitude (m)")
```
## Example Code
The code in its entirety will look something like this: <br />
**NOTICE** that we must first import modules **numpy** and **matplotlib** <br />
Then we must set up the figure and axes limits <br />
Followed by defining the **CIRCLE** function <br />
Finally, we can follow the procedure as shown above in the "Getting Started" Section
```Python
import numpy as np
import matplotlib.pyplot as plt 

# First set up the figure, the axis, and the plot element we want to plot
fig = plt.figure()
ax = plt.axes(xlim=(-1, 3), ylim=(-2, 1)) #set axes limits
ax.set_aspect('equal') #this will ensure that circle looks circular (as opposed to elliptical)

def circle(r,x_0,y_0,res): #r between 0->1
    theta = np.linspace(0, 2*np.pi,res) # theta goes from 0 to 2pi

    # the radius of the circle applied below
    # compute cartesian (rectangular) x1 and x2 coords
    circle_x1 = r*np.cos(theta) + x_0 #offset circle by desired IniPos, x_0
    circle_y1 = r*np.sin(theta) + y_0 #offset circle by desired IniPos, y_0
    return circle_x1, circle_y1, x_0, y_0 #return values for later use

## Draw circles at specified resolution, initial position, and radius
#Specify resolution, initial position, and radius    
res = 100 # Resolution of shape. keep between 50->200
x_0 = 0 ; y_0 = -0.5 # initial x,y position
radius1 = 1; radius2 = 0.5 #radius of circles 1 & 2
x1, y1, x1_0, y1_0 = circle(radius1,x_0,y_0,res)  #r between 0->1
x2, y2, x2_0, y2_0 = circle(radius2,x_0,y_0,res) #r between 0->1
centroid1 = np.array([x1_0,y1_0]) #centroid of circle

#plot circles in orange and blue. include title and labels
plt.plot(x1,y1,'b',) #plot circle1 in blue
plt.plot(x2,y2,color='orange') #plot circle2 in orange
plt.plot(centroid1[0],centroid1[1],'ko') #plot centroid point in black
plt.title("Kinematic Fun, res=%d" % res) #display resolution in Title
# plt.title("Kinematic Fun, origin=(%1.2f,%1.2f)" %(x_0,y_0)) #display origin coords in Title
plt.xlabel("time (s)"); plt.ylabel("Amplitude (m)")

```

## Example Output
<p align="center"><img src="https://github.com/SceneDuGreene/circle_plot/blob/main/res%3D100.PNG" title="circle_plot"> </p>

## Example Output: Changing Inital Position

>```Python
>x_0 = 0.0 ; y_0 = -0.5 # initial x,y position = (0.0,-0.5)
>```
><p align="center"> <img src="https://github.com/SceneDuGreene/circle_plot/blob/main/circle_changing_initial_position.png" height=100% width=100%> </p>

## Comparing Resolution
>Changing the *resolution* will change the shape of the plot. Mathmatically, only 3 non-colinear points (*res=4*) is enough to describe a circle with a particular radius; however, this isn’t visually satisfying! <br /> 
>>At around *res=20*, the shape starts to look more as we would expect, but with many bumps. The bumps start to smooth out at around res=50. <br />
>>>In general, I like to keep the *res= 100*. **Keep in mind, changing the resolution will change the number of points that make up the circle.**     
<p align="left"><img src="https://github.com/SceneDuGreene/circle_plot/blob/main/resolution_compare.png"> </p>
