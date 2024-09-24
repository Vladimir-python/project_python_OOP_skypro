from src.product import Product
from src.products_subclasses import Smartphone, LawnGrass

class Category:
    def __init__(self, name, description, products):
        self._name = name
        self._description = description
        self.__products = products

    @property
    def products(self):
        product_info = [f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.'
                        for product in self.__products]
        product_info_str = '\n'.join(product_info)
        return product_info_str

    def add_product(self, product):
        if isinstance(product, (Product, Smartphone, LawnGrass)):
            self.__products.append(product)
        else:
            raise TypeError("Only instances of Product, Smartphone, or LawnGrass can be added to the category")

    def __str__(self):
        total_products = sum(product.quantity for product in self.__products)
        return f"{self._name}, количество продуктов: {total_products} шт."

    def __add__(self, other):
        total_cost = sum(product.price * product.quantity for product in self.__products) + sum(product.price * product.quantity for product in other.__products)
        return total_cost
