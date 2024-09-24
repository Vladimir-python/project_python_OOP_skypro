from src.product import Product
from src.category import Category


def test_add_product():
    product1 = Product("Test Product 1", "Description 1", 50.0, 5)
    product2 = Product("Test Product 2", "Description 2", 75.0, 8)
    category = Category("Test Category", "Category Description", [product1])

    assert len(category._Category__products) == 1
    category.add_product(product2)
    assert len(category._Category__products) == 2


def test_products_property():
    product1 = Product("Test Product 1", "Description 1", 50.0, 5)
    product2 = Product("Test Product 2", "Description 2", 75.0, 8)
    category = Category("Test Category", "Category Description", [product1, product2])

    assert category.products == "Test Product 1, 50.0 руб. Остаток: 5 шт.\nTest Product 2, 75.0 руб. Остаток: 8 шт."

