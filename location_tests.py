import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    # Add more tests!
    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 5, 5)
        loc3 = Location("SLO", 5, 5)
        loc4 = Location("Paris", 35.3, -120.7)
        loc5 = Location("Paris", 35.3, -120.700000001)
        self.assertEqual(loc2, loc3)
        self.assertNotEqual(loc1, loc2)
        self.assertNotEqual(loc1, loc4)
        self.assertEqual(loc4, loc5)

if __name__ == "__main__":
        unittest.main()
