# 153 = 1*1+ 5*5*5+ 3*3*3

num = 153


def armstrong_number(numbers):
    sum = 0
    for i in str(numbers):
        # print(i)
        sum += int(i) ** len(str(numbers))
        # print(sum)

    if sum == numbers:
        return True
    # return sum


print(armstrong_number(num))

'''Alternative method to solve the problem using int slicing and reminder method'''

num1 = 153
l = len(str(num1))
# print(l)
add = 0
# a = num1 % 10
# print(num1 % 10**int(l))  # Alternative method idk how but works
for i in range(l):
    if num1 > 0:
        add += (num1 % 10) ** int(l)
        # print('add:', add)
        num1 = num1//10
        # print('number after /10: ',num1)
print(add)

""" Printing Armstrong numbers upto certain range using loops """
for i in range(100, 1000):
    if armstrong_number(i) is True:
        print("The given number is armstrong", i)
