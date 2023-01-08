import unittest
from contains_duplicate import check_duplicate

class TestTask(unittest.TestCase):
    def test_contains_duplicate(self):
        self.assertEqual(check_duplicate([1,2,3,1]), True)
        self.assertEqual(check_duplicate([1,2,3,4]), False)
        self.assertEqual(check_duplicate([1,1,1,3,3,4,3,2,4,2]), True)

