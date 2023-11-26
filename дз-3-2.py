a=int(input("Введіть число: "))
b=a//10
c=a%10
if b<c:
    print("Перша цифра менше")
elif b>c:
    print("Друга цифра менше")
else:
    print("Цифри рівні")