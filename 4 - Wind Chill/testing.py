import unittest

from wind_chill import*


class MyFirstTests(unittest.TestCase):

    def test_convertTemp(self):
        self.assertEqual(convertTemp(10,15), -6.5895344209562525)


if __name__ == '__main__':
    unittest.main()
