'''
atuple = (10,20,30,40)
sample =list()
for i in atuple:
    sample.append(i)
a =sample[0]
b =sample[1]
c =sample[2]
d =sample[3]
print(a,b,c,d)
'''
'''
tuple1 =(11,[22,33],44,55)
print(type(tuple1))
sample = list(tuple1)
print(type(sample))
del sample[1]
print(sample.insert(1,[222,33]))
print(sample)
'''
'''
tuple1 = (('a',23),('b',37),('c',11),('d',29))
a = list(sorted(tuple1))
print(a[2],a[0],a[3],a[1])
'''
'''
for i in range(1,6):
    print('\n')
    for j in range(1,i):
        print(j,end='')
'''
# for i in range(1,9):
#     print(i**3)
import random
# list = ['Head', 'Tails']
# random1 = random.choice(list)
# print(random1)
random_side = random.randint(0,1)
total = 0
if random_side == 0:
    print('Head')
else:
    print('Tails')
sides = ['Head','Tail']
n = random.randint(0,1)
print(sides[n])