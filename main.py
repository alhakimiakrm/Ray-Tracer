import math

class vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return vector3D(self.x * scalar, self.y * scalar, self.z *  scalar)
        raise TypeError("Scalar must be a number.")
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar):
        if scalar == 0:
            raise ValueError("Cannot divide by zero.")
        return vector3D(self.x / scalar, self.y / scalar, self.z / scalar)
    
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def __repr__(self):
        return f"vector3D({self.x}, {self.y}, {self.z})"

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return (round(self.x / mag, 2), round(self.y / mag, 2), round(self.z / mag, 2))

    @staticmethod
    def dot_product(vector1, vector2):
        return vector1.x * vector2.x + vector1.y * vector2.y + vector1.z * vector2.z

    @staticmethod
    def add(vector1, vector2):
        return vector3D(vector1.x + vector2.x, vector1.y + vector2.y, vector1.z + vector2.z)

    @staticmethod
    def subtract(vector1, vector2):
        return vector3D(vector1.x - vector2.x, vector1.y - vector2.y, vector1.z - vector2.z)

    @staticmethod
    def multiply(vector1, scalar):
        return vector3D(vector1.x * scalar, vector1.y * scalar, vector1.z * scalar)

    @staticmethod
    def divide(vector1, scalar):
        if scalar == 0:
            raise ValueError("Cannot divide by zero.")
        return vector3D(vector1.x / scalar, vector1.y / scalar, vector1.z / scalar)


if __name__ == "__main__":
    vector3D
