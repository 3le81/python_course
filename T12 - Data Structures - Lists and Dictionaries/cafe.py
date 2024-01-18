# List to store the items sold in the cafe
menu = ["Espresso", "American Coffee", "Tea",
        "Assorted Sandwiches", "Velvet Cake"]

# Dictionary representing available stock for each item
stock = {
    "Espresso": 100,
    "American Coffee": 100,
    "Tea": 50,
    "Assorted Sandwiches": 30,
    "Velvet Cake": 20
}

# Dictionary representing the price for each item
price = {
    "Espresso": 1.00,
    "American Coffee": 2.50,
    "Tea": 1.50,
    "Assorted Sandwiches": 5.00,
    "Velvet Cake": 3.00
}

# Calculate the total stock worth in the cafe using a list comprehension
total_stock = sum(stock[item] * price[item] for item in menu)

# Print a message with the result of the calculation using an f-string
print(f'The total value of the cafe\'s stock is: £{total_stock:.2f}')
