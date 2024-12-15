a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=int(input("Enter third number : "))

if a>=b and a>=c:
    print("first number is large",a)
elif b>=c:
    print("Second number is large",b)
else:
    print("Third number is large",c)