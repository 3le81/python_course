# Triathlon Award Calculator

# Get input from the user for each event time:
swimming_time = int(input("Enter swimming time (in minutes): "))
cycling_time = int(input("Enter cycling time (in minutes): "))
running_time = int(input("Enter running time (in minutes): "))

# Calculate total time of the triathlon:
total_time = swimming_time + cycling_time + running_time

# Print out the total time taken:
print(f"Total time taken: {total_time} minutes")

# Determine the award based on the total time:
if total_time <= 100:
    # If total time is 100 minutes or less, it's "Provincial Colours"
    award = "Provincial Colours"
elif total_time <= 105:
    # If total time is more than 100 but 105 or less, it's "Provincial Half Colours"
    award = "Provincial Half Colours"
elif total_time <= 110:
    # If total time is more than 105 but 110 or less, it's "Provincial Scroll"
    award = "Provincial Scroll"
else:
    # If total time is more than 110, no award is given
    award = "No award"

# Output the award:
print(f"Award: {award}")
