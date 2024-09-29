from abc import ABC, abstractmethod


class BaseProduct(ABC):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def get_total_price(self):
        pass
