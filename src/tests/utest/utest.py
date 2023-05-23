def sum(x, y):
    return x + y

import unittest

class TestSum(unittest.TestCase):

     def test_sum(self):
        self.assertEqual(sum(8, 9), 17, "Sum of 8 + 9 = 7")
        
     def test_no_sum(self):
        self.assertEqual(sum(8, 9), 17, "Sum of 8 + 9 = 7")
         

if __name__ == '__main__':
    unittest.main(verbosity=2)
