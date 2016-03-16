# Boring Flightsim

To honour all pilots out there who spend hours and hours everyday in their planes to get us safely from A to B, I bring you the **Boring Fligh Sim**. This flight simulator has no thrills, no effects or extraordinary features. It is just about getting you job done, press the right buttons and make smooth plane movements to make you passengers feel relaxed on board.

*Avoid fast movements, be wise in you decisions and fly smoothly...*

The simulator is not very accurate and only a pet project for programming breaks while writing my PhD thesis. It tries to simulate the 2D behavoiur of an [Airbus A 320-200](https://en.wikipedia.org/wiki/Airbus_A320_family#A320).

![Screenshot](https://raw.githubusercontent.com/deltaflyer/boringflightsim/master/graphics/screenshot.png)

## Getting Started

To use boring flightsim, you need **Python 2.7** and **pygame**. The software was written in Ubuntu 14.04 LTS. You can start like this:

```bash
sudo apt-get install git python-pygame
git clone https://github.com/deltaflyer/boringflightsim.git
cd boringflightsim
./run.sh
```
## Flight Controls
![W](http://dabuttonfactory.com/button.png?t=W&f=Calibri-Bold&ts=24&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=gradient&bgc=3d85c6&ebgc=073763) **Increase thrust**

![S](http://dabuttonfactory.com/button.png?t=S&f=Calibri-Bold&ts=24&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=gradient&bgc=3d85c6&ebgc=073763) **Decrease thrust**

![Toggle the landing gear](http://dabuttonfactory.com/button.png?t=G&f=Calibri-Bold&ts=24&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=gradient&bgc=3d85c6&ebgc=073763) **Toggle the landing gear**

![Toggle the airbreak ](http://dabuttonfactory.com/button.png?t=A&f=Calibri-Bold&ts=24&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=gradient&bgc=3d85c6&ebgc=073763) **Toggle the airbreak**

![Pull nose up](http://dabuttonfactory.com/button.png?t=Arrow-Down&f=Calibri-Bold&ts=24&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=gradient&bgc=3d85c6&ebgc=073763) **Pull nose up**

![Push nose down](http://dabuttonfactory.com/button.png?t=Arrow-Up&f=Calibri-Bold&ts=24&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=gradient&bgc=3d85c6&ebgc=073763) **Push nose down**


## Flying Advises

* Accelerate to 100 knots, in order to pull the nose of plane up and start flying
* If your speed is below 100 knots, you cannot tilt the plane anymore as air is not fast enough to produce the necessary forces
* For slowing down toggle the air break by pressing *A* The multifunction display shows the state of the airbreak.
* Try to land between 50-150 feet/minute vertical speed and 140 kts horizontal speed

## Bugs and Featues

If you find a bug, please fix it and provide a pull request. The same is fine for new features. Any contribution is welcome.

## The MIT License (MIT)
Copyright (c) Oliver Wannenwetsch for the [Python User Group](http://www.goepy.de) Göttingen 2016. The software is licensed under the MIT Licence. 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Copyright Texture-Pack

The textures used in Boring FlightSim are subject of following sources:
* cloud1.png - http://opengameart.org/content/2d-clouds
* cloud2.png - http://opengameart.org/content/2d-clouds
* cloud3.png - http://opengameart.org/content/2d-clouds
* icon.png - http://icon-icons.com/de/symbol/Flug-Flugzeug-Flugzeug/30822
* gras.png - http://opengameart.org/content/seamless-grass-textures-20-pack
* buildings-layer.ong - http://opengameart.org/content/urban-landscape

## Copyright Fonts

* DIGITAL DISPLAY TFB - http://truefonts.blogspot.com/2012/11/digital-display-tfb.html
* PxPlus IBM VGA9 - http://int10h.org/oldschool-pc-fonts/fontlist/
