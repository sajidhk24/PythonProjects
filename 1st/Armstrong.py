# armstrong number
# len of number = power of each number and its sum
# if the of power of each number is equal to original number
# than number is Armstrong

###############################################################

a = int(input())
print(len(str(a)))
b = 0
for i in str(a):
    b += int(i)**int(len(str(a)))
print(b)
if a == b:
    print('y')
else:
    print('n')

###############################################################

number = int(input('NO: '))
b = 0


def armstrong(number):
    global b
    for i in str(number):
        b += int(i)**int(len(str(number)))
        return b


if b == number:
    print('is armstrong')
else:
    print('Not armstrong')
(armstrong(number))