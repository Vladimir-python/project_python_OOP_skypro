# tests/test_category.py

import unittest
from src.product import Product
from src.category import Category


class TestCategory(unittest.TestCase):

    def test_add_product(self):
        product1 = Product("Test Product 1", "Description 1", 50.0, 5)
        product2 = Product("Test Product 2", "Description 2", 75.0, 8)
        category = Category("Test Category", "Category Description", [product1])

        self.assertEqual(len(category._Category__products), 1)
        category.add_product(product2)
        self.assertEqual(len(category._Category__products), 2)

    def test_products_property(self):
        product1 = Product("Test Product 1", "Description 1", 50.0, 5)
        product2 = Product("Test Product 2", "Description 2", 75.0, 8)
        category = Category("Test Category", "Category Description", [product1, product2])

        expected_output = "Test Product 1, 50.0 руб. Остаток: 5 шт.\nTest Product 2, 75.0 руб. Остаток: 8 шт."
        self.assertEqual(category.products, expected_output)


if __name__ == '__main__':
    unittest.main()
