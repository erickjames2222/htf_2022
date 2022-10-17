Number = int(input("Enter the Number to Check Disarium Number = "))
length = len(str(Number))

Temp = Number
Sum = 0
rem = 0

while Temp > 0:
    rem = Temp % 10
    Sum = Sum + int(rem**length)
    Temp = Temp // 10
    length = length - 1

print("The Sum of the Digits = %d" %Sum)

if Sum == Number:
    print("\n%d is a Disarium Number." %Number)
else:
    print("%d is Not a Disarium Number." %Number)