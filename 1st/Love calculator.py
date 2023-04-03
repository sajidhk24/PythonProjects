# take 2 names as a input
# count 'TRUE LOVE' in input values
print('Love calculator')
name1 = str(input('enter 1st name\n').lower())
name2 = str(input('enter 2nd name\n').lower())
lower_case = name1 + name2
t = lower_case.count('t')
r = lower_case.count('r')
u = lower_case.count('u')
e = lower_case.count('e')
true = t+r+u+e
l = lower_case.count('l')
o = lower_case.count('o')
v = lower_case.count('v')
e = lower_case.count('e')
love = l+o+v+e
love_score = int(true+love)
if love_score<10 or love_score<90:
    print(f'Your love score is {love_score},you are together like "coke" and "mentos"')
elif love_score<=40 and love_score>=50:
    print(f'Your love score is {love_score},"you are aright together"')