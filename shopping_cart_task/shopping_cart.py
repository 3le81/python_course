# 1: Data Structure
cart_items = []  # List to store items in the cart
item_prices = {
    "Dog Food": 25.99,
    "Cat Litter": 12.50,
    "Pet Toy": 8.75,
    "Fish Tank": 40.00,
    "Bird Cage": 30.50
}

# 2: User Menu
while True:
    # Display menu options to the user
    print("\n==== Paws n Cart ====")
    print("1. View Cart")
    print("2. Add Item to Cart")
    print("3. Remove Item from Cart")
    print("4. View Total Cost")
    print("5. Checkout")
    print("6. Exit")

    # Get user choice
    choice = input("Enter your choice (1-6): ")

# 3: Manipulating the Cart
    if choice == "1":
        # Display the items in the cart with their prices in a formatted manner
        if not cart_items:
            print("Your cart is empty.")
        else:
            print("Your Cart:")
            print("{:<5} {:<20} {:<10}".format("Index", "Product", "Price"))
            print("=" * 40)
            for i, item in enumerate(cart_items, 1):
                print("{:<5} {:<20} £{:<10.2f}".format(
                    i, item, item_prices[item]))

    elif choice == "2":
        # Add an item to the cart
        print("Available Products:")
        for i, (product, price) in enumerate(item_prices.items(), 1):
            print(f"{i}. {product} (£{price:.2f})")
        try:
            selected_index = int(
                input("Enter the number of the item you want to add: "))
            if 1 <= selected_index <= len(item_prices):
                selected_product = list(item_prices.keys())[selected_index - 1]
                cart_items.append(selected_product)
                print(f"{selected_product} added to your cart.")
            else:
                print("Invalid index. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif choice == "3":
        # Remove an item from the cart
        if not cart_items:
            print("Your cart is empty. Nothing to remove.")
        else:
            print("Your Cart:")
            for i, item in enumerate(cart_items, 1):
                print(f"{i}. {item}")
            try:
                item_index = int(
                    input("Enter the number of the item to remove: ")) - 1
                removed_item = cart_items.pop(item_index)
                print(f"{removed_item} removed from your cart.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid item number.")

    elif choice == "4":
        # View the total cost of the items in the cart
        total_cost = sum(item_prices[item] for item in cart_items)
        print(f"\nTotal Cost of Your Cart: £{total_cost:.2f}")

    elif choice == "5":
        # Checkout
        print("Thank you for shopping with Paws n Cart! Your order is complete.")
        break

    elif choice == "6":
        # Exit the program
        print("Exiting Paws n Cart. Goodbye!")
        break

    else:
        # Handle invalid choices
        print("Invalid choice. Please enter a number between 1 and 6.")
