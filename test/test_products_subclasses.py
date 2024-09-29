import pytest
from src.product import Product
from src.category import Category
from src.products_subclasses import Smartphone, LawnGrass

def test_add_product_only_allowed_classes():
    category = Category("Category Name", "Category Description", [])
    product1 = Product("Product 1", "Description", 10, 5)
    product2 = Smartphone("Smartphone 1", "Description", 500, 2, "Efficiency", "Model", "Memory", "Color")
    product3 = LawnGrass("Lawn Grass 1", "Description", 20, 10, "Country", "Germination Period", "Green")
    other_product = "Some other product"

    category.add_product(product1)
    category.add_product(product2)
    category.add_product(product3)

    with pytest.raises(TypeError):
        category.add_product(other_product)
