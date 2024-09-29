from src.product import Product


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
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            raise TypeError("Only instances of Product can be added to the category")

    def calculate_average_price(self):
        total_price = sum(product.price for product in self.__products)
        total_quantity = sum(product.quantity for product in self.__products)

        if total_quantity == 0:
            return 0
        else:
            return total_price / total_quantity

    def __str__(self):
        total_products = sum(product.quantity for product in self.__products)
        return f"{self._name}, количество продуктов: {total_products} шт."

    def __add__(self, other):
        if not isinstance(other, Category):
            raise TypeError("Cannot add a non-Category object")

        total_cost = sum(product.price * product.quantity for product in self.__products) + sum(
            product.price * product.quantity for product in other.__products)
        return total_cost
