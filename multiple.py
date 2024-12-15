num=int(input("Enter number : "))
divisor=int(input("Enter divisor : "))
if(num%divisor==0):
    print(num," is a Divisable by ",divisor)
    print(divisor," is multiple of ",num)
else:
    print(num," is not divisable by ",divisor)
    print(divisor," is not a multiple of ",num)