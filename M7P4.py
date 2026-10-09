print("You and your employees need to decide if he or she or you wants to know his or her Gross Pay. ")
print()

runProgram = input("Would you like to know your Gross Pay? (Yes/No): ")

employeeCount = 0
totalGrossPay = 0

if runProgram.lower() in ("yes", "y"):
    while runProgram.lower() in ("yes", "y"):

        LastName = input("What is your last name? ")
        Hours = float(input("How many hours did you work? "))
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
        AveragePay = totalGrossPay/employeeCount

        print()
        print("Last Name:", LastName)
        print("Hours:", Hours)
        print("Gross Pay: ${:,.2f}".format(GrossPay))
        print()
        print("Sum of all Gross Pays: ${:,.2f}".format(totalGrossPay))
        print("Number of employees entered:", employeeCount)
        print("Average Pay: ${:,.2f}".format(AveragePay))
        print()
        runProgram = input("Would you like to enter another employee to run the program? (Yes/No): ")

print()
print("Program ended. Have a nice day!")