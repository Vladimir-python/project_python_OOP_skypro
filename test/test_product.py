# tests/test_product.py

import unittest
from src.product import Product


class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product1 = Product("Test Product 1", "Description 1", 10, 5)
        self.product2 = Product("Test Product 2", "Description 2", 20, 3)

    def test_get_total_price(self):
        self.assertEqual(self.product1.get_total_price(), 50)
        self.assertEqual(self.product2.get_total_price(), 60)


if __name__ == '__main__':
    unittest.main()
