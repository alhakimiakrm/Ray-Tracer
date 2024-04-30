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
    WIDTH = 320
    HEIGHT = 200
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
    vector1 = vector3D(1, -2, -2)
    vector2 = vector3D(3, 6, 9)
    scalar = 2

    print("Magnitude of Vector 1:", vector1.magnitude())
    print("Normalized Vector 1:", vector1.normalize())
    print("Dot Product of Vector 1 and Vector 2:", vector3D.dot_product(vector1, vector2))

    result_vectorA = vector3D.add(vector1, vector2)
    result_vectorS = vector3D.subtract(vector1, vector2)
    result_vectorM = vector3D.multiply(vector1, scalar)
    result_vectorD = vector3D.divide(vector1, scalar)

    print("Vectors added together: (", result_vectorA.x, ", ", result_vectorA.y, ", ", result_vectorA.z, ")", sep="")
    print("Vectors subtracted: (", result_vectorS.x, ", ", result_vectorS.y, ", ", result_vectorS.z, ")", sep="")
    print("Vectors multiplied: (", result_vectorM.x, ", ", result_vectorM.y, ", ", result_vectorM.z, ")", sep="")
    print("Vectors divided: (", result_vectorD.x, ", ", result_vectorD.y, ", ", result_vectorD.z, ")", sep="")
