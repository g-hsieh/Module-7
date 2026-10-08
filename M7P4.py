print("You and your employees need to decide if he or she or you want to run this program. ")
print()

runProgram = input("Would you like to try running the program? (Yes/No): ")

employeeCount = 0
totalGrossPay = 0

while runProgram.lower() == "yes":

    LastName = input("What is your last name? ")
    Hours = float(input("How many hours did you work today? "))
    RatePay = float(input("What is your rate pay? "))

    if Hours <= 40:
        GrossPay = Hours * RatePay
    else:
        RegularPay = 40 * RatePay
        OvertimeHours = Hours - 40
        OvertimePay = OvertimeHours * RatePay * 1.5
        GrossPay = RegularPay + OvertimePay

    totalGrossPay += GrossPay
    employeeCount += 1

    print()
    print("Last Name:", LastName)
    print("Hours:", Hours)
    print("Gross Pay: ${:,.2f}".format(GrossPay))
    print("Number of employees entered:", employeeCount)
    print()

    runProgram = input("Would you like to enter another employee to run the program? (Yes/No): ")

print()
print("Program ended.")
print("Total number of employees entered:", employeeCount)
print("Total gross pay: ${:,.2f}".format(totalGrossPay))