# print(("machine learning {} which gives machine the ability to {}").split())
# a=['sajid', 'sarah', 'rohit']
# print(' '.join(a))
# print(("may i come in {}, i was late bcz of {}").format("mam",'traffic'))
# print(f 'what is the value of {12/2}')
# find the use of eval

# To write acronym
name = "Machine learning"
ac = name.split()
a = " "                 # importance of taking black variable then adding the value in it
for i in ac:
    a = a + str(i[0])
    print(a)

w = "neural network"
e = w.split()
for i in e:
    v = str(i[0].upper()+i[1])          # or str(i[0:1]
    print(v)

h = "peace be upon him"
f = h.split()
g = " "
for i in f:
    g = g+str(i[0].upper())
    print(g)


import qrcode
#img = qrcode.make("www.sajidhk24@gamil.com")
#img.show()

#img = qrcode.make("Hi, this is sajid \
#how are you?")
#img.show()

'''
# To change Celsius in fahrenheit:

def fahrenheit():
    Celsius = float(input("Enter celsius value to change into fahrenheit: "))
    F = float((Celsius*9/5+32))
    print(F)
    return fahrenheit()
# To change Fahrenheit into celsius:
def Celsius():
    Fahrenheit = float(input("Enter the fahrenheit value to change into celsius: "))
    C = float((Celsius*5/9)+32)
    print(C)
    return Celsius()

print(fahrenheit())
'''
'''
# To use coloroma
import colorama
from colorama import Fore, Back,Style
print(Fore.RED+Back.GREEN+"How are you?\n whats going on.."+ Fore.GREEN+Back.RED+"I am good. Just preparing for exams")
'''

def text():
    tex = str(input())
    print(tex)
    print(sum)
    return text()
#print(text())

#while(True):
    #reply = str(input((":")))
    #print(reply)
    #if reply == "stop":
        #break
        #print(reply)
'''
import random
choice = ('computer')
computer = random.choice(choice)
print(computer)

lis = list(input())
reverse = lis[::-1]
print(reverse)
'''
#def reverse(l):
    #element = []
    #element.append(i[::-1])
    #return element
#words = ['abc','def','ghi']
#print(reverse(words))

# filter odd even
# define a function
# list take input eg [1,2,3,4,5,6,7,8]
# output [[1,3,5,7],[2,4,6,8]]

def filter_odd_even(l):
    odd_nums = []
    even_nums = []
    for i in l:
        if i%2==0:
            even_nums.append(i)
        else:
            odd_nums.append(i)
    output = [odd_nums, even_nums]
    return output
nums = [1,2,3,4,5,6,7,8,9,10]
print(filter_odd_even(nums))

# common element finder function
# define a functions which takes 2 lists as input and retur a list
# which contains common elements of both lists
# eg = [1,2,3,4,5,6,7],[1,4,5,2,10,11]
# output = [1,4,5,2

def common_element_finder(list1, list2):
    output= []
    for i in list1:
        if i in list2:
            output.append(i)
        return output

print(common_element_finder([1,2,3,4,5,6,7,8,9,0],[2,4,1,8,11]))
num =1
while(num<=10):
    print(num**2)
    num = num+1

x= 5--1--2--5--66
print(x)
