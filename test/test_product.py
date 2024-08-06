from src.product import Product


def test_new_product():
    product_params = {"name": "Test Product", "description": "Test Description", "price": 100.0, "quantity": 10}
    new_product = Product.new_product(product_params)
    assert new_product.name == "Test Product"
    assert new_product.description == "Test Description"
    assert new_product.price == 100.0
    assert new_product.quantity == 10
