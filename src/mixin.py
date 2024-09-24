# mixin.py
class InfoMixin:
    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        print(f"Object created from class {self.__class__.__name__} with parameters: {name}, {description}, {price}, {quantity}")

    def __repr__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."
