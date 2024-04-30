#!/usr/bin/env python
from color import Color
from engine import RenderEngine
from point import Point
from sphere import Sphere
from vector_class import Vector3d
from scene import Scene


def main():
    WIDTH = 320
    HEIGHT = 200
    camera = Vector3d(0, 0, -1)
    object = [Sphere(Point(0, 0, 0), 0.5, Color.from_hex("#FF0000"))]
    scene = Scene(camera, object, WIDTH, HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)
    
    with open("pixel_gen.ppm", "w") as img_file:
        image.write_ppm(img_file)


if __name__ == "__main__":
    main()
