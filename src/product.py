class Product:
    def __init__(self, name, description, price, quantity):
        if quantity == 0:
            raise ValueError("Количество товаров не может быть нулевым")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_params):
        return cls(product_params["name"], product_params["description"], product_params["price"],
                   product_params["quantity"])

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Cannot add products of different types")

        total_cost = (self.price * self.quantity) + (other.price * other.quantity)
        return total_cost

    def get_total_price(self):
        return self.price * self.quantity
