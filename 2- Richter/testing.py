import unittest

from richter import *


class MyFirstTests(unittest.TestCase):

    def test_convertJoules(self):
        self.assertEqual(convertJoules(1), 1995262.3149688789)


if __name__ == '__main__':
    unittest.main()
