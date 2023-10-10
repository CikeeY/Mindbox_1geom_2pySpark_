import unittest
from Module import Circle
from Module import Triangle

class TestModule(unittest.TestCase):
  def setUp(self):
    self.moduleCir = Circle((0, 0), (5, 0))
    self.triangle1 = Triangle((0, 0), (10, 0), (0, 5))
    self.triangle2 = Triangle((0, 0), (1, 0), (0, 1))
  def test_radius(self):
    self.assertEqual(self.moduleCir.radius(), 5.0)
  def test_Circle_area(self):
    self.assertEqual(self.moduleCir.area(), 78.53981633974483)
  def test_Triangle_perimeter(self):
    self.assertEqual(self.triangle1.perimeter(), 13.090169943749475)
  def test_Triangle_area(self):
    self.assertEqual(self.triangle1.area(), 25.000000000000004)
  def test_Triangle_isRight(self):
    self.assertEqual(self.triangle1.isRight(), True)
  def test_Triangle_isRight(self):
    self.assertEqual(self.triangle2.isRight(), False)

if __name__ == "__main__":
  unittest.main()