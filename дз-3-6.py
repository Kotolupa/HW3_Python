a=int(input("Enter number a: "))
b=int(input("Enter number b: "))
count=1
for elem in range(a,b+1):
    if elem%6==0:
       count=count*elem
print(count)