'''
# To test given value is even or odd
n = int(input("Enter your number to be tested:\n"))
n2 = int(2)
value = (n/n2)
if value == ((round(value,0))):
    print("Even",value)
else:
    print("odd",value)
'''
'''
# To check if the given number is even or odd
num = int(input('Enter a number:' ))
if (num % 2 ) ==0:
    print("{0} is Even". format(num))
else:
    print("{0} is odd". format(num))
'''
'''
# To check prime numbers
N = int(input("Enter number to be tested Prime or not:\n"))
for i in (1,100):
    value = (N/i)
    print(value)
    if value == (value//i):
        print("Given number is not prime")
    elif value is float:
        print(N,"is prime")
'''
'''

# To find the average of numbers
def average(a,b):
    return ((a+b)/2)
print(average(12,13))
'''

# To take input as a even and odd to give its sum
#odd = int(input())
#even = int(input())
#if (odd%2 !=0 and even%2 ==0):
    #print(odd+even)


'''
# To take random odd and even numbers and then print sum of those random numbers
import random
odd = random.randint(1,100)
even = random.randint(1,100)
if odd%2!= 0:
    print(odd,"odd")
if even%2==0:
    print(even,"even")
sum = (odd+even)
print(sum)
'''
'''
# To print a table of given number
n = int(input("Enter the number to: \n"))
for i in range(1,10):
    #multiplication = n*i
    print(n*i)
'''
'''
# To print a table for a given number using while loop
i = 1
N = int(input())
while(i<=10):
    print(N*i)
    i+=1
'''
'''
def prime_checker(number):
    isprime =True
    for i in range(2,number):
        if number%i ==0:
            isprime = False
        if isprime:
            print(number, 'is prime')
        else:
            print(number, 'is not prime')
prime_checker(13)
'''