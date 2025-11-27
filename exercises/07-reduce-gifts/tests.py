import unittest
import app


class TestReduceGifts(unittest.TestCase):
    def test_example1(self):
        prices = [3, 2, 1, 4, 6, 5]
        self.assertEqual(app.reduce_gifts(prices, 3, 14), 1)

    def test_example2(self):
        prices = [9, 6, 7, 2, 7, 2]
        self.assertEqual(app.reduce_gifts(prices, 3, 14), 2)

    def test_no_removals_needed(self):
        prices = [1, 1, 1, 1]
        self.assertEqual(app.reduce_gifts(prices, 3, 10), 0)

    def test_short_array(self):
        prices = [5, 5]
        self.assertEqual(app.reduce_gifts(prices, 3, 5), 0)


if __name__ == '__main__':
    unittest.main()
