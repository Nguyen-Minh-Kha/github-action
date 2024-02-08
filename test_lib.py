import unittest
from lib import average_positive_values

class TestAveragePositiveValues(unittest.TestCase):

  def test_empty_list(self):
		self.assertEqual(average_positive_values([]), 0)

  def test_all_negative_values(self):
		self.assertEqual(average_positive_values([-1, -2, -3]), 0)

  def test_some_positive_values(self):
		self.assertEqual(average_positive_values([1, -2, 3]), 2)

  def test_all_positive_values(self):
		self.assertEqual(average_positive_values([1, 2, 3]), 2)

  def test_fail(self):
		self.assertEqual(average_positive_values(['a', 45, "EE", average_positive_values()]), 2)

if __name__ == '__main__':
  unittest.main()
