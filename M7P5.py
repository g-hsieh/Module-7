print("You and your friends need to decide if he or she wants to run this program to enter a quantity and price of an item to buy at the store.")
print()

runProgram = input("Would you like to know how many items you are buying? (YES/NO): ")
runProgram = input("Would you like to know your total discounts and your total amount? (YES/NO): ")

Price = 0
extPrice = 0
DiscountAmount = 0
Total = 0
totalDiscount = 0
ItemCount = 0

while runProgram.lower() == "yes":

    Item = input("What's the item you're buying? ")
    Quantity = float(input("What's the quantity of that item? "))
    Price = float(input("What's the price of that item? "))

    extPrice = Quantity * Price

    if extPrice >= 10000:
        DiscountAmount = extPrice * 0.25
    else:
        DiscountAmount = extPrice * 0.10

    Total = extPrice - DiscountAmount
    totalDiscount += DiscountAmount
    ItemCount += 1

    print()
    print("Item:", Item)
    print("Quantity:", Quantity)
    print("Price: ${:,.2f}".format(Price))
    print("Extended Price: ${:,.2f}".format(extPrice))
    print("Discount Amount: ${:,.2f}".format(DiscountAmount))
    print("Item Number:", ItemCount)
    print()

    runProgram = input("Would you like to enter another item? (Yes/No): ")

print()
print("Program ended.")
print("Total number of items you entered:", ItemCount)
print("Total discounts: ${:,.2f}".format(totalDiscount))
print("Total Amount: ${:,.2f}".format(Total))