from products import Product


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum
    
    def show_product_details(self):
        details = super().show_product_details()
        details += f" (Limited to {self.maximum} per order)"
        return details
