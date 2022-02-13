# Print greeting
print("Welcome to Sales Calculator!.")
# ask for the bill
before_tax_price = float(input("What is your your bill $"))
# ask for sales percent
sales_tax_rate = float(input("What is your sales percent? 5, 10, 15 ?\n"))

# Calculation
sales_tax_rate_percent = sales_tax_rate / 100
print(sales_tax_rate_percent)

after_tax_price = round(sales_tax_rate_percent * before_tax_price + before_tax_price, 2)

# Final output 
print(f"Your total bill is ${after_tax_price}")