# Program uses nested loops to display a multiplication table
# for the numbers 1 through 12.

num = 1
for i in range(1, 13):
    print("Multiplication table of ", num)
    for i in range(1, 13):
        print(num, " x ", i, " = ", (num * i))
    num = num + 1
    
