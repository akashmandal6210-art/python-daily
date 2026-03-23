number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
#addition
add=number1+number2
print("the sum of",number1,"and",number2,"is",add)
#subtraction
sub=number1-number2
print("the subtraction of",number1,"and",number2,"is",sub)
if number2!=0:
    div=number1/number2
    print("the division of",number1,"and",number2,"is",div)
else:
    print("division by zero is not allowed")
    if number2!=0:
        flr=number1//number2
        print("the floor of",number1,"and",number2,"is",flr)
        mul=number1*number2
        print("the multiplication of ",number1,"and",number2,"is",mul)
        exp=number1**number2
        print("the exponent of",number1,"and",number2,"is",exp)
