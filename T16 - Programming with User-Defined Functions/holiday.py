# Function to calculate the cost of the hotel based on the number of nights
def hotel_cost(num_nights):
    # Assuming a fixed cost per night for the hotel
    hotel_night_cost = 100  # This value can be changed as needed
    return num_nights * hotel_night_cost


# Function to calculate the cost of a plane ticket based on the destination city
def plane_cost(city_flight):
    # Dictionary mapping valid cities to their respective costs
    city_costs = {
        "new york": 300,
        "los angeles": 250,
        "chicago": 200
    }

    # Convert user input to lowercase for case-insensitive comparison
    city_flight_lower = city_flight.lower()

    # Check if the input is a valid city
    if city_flight_lower in city_costs:
        return city_costs[city_flight_lower]  # Return the cost for the city

    # If the input is not valid, return 0 as the default cost
    return 0


# Function to calculate the cost of car rental based on the number of days
def car_rental(rental_days):
    # Assuming a fixed daily rental cost for the car
    daily_rental_cost = 50  # This value can be changed as needed
    return rental_days * daily_rental_cost


# Function to calculate the total cost of the holiday by combining hotel, plane, and car rental costs
def holiday_cost(num_nights, city_flight, rental_days):
    # Calculate total cost for each component
    total_hotel_cost = hotel_cost(num_nights)
    total_plane_cost = plane_cost(city_flight)
    total_car_rental_cost = car_rental(rental_days)

    # Return the sum of all costs
    return (total_hotel_cost + total_plane_cost + total_car_rental_cost)


# Set of the valid cities
valid_cities = {"new york", "los angeles", "chicago"}

# Get user input for city
city_flight = input(
    "Enter the city you will be flying to (New York, Los Angeles, Chicago): ").lower()

# Check if the input is a valid city
while city_flight not in valid_cities:
    print("Please enter a valid city.")
    city_flight = input(
        "Enter the city you will be flying to (New York, Los Angeles, Chicago): ").lower()

# Get user inputs for other details, with error handling
try:
    num_nights = int(
        input("Enter the number of nights you will be staying at a hotel: "))
    rental_days = int(
        input("Enter the number of days you will be hiring a car: "))
except ValueError:
    print("Please enter valid numeric values for nights and rental days.")
    exit()

# Calculate total holiday cost
total_cost = holiday_cost(num_nights, city_flight, rental_days)

# Print details about the holiday in a table-like format
print("\nYour Holiday Details:\n")
print(f"City of Flight:            {city_flight.upper()}")
print(f"Number of Nights :         {num_nights}")
print(f"Number of Rental Days:     {rental_days}")
print(f"\nYour Total Holiday Cost:   £{total_cost}")
