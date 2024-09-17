A = float(input("Enter the First digit: "))
B = float(input("Enter the Second digit: "))
o = str(input("Enter the Operation(+,-,*,/): "))
if (o == '+'):
    res = A + B
elif (o == '-'):
    res = A - B
elif (o == '*'):
    res = A * B
elif (o == '/'):
    res = A / B
else:
    print("ERROR: Invalid Input")
print("RESULT: ",res)