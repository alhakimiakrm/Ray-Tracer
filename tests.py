import unittest
from main import vector3D  

class TestVectors(unittest.TestCase):
    
    def setUp(self):
        self.v1 = vector3D(1, -2, -2)
        
    def test_magnitude(self):
        self.assertAlmostEqual(self.v1.magnitude(), 3)

if __name__ == "__main__":
    unittest.main()
