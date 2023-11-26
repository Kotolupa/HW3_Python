n=int(input("Enter number: "))
while n>1:
    if n%10==2:
        print("True")
        n=n-n
    else: n=n//10
print("False")