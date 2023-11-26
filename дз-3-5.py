a=int(input("Enter number a: "))
b=int(input("Enter number b: "))
for elem in range(a,b+1):
    count=0
    while count<elem:
        print(elem)
        count=count+1