import unittest 
from main import vector3D
from vector import Vector

class TestVectors(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector(1.0, -2.0, -2.0)
        
    def test_magn(self):
        self.assertEqual(self.v1.magnitude(), 3)
        
        
if __name__ == "__main__":
    unittest.main()
