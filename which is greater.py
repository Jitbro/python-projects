a = int(input("num1: "))
b = int(input("num2: "))
c = int(input("num3: "))

if a>b and a>c:
    print("num1 is bigger")
elif b>a and b>c:
    print("num2 is bigger")
# elif c>a and c>b:
#     print("c is bigger")
else:
    print("num3 is bigger")