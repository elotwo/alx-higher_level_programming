import unittest
from models.rectangle import Rectangle
import sys
sys.path.append('/home/emmanuel/alx-higher_level_programming/0x0C-python-almost_a_circle/tests')
class Testrectangle(unittest.TestCase):
    def test_constructor(self):
        rect = Rectangle(5,9)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 9)
    def test_display(self):
        rect = Rectangle(5, 9)
        result = rect.display()
if __name__ == '__main__':
    unittest.main()

