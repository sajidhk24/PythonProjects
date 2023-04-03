# 1
a=int(input("Enter 1st Number:"))
b=int(input("Enter 2nd Number:"))
s=a+b
print("The Sum Is:",s)

# 2
r=int(input("Enter The Value of Radius:"))
a=2*3.14*r
print("Circumferece of Circle:",a)

# 3
p=int(input("Enter Principal Value:"))
r=int(input("Enter Rate:"))
t=int(input("Enter Time:"))
s=(p*r*t)/100
print("Simple Interest Is:",s)

# 4
import string
for i in string.ascii_uppercase:
    print(i,end=" ")

# 5
n=int(input("Enter Number:"))
i=1
while (i<=n//2):
    if (n%i==0):
        print(i)
    i+=1
print(n)

# 6
n=int(input("Enter Number:"))
i,s=1,0
while (i<=n//2):
    if(n%i==0):
        s+=i
    i+=1
s+=n
print("Sum of factors of",n,"is",s)

# 7
n=int(input("How many times you want to print the series:"))
a,b=0,1
print(a)
print(b)
i=3
while (i<=n):
    s=a+b
    print(s)
    a=b
    b=s
    i+=1

# 8
n=int(input("Enter Number:"))
t=n
rev=0
while (n>0):
    r=n%10
    rev=rev*10+r
    n=n//10
print("Reverse of",t,"is",rev)

# 9
a=int(input("Enter 1st Number:"))
b=int(input("Enter 2nd Number:"))
c=int(input("Enter 3rd Number:"))
if ((a>b)and(a>c)):
    max=a
elif ((b>a)and(b>c)):
    max=b
else:
    max=c
while((max%a!=0)or(max%b!=0)or(max%c!=0)):
    max+=1
print("LCM of",a,b,c,"is","\n",max)

# 10
a=int(input("Enter 1st Number:"))
b=int(input("Enter 2nd Number:"))
c=int(input("Enter 3rd Number:"))
if ((a<b)and(a<c)):
    min=a
elif ((b<a)and(b<c)):
    min=b
else:
    min=c
while((a%min!=0)or(b%min!=0)or(c%min!=0)):
    min-=1
print("HCF of",a,b,c,"is",min)

# 11
n=int(input("Enter Number:"))
t=n
f=1
while(n>1):
    f=f*n
    n=n-1
print("Factorial of",t,"is",f)

# 12
n=int(input("Enter Number You Want To Check Prime:"))
f=0
i=2
while(i<=n//2):
    if(n%i==0):
        f=1
        break
    i+=1
if (f==0):
    print("Prime Number")
else:
    print("Not prime")

# 13
n=int(input("Enter Number Till You Want To Check Prime:"))
if (n==1):
    print("1 is a unique number")
elif (n==2):
    print("2 is the only even prime number")
i=3
while(i<=n):
    f=0
    j=2
    while(j<=i//2):
        if(i%j==0):
            f=1
            break
        j+=1
    if(f==0):
        print(i,end=",")
    i+=1

# 14
n=int(input("Enter The Number You Want To Print The Table:"))
i=1
for i in range(1,11):
    print(n,"*",i,"=",n*i)
    i+=1

# 15
m=int(input("Enter The Number Till You Want To Print The Table:"))
n=2
while(n<=m):
    i=1
    for i in range(1,11):
        print(n,"*",i,"=",n*i)
        i+=1
    n+=1

# 16
n=int(input("Enter Number You Want To Check Perfect:"))
s=0
for i in range(1,n):
    if(n%i==0):
        s+=i
if (s==n):
    print("It is a perfect number")
else:
    print("It is not a perfect number")

# 17
# Pattern

# 18
l=[]
a=input("Enter Data To Add In The List:")
l.append(a)
print("Enter 3 Values To Add The List")
a1=input("Enter First Value:")
a2=input("Enter Second Value:")
a3=input("Enter Third Value:")
l.extend([a1,a2,a3])
print(l)