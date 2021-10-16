# This program asks the user to input a year between 1895 and
# 2020, then tells the user what era of film history
# that year falls into.

# This module displays a menu where the user can choose whether to enter a year or
# quit the program
def display_menu():
    user_input = 0.0
    while(user_input != "q"):
        print("To find the era of film history a certain year falls into, type 1.")
        print("To quit this program, type q.")
        menu_input = input("\nEnter your choice here: ")
        if (menu_input == "1"):
            get_year()
        elif (menu_input == "q"):
            print("Exiting program...")
            break
        else:
            print("Invalid input; please enter ""1"" or ""q"".\n")


# This module gets the year from the user
def get_year():
    year = int(input("Please enter a year between 1895 and 2020: "))
    get_era(year)

# This module determines what era the given year fits into.
def get_era(year):
    if (year < 1895):
        print("This year comes before any of the eras of film history.\n")
    elif (year >= 1895 and year <= 1910):
        print(year, "falls into the Pioneer Era.\n")
    elif (year >= 1911 and year <= 1926):
        print(year, "falls into the Silent Era.\n")
    elif (year >= 1927 and year <= 1940):
        print(year, "falls into the era of Talkies and the rise of Hollywood.\n")
    elif (year >= 1941 and year <= 1954):
        print(year, "falls into the Golden Era of film and the restructuring of Hollywood.\n")
    elif (year >= 1955 and year <= 1976):
        print(year, "falls into the New Hollywood era and the decline of studio films.\n")
    elif (year >= 1977 and year <= 1999):
        print(year, "falls into the dawn of the modern film industry and the rise of blockbusters.\n")
    elif(year >= 2000 and year <= 2020):
        print(year, "falls into the modern film industry era.\n")
    else:
        print("This isn't a time machine; you can't look into the future!\n")



# Main body of program:
# ---------------------

display_menu()
