# Program asks the user to enter a distance in kilometers,
# and then converts tjat distance to miles

# Conversion module
def convert_kilometers_to_miles(kilometers):
    miles = kilometers * 0.6214
    return miles

# Main body of program
distance_in_kilometers = int(input("Please enter a distance in kilometers: "))
distance_in_miles = convert_kilometers_to_miles(distance_in_kilometers)
print(str(distance_in_kilometers) +
      " kilometers is equal to " + str(distance_in_miles) + " miles.")
