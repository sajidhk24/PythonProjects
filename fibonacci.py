# Fibonacci numbers
# 0,1,1,2,3,5,8,13....nth
number = int(input('Enter the range of fibonacci require: '))
a = 0
b = 1
print(a)
fib = []
for i in range(number):
    c = a+b
    a = b
    b = c
    fib.append(b)
    print(b)
print(fib)