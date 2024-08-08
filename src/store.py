class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product: {self.name}, Description: {self.description}, Price: {self.price}, Quantity: {self.quantity}"

    def __repr__(self):
        return self.__str__()


class Category:
    category_count = 0
    product_count = 0

    @classmethod
    def get_category_count(cls):
        return cls.category_count

    @classmethod
    def get_product_count(cls):
        return cls.product_count

    def __init__(self, name: str, description: str, products: list):
        self._name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, "
                         "но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(Category.get_category_count())
    print(Category.get_product_count())

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, "
                         "станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.get_category_count())
    print(Category.get_product_count())
