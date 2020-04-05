# pythonMouseMover
A "screensaver" written in python. **The sauce** should contain as few characters and lines as possible!
In other words **the sauce** must be as compact as possible!

# Unstable program?
This program is **very** unstable because of how it checks if the courser has reached the border of the screen.

For instance if you have a screen width of 1200 pixels you need to check if the Y-position of the courser fulfills one of thees conditions:
```
m.position[1]>1078 or m.position[1]<0
```
First of all note that m is the mouse and position[1] gives the Y-position of the courser.
But because **the sauce** needs to be as short as possible we do not check if the border is reached with a simple *greater* or *smaller* comparison.
The shorter and less reliable way looks like this:
```
m.position[1] in in[1078,0]
```
This is less reliable in the sense that it will not work on every machine. To make it work the *lower* and *right* border values will require adjustment.
In addition the program is written for screens with an aspect ratio of 16:9 with a resolution of 1920:1080 pixels. 
You can ignore the aspect ratio as it is a result of the resolution.
If you have a different resolution and you want this project to *work* as it shohld you will have to make a few adjustments.

# Adjusments
To make this program work for different resolutions you will have to edit **the sauce**.
Those adjusements will be made in line 7 and 8.
Change **the sauce** as follows:
```
7   x=-x if m.position[0] in[<YOUR_SCREEN_WIDTH>  - 2,0] else x
8   y=-y if m.position[1] in[<YOUR_SCREEN_HEIGHT> - 2,0] else y
```
The *-2* is optional but i find the program works better and more reliable if the courser does not leave the screen completely.  
