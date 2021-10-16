# This program asks the user to enter 20 names, separated by commas,
# into a string array,
# then sorts that array in alphabetical order and displays
# its contents.
# The program uses the "bubble sort" method.

# Funtion gets user input
def get_user_input():
    list_of_names = []
    separator = ","
    list_of_names = input("Please enter 20 names, separated with commas: ")
    list_of_names = list_of_names.split(separator)
    return list_of_names

# Funtion uses bubble sort to sort the array alphabetically
def bubble_sort(list_of_names):
    for names in range(0, len(list_of_names) - 1):
        for x in range(0, len(list_of_names) - 1 - names):
            if list_of_names[x] > list_of_names[x + 1]:
                list_of_names[x], list_of_names[x + 1] = list_of_names[x + 1], list_of_names[x]
    return list_of_names

# Funtion displays the sorted array
def display_sorted_array(list_of_names):
    print("Here are the names you entered, sorted alphabetically:\n")
    for name in list_of_names:
        print(name + "\n")


list_of_names = get_user_input()
bubble_sort(list_of_names)
display_sorted_array(list_of_names)
