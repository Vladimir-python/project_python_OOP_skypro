from src.store import Product, Category


def test_product_initialization():
    product = Product("Test Product", "Description", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_category_initialization():
    products = [Product("Product 1", "Description 1", 50.0, 5), Product("Product 2", "Description 2", 75.0, 8)]
    category = Category("Test Category", "Category Description", products)
    assert category.name == "Test Category"
    assert category.description == "Category Description"
    assert category.products == products


def test_category_count():
    initial_count = Category.get_category_count()
    products = [Product("Product 3", "Description 3", 60.0, 3), Product("Product 4", "Description 4", 80.0, 6)]
    Category("Test Category 2", "Category Description 2", products)
    assert Category.get_category_count() == initial_count + 1


def test_product_count():
    initial_count = Category.get_product_count()
    products = [Product("Product 5", "Description 5", 70.0, 2)]
    Category("Test Category 3", "Category Description 3", products)
    assert Category.get_product_count() == initial_count + len(products)
