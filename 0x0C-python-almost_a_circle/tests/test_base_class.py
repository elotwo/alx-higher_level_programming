import sys
sys.path.append('/home/emmanuel/alx-higher_level_programming/0x0C-python-almost_a_circle/tests')
import unittest
from models.base import Base
class TestBase(unittest.TestCase):
    def tes_Base(self):
        b1 = Base(id=100)
        self.assertEqual(b1.id, 100)
    def test_init_without_id(self):
         b2 = Base()
         self.assertEqual(b2.id, 1)
         b3 = Base()
         self.assertEqual(b3.id, 2)
         b4 = Base()
         self.assertEqual(b4.id, 3)
    if __name__ == '__main__':
        unittest.main()
