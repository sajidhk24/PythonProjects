# to find the repeating numbers and its occurrence
"""
arr = [11, 2, 3, 1, 4, 4, 6, 4, 3, 3, 6]
count = 0
le = len(arr)
for i in range(le):
    # print(arr[i])
    for j in range(i + 1, le):
        if arr[i] == arr[j]:
            # print(arr[i], arr[j])
            count += 1
            # arr.remove(arr[i])
            # le -= 1
print(count)
"""

# # counting not from array but form integers

count = 0
n = int(1234112452342143341)
# print(arr2%10)
# print(arr2//10)
while n != 0:
    if n % 10 == 1:
        count += 1
        n = n // 10
    else:
        n = n//10

print(count)
