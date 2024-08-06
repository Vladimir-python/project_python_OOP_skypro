class Category:
    def __init__(self, name, description, products):
        self._name = name
        self._description = description
        self._products = products

    @property
    def products(self):
        product_info = [f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.'
                        for product in self._products]
        product_info_str = '\n'.join(product_info)
        return product_info_str

    def add_product(self, product):
        self._products.append(product)

