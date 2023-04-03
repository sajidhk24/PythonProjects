
'''
# How to define your own functions
def sum(a,b):
    print(a+b)
    return a + b
z = sum(12,4)
print(z)

'''


# Palindrome
def palidrome(names):
    reverse = names[::-1]
    if names == reverse:
        return True
    else:
        return False

print(palidrome("naman"))
print(palidrome("horse"))
print(palidrome("able was i ere i saw elba"))
# Fibonacci series
# it  is a series of number which is sum of previous numbers
# ask users to for number of fibonacci series
a = 0
b = 1
for i in range(1, 20):
    c = a + b
    a = b
    b = c
    print(c, end=",")


'''
print("my name is sajid\n khan")
print("my name is sajid",end="" 
"khan")
import sys
ver=sys.version
print(ver)
from datetime import datetime
now= datetime.now
print(now)
myself= "my name is sajid"
print(myself.upper())
print(len(myself))

a = ('this is an example of\
 how to write a multiline variables')
print(a)
'''



import sys
ver = sys.version
print(ver)

print("lineAlineB")
print("""hello
world""")
print('hel\bllo')
print(round(2**0.5,8))  # round is to round up digit to certain numbers

for f in ["sajid","joe","brad","angelina"]:
    invite = "hi " + f + "come to my party"
    print(invite)


'''

import turtle
wn = turtle.Screen()
wn.bgcolor("green")
wn.title("hello turtle")
alex= turtle.Turtle()
alex.forward(50)
alex.left(100)
wn.mainloop()

'''

'''
first_name = ("sajid")
second_name = ("khan")
print(first_name,  second_name)    # we can use , as to add two strings

name,age = "sajid", 20
print(name, age)    # we can do more with variable
print(age, name)

name, age = input("enter your name and age\n").split()
print(name)
print(age) # we can put two values altogether dont forget to space between values


name = "sajid"
age = "20"      # this is another method to create or to print together
print("hello {} and your age is {},".format(name , age))
'''
a = 24
b = 23
c = sum((a,b))
print(c)

def function(a,b):
    print(a+b//2)
function(12,12)
f=open("hello.txt", "w")
f.write("I am practising python\n")
f.write("this is my second day of practising python")
f.close()

import random
a = random.randint(1,100)
print(a)

import random
b = random.randrange(1, 100, 5)
print(b)

num1,num2,num3 = 12, 20, 30
print((num1 + num2 + num3)/2)

q = (22/3)
print(round(q,3))

def sum(a,b):
    return a+b
s = sum(12,3)
print(s)



def loop3():
    for a in range(0,10):
        print(a)
        if a == 3:
            # We found a three, let's stop looping
            break
    print ("Found 3!")

loop3()

def loop():
    for a in range(0,100):
        print(a)
        if a == 50:
            break
    print("you got the right value")
loop()


import datetime
now = datetime.datetime.now()
print(now)

print(round(223/12,3)) # in order to round off a sum or any mathamatical calculation in ppython wee use round module and then we calculate the value inside the round module using pring or eigher making a variable

from datetime import datetime
now = datetime.now()
print(now)


 # to make dicision
'''
name= input("Enter your name\n N")
age = int(input("Enter your age\n A"))
if name[0] =="A" and age == 10:
    print("You are not eligible")
else:
    print("Condition satisfied")
'''

'''
print("my name is sajid\n khan")
print("my name is sajid",end="" 
"khan")
import sys
ver=sys.version
print(ver)
from datetime import datetime
now= datetime.now
print(now)
myself= "my name is sajid"
print(myself.upper())
print(len(myself))

a = ('this is an example of\
 how to write a multiline variables')
print(a)
'''



import sys
ver = sys.version
print(ver)

print("lineAlineB")
print("""hello
world""")
print('hel\bllo')
print(round(2**0.5,8))  # round is to round up digit to certain numbers

for f in ["sajid","joe","brad","angelina"]:
    invite = "hi " + f + "come to my party"
    print(invite)


'''

import turtle
wn = turtle.Screen()
wn.bgcolor("green")
wn.title("hello turtle")
alex= turtle.Turtle()
alex.forward(50)
alex.left(100)
wn.mainloop()

'''

'''
first_name = ("sajid")
second_name = ("khan")
print(first_name,  second_name)    # we can use , as to add two strings

name,age = "sajid", 20
print(name, age)    # we can do more with variable
print(age, name)

name, age = input("enter your name and age\n").split()
print(name)
print(age) # we can put two values altogether dont forget to space between values


name = "sajid"
age = "20"      # this is another method to create or to print together
print("hello {} and your age is {},".format(name , age))
'''
a = 24
b = 23
c = sum((a,b))
print(c)

def function(a,b):
    print(a+b//2)
function(12,12)
f=open("hello.txt", "w")
f.write("I am practising python\n")
f.write("this is my second day of practising python")
f.close()

import random
a = random.randint(1,100)
print(a)

import random
b = random.randrange(1, 100, 5)
print(b)

num1,num2,num3 = 12, 20, 30
print((num1 + num2 + num3)/2)

q = (22/3)
print(round(q,3))

def sum(a,b):
    return a+b
s = sum(12,3)
print(s)



def loop3():
    for a in range(0,10):
        print(a)
        if a == 3:
            # We found a three, let's stop looping
            break
    print ("Found 3!")

loop3()

def loop():
    for a in range(0,100):
        print(a)
        if a == 50:
            break
    print("you got the right value")
loop()


import datetime
now = datetime.datetime.now()
print(now)

print(round(223/12,3)) # in order to round off a sum or any mathamatical calculation in ppython wee use round module and then we calculate the value inside the round module using pring or eigher making a variable

from datetime import datetime
now = datetime.now()
print(now)


 # to make dicision
'''
name= input("Enter your name\n N")
age = int(input("Enter your age\n A"))
if name[0] =="A" and age == 10:
    print("You are not eligible")
else:
    print("Condition satisfied")
'''














