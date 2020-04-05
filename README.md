# pythonMouseMover
This is an opensauce "screensaver" written in python. **The sauce** should contain as few characters and lines as possible!
In other words **the sauce** must be as compact as possible!  
**The sauce** currently contains 181 characters. The record is an alternative solution by Reddit user [HolzmindenScherfede](https://www.reddit.com/user/HolzmindenScherfede/) with 158 characters!
  
Before all else we want to thank you for choosing **pythonMouseMover**! :)

## Alternative solution
 
Due to better solutions that I can not possibly take any credit for the branch [alternativeSolutions](https://github.com/jasZnerol/pythonMouseMover/tree/alternativeSolutions) exists.

## Unstable program?
This program is **very** unstable because of how it checks if the courser has reached the border of the screen.

For instance if you have a screen height of 1080 pixels you need to check if the Y-position of the courser fulfills one of thees conditions:
```
m.position[1]>1078 or m.position[1]<0
```

First of all note that m is the mouse object and position[1] gives the Y-position of the courser.
But because **the sauce** needs to be as short as possible we do not check if the border is reached with a simple *greater* or *smaller* comparison.
The shorter and less reliable way looks like this:
```
m.position[1] in in[1078,0]
```
This is less reliable in the sense that it will not work on every machine. To make it work the *lower* and *right* border values will require adjustment.
In addition the program is written for screens with an aspect ratio of 16:9 with a resolution of 1920:1080 pixels. 
You can ignore the aspect ratio as it is a result of the resolution.
If you have a different resolution and you want this project to *work* as it shohld you will have to make a few adjustments.

## Adjustments
To make this program work for different resolutions you will have to edit **the sauce**.
Those adjustments will be made in line 7 and 8.
Change **the sauce** as follows:
```
x*=1-2*(m.position[0] in[<WIDHT_OF_YOUR_SCREEN>  - 2,0])    
y*=1-2*(m.position[1] in[<HEIGHT_OF_YOUR_SCREEN> - 2,0])
```
The *-2* is optional but i find the program works better and more reliable if the courser does not leave the screen completely. 

## How to run the sauce
To run **the sauce** python3 is required. It may run on previous version but it was not intendet to. Due to the minimal nature
of **the sauce** running it is also very simple and goes as follows:
```
pip install -r requirements.txt && python app.py
```

## How to exist the sauce
You can **ctrl + c** to exit the program. If you are on Windows hitting **ctrl + alt + del** will also terminate the program.

## Credits
See credits [here.](https://github.com/jasZnerol/pythonMouseMover/blob/master/CONTRIBUTING.md)

## License
See license [here.](https://github.com/jasZnerol/pythonMouseMover/blob/master/LICENSE)
