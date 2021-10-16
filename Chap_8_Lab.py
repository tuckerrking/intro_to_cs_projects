# This program uses two parallel arrays and a loop
# to print out the number of days in each month.

# String array with the names of each month.
names_of_months = ['January', 'February', 'March', 'April', 'May',
          'June', 'July', 'August', 'September', 'October',
          'November', 'December']

# Integer array containing the number of days in each month.
num_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for month, day in zip(names_of_months, num_of_days):
    print('{} has {} days.'.format(month,day))
