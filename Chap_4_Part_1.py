# Program gets two names from user input,
# then displays them alphabetically

def get_name_1():
    name_1 = input("Please enter a name: ")
    return name_1

def get_name_2():
    name_2 = input("Please enter a second name: ")
    return name_2

def compare_names(name_1, name_2):
    if name_1 < name_2:
       print(name_1)
       print(name_2)
    elif name_1 == name_2:
        print("You've entered the same name twice.")
    else:
        print(name_2)
        print(name_1)

# Main body of program

name_1 = get_name_1()
name_2 = get_name_2()
compare_names(name_1, name_2)
