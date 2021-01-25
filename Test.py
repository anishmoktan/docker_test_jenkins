import unittest

class TestCalc(unittest.TestCase):

    def test_add(self):
        result = 10 + 5
        self.assertEqual(result,15)

    def test_add_1(self):
        result = 10 + 5
        self.assertEqual(result,15)

    def test_add_2(self):
        result = 10 + 6
        self.assertEqual(result,15)

if __name__ == '__main__':
    unittest.main()
