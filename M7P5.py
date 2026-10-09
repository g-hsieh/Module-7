runProgram = input("Would you like to know the total discounts and total amount for your order? (YES/NO): ")

Price = 0
extPrice = 0
DiscountAmount = 0
Total = 0
totalDiscount = 0
totalAmount = 0
ItemCount = 0

if runProgram.lower() in ("yes", "y"):
    while runProgram.lower() in ("yes", "y"):

        Item = input("What's the item you're buying? ")
        Quantity = int(input("What's the quantity of that item? "))
        Price = float(input("What's the price of that item? "))

        extPrice = Quantity * Price

        if extPrice >= 10000:
            DiscountAmount = extPrice * 0.25
        else:
            DiscountAmount = extPrice * 0.10

        Total = extPrice - DiscountAmount
        totalAmount += Total
        totalDiscount += DiscountAmount
        ItemCount += 1

        print()
        print("Item:", Item)
        print("Quantity:", Quantity)
        print("Price: ${:,.2f}".format(Price))
        print("Extended Price: ${:,.2f}".format(extPrice))
        print("Discount Amount: ${:,.2f}".format(DiscountAmount))
        print("Total after discount: ${:,.2f}".format(Total))
        print("Number of items:", ItemCount)
        print()
        runProgram = input("Would you like to enter another item? (Yes/No): ")

print()
print("Program ended.")
print("Total number of items you entered:", ItemCount)
print("Total Amount after discounts: ${:,.2f}".format(totalAmount))
print("Total discounts: ${:,.2f}".format(totalDiscount))
print("Total Amount: ${:,.2f}".format(Total))