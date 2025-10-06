a = int(input("Enter the 1st num: "))
b = int(input("Enter the 1st num: "))
op =input("Operator: ")
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="/":
    print(a/b)
else:
    print("SyntaxError")