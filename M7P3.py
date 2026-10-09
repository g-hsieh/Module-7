print("Decide whether you want to do this program or let one of your friends do it.")
print()

runProgram = input("Would you like to try running the program? (Yes/No): ")

studentCount = 0

if runProgram.lower() in ("yes", "y"):
    while runProgram.lower() in ("yes", "y"):

        LastName = input("What's your last name? ")
        ExamScore1 = float(input("What is your first exam score? "))
        ExamScore2 = float(input("What is your second exam score? "))

        Average = (ExamScore1 + ExamScore2) * 0.5

        studentCount += 1

        print()
        print("Last Name:", LastName)
        print("Average:", Average)
        print("Number of students entered:", studentCount)
        print()

        runProgram = input("Would you like to enter another student to run the program? (Yes/No): ")

print()
print("Program ended.")
print("Total number of students entered:", studentCount)