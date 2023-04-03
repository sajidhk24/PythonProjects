# reverse the number eg if num = 12345 then output will be 54321

n = int(123045)
# output = 54321
# 50+4
# 54*10+3
# 543*10+2
# 5432*10+1

ans = 0
while n > 0:
    rem = n % 10
    # now removing rem value from n
    n = n // 10
    # multiplying ans value * 10 to add rem
    ans = ans * 10 + rem
print(ans)
# Reversing using string
s = str(n)  # converting int into string
m = (s[::-1])  # storing inverse value in a string
print(int(m))  # changing again string into int
