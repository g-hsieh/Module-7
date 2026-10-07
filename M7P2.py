print("Begin entering a start, stop, and increment value from the keyboard.")

startValue = int(input("What's the start value? "))
endValue = int(input("What's the stop value? "))
incrementValue = int(input("What is the increment value? "))

count = startValue

while count <= endValue:
    print(count)
    count = count + incrementValue