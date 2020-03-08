import unittest
from HW4 import Person
from HW4 import Point

# result = aws_boto3_data_filter.iterate_and_find()
# print(result)
# expected = data_etm_0510
# self.assertEqual(result, expected)


class TestHW4(unittest.TestCase):
    """Unittest for SGRC Linter"""

    def test_lastname(self):
        """test last_name"""
        teacher = Person("Diane", "Chen")
        result = teacher.last_name
        expected = "Chen"
        self.assertEqual(result, expected)

    def test_name(self):
        """test name """
        teacher = Person("Diane", "Chen")
        result = teacher.name
        expected = 'Chen, Diane'
        self.assertEqual(result, expected)

    def test_full_name(self):
        """test full name """
        teacher = Person("Diane", "Chen")
        result = teacher.full_name
        expected = 'Diane Chen'
        self.assertEqual(result, expected)

    def test_first_name(self):
        """test changing firstname and get the result"""
        teacher = Person("Diane", "Chen")
        teacher.first_name = "D. D."
        result = teacher.first_name
        expected = "D. D."
        self.assertEqual(result, expected)
        result2 = teacher.full_name
        expected2 = 'D. D. Chen'
        self.assertEqual(result2, expected2)

    def test_point_repr(self):
        """test repr_output"""
        point = Point(x=3, y=4)
        result = repr(point)
        expected = 'Point(x=3, y=4)'
        self.assertEqual(result, expected)

    def test_point_str(self):
        """test str_output"""
        point = Point(x=3, y=4)
        result = str(point)
        expected = 'Point at (3, 4)'
        self.assertEqual(result, expected)

    def test_point_default(self):
        """test last_name"""
        point2 = Point()
        result = point2
        expected = 'Point(x=0, y=0)'
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
