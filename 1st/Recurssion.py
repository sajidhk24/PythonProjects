from time import time

'''
start = time()
def fib(n):

    if n < 2:
        return n
    else:
        a = fib(n - 2) + fib(n - 1)
        return a


print(fib(12))
print(f'time taken to return value is {time()}-{start} ')

# This is the example of Dynamic Programming

cache = {}

start1 = time()
def fibo1(n):

    if n in cache:
        return cache[n]
    elif n < 2:
        cache[n] = n
        return cache[n]
    else:
        cache[n] = fibo1(n - 1) + fibo1(n - 2)
        return cache[n]


print(fibo1(12))
print(cache)
print(f'time taken by dp is {time()}-{start1}')
'''

# Taking a number and returning its sum

'''
def cummulative(n):
    if n == 0 or n == 1:
        return n
    else:
        value = n + cummulative(n - 1)
        return value


print(cummulative(12))
# To return sum of all numbers in array
value = 0
arr = [0, 12, 3, 4, 121, 0]
for i in arr:
    value += i
print(value)   #O(n)

'''

'''
# To find the factorial of a number
n = int(input('enter the number: '))
def fac(n):
    if n <= 2:
        return n
    else:
        return n * fac(n - 1)


print(fac(n))

'''

'''
# Taking a list of number and return its product
def ProductOfArray(arr):
    if len(arr) == 0:
        return arr
    elif len(arr) == 1:
        return arr[0]
    else:
        return arr[len(arr) - 1] * ProductOfArray(arr[:len(arr)-1])


print(ProductOfArray([2, 3, 4, 5]))

'''

'''
def productOfArray(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[len(arr) - 1] * productOfArray(arr[:len(arr) - 1])

print(productOfArray([12,3,2,2]))
'''

'''

def StringPallindrome(string):
    if len(string) == 0:
        return True

    else:
        if string[0] != string[len(string) - 1]:
            return False
        else:
            return StringPallindrome(string[1:-1])


print(StringPallindrome("apapka"))

'''
# Reverse a string

'''
def Revstr(string):
    if len(string) == 0:
        return string[0]
    elif string[0] != string[len(string) - 1]:
        return False
    else:
        return Revstr(string[1, -1])


print(Revstr('samosa'))

'''

# To extend a array inside a array
'''
ls = [[1], 2, 3, 4, [5, 6, 7], 8]
ls2 = []
for i in ls:
    if type(i) is list:
        ls2.extend(i)
    else:
        ls2.append(i)

print(ls2)

arr = [[1], 2, 3, 4, [5, 6, 7], 8]


def Arrinsidearr(arr):
    arr2 = []
    for i in arr:
        if type(i) is list:
            return arr2.extend(i)
        else:
            return arr2.append(i)


print(Arrinsidearr(arr))

'''

# To capitalize first element of an array

'''
arr = ['foo', 'hello']
arr2 = []
for i in arr:
    arr2.append(i.upper())




def capitalizeWords(arr):
    if len(arr) == 0:
        return arr
    else:
        return [arr[0].upper()] + capitalizeWords(arr[1:])


print(capitalizeWords(['foo', 'hello', 'yes']))

'''
# Returning the sum of numbers present in dictionary
'''

obj = {
  "a": 2,
  "b": {"x": 2, "y": {"foo": 3, "z": {"bar": 2}}},
  "c": {"p": {"h": 2, "r": 5}, "q": 'ball', "r": 5},
  "d": 1,
  "e": {"nn": {"lil": 2}, "mm": 'car'}
}


def returningSum(dic):
    plus = 0
    for k in dic.values():   # Debugging require
        if type(k) is int:
            plus += k
        else:
            return plus


print(returningSum(obj))
'''

'''
def greaterElement(ar, n):
    # Complete the function
    for i in range(n):
        for j in range(i +1):
            if ar[i] < ar[j]:
                get = ar[j], ar[i]
                ar[i], ar[j] = get
    else:
        return ar


arr = [12, 21, 42, 4, 5, 6]
n = len(arr)
x = (greaterElement(arr, n))
print(x)
'''
arr = [1,2,3,4,5]
output = [3,4,5,1,2]

x = len(arr)//2+1
y = len(arr)
ls = []
for i in range(x, len(arr)+1):
    ls.append(i)
for j in range(1,x):
        ls.append(j)

print(ls)


def popping(arr):
    x = len(arr) // 2
    for i in range(x, len(arr)):
        arr.pop(i)
    return popping(0,x)


popping([1,2,3,4,5,6,7])



