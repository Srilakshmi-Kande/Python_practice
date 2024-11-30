n=int(input("enter range : "))
sum=0
for n in range(1,n+1):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        print(n,end="")
        print("")
        sum+=n
print("sum of prime numbers is ",sum)