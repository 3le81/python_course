# # Example 1 of logical error
xmas_lights = "off"
user_choice = int(input("Choose 0 for OFF or 1 for ON: "))

# Logical error by reversing the condition and still the code works
if user_choice == 0:
    xmas_lights = "ON"
else:
    xmas_lights = "OFF"

print(f"xmas_lights are {xmas_lights}")
print("*" * 80)


# # Example 2 of logical error
# xmas_lights = "off"
# # Logical error, not casting to integer and still the code works
# user_choice = (input("Choose 0 for OFF or 1 for ON: "))

# if user_choice == 1:
#     xmas_lights = "ON"
# else:
#     xmas_lights = "OFF"

# print(f"xmas_lights are {xmas_lights}")
