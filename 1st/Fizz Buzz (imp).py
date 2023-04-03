# Fizz Buzz Excercise
# if number is divisible by 3 say "fizz"
# if number is divisible by 5 say "bizz"
#if number is divisible by both say "fizz_buzz"
ranges = int(input("enter the range:"))
for i in range(0 , ranges):
    if i%3 == 0:
        print('fizz')
    elif i%5 == 0:
        print('buzz')
    elif i%3==0 and i%5==0:
        print('fizz-buzz')
    else:
        print(i)