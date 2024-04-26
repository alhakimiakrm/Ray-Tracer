import unittest
import main

main.vector3D

class TestVectors(unittest.TestCase):
    
    def setUp(self):
        self.v1 = main.vector3D(1, -2, -2)
        self.v2 = main.vector3D(3, 6, 9)
        
    def test_magnitude(self):
        self.assertAlmostEqual(self.v1.magnitude(), 3)
        
    def test_add(self):
        result = self.v1 + self.v2
        self.assertEqual(result.x, 4)
        self.assertEqual(result.y, 4)
        self.assertEqual(result.z, 7)
    
    def test_sub(self):
        result = self.v1 - self.v2
        self.assertEqual(result.x, -2)
        self.assertEqual(result.y, -8)
        self.assertEqual(result.z, -11)
    
    def test_multiplication(self):
        result = self.v1 * 2
        self.assertEqual(result.x, 2)
        self.assertEqual(result.y, -4)
        self.assertEqual(result.z, -4)
        
    def test_division(self):
        result = self.v1 / 3
        self.assertAlmostEqual(result.x, 1 / 3)
        self.assertAlmostEqual(result.y, -2 / 3)
        self.assertAlmostEqual(result.z, -2 / 3)

if __name__ == "__main__":
    unittest.main()