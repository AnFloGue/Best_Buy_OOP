from products import Product
from limited_product import LimitedProduct
from store import Store
from promotions import SecondHalfPrice, ThirdOneFree, PercentDiscount

# setup initial stock of inventory
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
    Product("Windows License", price=125, quantity=0),  # Assuming NonStockedProduct is similar to Product
    LimitedProduct("Shipping", price=10, quantity=250, maximum=1)  # LimitedProduct with maximum attribute
]

# Create promotion catalog
second_half_price = SecondHalfPrice("Second Half price!")
third_one_free = ThirdOneFree("Third One Free!")
thirty_percent = PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

# Example usage
print("-----------------------------")
for product in product_list:
    print(product.show_product_details())
print("-----------------------------")

my_tienda = Store(product_list)


def start(store):
    while True:
        print()
        print("-----------------------------")
        print("Welcome to MY TIENDA!")
        print("-----------------------------")
        print("Menu:")
        print("-----------------------------")
        
        print("1. Inventory of products in store")
        print("2. Total quantity of items in store")
        print("3. Make an order")
        print("4. Quit")
        print("-----------------------------")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("-----------------------------")
            products = store.get_all_active_products()
            for product in products:
                print(product.show_product_details())
            print("-----------------------------")
        
        elif choice == '2':
            print("-----------------------------")
            total_quantity = store.get_total_quantity()
            print(f"\nTotal quantity of items in store: {total_quantity} units")
            print("-----------------------------")
        
        elif choice == '3':
            print("-----------------------------")
            shopping_list = []
            
            while True:
                product_name = input("Enter product name (or 'done' to finish): ")
                
                if product_name.lower() == 'done':
                    break
                
                quantity = int(input("Enter quantity: "))
                
                product_found = False
                for item in store.get_all_active_products():
                    if item.name.lower() == product_name.lower():
                        product = item
                        product_found = True
                        shopping_list.append((product, quantity))
                        break
                
                if not product_found:
                    print("Product not found.")
            
            total_price_no_taxes = store.order(shopping_list)
            print("-----------------------------")
            print(f"\nYour Shopping List:")
            print("-----------------------------")
            
            for product, quantity in shopping_list:
                print(f"{product.name} - {quantity} units")
            print(f"Total price of the order: {total_price_no_taxes}")
        
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print(f"\nInvalid choice. Please try again.")


if __name__ == '__main__':
    start(my_tienda)
