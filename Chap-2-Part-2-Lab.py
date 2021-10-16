# Program computes how much an employee should be paid
# Asks the user a) how many hours they worked,
# b) what their hourly pay is,
# and c) how much money they want taken out for taxes.

# Get the needed information:
hoursWorked = float (input ("Enter the number of hours you've worked: "))
hourlyPay = float (input ("Enter your hourly pay: "))
taxes = float (input ("Enter the amount you want taken out for taxes: "))

# Perform computation to get paycheck amount
paycheck = (hoursWorked * hourlyPay) - taxes

# Print out paycheck amount
print("Your paycheck will be ", paycheck)
