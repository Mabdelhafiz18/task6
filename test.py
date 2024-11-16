#mohamed abdelhafiz 
# ahmed osama 
#https://github.com/Mabdelhafiz18/task6.git
import unittest
from calculator import Calc  # Import the Calc class correctly

class TestCalculator(unittest.TestCase):
    def test_add(self):
        result = Calc.add(2, 2)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()  # Call unittest.main() properly
