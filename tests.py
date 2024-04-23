import unittest 
from main import vector3D

class TestVectors(unittest.TestCase):
    vector = vector3D.__init__.self.magnitude()
    
    def setUp(self):
        self.v1 = vector3D(1,-2, -2)
        
    def test_magn(self):
        self.assertEqual(vector.magnitude(), 3)
        
        
if __name__ == "__main__":
    unittest.main()
