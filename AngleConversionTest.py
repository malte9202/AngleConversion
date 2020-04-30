import unittest
from unittest import mock
from AngleConversion import *


class TestAngleConversion(unittest.TestCase):
    @mock.patch('AngleConversion.get_conversion_type', create=True)
    def test_get_conversion_type(self,mocked_conversion_type):
        mocked_conversion_type.side_effect = [1]
        result = AngleConversion.get_conversion_type()
        self.assertEqual(result, 1, "Should be 1")

    def test_rad_to_degree(self):
        self.assertEqual(AngleConversion.convert_angle(1, 0.6), 34.38, "Should be 34.38")
        self.assertEqual(AngleConversion.convert_angle(1, 0), 0, "Should be 0")
        self.assertEqual(AngleConversion.convert_angle(1, 2), 114.59, "Should be 114.59")

    def test_degree_to_rad(self):
        self.assertEqual(AngleConversion.convert_angle(2, 90), 1.57, "Should be 1.57")
        self.assertEqual(AngleConversion.convert_angle(2, 180), 3.14, "Should be 3.14")
        self.assertEqual(AngleConversion.convert_angle(2, 360), 6.28, "Should be 6.28")


if __name__ == '__main__':
    unittest.main()
