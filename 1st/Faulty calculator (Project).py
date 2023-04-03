# To create a faulty calculator
    # 43 * 3=
    # 56 + 9= 77
    # 56 / 6= 4

a = int(input("enter your first number, a\n"))
b = int(input("enter your second number, b\n"))
c = input("please select your choice: *,+,-\n")
if a == 43 and b ==3 and c == "*":
    print(777)
elif a == 56 and b == 9 and c == "+":
    print(77)
elif a == 56 and b == 6 and c == "/":
    print(4)


