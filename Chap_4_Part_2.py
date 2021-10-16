# Program asks the user to enter an object's mass in kilograms,
# then calculates its weight in Newtons.
# If the object's weight is greater than 1000 Newtons,
# the program will display "The object is too heavy."
# If the object's weight is less than 10 Newtons,
# the program will display "The object is too light."

def get_mass():
    mass = float(input("Please enter the mass of the object: "))
    return mass

def get_weight(mass):
    weight = mass * 9.8
    return weight

# Main body of program

mass = get_mass()
weight = get_weight(mass)
if weight > 1000:
    print("The object is too heavy.")
elif weight < 10:
    print("The object is too light.")
else:
    print("The object has a weight of " + str(weight) + " Newtons.")
