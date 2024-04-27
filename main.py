#!/usr/bin/env python

from image import image
from color import color

"""

First row: 
    1. RED = (1, 0, 0)
    2.GREEN = (0, 1 ,0)
    3.BLUE = (0, 0, 1)
    
Second row:
    1. R+G = (1, 1, 0)
    2. R+G+B = (1, 1, 1)
    3. R*.001 = (0.001, 0, 0)
    
    We are creating a 3x2 pixel image made of different colored pixels. 
    Must be saved as a PPM file. 
    
    
"""

def main():
    WIDTH = 3
    HEIGHT = 2
    im = image(WIDTH, HEIGHT)
    RED = color(x = 1 , y = 0, z = 0)
    GREEN = color(x = 0, y = 1, z = 0)
    BLUE = color(x = 0, y = 0, z = 1)
    
    im.set_pixel(0, 0, RED)
    im.set_pixel(1, 0, GREEN)
    im.set_pixel(2, 0, BLUE)
    
    im.set_pixel(0, 1, RED + GREEN)
    im.set_pixel(1, 1, RED + BLUE + GREEN)
    im.set_pixel(2, 1, RED * 0.001)
    
    with open("pixel_gen.ppm", "w") as img_file:
        im.write_ppm(img_file)

if __name__ == "__main__":
    main()
        

