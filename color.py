from vector_class import Vector3d

class Color(Vector3d):
    @classmethod
    def from_hex(cls, hexcolor = "#000000"):
        x = int(hexcolor[1:3], 16 ) / 255.0 
        y = int(hexcolor[3:5], 16 ) / 255.0 
        z = int(hexcolor[5:7], 16 ) / 255.0
        return cls(x, y, z) 