size=int(input("enter size : "))
count=0
for i in range(size):
    for j in range(size):
        print(chr(65+count),end=" ")
        count+=1
    print()
print("--------------------------------------")
for i in range(size):
    for j in range(size):
        print(chr(65+i),end=" ")
    print()
print("--------------------------------------")
for i in range(size):
    for j in range(65,65+size):
        print(chr(j),end=" ")
    print()
print("--------------------------------------")
for i in range(size):
    for j in range(i+1):
        print(chr(j+65),end=" ")
    print()
print("--------------------------------------")
for i in range(size):
    for j in range(1,size-i):
        print(" ",end="")
    for k in range(i+1):
        print(chr(65+k),end=" ")
    print()