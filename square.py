n=int(input("enter number of rows(columns)"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end="")
    print("")
print("------------------------------------")
for i in range(1,n+1):
    for j in range(i,n+1):
        print(j,end="")
    print("")
print("------------------------------------")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print("")