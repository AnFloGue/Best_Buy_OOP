class Store:
    def __init__(self, products):
        self.products = products  # Initialize the products attribute

    def get_all_active_products(self):
        # Return a list of products that are available (quantity > 0)
        return [product for product in self.products if product.quantity > 0]

    def get_total_quantity(self):
        # Return the total quantity of all products
        return sum(product.quantity for product in self.products)

    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            if product.quantity >= quantity:
                total_price += product.price * quantity
                product.quantity -= quantity  # Update product quantity
            else:
                print(f"Not enough stock for {product.name}")
        return total_price