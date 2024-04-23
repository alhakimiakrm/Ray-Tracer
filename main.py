import math


class vector3D:
    """A  three element vector used in 3D graphics to simulate things such as Ray Tracing, such as in this instance."""
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.magnitude = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        self._normalized = None  # Lazy initialization for normalized vector

    def normalize(self):
        if self.magnitude == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return (self.x / self.magnitude, self.y / self.magnitude, self.z / self.magnitude)

    def get_normalized(self):
        if self._normalized is None:
            self._normalized = self.normalize()
        return self._normalized

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

    def get_magnitude(self):
        return self.magnitude

if __name__ == "__main__":
    vector1 = vector3D(1, -2, -2)
    vector2 = vector3D(3, 6, 9)
    scalar = 2

    print("Magnitude of Vector 1:", vector1.get_magnitude())
    print(f"Normalized Vector 1:", vector1.get_normalized())
    print("Dot Product of Vector 1 and Vector 2:", vector3D.dot_product(vector1, vector2))

    result_vectorA = vector3D.add(vector1, vector2)
    result_vectorS = vector3D.subtract(vector1, vector2)
    result_vectorM = vector3D.multiply(vector1, scalar)
    result_vectorD = vector3D.divide(vector1, scalar)

    print("Vectors added together: (", result_vectorA.x, ", ", result_vectorA.y, ", ", result_vectorA.z, ")", sep="")
    print("Vectors subtracted: (", result_vectorS.x, ", ", result_vectorS.y, ", ", result_vectorS.z, ")", sep="")
    print("Vectors multiplied: (", result_vectorM.x, ", ", result_vectorM.y, ", ", result_vectorM.z, ")", sep="")
    print("Vectors divided: (", result_vectorD.x, ", ", result_vectorD.y, ", ", result_vectorD.z, ")", sep="")
