# presentation on srings and variable functiosn

#print(100*("hello world\n"))
#print("sajid",end="")   # instead of end =", we can also use \
                        # we use end statement to remove spacing within ptint statement while use of \ is in the statement
#print("hussain")

# if you wish to enter a number
#print("please enter your date of birth")
#inpnum= input()
#print("you have entered", inpnum)

#if you want to capitalise or change letters in string
from typing import List, Union, Any

x=("Programming is a language which computers understand and function on it")
#print(x[0:11])
#print(x.replace("Programming","Python")) #line 64
#print(len(x))
#print(x.isdigit())
#print(x.swapcase())



                          # calculation on python
'''
x=(58988)
y=(79889)
print(x*y)

# def function uses
def say_hello():
    print("hello")
def say_good_bye():
    print("why say good bye")

say_hello()
say_hello()
say_good_bye()


# please dont remove these lines,
# this is an example of comment and its use
#print(''hello world'')
#print("hello\n" "world")
#print("world")
'''

'''
var1= ("string example")
var2= 35
var3=89.23
var4= ("another string example")


print("please enter your number")
inpum=input()
print("you have entered",inpum)


mystr = "my name is sajid"
print(len(mystr))
print(mystr[0:8:2])
print(mystr[::-2]) #slyching of strings backward
print(mystr.isalnum())
print(mystr.count("s"))
print(mystr.replace("sajid","computer")) #this is wromg do some research



#how to create a list
#Grocery = [rice, pulsesls, deodrant, colgate, 34] # str function on double qoute
grocery=["rice","colgate","pulses","deodrant",34]
grocery.reverse()
grocery.pop()

print(grocery)



def say_hello():
    print("hello sajid")
    print("what can i do for you")
def close():
    print("i am always here to help")

say_hello()
close()


# how to make a dictionary
#d1 = {}
#print(type(d1))

#a=78
#print(type(a))
s= set()
#s_from_list=(1,2,3,4)
#print(s_from_list)
#print(type(s_from_list))
s.add(100)
s.add(2)
s.add(128)
print(s)
print(max(s))
s.remove(128)

'''
           #if you wanted to enter into a statement then we use : sign
'''
var1=234
var2=12
if var2<var1:
    print("false")
else:
    print("true")

var1=1
var2=10
var3=int(input())
if var3>var2:
    print("Greater")
else:
    print("lesser")

a=18
b=35
c=int(input())
if c>b:
    print("lesser")
if c==b:
    print("equal")
else:print("greater")
'''
            # list function in if else statement
'''
x=[1,2,3,4,5]
if 3 in x:
    print("yes")
if 10 in x:
    print("true")
else: print("no")       # problem while solving= use {} this while writting dictionary

d={"sajid": "24062002",
            "mohan": "23052001"}
name=input("enter your name")
print(d[name])

'''
'''
print("Enter 1st Numbers")
Num1=(int(input()))
print("Enter 2nd Number")
Num2=(int(input()))
print('Choose your sign'+" +,-,*,/")
Num3=(input())
# {design a faulty calculator
if Num1==45 and Num2==3 and Num3=="*":
   print('555')
   
   
'''

'''
    i=0
    while (True): 
         i=i+1
print(i)
continue   # we use continue to avoid other commands and returns to while statement

if i<100:
    print(i)
\
while (True):
inp= int(input("Enter a Number"))
if inp>100:
    print("Congrats you entered", inp)
    break
else:
    print("try again\n")
    continue
'''





'''

# loop
list = ["harry","larry","marry"]
print(list[0],list[1])
# but using loop we can print all above lists
for item in list :
    print(list)

list1=["harry",
       "marry",
       "cherry",
       "larry"]
# print(list1[0],list1[2],list1[3])
for item in list1:
    print(list1)

 # Use of F fuction

print(f" {3} int and floaters")
print(f"{10} lollypop and {5} choclates")

list2=[["detergent",2], ["maggie",8]]
for item, quantity in list2:
    print(list2)
'''
'''
list=[19,28,10,38,56,88,69]
for item in list:
    if str(list).isnumeric() and list> 50:  # remeber by heart
        print(list)
'''


          # While loop
'''
i=0
while (i<45):
     print(i)
     i=i+1
j=0
while (j<10):
 print(j, end= "")
 j=j+1

 h=11
 while (h<100):
     print(h)
     h= h+10
     
     '''



         # break and continue
'''
i=0

while (True):
   i=i+1
   if i<100:
    print(i)
'''

      # Opreatorss:
'''
#1 Arithmatic Opreators :
print('5+6 is' , 5+6)
print('5*6 is' , 5*6)
print('5-6 is' , 5-6)
print('5/6 is' , 5/6)
print('56 is' , 56)

#2 Assignment opreator
x= 5
print(x)
x+=7     # += is Opreator
print(x)
x/= 10
print(x)
x*=8
print(x) # search google for furthure list

#2 Comparision  "
i =8
print(i==5)

print(i<=8)

print(i>=8)


#3 Logical "
a= True
b= False
print(a and b)
print(a and a)
print(b and b)
print(a or a)
print(a or b)
print(b or b)


#4 Identity "

a= True
b= False

print(a is not a)
print(a is not b)
print(b is not a)
print(b is not b)

#5 Membership "
list= [3,4,6,8,10,12]
print(3 not in list)
print(4 in list)


#6 Bitwise "

print(0 and 1)
print (0 | 1)        # "|" means "or"
print(0 and 3)
print(0|3)

'''


# short if else
'''
a= int(input("Enter your number a\n"))
b= int(input("Enter your number b\n"))

if (a<b):
        print("b is greater than a")
else:
        print(' a is greater than b')

'''


# function

a = 2
b = 7
c = sum((a,b)) #built in function # for creating user function we need def function
print(c)



def function():
    print("Hello you are in function, :)")
function()
function()


def function2(a,b):
   average= (a+b)/2
   print(average)
   return average
v = function2(88,23)
print(v)


def function3():
    """this is an example of doctrane which is not comment inside function"""
print(function3.__doc__)


#try except exception as and handling
'''
print('enter your 1st number\n')
imp1 = input()
print('enter your second number\n')
print('enter your second number\n')
imp2 = input()
try:
    print("sum of these number", int(imp1)+int(imp2))

except Exception as e:
    print(e)
print("line is now succesfully print even after having error in upper code")

# this is how we use except Exception and try'''

'''

 # file IO basics


there are few modes in file to os 
"r" - we called it r mode in this mode we read a file its also a default type
"w" - we called it w mode in this mode we write a file
"x" - we called it x mode in this mode we create a file
"a" - we called it a mode in this mode we add something on a file
"t" - text mode also a default type
"b" - b mode is use for binary 
"+" - we called it plus mode in this mode we read and write ie r and w mode

 '''
# writting and appending a file

#f = open("sajid.txt", "w")
#f.write("im good how are you\
#and yo")

#f.close()
# check project a new file has created


# excercise pattern printing
'''
input = interger n 
boolean = true  and false

if true for n =4
    *
    **
    ***
    ****
for false n  5
    **** 
    ***
    **
    *

'''

# using block to open a file
'''with open("your file name. ) as f:
a = f.read(4)
print(a)'''

# global vriables and global keywords

# recurssion
# \t is use to make space equal to tab






