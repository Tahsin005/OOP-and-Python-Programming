cost_price = int(input("Enter the cost_price of the product : "))
selling_price = int(input("Enter the selling_price of the product : "))
made = selling_price - cost_price
if made > 0:
    print("Profit :" , made)
elif made < 0:
    print("Loss :", (made * (-1)))
else:
    print("No profit or loss.")