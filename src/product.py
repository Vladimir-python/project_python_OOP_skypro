class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_params):
        return cls(product_params["name"], product_params["description"], product_params["price"], product_params["quantity"])

