x=int(input("Enter age T: "))
y=int(input("Enter age M: "))
a=((x+y)/2)
if x<y:
    print(a-x, "на стільки Тетянка молодша за середній вік")
    print(y-a, "на стільки Мітя старший за середній вік")
else:
    print(a-y, "на стільки Мітя молодший за середній вік")
    print(x-a, "на стільки Тетянка старша за середній вік")