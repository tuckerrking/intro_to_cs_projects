# Program takes user input and calculates
# sale price after tax

def get_sale_price():
    sale_price = float(input ("Enter the sale price: "))
    return sale_price

def get_tax_rate():
    tax_rate = float(input ("Enter the tax rate: "))
    return tax_rate

def calculate_new_price(sale_price, tax_rate):
    new_price = sale_price + (sale_price * tax_rate)
    print ("The final price is ", new_price)


# Main body of program
sale_price = get_sale_price()
tax_rate = get_tax_rate()
final_price = calculate_new_price(sale_price, tax_rate)

